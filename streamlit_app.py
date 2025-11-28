import streamlit as st

st.set_page_config(page_title="지민이의 등교 준비", layout="centered")

# 배경 이미지(학교) - Unsplash 이미지 사용
BACKGROUND_IMG = "https://images.unsplash.com/photo-1513258917318-a3406841bd33?auto=format&fit=crop&w=1400&q=80"

css = """
<style>
.stApp {
    background-image: url('{{IMG}}');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
.overlay {
    position: fixed; top:0; left:0; width:100%; height:100%;
    background: rgba(255, 182, 193, 0.35); /* 연한 핑크 오버레이 */
    z-index: 0;
    pointer-events: none;
}
.content {
    position: relative; z-index: 1; padding: 2rem 1rem;
}
.big-title {
    font-size:32px; font-weight:700; color:#33052d; margin-bottom:6px;
}
.subtitle {
    color:#4a083f; margin-bottom:18px;
}
.small-instruction { font-size:14px; color:#4a083f; margin-bottom:18px; }
</style>
<div class="overlay"></div>
"""
css = css.replace("{{IMG}}", BACKGROUND_IMG)
st.markdown(css, unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='content'>", unsafe_allow_html=True)
    st.markdown("<div class='big-title'>🎈 지민이의 등교 준비</div>", unsafe_allow_html=True)
    # 게임 방법 내용을 타이틀 아래에 작은 글씨로 표시
    st.markdown("<div class='small-instruction'>지민이가 학교에 제시간에 가도록 도와줘! 그러기 위해선 시계를 정확하게 읽어줘야 해! 모두 지민이를 도와줘!</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        # 게임 방법 버튼 제거 — 설명은 타이틀 아래에 고정 텍스트로 표시됨
        pass

    with col2:
        if st.button("게임 시작"):
            st.success("게임을 시작합니다! 준비가 완료되면 다음 화면으로 이동합니다.")
            st.write("(여기에는 실제 게임 로직/화면이 들어갑니다 — 원하시면 구현해드릴게요.)")

    st.markdown("</div>", unsafe_allow_html=True)

