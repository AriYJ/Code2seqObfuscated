Final project for 6156 Topics In Software Engineering (Spring 2021) - Team Deep Understanding

# All Project Assignments
All project assignments (proposal, revised proposal, first progress report, second progress report, demo slides) can be found in the 'milestone assignments' folder

# Code, Scripts, Configurations, etc.
Below is a list of scripts we have created/edited for the project. They can be found in the 
+ Edited path to point to obfuscated data: preprocess.sh (code2seq, preprocessing data)
+ Edited path to point to preprocessed data: train.sh (code2seq, model training)
+ Configured hyperparameters: config.py (code2seq, model training)
+ Customized script for submission data: interactive_prediction.py (code2seq)
+ Code to get most similar pairs of methods and evaluate accuracy: similarity_accuracy.py

# Raw Data From Experiments
+ CSV Output from evaluating the submission data with the original java-small model:
+ CSV Output from evaluating the submission data with the obfuscated model:
+ CSV Output of most similar pairs of methods with the original java-small model: nonobfuscated_final_output.csv
+ CSV Output of most similar pairs of methods with the obfuscated model: obfuscated_13epoch_final_output.csv
<MORE INFO>

# Project Overview
We retrained the code2seq model with obfuscated data, used the new model to evalute student submissions from Columbia's 4156 Advanced Software Engineering (Fall 2020) and compared results to that of the original code2seq small-java model.

# How To Run This Project
After you get the CSV from evaluating the submission data, replace the filename in similarity_accuracy.py, set the desired output filename, and run the python file. The accuracy score will get printed.
<MORE INFO>

# Relevant Sources:
- Code2seq: https://github.com/tech-srl/code2seq
- Obfuscator: https://github.com/basedrhys/obfuscated-code2vec
- Java-small dataset: https://s3.amazonaws.com/code2seq/datasets/java-small.tar.gz

