# Task-conditioned Domain Adaptation for Pedestrian Detection in Thermal Imagery 

### Reference
* https://github.com/mrkieumy/task-conditioned



### Setting
* You can download weights file for pre-trained and put them inside 'weights' folder
 	* <a href="https://drive.google.com/file/d/1tEVCcBZKN9eubZrPZWEMb6LWfPB2WeYx/view?usp=sharing">TC_Det_Detector.weights </a> 
	* <a href="https://drive.google.com/file/d/1RDzTEuYNJ3p9snmyGWQ6Irj-Ja6HL-DX/view?usp=sharing">kaist_mixing80_20.weights </a>.
	* <a href="https://drive.google.com/file/d/1xiSKTNEB5ng0T5kgyjUKytlpn3q84uK6/view?usp=sharing">kaist_visible_detector.weights </a>
	* <a href="https://drive.google.com/file/d/1Kyoyira0liRRr_FOY8DDSeATLQAwXtu-/view?usp=sharing">kaist_thermal_detector.weights </a>
	or ours best weight kaist detector augmented with GANs model.


### Evaluation Performance includes mAP and Miss Rate:
Evaluation mean Average Precision (mAP) as well as Log Average Miss Rate (LAMR) of the detector over the test set.
Noted that, Log Average Miss Rate and Precision on reasonable setting (daytime, nighttime, and day & night) is the standard evaluation of the state-of-the-art on KAIST dataset.
```
python faster_eval.py -i <detection results folder>
```


The paper is available here <a href="https://www.researchgate.net/publication/343167450_Task-conditioned_Domain_Adaptation_for_Pedestrian_Detection_in_Thermal_Imagery"> Task-conditioned Domain Adaptation for Pedestrian Detection in Thermal Imagery </a>

## Citation
We really hope this repository is useful for you. Please cite our paper as
```
@inproceedings{KieuECCV2020taskconditioned,
	Author = {Kieu, My and Bagdanov, Andrew D and Bertini, Marco and Del Bimbo, Alberto},
	Booktitle = {Proc. of European Conference on Computer Vision (ECCV)},
	Title = {Task-conditioned Domain Adaptation for Pedestrian Detection in Thermal Imagery},
	Year = {2020}
	}

```

If you have any comment or question about this repository, please leave it in Issues.

Other contribution, please contact me by email: my.kieu@unifi.it.

Thank you so much for your interest in our work.
