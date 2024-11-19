#20416 오상렬 틀 제작

import cv2
import numpy as np
from matplotlib import pyplot as plt

# matplotlib 한글 폰트
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

# 이미지 불러오기
image_start = input()
image_bring = image_start
image = cv2.imread(image_bring)

# 이미지를 HSV 색상으로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 이미지 빨간색 분석 함수
def scan_red(hsv_image, hue_leave=10, sat_max=100):    # 이미지의 빨간색 부분을 자동 탐색

    # 채널을 분리
    channel = hsv_image[:, :, 0]
    channe2 = hsv_image[:, :, 1]
    
    # 채도가 100 이상인 부분을 분석 대상ㄱ
    red_hue_vl = channel[channe2 > sat_max]
    
    # 채널 히스토그램을 계산합니다.
    hist, bins = np.histogram(red_hue_vl, bins=180, range=[0, 180])
    
    # 히스토그램 값을 계산
    part1 = np.sum(hist[:10])   # 0-10
    part2 = np.sum(hist[160:])  # 160-180
    
    # 더 큰 합을 가지는 영역을 기준으로 빨간색 범위 설정(gpt 사용)
    if part1 >= part2:
        red_hue_peak = np.argmax(hist[:10])
        low_red = np.array([red_hue_peak - hue_leave, 100, 100])
        up_red = np.array([red_hue_peak + hue_leave, 255, 255])
    else:
        low_red = np.array([160 - hue_leave, 100, 100])
        up_red = np.array([180, 255, 255])

    return low_red, up_red

# 이미지에 적용하여 빨간색 부분을 파란색으로 변경
low_red, up_red = scan_red(hsv_image)
mask = cv2.inRange(hsv_image, low_red, up_red)

# 이미지 사본 생성 빨간색 부분에 파란색 사용
blue_image = image.copy()
blue_image[mask > 0] = [255, 0, 0]  # 파란색 적용

# 보여주기
plt.figure(figsize=(10, 5)) #크기
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("원본")   #제목
plt.axis("off") #이미지 빼고 다른거 끄기

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(blue_image, cv2.COLOR_BGR2RGB))
plt.title("바뀐거") #제목
plt.axis("off") #이미지 빼고 다른거 끄기

plt.show()
