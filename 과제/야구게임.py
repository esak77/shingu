#-*-coding:utf-8-*-


n="YES"
while(n=="YES"):
    import random
    score=["0","0","0"]
    score[0]=str(random.randint(1,9))
    score[1]=score[0]
    score[2]=score[0]

    while (score[0] == score[1]):
        score[1]=str(random.randint(1,9))
    while (score[0] == score[2] or score[1] == score[2]):
        score[2]=str(random.randint(1,9))


    total = 0
    strike = 0
    ball = 0

    print "Play BaseBall Game Play"
    while ( strike < 3):
        print "숫자를 입력하세요"
        count = str(raw_input())
        x=count.isdigit()
        d= len(count)
        if(count == "0"):
            print "종료합니다."
            break
        elif(d!=3):
            print"3자리 숫자를 입력하세요."
            continue
        elif(x==False):
            print "숫자가 아닙니다."
            continue
        elif(count[0] == count[1] or count[1] == count[2] or count[0] == count[2]):
            print "숫자가 중복됩니다."
            continue
    
        strike = 0
        ball = 0

        for i in range(0,3):
            for j in range(0,3):
                if(count[i]==str(score[j]) and i == j):
                    strike += 1
                elif count[i] == str(score[j]) and i != j:
                    ball += 1
        print strike,' Strike', ball , 'Ball'
        total += 1

    if(count == "0"):
            break
    print 'You wint this game. You`played', total , 'times' , "\n"
    
    print "또 하시겠습니까?(YES/NO)"
    result = str(raw_input())
    result = result.upper()
    if(result == "YES"):
        print "다시시작합니다."
    elif(result == "NO"):
        print "종료합니다."
        break

    elif(result != "NO"):
         while( result != "YES" or result != "NO"):
             print "다시 입력하세요"
             result = str(raw_input())
             result = result.upper()
             if(result == "YES" or result == "NO"):
                  break
         if(result=="NO"):
               print "종료합니다"
               break
        




