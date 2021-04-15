Final project for 6156 Topics In Software Engineering (Spring 2021) - Team Deep Understanding

# Project Overview
The project aims to build a code understanding tool that helps find code clones across multi-file projects. The tool will be based on machine learning techniques and models. A motivating scenario for such a tool is that if a developer wants to understand a piece of code that s/he has encountered for the first time,  it would be helpful to find similar and familiar code that the developer might have developed before. 

We attempted to answer two research questions: 1) if obfuscation of variable names yield an improved code2seq model, and 2) how we can utilize code2seq model’s output for code similarity.

In order to answer these questions, we 1) retrained the code2seq model with obfuscated data, 2) used the new model to evalute student submissions from Columbia's 4156 Advanced Software Engineering (Fall 2020) and 3) compared results to that of the original code2seq small-java model.

# All Project Assignments
All project assignments (proposal, revised proposal, first progress report, second progress report, demo slides, final report) can be found in the 'All_Project_Assignments' directory

# Code, Scripts, Configurations, etc.
Below is a list of scripts we have created/edited for the project. They can be found in the 'Code_Scripts_Configurations' directory
+ Edited path to point to obfuscated data: preprocess.sh (code2seq, preprocessing data)
+ Edited path to point to preprocessed data: train.sh (code2seq, model training)
+ Configured hyperparameters: config.py (code2seq, model training)
+ Customized script for submission data: interactive_prediction.py (code2seq)
+ Code to get most similar pairs of methods and evaluate accuracy: similarity_accuracy.py

# Output From Experiments
All output from experiments (we conducted no user studies) can be found in the 'Raw\_Data\_From\_Experiments' and 'Final\_Output' directory. All files are listed below.
+ CSV Output from evaluating the submission data with the original java-small model: output_code2seq_small_model_iter2.csv
+ CSV Output from evaluating the submission data with the obfuscated model: output_obfuscated_13epoch_model.csv
+ CSV output of most similar pairs of methods with the original java-small model: nonobfuscated\_final\_output.csv
+ CSV output of most similar pairs of methods with the obfuscated model: obfuscated\_13epoch\_final_output.csv
+ Two accuracy score outputs are at the end of similarity_accuracy.pdf

# Training and Testing datasets
`Dataset` directory contains the datasets used for training the code2seq models and testing them:
+ ASE_test_dataset.tar.gz contains 105 submissions from ASE Fall-2020 (Testing dataset)
+ java-small.tar.gz is the dataset used for training the original code2seq model.
+ java-small-obfuscated.tar.gz is the dataset used for training the obfuscated code2seq model.

# Models
Both original and obfuscated code2seq models used in the study are located insode the `Model` directory.

# How To Run This Project
+ Clone code2seq repository
+ Copy all files inside `Code\_Scripts\_Configurations' directory into the code2seq repo and replace files.
+ Please follow the instruction provided in [code2seq repository](https://github.com/tech-srl/code2seq) to train/test the model.
+ 
+ After you get the CSV file from evaluating the submission data, replace the input filename in similarity\_accuracy.py, set the desired output filename, and run similarity_accuracy.py. The accuracy score will get printed.

# Relevant Sources:
- Code2seq: https://github.com/tech-srl/code2seq
- Obfuscator: https://github.com/basedrhys/obfuscated-code2vec
- Java-small dataset: https://s3.amazonaws.com/code2seq/datasets/java-small.tar.gz


