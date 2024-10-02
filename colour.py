from PIL import Image # 이미지 처리를 위한 pillow 라이브러리
import matplotlib.pylab as plt # 주피터 노트북 상으로 이미지 출력을 위한 plt 모듈
r = Image.open('D:/temp/pika.png') # 피카츄 이미지 객체 불러와서 r로 저장

m_size = 10  # 모자이크 크기 10
x_m =r.size[0] % m_size
y_m =r.size[1] % m_size
x_p = m_size - x_m
y_p = m_size - y_m
r_new = Image.new(r.mode, (r.size[0]+x_p, r.size[1]+y_p),(255,255,255))
r_new.paste(r, (0,0))
r=r_new # 모자이크 크기 기준으로 딱 나눠 떨어지도록 그림 수정

for i in range(0, r.size[0],m_size):
    for j in range(0, r.size[1],m_size):
        r_sum = 0
        g_sum = 0
        b_sum = 0
        for ii in range(i, i+m_size):
            for jj in range(j, j+m_size):
                rgb = r.getpixel((ii,jj))
                r_sum += rgb[0]
                g_sum += rgb[1]
                b_sum += rgb[2]
        r_a = round(r_sum/m_size**2) # rgb 평균 구하기
        g_a = round(g_sum/m_size**2)
        b_a = round(b_sum/m_size**2)
        ##### 이 사이에 코드 추가 #####
        for ii in range(i, i+m_size):
            for jj in range(j, j+m_size):
                r.putpixel((ii,jj),(r_a,g_a,b_a)) # rgb 평균 구해서 색깔 집어 넣기