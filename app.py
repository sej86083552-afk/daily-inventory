import streamlit as st
import pandas as pd

st.set_page_config(page_title="일일 재고 현황표", layout="wide")

st.title("📦 일일 재고 현황표")

st.markdown("""
엑셀에서 **장치장 / 곡종 / 재고량** 데이터를 복사해서  
아래 칸에 붙여넣고 버튼을 누르세요.
""")

raw_text = st.text_area(
    "데이터 입력 (엑셀 복사/붙여넣기)",
    height=200,
    placeholder="장치장\t곡종\t재고량\nA101\tWUR\t1600"
)

if st.button("현황표 업데이트"):
    if raw_text.strip() == "":
        st.warning("데이터를 입력해주세요.")
    else:
        rows = []
        for line in raw_text.strip().splitlines():
            parts = line.split()
            if len(parts) >= 3:
                rows.append(parts[:3])

        df = pd.DataFrame(rows, columns=["장치장", "곡종", "재고량"])
        st.success("✅ 데이터 변환 완료")
        st.dataframe(df, use_container_width=True)
