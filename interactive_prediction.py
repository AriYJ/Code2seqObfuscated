from common import Common
from extractor import Extractor
import os
import csv
from pathlib import Path
import re

SHOW_TOP_CONTEXTS = 10
MAX_PATH_LENGTH = 8
MAX_PATH_WIDTH = 2
EXTRACTION_API = 'https://po3g2dx2qa.execute-api.us-east-1.amazonaws.com/production/extractmethods'


class InteractivePredictor:
    exit_keywords = ['exit', 'quit', 'q']

    def __init__(self, config, model):
        model.predict([])
        self.model = model
        self.config = config
        self.path_extractor = Extractor(config, EXTRACTION_API, self.config.MAX_PATH_LENGTH, max_path_width=2)

    @staticmethod
    def read_file(input_filename):
        with open(input_filename, 'r') as file:
            return file.readlines()

 
    def predict(self): 
        fileDir = os.path.dirname(os.path.realpath('__file__')) 
        #start_num, end_num = 1, 105 
        with open('../output.csv', 'w+') as csvfile: 
            filewriter = csv.writer(csvfile, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL) 
            filewriter.writerow(['submission_id', 'file_name', 'method_name', 'prediction']) 
        for path in Path('../dataset').rglob('*.java'): 
            print(path) 
            input_filename = os.path.join(fileDir, path) 
            input_filename = os.path.abspath(os.path.realpath(input_filename)) 
            submission_num_regex = re.compile(r'(Submission_)(\d+)') 
            submission_num = submission_num_regex.search(input_filename).groups()[1] 
            print(submission_num) 
            java_file_regex = re.compile(r'([a-zA-Z]+)(\.java)') 
            java_file_name = java_file_regex.search(input_filename).group(1) 
            print(java_file_name) 
        #for num in range(start_num, end_num + 1): 
        #    for name in ['GameBoard', 'Message', 'Move', 'Player']: 
        #        print('Serving' + str(num) + name) 
        #        path = '../dataset/Submission_' + str(num) + '/hw1/src/main/java/models/' + name + '.java' 
        #        input_filename = os.path.join(fileDir, path) 
        #        input_filename = os.path.abspath(os.path.realpath(input_filename)) 
            if os.path.exists(input_filename) and submission_num and java_file_name and java_file_name != "UiWebSocket": 
                print("Serving_submission" + submission_num + "_" + java_file_name + ".java") 
                user_input = ' '.join(self.read_file(input_filename)) 
                try: 
                    predict_lines, pc_info_dict = self.path_extractor.extract_paths(user_input) 
                except ValueError: 
                    print('ValueError passed') 
                    pass 
                except TimeoutError: 
                    print('TimeoutError passed') 
                    pass 
                     
                model_results = self.model.predict(predict_lines) 
 
                prediction_results = Common.parse_results(model_results, pc_info_dict, topk=SHOW_TOP_CONTEXTS) 
                for index, method_prediction in prediction_results.items(): 
                    print('Original name:\t' + method_prediction.original_name) 
                    if self.config.BEAM_WIDTH == 0: 
                        print('Predicted:\t%s' % [step.prediction for step in method_prediction.predictions]) 
                        with open('../output.csv', 'a+') as csvfile: 
                            prediction_str = '|'.join([step.prediction for step in method_prediction.predictions]) 
                            filewriter2 = csv.writer(csvfile, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL) 
                            filewriter2.writerow([submission_num, java_file_name, method_prediction.original_name, prediction_str]) 
                            #filewriter2.writerow([str(num), name, method_prediction.original_name, prediction_str]) 
                        for timestep, single_timestep_prediction in enumerate(method_prediction.predictions): 
                            print('Attention:') 
                            print('TIMESTEP: %d\t: %s' % (timestep, single_timestep_prediction.prediction)) 
                            for attention_obj in single_timestep_prediction.attention_paths: 
                                print('%f\tcontext: %s,%s,%s' % ( 
                                    attention_obj['score'], attention_obj['token1'], attention_obj['path'], 
                                    attention_obj['token2'])) 
                    else: 
                        print('Predicted:') 
                        for predicted_seq in method_prediction.predictions: 
                            print('\t%s' % predicted_seq.prediction) 
