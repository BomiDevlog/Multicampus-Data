import requests
import pandas as pd

def get_lottery_draw_info(start_round, end_round):                                      # 조회 원하는 시작, 종료 라운드 입력
    no_1 = []                                                                           # 당첨번호 6개, 보너스 번호, 추첨일자, 라운드 정보 리스트 생성
    no_2 = []
    no_3 = []
    no_4 = []
    no_5 = []
    no_6 = []
    no_bonus = []
    draw_date = []
    round_num = []
    
    for round_number in range(start_round, end_round + 1):
        url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={}'   # url 주소 (라운드 정보는 비워둠)
        url = url.format(round_number)                                                 # 입력 받은 라운드 정보 추가
        req_result = requests.get(url)                                                 # 원하는 라운드 정보 추가된 url로 데이터 요청
        json_result = req_result.json()                                                # JSON 데이터 가져오기
        #print(json_result)
        print(round_number)
        
        round_num.append(round_number)                                                 # 조회된 데이터 및 라운드 정보 리스트에 입력
        draw_date.append(json_result.get('drwNoDate', None))
        no_1.append(json_result.get('drwtNo1', None))
        no_2.append(json_result.get('drwtNo2', None))
        no_3.append(json_result.get('drwtNo3', None))
        no_4.append(json_result.get('drwtNo4', None))
        no_5.append(json_result.get('drwtNo5', None))
        no_6.append(json_result.get('drwtNo6', None))
        no_bonus.append(json_result.get('bnusNo', None))
        
        dict_lottery_num = {"round":round_num, "DrawDate":draw_date, "No1":no_1, "No2":no_2, 
                            "No3":no_3, "No4":no_4, "No5":no_5, "No6":no_6, "NoBonus":no_bonus}  # 딕셔너리 자료형에 입력
        
    df_lottery_num = pd.DataFrame(dict_lottery_num)                                     # 데이터 프레임에 딕셔너리 데이터 입력
    
    return df_lottery_num                                                               # 데이터 프레임 반환

df = get_lottery_draw_info(1000,1008)                                                   # ex) 1000 ~ 1008회차까지 조회 후 결과 데이터 프레임 변수에 저장

print(df)                                                                               # 조회 결과 출력

df.to_csv("lottery_win_num.csv")                                                         # 조회 결과 csv 파일 저장. 엑셀로 열기 가능

'''
1. 각 데이터를 담을 그릇을 선언 (리스트라는 자료형)
2. 당첨번호 url로 접근해 결과값 얻음
3. 결과 값에서 추첨날짜, 추첨번호를 각 리스트에 담음
4. 원하는 회차만큼 2~3번 반복
5. 데이터 프레임이라는 그릇에 전체 데이터 담음
6. 엑셀에서 열기 가능한 csv확장자 파일에 저장
'''