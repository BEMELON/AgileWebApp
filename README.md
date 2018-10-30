# AgileWebApp
make agile web app
1 . How to Start
- easy_install django-messages  
- Konlpy(자연어 처리, 비트 설정 체크)  
    `pip install konlpy`   (konlpy 공식 사이트 : http://konlpy.org/ko/latest/)  
    `pip install pytagcloud` (wordcloud를 만드는 모듈 입니다. )  
    `pip install pygame` (wordcloud 를 만드는데 필요한 모듈입니다.)  
    `pip install simplejson`   
    `pip install matplotlib`  
    `pip install numpy`  
    `pip install psycopg2`  
2. 폰트 설정
    -pytagcloud 모듈 설치가 선행  
    1. pytagcloud 모듈이 설치된 폴더로 이동해야됩니다.  
     (C:\Users\사용자계정\AppData\Local\Programs\Python\Python36\Lib\site-packages\pytagcloud)  
     주로 이폴더에 pytagcloud 설치가 되는데, 사용자마다 위치가 조금씩 다를 수 있습니다.  
    2. pytagcloud 에서 fonts 폴더로 이동합니다.   
    3. github에 나눔 글꼴 파일을 같이 올렸습니다. (NanumGothic)  
     (http://ngio.tistory.com/m/5264 여기서도 받을 수 있습니다.)  
    4. 나눔글꼴파일(NanumGothic.ttf)를 2번에서의 fonts 폴더에 넣어주고, fonts.json 을 열어줍니다.  
    5. 적절한 위치?에 아래와 같은 코드를 추가해줍니다.  
    ```
    {  
    "name": "Nanum Gothic",  
    "ttf": "NanumGothic.ttf",  
    "web": "http://fonts.googleapis.com/earlyaccess/nanumgothic.css"  
  	},  
    ```
3. 엑셀 output
- http://www.hanul93.com/openpyxl-basic/  
위 사이트를 따라 openyxl설치  

-https://pypi.python.org/pypi/xlwt 
-위 홈페이지에서 최신 버전의 xlwt를 다운로드하고  
`pip install xlwt`
4. 차트, 차트 이미지 추출  
`pip install plotly --upgrade`  
`pip install ipython`  
