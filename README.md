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

# Raw Data from Experiments
We have included datasets, models, outputs in the 'Raw_Data_From_Experiments' directory. More specifically, there are a few sub-directories within 'Raw_Data_From_Experiments': 'Dataset', 'Models' and 'Final_Output'. 'Dataset' contains the original java-small dataset as provided by code2seq, the obfuscated dataset we constructed and the 4156 student submission dataset. 'Models' contains both the original java-small model as provided by code2seq and the obfuscated model we trained. 'Final_Output' contains the similarity results we have obtained from both the original java-small code2seq model and the obfuscated model. These results are the basis of our comparison. Please see the subsections below for more details of the contents within the directory.

## Output From Experiments
All output from experiments (we conducted no user studies) can be found in the 'Raw\_Data\_From\_Experiments' and 'Final\_Output' directory. All files are listed below.
+ CSV Output from evaluating the submission data with the original java-small model: output_code2seq_small_model_iter2.csv
+ CSV Output from evaluating the submission data with the obfuscated model: output_obfuscated_13epoch_model.csv
+ CSV output of most similar pairs of methods with the original java-small model: nonobfuscated\_final\_output.csv
+ CSV output of most similar pairs of methods with the obfuscated model: obfuscated\_13epoch\_final_output.csv
+ Two accuracy score outputs are at the end of similarity_accuracy.pdf

## Training and Testing datasets
'Raw_Data_From_Experiments/Dataset' directory contains the datasets used for training the code2seq models and testing them:
+ ASE_test_dataset.tar.gz contains 105 submissions from ASE Fall-2020 (Testing dataset)
+ java-small.tar.gz is the dataset used for training the original code2seq model.
+ java-small-obfuscated.tar.gz is the dataset used for training the obfuscated code2seq model.

## Models
Original code2seq small model trained on java-small for 13 epochs: 'Raw_Data_From_Experiments/Models/Original'
Obfuscated code2seq model we trained in the project for 13 epochs: 'Raw_Data_From_Experiments/Models/Obfuscated' (please read README.md for instructions on merging)

# How To Run This Project
+ Clone code2seq repository
+ Take a look at all files inside `Code\_Scripts\_Configurations' directory. You should be able to find files with the same names (all but 'similarity_accuracy.py') in the code2seq repository. Replace these four files origianl to code2seq with the four edited ones from `Code\_Scripts\_Configurations'. Then copy 'similarity_accuracy.py' into the code2seq repository.
+ Please follow the instruction provided in [code2seq repository](https://github.com/tech-srl/code2seq) to train/test the model.
+ If you wish to obfuscated the data yourself, feed the student submission dataset in 'Raw_Data_From_Experiments/Dataset/ASE_test_dataset.tar.gz' into the obfuscation tool following the instructions at https://github.com/basedrhys/obfuscated-code2vec. Then follow instructions at https://github.com/tech-srl/code2seq to preprocess the data, train the model and evaluate the model.
+ If you wish to take the obfuscated data and preprocess it, train the model and evalute the trained model, start with 'Raw_Data_From_Experiments/Dataset/java-small-obfuscated.tar.gz'
+ If you wish to directly evaluate the obfuscated model, take 'Raw_Data_From_Experiments/Models/Obfuscated' as your model and follow the instructions at https://github.com/tech-srl/code2seq
+ After you get the CSV file from evaluating the submission data, replace the input filename in similarity\_accuracy.py, set the desired output filename, and run similarity_accuracy.py. The accuracy score will get printed.
+ If you wish to go straight to the comparison results, please go to 'Raw\_Data\_From\_Experiments/Final\_Output' for results to base your analysis on.

# Relevant Sources:
- Code2seq: https://github.com/tech-srl/code2seq
- Obfuscator: https://github.com/basedrhys/obfuscated-code2vec
- Java-small dataset: https://s3.amazonaws.com/code2seq/datasets/java-small.tar.gz


