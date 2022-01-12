import os
import argparse
import evaluation as EVAL

def convert(faster_detection_results, output_txt):

    fo = open(output_txt, "w")
    for entry in os.listdir(faster_detection_results):
        if(entry.endswith(".txt")):
            filename = entry.replace(".txt","")
            input_txt = os.path.join(faster_detection_results,entry)

            fp = open(input_txt, "r")

            lines = fp.readlines()

            for line in lines:
                split_line = line.split(' ')

                object_type = split_line[0]
                confidence = split_line[1]
                startX = split_line[2]
                startY = split_line[3]
                endX = split_line[4]
                endY = split_line[5]
                fo.write(' '.join([filename, confidence, startX, startY, endX, endY]))


            fp.close()
    fo.close()




if __name__ == '__main__':
    
    output_txt = '/home/superorange5/Research/KAIST_research/task-conditioned/results/det_test_person.txt'
    input_path = '/home/superorange5/Research/2019_deepMI3/deepMI3/faster-RCNN/output'
    model_subfolder = 'fasterRD' #'KAIST_fasterRCNN_vgg16_FedAvg_AVG'
    epoch = 30 
    for i in range(epoch):
#    parser = argparse.ArgumentParser()
#    parser.add_argument('--input', '-i', type=str, help='input detection results')
#    args, _ = parser.parse_known_args()
        input_folder = os.path.join(input_path, model_subfolder,'KAIST_fasterRCNN_vgg16_'+str(i+1),'detection_results/')

        convert(input_folder, output_txt)
        EVAL.evaluation_models()

