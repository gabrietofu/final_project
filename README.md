# 🍞 군집분석 기반 빵 맛집 추천 서비스

</br>

## 👩🏻‍💻 팀원

<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/DIB-PP"><img src="https://avatars.githubusercontent.com/u/155515440?s=64&v=4" width="100px;" alt="황기쁨"/><br /><sub><b>황기쁨 (팀장)</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/augnoel"><img src="https://avatars.githubusercontent.com/u/157769634?s=64&v=4" width="100px;" alt="정노을"/><br /><sub><b>정노을</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/gabrietofu"><img src="https://avatars.githubusercontent.com/u/157769636?v=4" width="100px;" alt="이정희"/><br /><sub><b>이정희</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/dataosean"><img src="https://avatars.githubusercontent.com/u/156559007?s=64&v=4" width="100px;" alt="배시현"/><br /><sub><b>배시현</b></sub></a><br /></td>      
    </tr>
  </tbody>
</table>

</br>

## 🚩 분석 목적

### 1. 사용자가 원하는 특성에 적합한 빵집 추천 서비스의 부재

### 2. 서울 소재 8개구 빵집 리뷰 데이터를 활용한 군집 분석 결과 기반의 추천 서비스 제작


## ✏ 프로젝트 개괄
- 소요 기간 : 4주
- 참여 인원 : 4명
- 사용 언어·툴
</br>
<table>
  <tbody>
    <tr>
      <td align="center"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOolZ-W3pvrU-iwrA7fZe3U-xxFRMb97S0Ti5K_g9ZRg&s" width="100px;" alt="GPT-4-Turbo"/><br /><sub><b>GPT 4 Trubo</b></sub></a><br /></td>
      <td align="center"><img src="https://velog.velcdn.com/images/jaehye0ng2/post/91fe86a6-6825-400a-bd91-e56ae038c083/image.png" width="100px;" alt="QGIS"/><br /><sub><b>QGIS</b></sub></a><br /></td>
      <td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" width="100px;" alt="Python"/><br /><sub><b>Python</b></sub></a><br /></td>
      <td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" width="100px;" alt="scikit learn"/><br /><sub><b>scikit learn</b></sub></a><br /></td>
      <td align="center"><img src="https://blog.zarathu.com/posts/2023-02-01-streamlit/logo.jpeg" width="100px;" alt="streamlit"/><br /><sub><b>streamlit</b></sub></a><br /></td>  
    </tr>
  </tbody>
</table>

</br>






















일정

3월 셋째주 : 데이터 수집, 개별 학습(머신러닝, 크롤링)

3월 넷째주 : 데이터셋 만들기(만약 일찍 끝나면 바로 모델링)

4월부터 : 모델링







Q&A(오전:소현 T)
튜터님 안녕하세요, 최종 프로젝트 관련해서 함께할수도 있는 멤버들과 프로젝트를 구상해보고있는데요,
구상 과정에서 의문사항이 생겨 방문드리기 전 서면으로 질문사항 먼저 남기려고합니다.
시간은 14시 30분 정도 방문하려고하는데 혹시 14시 30분 안 되신다면 가능하신 시간 말씀해주시면 그 시간에 방문하겠습니다 :-)

Q.1 데이터셋 관련
 1) 대용량 데이터라고 불리려면 '행의 개수'가 몇 개 정도 됐을때 대용량 데이터라고 할 수 있나요?
 2) 대용량 데이터셋을 구축한다고했을때 데이터셋을 하나로, n개로 나누는 것 중에서 어떤 방식을 추천하시는지와 현업에서는 어떤식으로 대용량 데이터셋을 구축하시는지 궁금합니다.
 3) 추가적으로 대용량 데이터를 n개의 데이터셋으로 나눠서 구축하고 머신러닝 모델링을 할 때 MEREGE, CONCAT, JOIN해서 모델링해도 무방한지도 궁금합니다.

Q.2
17년도부터 22년까지의 데이터를 학습시켜서 23년도(1년 뒤)의 매출을 예측하고자하는데
저희가 생각하고있는 방식은 다음과 같습니다.
1. 17년도부터 21년도의 독립변수를 가지고서 22년도의 매출을 예측하고 실제 22년도 매출과 비교해서 모델의 정확성 체크
2. 18년도부터 22년도의 독립변수를 가지고서 23년도(1년 뒤 매출)의 매출을 예측
3. 19년도부터 23년도의 독립변수를 가지고서 24년도(2년 뒤 매출)의 매출을 예측
여기서부터 질문사항입니다.
 1) 이 때 23년도(1년 뒤)의 독립변수는 별도의 예측모델을 만들어서 값을 예측해야하는 것인지
 2) 종속변수인 '매출'을 독립변수에 넣어서 학습을 시켜도 무방한지
에 대한 튜터님의 의견 여쭙고싶습니다.
