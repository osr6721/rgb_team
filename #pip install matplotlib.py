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
image_path = input("이미지 파일 경로를 입력하세요: ")
image = cv2.imread(image_path)

# 이미지를 HSV 색상으로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

if blindness == '녹색맹':
    # 녹색 범위 설정 함수
    def scan_green(hue_leave=10, sat_min=100, val_min=100):
        low_green = np.array([35 - hue_leave, sat_min, val_min])
        up_green = np.array([85 + hue_leave, 255, 255])
        return low_green, up_green

    # 녹색 범위 설정
    low_green, up_green = scan_green()

    # 녹색 범위의 마스크 생성
    mask = cv2.inRange(hsv_image, low_green, up_green)

    # 이미지 사본을 만들어 녹색 부분을 빨간색으로 변경
    red_image = image.copy()
    red_image[mask > 0] = [0, 0, 255]  # 녹색 부분을 빨간색으로 변경

    # 결과 출력
    plt.figure(figsize=(10, 5))  # 이미지 크기 설정
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("원본 이미지")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(red_image, cv2.COLOR_BGR2RGB))
    plt.title("녹색을 빨간색으로 변경")
    plt.axis("off")

    plt.show()

elif blindness == '적색맹':
    # 빨간색 범위를 설정하는 함수
    def scan_red(hue_leave=10, sat_min=100, val_min=100):
        low_red1 = np.array([0, sat_min, val_min])
        up_red1 = np.array([10 + hue_leave, 255, 255])

        low_red2 = np.array([170 - hue_leave, sat_min, val_min])
        up_red2 = np.array([180, 255, 255])

        return (low_red1, up_red1), (low_red2, up_red2)

    # 빨간색 범위 설정
    (red_low1, red_up1), (red_low2, red_up2) = scan_red()

    # 빨간색 범위의 마스크 생성
    mask1 = cv2.inRange(hsv_image, red_low1, red_up1)
    mask2 = cv2.inRange(hsv_image, red_low2, red_up2)
    mask = cv2.bitwise_or(mask1, mask2)

    # 이미지 사본을 만들어 빨간색 부분을 녹색으로 변경
    green_image = image.copy()
    green_image[mask > 0] = [0, 255, 0]  # 빨간색 부분을 녹색으로 변경

    # 결과 출력
    plt.figure(figsize=(10, 5))  # 이미지 크기 설정
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("원본 이미지")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(green_image, cv2.COLOR_BGR2RGB))
    plt.title("빨간색을 녹색으로 변경")
    plt.axis("off")

    plt.show()

elif blindness == '청색맹':
    # 파란색 범위 설정 함수
    def scan_blue(hue_leave=10, sat_min=100, val_min=100):
        low_blue = np.array([100 - hue_leave, sat_min, val_min])
        up_blue = np.array([130 + hue_leave, 255, 255])
        return low_blue, up_blue

    # 파란색 범위 설정
    low_blue, up_blue = scan_blue()

    # 파란색 범위의 마스크 생성
    mask = cv2.inRange(hsv_image, low_blue, up_blue)

    # 이미지 사본을 만들어 파란색 부분을 초록색으로 변경
    green_image = image.copy()
    green_image[mask > 0] = [0, 255, 0]  # 파란색 부분을 초록색으로 변경

    # 결과 출력
    plt.figure(figsize=(10, 5))  # 이미지 크기 설정
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("원본 이미지")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(green_image, cv2.COLOR_BGR2RGB))
    plt.title("파란색을 초록색으로 변경")
    plt.axis("off")

    plt.show()

elif blindness == '전색맹':
    # 이미지를 흑백(그레이스케일)으로 변환
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 결과 출력
    plt.figure(figsize=(10, 5))  # 이미지 크기 설정
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("원본 이미지")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(gray_image, cmap='gray')
    plt.title("흑백 이미지")
    plt.axis("off")

    plt.show()

else:
    print("해당 색맹은 없습니다.")