a = input("단어를 입력하세요")
b = len(a)                      #단어를 입력받고 그 단어의 길이값을 받는다 
for i in range(0, b):           #0부터 a에서 입력받는 단어의 길이값을 반복하는 범위로 설정한다
    if (a[i] != a[b - (i+1)]):  #이후 if 문을 이용하여 각각 끝값부터 대조되는 값이 같지 않다면 False를 출력하고 프로그램을 종료시킨다
        print("False")
        break
else:
    print("True")               #만약 그렇지 않다면 True 로 회문이라는것을 인정하고 프로그램을 종료시킨다   
print("!")