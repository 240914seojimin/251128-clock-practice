import streamlit as st

st.set_page_config(page_title="지민이의 등교 준비", layout="centered")

# 배경 이미지(핑크톤 소녀 방) - Unsplash 이미지 사용
BACKGROUND_IMG = "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=1400&q=80"

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
</style>
<div class="overlay"></div>
"""
css = css.replace("{{IMG}}", BACKGROUND_IMG)
st.markdown(css, unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='content'>", unsafe_allow_html=True)
    st.markdown("<div class='big-title'>🎈 지민이의 외출 준비</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>핑크핑크한 방에서 준비를 도와줘요.</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        if 'show_instructions' not in st.session_state:
            st.session_state.show_instructions = False

        if st.button("게임 방법", key='open_instructions'):
            st.session_state.show_instructions = True

    with col2:
        if st.button("게임 시작"):
            st.success("게임을 시작합니다! 준비가 완료되면 다음 화면으로 이동합니다.")
            st.write("(여기에는 실제 게임 로직/화면이 들어갑니다 — 원하시면 구현해드릴게요.)")

    # 쿼리 파라미터로 모달 닫기 처리(HTML 내부 링크에서 사용)
    params = st.experimental_get_query_params()
    if 'close_modal' in params:
        st.session_state.show_instructions = False
        # 쿼리 파라미터 제거
        st.experimental_set_query_params()

    # 모달 표시
    if st.session_state.get('show_instructions', False):
        top_col1, top_col2 = st.columns([9, 1])
        with top_col2:
            if st.button("X", key='close_instructions'):
                st.session_state.show_instructions = False

        modal_css = """
        <style>
        .modal-overlay {
            position: fixed; top:0; left:0; width:100%; height:100%;
            background: rgba(0,0,0,0.45); z-index: 999; display:flex;
            align-items:center; justify-content:center;
            pointer-events: none; /* 오버레이는 클릭을 막지 않음 */
        }
        .modal-box {
            position: relative;
            background: rgba(255,255,255,0.98); border-radius:12px; padding:36px 24px 24px 24px; width:min(640px,90%);
            box-shadow: 0 6px 30px rgba(0,0,0,0.2); color:#2e0b2e;
            pointer-events: auto; /* 박스 내부는 클릭 가능 */
        }
        .modal-title { font-size:20px; font-weight:700; margin-bottom:8px; }
        .modal-body { font-size:16px; line-height:1.6; margin-bottom:14px; }
        .modal-close-btn {
            position: absolute; top:10px; right:12px; display:inline-block;
            padding:6px 10px; background:#f8d1da; color:#3b0733; border-radius:8px; text-decoration:none;
            font-weight:700; box-shadow: 0 2px 6px rgba(0,0,0,0.12);
        }
        .modal-close-btn:hover { background:#f3b9c9 }
        </style>
        <div class="modal-overlay">
                    <div class="modal-box" id="js-modal-box">
                        <a href="#" class="modal-close-btn" onclick="document.getElementById('js-modal-box').parentElement.style.display='none'; return false;">닫기</a>
            <div class="modal-title">게임 방법</div>
            <div class="modal-body">지민이가 학교에 제시간에 가도록 도와줘! 그러기 위해선 시계를 정확하게 읽어줘야 해! 모두 지민이를 도와줘!</div>
          </div>
        </div>
        """
        st.markdown(modal_css, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

