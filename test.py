print("HELLO WORLD!") #HELLO WORLD 출력
print("이름: 박주희")#이름 출력
print("학번: 202101533")#학번 출력
print("학과: 컴퓨터공학부")#학과 출력
print("좋아하는 과목: 정보") #좋아하는 과목 출력
print("Hufs. Division of Computer Engineering")


#입력된 n만큼 'computer'출력하기(n > 2)
n = int(input()) #n입력받기
if n > 2:
	for i in range(n):
		print("computer") #입력 받은 n만큼 print 반복하기
	
else:
	print("3이상 입력하세요") #2이상이 아닌 경우
	
