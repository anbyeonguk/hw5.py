def read_single_digit():
    digits ={
        0: '영',
        1: '일',
        2: '이',
        3: '삼',
        4: '사',
        5: '오',
        6: '육',
        7: '칠',
        8: '팔',
        9: '구'
    }
    return digits

n = input('세 자리 정수 입력: ')

def read_number(number):
    digits = read_single_digit()
    if number[0] != '0':
       a= digits[int(number[0])]
    if number[1] != '0':
      b=digits[int(number[1])]
    if number[2] != '0':
       c=digits[int(number[2])]
    print(a, b, c)
    

read_number(n)