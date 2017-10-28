import turtle as t
import random
#준비 하기
t.shape("circle")
t.speed(0)
t.pensize(7)
t.pencolor("black")
t.bgcolor("yellow")

#좌상단으로 펜 옮기기
t.up()
t.goto(-380,320)

#500X500 사이즈의 큰 네모 만들기
t.down()
for x in range(4):
    t.fd(500)
    t.rt(90)
    
#장애물 만들기
t.up()
t.goto(-280,220)
t.down()
t.seth(0)

#1번 장애물
for x in range(4):
    t.fd(50)
    t.rt(90)
    
#2번 장애물
t.up()
t.goto(-30,220)
t.down()
t.seth(0)
for x in range(4):
    t.fd(50)
    t.rt(90)
    
#3번 장애물
t.up()
t.goto(-280,-30)
t.down()
t.seth(0)
for x in range(4):
    t.fd(50)
    t.rt(90)
#4번 장애물
    
t.up()
t.goto(-30,-30)
t.down()
t.seth(0)
for x in range(4):
    t.fd(50)
    t.rt(90)

#사각형의 중앙으로 펜 옮기기
t.up()
t.goto(-130,70)

#초기 랜덤 값 세팅
t.seth(random.randint(1,360))

#무한대로 1씩 직진하며 x와 y의 좌표를  저장
while True:
    a = t.xcor()
    b = t.ycor()
    #x와 y의 좌표가 내가 그린 네모밖의 좌표값으로 갈 때
    if t.xcor()>120 or t.xcor()<-380 or t.ycor()<-180 or t.ycor()>320:
        #입사x좌표, 입사y좌표, 입사각을 저장한다.
        x = t.xcor()
        y = t.ycor()
        ia = t.heading()
#벽에 부딛힐 때
        #오른쪽 벽에 부딛힐 때
        if x>120:
            #위에서 아래로
            if y<b:
                t.rt(2*(ia-270))
            #아래에서 위로
            else:
                t.lt(2*(90-ia))
        #왼쪽 벽에 부딛힐 때
        if x<-380:
            #위에서 아래로
            if y<b:
                t.lt(2*(270-ia))
            #아래에서 위로
            else:
                t.rt(2*(ia-90))
        #아래쪽 벽에 부딛힐 때
        if y<-180:
            #오른쪽에서 왼쪽으로
            if x<a:
                t.rt(2*(ia-180))
            #왼쪽에서 오른쪽으로
            else:
                t.lt(2*(360-ia))
        #위쪽 벽에 부딛힐 때
        if y>320:
            #오른쪽에서 왼쪽으로
            if x<a:
                t.lt(2*(180-ia))
            #왼쪽에서 오른쪽으로
            else:
                t.rt(2*ia)

#1번 장애물에 부딛힐 때
    if -280<t.xcor() and t.xcor()<-230 and 170<t.ycor() and t.ycor()<220:
        ia = t.heading()
        x_1 = t.xcor()
        y_1 = t.ycor()
        #왼쪽 벽에 부딛 힐 때
        if x_1<=-280+1 and 170+1<=y_1 and y_1<=220-1:
            #위에서 아래로
            if y_1<b:
                t.rt(2*(ia-270))
            #아래에서 위로
            else:
                t.lt(2*(90-ia))
        #오른쪽 벽에 부딛 힐 때
        if x_1>=-230-1 and 170+1<=y_1 and y_1<=220-1:
            #위에서 아래로
            if y_1<b:
                t.lt(2*(270-ia))
            #아래에서 위로
            else:
                t.rt(2*(ia-90))
        #위쪽 벽에 부딛 힐 때
        if -280+1<=x_1 and x_1<=-230-1 and y_1>=220-1:
            #오른쪽에서 왼쪽으로
            if x_1<a:
                t.rt(2*(ia-180))
            #왼쪽에서 오른쪽으로
            else:
                t.lt(2*(360-ia))
        #아래쪽 벽에 부딛 힐 때
        if -280+1<=x_1 and x_1<=-230-1 and y_1<=170+1:
            #오른쪽에서 왼쪽으로
            if x_1<a:
                t.lt(2*(180-ia))
            #왼쪽에서 오른쪽으로
            else:
                t.rt(2*ia)

