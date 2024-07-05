```ascii
                _____      _                    _____      _ 
               |  __ \    (_)                  |  __ \    | |
               | |__) | __ _ _ __ ___   ___ _ _| |__) |_ _| |
               |  ___/ '__| | '_ ` _ \ / _ \ '__|  ___/ _` | |
               | |   | |  | | | | | | |  __/ |  | |  | (_| | |
               |_|   |_|  |_|_| |_| |_|\___|_|  |_|   \__,_|_|
```
### Automating primer preperation for demultiplexing
#### Made to compliment cLweinrich/demux

##### Usage:
To run this program, please open config.yaml and adjust lines 4-7 to match your directory layout. Then, ensure you have executable permissions on the run-PrimerPal.sh file (chmod +x ...) and run it like a typical .sh file (./run-PrimerPal.sh).

##### Input data structure:
- Sample-List.csv
This file should have three columns. One for the name of your sample, one for the Forward-Primer name, and one for the Reverse-Primer name.
- Primer-Sequences.csv
This file should contain the names of the primers and the label sequence. The primer sequence is optional since the program will request it upon running run-PrimerPal.sh. However, it is nice to have the primer sequence in a common place so that you can copy and paste.

Note: PrimerPal requests a manual input of the forward and reverse primer sequences to prevent misinterpretation for autmomated text searching. This is an intentional design to prevent computer error.
