import os
import numpy as np
import brambox.boxes as bbb
import matplotlib.pyplot as plt
import scipy.interpolate

def meanAP_LogAverageMissRate(input_json):

    identify = lambda f: os.path.splitext("/".join(f.rsplit('/')[-3:]))[0]

    # parse ground truth from all videos in all sets
    ground_truth = bbb.parse('anno_dollar', 'annotations/*/*/*.txt', identify, occlusion_tag_map=[0.0, 0.25, 0.75])
    # print(len(ground_truth))
    # print(identify)
    # filter ground truth by marking boxes with the ignore flag
    bbb.filter_ignore(ground_truth, [bbb.ClassLabelFilter(['person']),  # only consider 'person' objects
                                     bbb.HeightRangeFilter((50, float('Inf'))),  # select instances of 50 pixels or higher
                                     bbb.OcclusionAreaFilter(
                                         (0.65, float('Inf')))])  # only include objects that are 65% visible or more

    for _, annos in ground_truth.items():
        for i in range(len(annos)):
            annos[i].class_label = 'person'

    # modify ground truth aspect ratio
    bbb.modify(ground_truth, [bbb.AspectRatioModifier(.41, modify_ignores=False)]);

    # split and copy to day and night ground truth
#    ground_truth_day = {key: values for key, values in ground_truth.items() if
#                        key.startswith('set06') or key.startswith('set07') or key.startswith('set08')}
#    ground_truth_night = {key: values for key, values in ground_truth.items() if
#                          key.startswith('set09') or key.startswith('set10') or key.startswith('set11')}

    # split and copy by scenes' GT
    ground_truth_campus = {key: values for key, values in ground_truth.items() if
                        key.startswith('set06') or key.startswith('set09') }

    ground_truth_road = {key: values for key, values in ground_truth.items() if
                        key.startswith('set07') or key.startswith('set10')}

    ground_truth_downtown = {key: values for key, values in ground_truth.items() if
                        key.startswith('set08') or key.startswith('set11') }

    def parse_detections(format, input, identify_fun=identify, clslabelmap=['person']):
        dets = bbb.parse(format, input, identify_fun, class_label_map=clslabelmap)
        bbb.modify(dets, [bbb.AspectRatioModifier(.41)])
        bbb.filter_discard(dets, [bbb.HeightRangeFilter((50 / 1.25, float('Inf')))])
        return dets


    detections_all = {}

    # detections_all['current'] = parse_detections('det_coco', 'results/conditioning/condition86e_mAP.json')
    # path_source = os.getcwd()
    # path_source = os.path.join(path_source, 'detection_results.json')
    path_source = input_json
    # print(path_source)
    detections_all['current'] = parse_detections('det_coco', path_source)

    # detections_all['Our: TD(V,V)'] = parse_detections('det_coco','results/adaptation/1_Visible_15e.json')
    # detections_all['Our: TD(T,T)'] = parse_detections('det_coco','results/adaptation/1_Thermal_15e.json')
    # detections_all['Our: TD(VT,T)'] = parse_detections('det_coco','results/adaptation/1_15e_toFT_34elike30e.json')
    # detections_all['Our: BU(VAT,T)'] = parse_detections('det_coco','results/adaptation/1_Adap30layers_From15_000014_best.json')
    # detections_all['Our: BU(VLT,T)'] = parse_detections('det_coco','results/adaptation/1_Layerwise5layers_from15e_000020_best.json')

    # detections_all['MSDS'] = parse_detections('det_coco','results/SOTA/MSDS.json')
    # detections_all['MSDS_sanitized'] = parse_detections('det_coco','results/SOTA/MSDS_sanitized.json')

    # split and copy to day and night detections
 #   detections_day = {}
 #   detections_night = {}
 #   for label, detections in detections_all.items():
 #       detections_day[label] = {key: values for key, values in detections.items() if
 #                                key.startswith('set06') or key.startswith('set07') or key.startswith('set08')}
 #       detections_night[label] = {key: values for key, values in detections.items() if
 #                                  key.startswith('set09') or key.startswith('set10') or key.startswith('set11')}

    detections_campus = {}
    detections_road = {}
    detections_downtown = {}
    for label, detections in detections_all.items():
        detections_campus[label] = {key: values for key, values in detections.items() if
                                 key.startswith('set06') or key.startswith('set09')}
        detections_road[label] = {key: values for key, values in detections.items() if
                                   key.startswith('set07') or key.startswith('set10')}
        detections_downtown[label] = {key: values for key, values in detections.items() if
                                   key.startswith('set08') or key.startswith('set11')}


    detectors_to_plot = ['current']
    # detectors_to_plot = ['Our: BU(VLT,T)', 'condition 86e map','Our: TD(V,V)','Our: TD(T,T)','Our: TD(VT,T)','Our: BU(VAT,T)','MSDS']


    
    return detections_all, detections_campus, detections_road, detections_downtown

