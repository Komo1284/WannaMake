"""
시작에 앞서
 
나는 아직 학원에서 이제 프로그래밍 언어를 어떤식으로 쓴다 정도만 배운 이제 막 코딩을 시작한 사람이다.
그래서 코딩을 해서 프로그램을 완성형으로 만든다던지 그런거 아직 할 줄 모른다...
언젠가는 내가 짠 코드를 이용해서 프로그램으로써 활용할 수 있는 날이 오면 좋겠다.
 
급하게 파이썬exe파일 만들기 등을 검색해보았는데 무슨 말인지 전혀 알아먹을 수가 없었고 어떤식으로 작성,작동하는 건지 조차 감이 잡히지 않는다. 이제 시작한 참이니 당연할 수도 있겠다. 
 
그래도 지금부터라도 이런거 하나하나 만들어가보면서 조금씩 어떤식으로 하면 완성형이 되는지 알아가 보려고 한다.
 
어떤 프로그램을 만들 것인가?
올해 초부터 아직까지 만남을 이어오고 있는 중학교떄 친구들과 함께 계를 시작했다.
계자체가 아에 처음이라 어떤식으로 진행이 되고 돈을 걷고, 사용하고.. 전혀 알지 못하는 상태였다.
그러나 이미 한두번 계에 참가한 적이 있는 친구들의 조언(?)과 여기저기 알아본 결과를 토대로 나름의 계칙을 정하기로 하였다.
 
 
1. 회장은 1년에 한번씩 돌아가면서 한다.(생일순)

2. 계모임은 1년에 2번
    여름 여행(계곡 or 풀빌라 등) 겨울 송년회
    (회장 주도 및 계원 합의하에 변동가능)

3. 모임비는 5명이상(2/3이상)참석일때 사용
    (단, 모임은 최소 한달전에 날짜를 정해야한다. 계모임(여름, 겨울)에 한해 
    해당되며 그 외에 5명이상이 모이게 될 경우 미리 공지하였고 불참자들이 동의하면 계비 사용 가능)

4. 계칙을 바꿀땐 찬반투표를 해서 5명이상(2/3이상)이 참가하고 과반의 투표를 따른다.

5. 경조사(생일,결혼식 등), 장례식등 개인부조는 각자하되
계비에서 5만원 이하의 화환(결혼, 장례식)을 그 당시의 회장이 정한다.
 
 
처음에 이런 계칙을 세운 이후에도 여러가지 얘기가 나와서 추가된 것들이 있지만 하나하나 기록해놓지 않아서 있는 것만 기록해두었다.
나중에, 추가된 계칙등을 정리한 것도 새롭게 업데이트하여 공지해두는 것이 좋을 것 같다.
 
다같이 모임비로써 사용함에 있어서는 불참자가 있더라도 동의를 받고 사용은 하되 총 계참가 인원에 비례하여 참가인원분만큼만 사용하도록 정했다. 예) 6명중 5명이 참가했다면 총 계비의 5/6만 사용하기로 함
 
이 점을 생각하여 총 사용된 여행비와 남아있는 계비등을 계산하여 이번여행에 참가한 인원이 각자 얼마를 부담하면 되는지 각자 사용한 금액만 입력하면 바로 계산해주는 프로그램을 짜보기로 했다.
 
코드를 직접 짜보자!
"""

a = int(input("계에 참가하고 있는 총 인원 수>>"))
b = int(input("이번 여행에 참가한 총 인원 수>>"))
c = int(input("현재 남은 총 계비는>>"))
x = (c*b)//a 
print("현재 사용할 수 있는 계비는",x,"원 입니다.")

m1 = 1 #친구1
m2 = 1 #친구2
m3 = 1 #친구3
m4 = 1 #친구4
m5 = 1 #친구5

result1 = 0 #친구1의 사용금액
result2 = 0 #친구2의 사용금액
#돈을 낸사람의 수에 따라 유동적으로 추가 및 제거가능

while m1 != 0 : 
    m1 = int(input("친구1이 사용한 금액은 >>")) 
    result1 += m1
    print("친구1이 총 사용한 금액은",result1,"원 입니다.")
while m2 != 0 : 
    m2 = int(input("친구2가 사용한 금액은 >>")) 
    result2 += m2
    print("친구2가 총 사용한 금액은",result2,"원 입니다.")
#마찬가지로 돈을 쓴 사람에 따라 반복문 개수 따로 설정
#이것 또한 돈을 낸사람이 몇명인지 숫자를 입력받게 하여 따로 반복문을 돌릴 수 있을 것 같지만 당장에 그런 코드가 떠오르지 않아 현재 내 머리로 가능한 수준으로만 만들었다.

result = result1 + result2 #총 사용금액
print("총 사용금액은",result,"원 입니다.")
y = 0 #추가로 내야할 돈
z = 0 #추가비용 인원 수대로 나눈 금액

if result > x : 
    y = result - x 
    z = y // b 
    m1 = z - result1 
    m2 = z - result2 
    m3 = z 
    m4 = z 
    m5 = z 
    print("친구1이 내야할 금액은",m1,"원 입니다.") 
    print("친구2가 내야할 금액은",m2,"원 입니다.") 
    print("친구3이 내야할 금액은",m3,"원 입니다.") 
    print("친구4가 내야할 금액은",m4,"원 입니다.") 
    print("친구5가 내야할 금액은",m5,"원 입니다.")
else: print("계비만으로 충당가능한 금액이기에 추가지불할 필요가 없습니다.")
 
 
"""
느낀점
실제로 이 코드를 이용하여 쉽게 정산을 완료했다.
물론 이 코드를 짤 시간에 그냥 계산기 두드리면서 계산했으면 더 빨리 계산 가능했을지도 모르겠다.
 
그래도 이런 시도하나하나 해보는 것이 내 코딩인생에 어떤식으로든 도움이 될거라 믿어 
의심치않고, 이런 프로그램들을 짜보면서 당연히 언젠간 막히는 날도 있을 것이다. 그럴 때, 어떤 방법을 사용하면 되는가 구글링을 해보며 새로 배우는 것도 많을 것이고, 
나아가 exe파일등을 만들어 다른사람들도 무언가 필요에 의해 내가 짠 코드를 이용해 쉽게 계산하고 일 처리가 가능하게 되었으면 좋겠다고 생각한다.
"""
