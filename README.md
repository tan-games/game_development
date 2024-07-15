# game_development
자랑스러운 신원고등학교 창업 동아리 게임 제작 GitHub

## 게임 기본 구조
엔티티, 폰트 파일 등 -> general 파일 -> main 파일

~~main과 general 파일의 병합에 대해서는 고민 중이다.~~

## 게임 기획 결과
### 기본 배경
정글, 도시, 바닷가(점프와 슬라이딩키를 서로 반대로 설정)   >>   이렇게 4가지 맵으로 차례대로 구성 , 공허세계 끝날시 다시 정글로 이어지는 구상 

### 스토리
이재윤이 "날아오는 김시우"와 "총을 쏘는 최승원"을 피해 모험을 떠나는 이야기 

### 캐릭터의 목적
이재윤 _ 장애물들을 피해 탐험함
김시우 _ 특정 높이에서 날아와 이재윤을 공격함
최승원 _ 이재윤이 화면에 잡힐때부터 총을 쏘기 시작하여 공격함 

### 키 설정
S키 > 화면의 1/3정도까지 점프
D키 > 슬라이딩 

### 오브젝트
1. 트램펄린 > 밟으면 원래의 점프에 비해 2/3정도까지 점프 (당연히 밟으면 점프한 상태로 앞으로 나아가야하고, 달려가면서 밟아야 하는 설정이어야함) 

2. 거울(땅과 하늘에 놓여있어야함) > 밟으면 하늘을 거꾸로 매달려서걸어다닐 수 있음 (땅에 있는 거울을 밟으면 하늘에 있는 거울로 나와서 상,하가 반전된채로 게임 플레이) 

3. 각종 돌멩이 > 밟으면 피가 한칸씩 줄게 됨(맵 중간중간 땅에 설치) 

4. 햄버거, 술 > 피가 늘게 하거나(햄버거), 3초동안 무적상태 즉, 
투명상태가 됨(재윤 선호 주종 술) 

5. 고드름(1/2, 1/4) > 하늘에 설치되어있는 장애물로 돌멩이와 마찬가지로 닿으면 피가 한칸씩 줄음 

6. 김시우 및 최승원 > 플레이어에게 공격을 가하며 피를 한칸씩 줄게함 

### 기본 설정
1. 이재윤은 왼쪽에서 오른쪽을 향해 달려감. 
2. 김시우는 오른쪽에서 왼쪽을 향해 날아옴
3. 최승원은 맵 중간중간 나타나 왼쪽을 향해 총을 쏨, 이재윤과 부딪히면 사라짐
4. 이재윤의 기본 피는 3칸으로 설정
5. 장애물이나 투사체에 맞으면 피가 한칸씩 깎이고 3칸이 모두 깎이는 즉시 게임 종료
6. 빨간색 포션을 먹으면 피가 한칸 증가 (단, 이미 3칸일 경우는 해당 없음)
7. 파란색 포션을 먹으면 무적상태가 되어 모든 장애물 및 투사체를 통과
8. 게임을 플레이 하면 할수록 플레이어 이동속도가 점점 빨라지게 됨
초기 속도: 플레이어는 10cm/초로 시작
시간 기반 증가: 매 20초마다 1cm/초씩 증가
예: 40초 후 속도 = 10 + 2 * 1 = 12cm /초
거리 기반 증가: 매 5000cm마다 1cm/초씩 증가
예: 10000 단위 후 속도 = 10 + 2 * 1 = 12 cm/초
최대 속도: 30 cm/초를 넘지 않음