#2번 장애물에 부딛힐 때
    if -30<t.xcor() and t.xcor()<20 and 170<t.ycor() and t.ycor()<220:
        ia = t.heading()
        x_2 = t.xcor()
        y_2 = t.ycor()
        #왼쪽 벽에 부딛 힐 때
        if x_2<=-30+1 and 170+1<=y_2 and y_2<=220-1:
            #위에서 아래로
            if y_2<b:
                t.rt(2*(ia-270))
            #아래에서 위로
            else:
                t.lt(2*(90-ia))
        #오른쪽 벽에 부딛 힐 때
        if x_2>=20-1 and 170+1<=y_2 and y_2<=220-1:
            #위에서 아래로
            if y_2<b:
                t.lt(2*(270-ia))
            #아래에서 위로
            else:
                t.rt(2*(ia-90))
        #위쪽 벽에 부딛 힐 때
        if -30+1<=x_2 and x_2<=20-1 and y_2>=220-1:
            #오른쪽에서 왼쪽으로
            if x_2<a:
                t.rt(2*(ia-180))
            #왼쪽에서 오른쪽으로
            else:
                t.lt(2*(360-ia))
        #아래쪽 벽에 부딛 힐 때
        if -30+1<=x_2 and x_2<=20-1 and y_2<=170+1:
            #오른쪽에서 왼쪽으로
            if x_2<a:
                t.lt(2*(180-ia))
            #왼쪽에서 오른쪽으로
            else:
                t.rt(2*ia)

 #3번 장애물에 부딛힐 때
    if -280<t.xcor() and t.xcor()<-230 and -80<t.ycor() and t.ycor()<-30:
        ia = t.heading()
        x_3 = t.xcor()
        y_3 = t.ycor()
        #왼쪽 벽에 부딛 힐 때
        if x_3<=-280+1 and -80+1<=y_3 and y_3<=-30-1:
            if y_3<b:
                t.rt(2*(ia-270))
            #아래에서 위로
            else:
                t.lt(2*(90-ia))
        #오른쪽 벽에 부딛 힐 때
        if x_3>=-230-1 and -80+1<=y_3 and y_3<=-30-1:
            #위에서 아래로
            if y_3<b:
                t.lt(2*(270-ia))
            #아래에서 위로
            else:
                t.rt(2*(ia-90))
        #위쪽 벽에 부딛 힐 때
        if -280+1<=x_3 and x_3<=-230-1 and y_3>=-30-1:
            #오른쪽에서 왼쪽으로
            if x_3<a:
                t.rt(2*(ia-180))
            #왼쪽에서 오른쪽으로
            else:
                t.lt(2*(360-ia))
        #아래쪽 벽에 부딛 힐 때
        if -280+1<=x_3 and x_3<=-230-1 and y_3<=-80+1:
            #오른쪽에서 왼쪽으로
            if x_3<a:
                t.lt(2*(180-ia))
            #왼쪽에서 오른쪽으로
            else:
                t.rt(2*ia)

#4번 장애물에 부딛힐 때
    if -30<t.xcor() and t.xcor()<20 and -80<t.ycor() and t.ycor()<-30:
        ia = t.heading()
        x_4 = t.xcor()
        y_4 = t.ycor()
        #왼쪽 벽에 부딛 힐 때
        if x_4<=-30+1 and -80+1<=y_4 and y_4<=-30-1:
            #위에서 아래로
            if y_4<b:
                t.rt(2*(ia-270))
            #아래에서 위로
            else:
                t.lt(2*(90-ia))
        #오른쪽 벽에 부딛 힐 때
        if x_4>=20-1 and -80+1<=y_4 and y_4<=-30-1:
            #위에서 아래로
            if y_4<b:
                t.lt(2*(270-ia))
            #아래에서 위로
            else:
                t.rt(2*(ia-90))
        #위쪽 벽에 부딛 힐 때
        if -30+1<=4_3 and x_4<=20-1 and y_4>=-30-1:
            #오른쪽에서 왼쪽으로
            if x_4<a:
                t.rt(2*(ia-180))
            #왼쪽에서 오른쪽으로
            else:
                t.lt(2*(360-ia))
        #아래쪽 벽에 부딛 힐 때
        if -30+1<=x_4 and x_4<=20-1 and y_4<=-80+1:
            #오른쪽에서 왼쪽으로
            if x_4<a:
                t.lt(2*(180-ia))
            #왼쪽에서 오른쪽으로
            else:
                t.rt(2*ia)
                
    t.fd(1)

