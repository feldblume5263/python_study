# 변수, 자료형, 조건문, 반복문, 기타 라이브러리

a = 2
b = 3
print(a + b)

first_name = 'Junhong'
last_name = 'Park'

print(first_name + ' ' + last_name)
#작은 따음표가 붙는건 문자열이다. 붙지 않는 건 다 변수이다.

print(str(a)+first_name)

a_list = ['사과', '감', '배']
print(a_list[0])
print(a_list[1])

a_list.append('수박')
print(a_list)



#딕셔너리

a_dict = {'name' : 'bob', 'age' : 24}
print(a_dict['name'])

a_dict['height'] = 187
print(a_dict)

a_dict['fruits'] = a_list
print([a_dict])
print(a_dict['fruits'][0])
#리스트는 숫자로 찾는다. 딕셔너리는 키 값으로 찾는다.

#조건문

age = 24

if age > 20:
    print('성인입니다.')
else:
    print('청소년입니다.')


#반복문

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0
for a_fruit in fruits:
    if a_fruit == '사과':
        count += 1
print(count)


people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    if person['age'] > 20:
        print(person['name'])

my_email = 'feldlbume5263@gmail.com'

# result = my_email.split('@')[1].split('.')[0]
result = my_email.replace('gmail', 'naver')
print(result)



#가상환경 개념
# venv
# dload 패키지 - url을 넣으면 이미지 다운로드가능하게 해주는 패키지

# import dload
# dload 패키지를 가져다 쓰겠다라는 의

# dload.save("https://spartacodingclub.kr/static/css/images/ogimage.png")
# dload.save("https://i.pinimg.com/564x/97/51/5b/97515b467d1a4e3ddc516331ed432d72.jpg")


#웹스크래핑(크롤링) 해보기
# 파이썬으로 브라우저 제어하기

# from selenium import webdriver
# driver = webdriver.Chrome('./chromedriver')

# driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EC%9D%B4%EC%9C%A0 ")

# import dload
#
# from bs4 import BeautifulSoup
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome('./chromedriver') # 웹드라이버 파일의 경로
# driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EC%9D%B4%EC%9C%A0")
# time.sleep(5) # 5초 동안 페이지 로딩 기다리기
#
# req = driver.page_source
# # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# # soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# # 이제 코딩을 통해 필요한 부분을 추출하면 된다.
# soup = BeautifulSoup(req, 'html.parser')
#
# thumbnails = soup.select('#imgList > div > a > img')
# i = 1
# for thumbnail in thumbnails:
#     img = thumbnail['src']
#     dload.save(img, f'img/{i}.jpg') #앞에 f를 쓰고 뒤에 {i}를 쓰면 i를 변수로 이용 가
#     i += 1
# print(thumbnails)
#
#
# driver.quit() # 끝나면 닫아주기


import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%8B%A0%EC%98%88%EC%9D%80")
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

thumbnails = soup.select('#_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div > a.thumb._thumb > img')

i = 1
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img, f'homework_day1/{i}.jpg')
    i += 1
driver.quit()