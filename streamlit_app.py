import streamlit as st
import random
import math

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
    background: rgba(0, 0, 0, 0); /* 오버레이 제거 - 학교 사진 그대로 표시 */
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
.school-icon {
    position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
    font-size: 200px; z-index: 0; opacity: 0.15; pointer-events: none;
}
</style>
<div class="overlay"></div>
<div class="school-icon">🏫</div>
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
            st.session_state.game_started = True
            # 게임 시작 시 랜덤 시간 설정
            if 'correct_hour' not in st.session_state:
                st.session_state.correct_hour = random.randint(7, 8)  # 7시~8시
                st.session_state.correct_minute = random.randint(0, 59)  # 0분~59분

    # 게임 화면
    if st.session_state.get('game_started', False):
        st.markdown("---")
        
        # 시계 그리기 (SVG)
        col_clock, col_button = st.columns([3, 1])
        
        with col_clock:
            st.markdown("<div style='text-align:center; font-size:20px; color:#2e0b2e; font-weight:600; margin-bottom:8px;'>오늘 지민이의 등교 시간이야!</div>", unsafe_allow_html=True)
            hour = st.session_state.correct_hour
            minute = st.session_state.correct_minute
            
            # 시침과 분침 각도 계산
            minute_angle = (minute * 6) - 90  # 분침: 6도/분
            hour_angle = ((hour % 12) * 30 + minute * 0.5) - 90  # 시침: 30도/시간
            
            # SVG 시계 생성
            clock_svg = f"""
            <svg width="300" height="300" viewBox="0 0 300 300">
              <!-- 배경 -->
              <circle cx="150" cy="150" r="140" fill="white" stroke="black" stroke-width="3"/>
              
              <!-- 시간 표시 -->
              <text x="150" y="40" text-anchor="middle" font-size="20" font-weight="bold">12</text>
              <text x="260" y="155" text-anchor="middle" font-size="20" font-weight="bold">3</text>
              <text x="150" y="270" text-anchor="middle" font-size="20" font-weight="bold">6</text>
              <text x="40" y="155" text-anchor="middle" font-size="20" font-weight="bold">9</text>
              
              <!-- 중심점 -->
              <circle cx="150" cy="150" r="5" fill="black"/>
              
              <!-- 분침 -->
              <line x1="150" y1="150" x2="150" y2="50" 
                    stroke="black" stroke-width="4" stroke-linecap="round"
                    transform="rotate({minute_angle} 150 150)"/>
              
              <!-- 시침 -->
              <line x1="150" y1="150" x2="150" y2="90" 
                    stroke="black" stroke-width="6" stroke-linecap="round"
                    transform="rotate({hour_angle} 150 150)"/>
            </svg>
            """
            st.markdown(clock_svg, unsafe_allow_html=True)
        
        with col_button:
            if st.button("🔄 다시하기"):
                st.session_state.correct_hour = random.randint(7, 8)
                st.session_state.correct_minute = random.randint(0, 59)
                st.session_state.user_answer_submitted = False
        
        # 답 입력 영역
        st.markdown("### 지민이의 등교 시간을 입력해줘!")
        
        col_hour, col_min = st.columns([1, 1])
        with col_hour:
            user_hour = st.number_input("시", min_value=0, max_value=23, value=7, key="user_hour")
        with col_min:
            user_minute = st.number_input("분", min_value=0, max_value=59, value=0, key="user_minute")
        
        if st.button("정답 확인"):
            st.session_state.user_answer_submitted = True
            st.session_state.user_hour = user_hour
            st.session_state.user_minute = user_minute
        
        # 정답 확인 결과
        if st.session_state.get('user_answer_submitted', False):
            user_time_minutes = st.session_state.user_hour * 60 + st.session_state.user_minute
            correct_time_minutes = st.session_state.correct_hour * 60 + st.session_state.correct_minute
            
            if user_time_minutes == correct_time_minutes:
                st.success("✅ 지민이는 학교에 잘 등교했어요!")
            elif user_time_minutes > correct_time_minutes:
                st.error("⏰ 큰일났어요! 지민이는 지각을 하고 말았어요!")
            else:  # user_time_minutes < correct_time_minutes
                st.warning("🏫 학교에 도착했지만 아무도 없어요...")
    else:
        st.success("게임을 시작합니다! 준비가 완료되면 다음 화면으로 이동합니다.")
        st.write("(여기에는 실제 게임 로직/화면이 들어갑니다 — 원하시면 구현해드릴게요.)")

    st.markdown("</div>", unsafe_allow_html=True)

