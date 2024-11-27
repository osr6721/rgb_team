#pip install matplotlib
#pip install opencv-python

import cv2
import numpy as np
from matplotlib import pyplot as plt

# matplotlib 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 이미지 불러오기
blindness = input("색맹의 종류를 입력하세요(적색맹, 녹색맹, 청색맹, 전색맹): ")
image_start = input("이미지 파일 경로를 입력하세요: ")
image_bring = image_start
image = cv2.imread(image_bring)

# 이미지를 HSV 색상으로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

if blindness == '적색맹':
    
    # 빨간색 범위를 자동으로 인식하는 함수
    def scan_red(hsv_image, hue_leave=10, sat_max=100):
        # 채널을 분리
        channel = hsv_image[:, :, 0]  # Hue 채널
        channe2 = hsv_image[:, :, 1]  # Saturation 채널
        
        # 채도가 100 이상인 부분을 분석 대상
        red_hue_vl = channel[channe2 > sat_max]
        
        # 채널 히스토그램 계산
        hist, bins = np.histogram(red_hue_vl, bins=180, range=[0, 180])
        
        # 히스토그램 값을 계산
        part1 = np.sum(hist[:10])   # 0-10 (빨간색 범위)
        
        # 빨간색 범위를 설정

        low_red = np.array([0 - hue_leave, 100, 100])  
        up_red = np.array([10 + hue_leave, 255, 255])

        return low_red, up_red

    # 빨간색 범위 설정
    low_red, up_red = scan_red(hsv_image)
    mask = cv2.inRange(hsv_image, low_red, up_red)

    # 이미지 사본을 만들어 빨간색 부분을 초록색으로 변경
    green_image = image.copy()
    green_image[mask > 0] = [0, 255, 0]  # 빨간색 부분을 초록색으로 변경 (BGR 형식)

    # 결과 출력
    plt.figure(figsize=(10, 5))  # 이미지 크기 설정
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("원본 이미지")  # 제목
    plt.axis("off")  # 이미지 외의 여백 제거

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(green_image, cv2.COLOR_BGR2RGB))
    plt.title("빨간색을 초록색으로 변경")  # 제목
    plt.axis("off")  # 이미지 외의 여백 제거

    plt.show()

elif blindness == '녹색맹':
    
     # 초록색 범위를 자동으로 인식하는 함수
    def scan_green(hsv_image, hue_leave=10, sat_max=100):
        # 채널을 분리
        channel = hsv_image[:, :, 0]  # Hue 채널
        channe2 = hsv_image[:, :, 1]  # Saturation 채널
        
        # 채도가 100 이상인 부분을 분석 대상
        green_hue_vl = channel[channe2 > sat_max]
        
        # 채널 히스토그램 계산
        hist, bins = np.histogram(green_hue_vl, bins=180, range=[0, 180])
        
        # 히스토그램 값을 계산
        part1 = np.sum(hist[50:70])   # 50-70 범위 (초록색)
        
        # 초록색 범위를 설정
        low_green = np.array([50 - hue_leave, 100, 100])
        up_green = np.array([70 + hue_leave, 255, 255])

        return low_green, up_green

    # 초록색 범위 설정
    low_green, up_green = scan_green(hsv_image)
    mask = cv2.inRange(hsv_image, low_green, up_green)

    # 이미지 사본을 만들어 초록색 부분을 빨간색으로 변경
    red_image = image.copy()
    red_image[mask > 0] = [0, 0, 255]  # 초록색 부분을 빨간색으로 변경 (BGR 형식)

    # 결과 출력
    plt.figure(figsize=(10, 5))  # 이미지 크기 설정
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("원본 이미지")  # 제목
    plt.axis("off")  # 이미지 외의 여백 제거

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(red_image, cv2.COLOR_BGR2RGB))
    plt.title("초록색을 빨간색으로 변경")  # 제목
    plt.axis("off")  # 이미지 외의 여백 제거

    plt.show()

elif blindness == '청색맹':
        # 파란색 범위를 자동으로 인식하는 함수
    def scan_blue(hsv_image, hue_leave=10, sat_max=100):
        # 채널을 분리
        channel = hsv_image[:, :, 0]  # Hue 채널
        channe2 = hsv_image[:, :, 1]  # Saturation 채널
        
        # 채도가 100 이상인 부분을 분석 대상
        blue_hue_vl = channel[channe2 > sat_max]
        
        # 채널 히스토그램 계산
        hist, bins = np.histogram(blue_hue_vl, bins=180, range=[0, 180])
        
        # 히스토그램 값을 계산
        part1 = np.sum(hist[100:140])   # 100-140 범위 (파란색)
        
        # 파란색 범위를 설정
        low_blue = np.array([100 - hue_leave, 100, 100])
        up_blue = np.array([140 + hue_leave, 255, 255])

        return low_blue, up_blue

    # 파란색 범위 설정
    low_blue, up_blue = scan_blue(hsv_image)
    mask = cv2.inRange(hsv_image, low_blue, up_blue)

    # 이미지 사본을 만들어 파란색 부분을 노란색으로 변경
    yellow_image = image.copy()
    yellow_image[mask > 0] = [0, 255, 255]  # 파란색 부분을 노란색으로 변경 (BGR 형식)

    # 결과 출력
    plt.figure(figsize=(10, 5))  # 이미지 크기 설정
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("원본 이미지")  # 제목
    plt.axis("off")  # 이미지 외의 여백 제거

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(yellow_image, cv2.COLOR_BGR2RGB))
    plt.title("파란색을 노란색으로 변경")  # 제목
    plt.axis("off")  # 이미지 외의 여백 제거

    plt.show()  

elif blindness == '전색맹':
    # 모든 색을 인식하고 회색으로 바꾸기
    gray_image = np.full_like(image, [128, 128, 128]) 

    # 결과 출력
    plt.figure(figsize=(10, 5))  # 이미지 크기 설정
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("원본 이미지")  # 제목
    plt.axis("off")  # 이미지 외의 여백 제거

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(gray_image, cv2.COLOR_BGR2RGB))
    plt.title("모든 색을 회색으로 변경")  # 제목
    plt.axis("off")  # 이미지 외의 여백 제거

    plt.show()

else:
    print("해당 색맹은 없습니다.")