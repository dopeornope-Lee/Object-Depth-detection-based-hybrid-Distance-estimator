# Object-Depth-detection-based-hybrid-Distance-estimator
비디오를 활용한 트랜스포머 Depth 측정모델을 융합한 거리측정 하이브리드 모델



## 1. 데이터셋 다운 받기


**드라이브**:
https://drive.google.com/file/d/1Yv-XkVmYVMIxMsoaX0wRP0uc7AgS9XTq/view?usp=sharing

구글드라이브에 접속 후, data.egg 파일을 프로젝트 폴더안의'./datasets/data/' 경로에 다운 (19GB라서 오래 걸림.)    
폴더의 'image', 'VKITTI', 'VKITTI_txt' 이렇게 3개가 나오도록 설정.

```
For example) './datasets/data/image', './datasets/data/VKITTI', './datasets/data/VKITTI_txt'
```

## 2. Preprocessing
* KITTI
```
'./kitti_detr_dataset.py'
```  
KITTI dataset이 나타내는 bbox와 DETR로 kitti image를 예측해서 나온 bbox가 무엇인지 비교하교, 실제 데이터의 bbox가 가르킨 객체를 DETR이 어떤 bbox로 표현해서 예측했는지 비교해서 DETR의 bbox만 저장하기.  
  
```
'./kitti_glpdepth_dataset.py'
```  
glpdepth로 KITTI image를 Depth map으로 표현 후, 위에서 나온 bbox로 Depth map을 잘라서(bbox 모양의 Depth map을 추출) 그 Depth map의 value(method: min, mean, ...)를 얻는다.   
   
* VKITTI2  
```
'./datasets/data/make_vkitti_dataset.py' 
```  
VKITTI 데이터 안에 있는 모든 Scene과 각각의 weather 정보에 대해서 데이터 정리  

```
'./vkitti_detr_dataset.py'
```
VKITTI dataset이 나타내는 bbox와 DETR로 kitti image를 예측해서 나온 bbox가 무엇인지 비교하교, 실제 데이터의 bbox가 가르킨 객체를 DETR이 어떤 bbox로 표현해서 예측했는지 비교해서 DETR의 bbox만 저장하기.  
  
 ```
 './vkitti_glpdepth_dataset.py'
 ```  
glpdepth로 VKITTI image를 Depth map으로 표현 후, 위에서 나온 bbox로 Depth map을 잘라서(bbox 모양의 Depth map을 추출) 그 Depth map의 value(method: min, mean, ...)를 얻는다.     
  
* Train, Validation, Test
```
'./datasets/train_test_split'
```  
```
KITTI dataset's ration == (train : Valid : Test = 7 : 1.5 : 1.5)
```
Preprocessing된 KITTI, VKITTI 데이터를 train, valid, test로 구분지어 준다. (width, height 변수 추가도 포함.)  
   
## Reference 
- Dataset  
http://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=2d  
https://europe.naverlabs.com/research/computer-vision/proxy-virtual-worlds-vkitti-2/  

- Model  
https://github.com/vinvino02/GLPDepth  
https://github.com/isl-org/MiDaS  
https://github.com/isl-org/DPT  
https://github.com/facebookresearch/detr  
