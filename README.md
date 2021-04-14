Final project for 6156 Topics In Software Engineering (Spring 2021) - Team Deep Understanding

# All Project Assignments
All project assignments (proposal, revised proposal, first progress report, second progress report, demo slides) can be found in the 'All_Project_Assignments' directory

# Code, Scripts, Configurations, etc.
Below is a list of scripts we have created/edited for the project. They can be found in the 'Code_Scripts_Configurations' directory
+ Edited path to point to obfuscated data: preprocess.sh (code2seq, preprocessing data)
+ Edited path to point to preprocessed data: train.sh (code2seq, model training)
+ Configured hyperparameters: config.py (code2seq, model training)
+ Customized script for submission data: interactive_prediction.py (code2seq)
+ Code to get most similar pairs of methods and evaluate accuracy: similarity_accuracy.py

# Raw Data From Experiments
All raw data from experiments (we conducted no user studies) can be found in the 'Raw_Data_From_Experiments' directory. All files are listed below.
+ CSV Output from evaluating the submission data with the original java-small model:
+ CSV Output from evaluating the submission data with the obfuscated model:
+ CSV Output of most similar pairs of methods with the original java-small model: nonobfuscated_final_output.csv
+ CSV Output of most similar pairs of methods with the obfuscated model: obfuscated_13epoch_final_output.csv
<MORE INFO>

# Project Overview
The project aims to build a code understanding tool that helps find code clones across multi-file projects. The tool will be based on machine learning techniques and models. A motivating scenario for such a tool is that if a developer wants to understand a piece of code that s/he has encountered for the first time,  it would be helpful to find similar and familiar code that the developer might have developed before. 

We attempted to answer two research questions: 1) if obfuscation of variable names yield an improved code2seq model, and 2) how we can utilize code2seq model’s output for code similarity.

In order to answer these questions, we 1) retrained the code2seq model with obfuscated data, 2) used the new model to evalute student submissions from Columbia's 4156 Advanced Software Engineering (Fall 2020) and 3) compared results to that of the original code2seq small-java model.

# How To Run This Project
After you get the CSV file from evaluating the submission data, replace the input filename in similarity_accuracy.py, set the desired output filename, and run similarity_accuracy.py. The accuracy score will get printed.
<MORE INFO>

# Relevant Sources:
- Code2seq: https://github.com/tech-srl/code2seq
- Obfuscator: https://github.com/basedrhys/obfuscated-code2vec
- Java-small dataset: https://s3.amazonaws.com/code2seq/datasets/java-small.tar.gz


