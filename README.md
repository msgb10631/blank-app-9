import streamlit as st

# 1. 앱 제목 및 설명 설정
st.title("🍿 영화관 세트메뉴 조합기")
st.write("파이썬 이중 for문을 활용해 모든 팝콘과 음료의 조합을 생성합니다.")

# 2. 데이터 정의 (기존 코드)
popcorn_options = ["기본", "카라멜", "어니언"]
drink_options = ["생수", "탄산음료"]

st.divider()  # 화면 분할 선

# 3. 레이아웃 구성 (메인 화면에 카드 형태로 배치)
st.subheader("📋 생성된 세트메뉴 리스트")

# 2열(Column) 레이아웃을 사용해 화면을 효율적으로 씁니다.
col1, col2 = st.columns(2)

# 인덱스를 활용해 왼쪽/오른쪽 열에 번갈아 출력하기 위한 변수
count = 0

# 4. 이중 for문 돌며 화면에 출력
for popcorn in popcorn_options:
    for drink in drink_options:
        # 출력할 텍스트 포맷팅
        menu_text = f"**세트메뉴:** {popcorn} 팝콘, {drink}"
        
        # col1과 col2에 번갈아가며 깔끔한 박스(info) 형태로 출력
        if count % 2 == 0:
            col1.info(menu_text)
        else:
            col2.info(menu_text)
        
        count += 1