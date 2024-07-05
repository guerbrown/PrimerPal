import pandas as pd
import re
import yaml
import os

def get_primer_info():
    num_primers = int(input("How many primers were used? "))
    primers = {}
    
    if num_primers == 1:
        forward_seq = input("Enter the forward primer sequence: ")
        reverse_seq = input("Enter the reverse primer sequence: ")
        primers["default"] = {"forward": forward_seq, "reverse": reverse_seq}
    else:
        for i in range(num_primers):
            pattern = input(f"Enter the text pattern for primer set {i+1} (regex accepted): ")
            forward_seq = input(f"Enter the forward primer sequence for {pattern}: ")
            reverse_seq = input(f"Enter the reverse primer sequence for {pattern}: ")
            primers[pattern] = {"forward": forward_seq, "reverse": reverse_seq}
    
    return primers

def main():
    try:
        # Load configuration
        with open('config.yaml', 'r') as config_file:
            config = yaml.safe_load(config_file)

        # Set working directory
        os.chdir(config['workdir'])

        # Read the Primer-Sequences.csv file
        primer_sequences = pd.read_csv(config['primer_sequences'], delimiter=',')
        
        # Check if the necessary columns exist in Primer-Sequences.csv
        primer_name_col = config['column_names']['primer_sequences']['primer_name']
        label_col = config['column_names']['primer_sequences']['label']
        if primer_name_col not in primer_sequences.columns or label_col not in primer_sequences.columns:
            raise KeyError(f'The Primer-Sequences.csv file must contain "{primer_name_col}" and "{label_col}" columns.')
        
        # Read the "Sample List" file
        sample_list = pd.read_csv(config['sample_list'], delimiter=',')
        
        # Check if the necessary columns exist in "Sample List"
        sample_id_col = config['column_names']['sample_list']['sample_id']
        forward_primer_col = config['column_names']['sample_list']['forward_primer']
        reverse_primer_col = config['column_names']['sample_list']['reverse_primer']
        if sample_id_col not in sample_list.columns or forward_primer_col not in sample_list.columns or reverse_primer_col not in sample_list.columns:
            raise KeyError(f'The Sample-List.csv file must contain "{sample_id_col}", "{forward_primer_col}", and "{reverse_primer_col}" columns.')
        
        # Get primer information from user
        primers = get_primer_info()
        
        # Create a dictionary for primer labels
        label_to_primer = {row[primer_name_col]: row[label_col] for _, row in primer_sequences.iterrows()}
        
        # Prepare the output data
        output_data = []
        for _, row in sample_list.iterrows():
            sample_id = row[sample_id_col]
            forward_primer = row[forward_primer_col]
            reverse_primer = row[reverse_primer_col]
            
            # Find the matching primer set using regex
            primer_set = next((p for p in primers if re.search(p, forward_primer)), "default")
            
            # Get the sequences and labels for forward and reverse primers
            forward_sequence = primers[primer_set]["forward"]
            reverse_sequence = primers[primer_set]["reverse"]
            forward_label = label_to_primer.get(forward_primer, 'Unknown')
            reverse_label = label_to_primer.get(reverse_primer, 'Unknown')
            
            # Append the row to output data
            output_data.append([
                sample_id,
                forward_label,
                reverse_label,
                forward_sequence,
                reverse_sequence
            ])
        
        # Write to output file without headers
        with open(config['output'], 'w') as f:
            for row in output_data:
                f.write(config['output_format']['delimiter'].join(row) + '\n')
        
        print(f"Output has been written to {config['output']}")
        
    except FileNotFoundError as e:
        print(f'Error: {e}')
    except KeyError as e:
        print(f'Error: {e}')
    except EOFError as e:
        print(f'Input was terminated unexpectedly: {e}')
    except ValueError as e:
        print(f'Invalid input: {e}')

if __name__ == '__main__':
    main()
