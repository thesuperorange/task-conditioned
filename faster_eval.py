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

    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, help='input detection results')
    args, _ = parser.parse_known_args()
    convert(args.input, output_txt)
    EVAL.evaluation_models()

