import streamlit as st

# 앱 레이아웃 설정
st.set_page_config(page_title="영화관 콤보 플래너", page_icon="🍿")

st.title("🍿 영화관 세트메뉴 조합기")
st.markdown("---")

# 1. 데이터 정의
popcorn_options = ["기본", "카라멜", "어니언"]
drink_options = ["생수", "탄산음료"]

# 2. 사이드바: 개별 선택 기능
st.sidebar.header("🎯 나만의 콤보 선택")
selected_popcorn = st.sidebar.selectbox("팝콘을 골라주세요", popcorn_options)
selected_drink = st.sidebar.selectbox("음료를 골라주세요", drink_options)

st.sidebar.success(f"**선택 완료:** {selected_popcorn} 팝콘 + {selected_drink}")

# 3. 메인 화면: 모든 조합 출력 (기존 for문 활용)
st.subheader("📋 전체 세트메뉴 목록")
st.info("파이썬의 중첩 반복문을 통해 생성된 모든 가능한 조합입니다.")

# 2개 열로 나누어 예쁘게 출력
cols = st.columns(2)
idx = 0

for popcorn in popcorn_options:
    for drink in drink_options:
        with cols[idx % 2]:
            st.warning(f"✨ **세트메뉴**: {popcorn} 팝콘, {drink}")
        idx += 1

st.markdown("---")
st.caption("Cinema Combo Algorithm v1.0 | Streamlit App")

