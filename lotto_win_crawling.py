import requests

def get_draw_lottoery_number(round_number):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={}'   # url 주소 (라운드 정보는 비워둠)
    url = url.format(round_num)                                                    # 입력 받은 라운드 정보 추가
    req_result = requests.get(url)                                                 # 원하는 라운드 정보 추가된 url로 데이터 요청
    json_result = req_result.json()                                                # JSON 데이터 가져오기
    print(json_result)                                                             # JSON 데이터 출력, 직접 브라우저에서 접속한 결과와 동일
    # print(type(json_result))

    # success_flag = json_result.get('returnValue', None)
    draw_date = json_result.get('drwNoDate', None)                                 # 추첨 일자 저장
    no_1 = json_result.get('drwtNo1', None)                                        # 당첨 번호 및 보너스 번호 저장
    no_2 = json_result.get('drwtNo2', None)
    no_3 = json_result.get('drwtNo3', None)
    no_4 = json_result.get('drwtNo4', None)
    no_5 = json_result.get('drwtNo5', None)
    no_6 = json_result.get('drwtNo6', None)
    no_bonus = json_result.get('bnusNo', None)
    
    # print('Success flag :', success_flag)
    print('round_num   : %s'%round_num)                                            # 라운드 정보, 당첨일자, 당첨번호 출력
    print('Draw Date   :', draw_date)
    print('Draw Number : %d, %d, %d, %d, %d, %d, bonus(%d)'%(no_1,no_2,no_3,no_4,no_5,no_6,no_bonus))

round_num = input('Input round number : ')
get_draw_lottoery_number(round_number=round_num)

#for n in range(5): 
#    # round_num = input('Input round number : ')   
#    round_num = str(n+1)
#    get_draw_lottoery_number(round_number=round_num)