import streamlit as st
import time

# 초기화
if '잔여시간' not in st.session_state:
    st.session_state.잔여시간 = 0
    st.session_state.cnt = 0
    st.session_state.running = False
    st.session_state.start_time = None
    st.session_state.timer_over = False

# 타이머 시작 함수
def start_timer():
    st.session_state.잔여시간 = 5  # 5초로 타이머 설정
    st.session_state.cnt = 0
    st.session_state.running = True
    st.session_state.start_time = time.time()  # 시작 시간을 기록
    st.session_state.timer_over = False  # 타이머가 종료되지 않았음을 표시

# 타이머 업데이트 함수
def update_timer():
    elapsed_time = time.time() - st.session_state.start_time
    remaining_time = max(0, 5 - int(elapsed_time))  # 5초에서 경과 시간 뺀 값
    st.session_state.잔여시간 = remaining_time
    
    if remaining_time <= 0:
        st.session_state.running = False
        st.session_state.timer_over = True

# 클릭 함수
def click():
    if st.session_state.running:
        st.session_state.cnt += 1

# 리셋 함수
def reset():
    st.session_state.cnt = 0
    st.session_state.timer_over = False
    st.session_state.running = False
    st.session_state.잔여시간 = 0

# UI 구성
st.title('주어진 시간동안 최대한 많이 클릭하세요!')

# Custom CSS로 스타일 추가
st.markdown("""
    <style>
        .timer {
            font-size: 2rem;
            font-weight: bold;
            color: #f39c12;
            text-align: center;
            padding: 20px;
            border-radius: 10px;
            background-color: #2c3e50;
            color: white;
        }
        .counter {
            font-size: 1.5rem;
            font-weight: bold;
            color: #16a085;
            text-align: center;
            padding: 10px;
            margin-top: 20px;
        }
        .button-container {
            display: flex;
            justify-content: center;
            margin-top: 30px;
        }
        .button {
            background-color: #3498db;
            color: white;
            padding: 15px 25px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1.2rem;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .button:hover {
            background-color: #2980b9;
        }
        .restart-button {
            background-color: #e74c3c;
        }
        .restart-button:hover {
            background-color: #c0392b;
        }
        .final-score {
            font-size: 2rem;
            font-weight: bold;
            color: #9b59b6;
            text-align: center;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# 타이머와 클릭 횟수 표시
st.markdown(f'<div class="timer">남은 시간: {st.session_state.잔여시간}초</div>', unsafe_allow_html=True)
st.markdown(f'<div class="counter">현재 횟수: {st.session_state.cnt}</div>', unsafe_allow_html=True)

# 타이머 종료 후 최종 결과 표시
if st.session_state.timer_over:
    st.markdown(f'<div class="final-score">최종 횟수: {st.session_state.cnt}</div>', unsafe_allow_html=True)
    if st.button('Restart', key="restart", on_click=reset):
        st.session_state.timer_over = False

# 버튼 섹션
st.markdown('<div class="button-container">', unsafe_allow_html=True)

if st.session_state.running:
    if st.button('클릭!', key="click", on_click=click, use_container_width=True):
        pass
else:
    if st.button('타이머 시작', key="start", on_click=start_timer, use_container_width=True):
        pass

st.markdown('</div>', unsafe_allow_html=True)

# 타이머 상태 업데이트
if st.session_state.running:
    update_timer()
    time.sleep(1)  # 매 초마다 타이머 갱신
    st.experimental_rerun()  # 화면을 다시 렌더링하여 타이머를 계속 갱신
