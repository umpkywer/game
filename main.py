import streamlit as st
import time

# 초기화
if '잔여시간' not in st.session_state:
    st.session_state.잔여시간 = 0
    st.session_state.cnt = 0
    st.session_state.running = False

def start_timer():
    st.session_state.잔여시간 = 5  # 5초로 타이머 설정
    st.session_state.cnt = 0
    st.session_state.running = True
    st.session_state.timer_job = time.time()  # 시작 시간을 기록
    st.session_state.timer_over = False  # 타이머가 종료되지 않았음을 표시
    st.experimental_rerun()

def update_timer():
    # 타이머 업데이트
    elapsed_time = time.time() - st.session_state.timer_job
    remaining_time = max(0, 5 - int(elapsed_time))  # 5초에서 경과 시간 뺀 값

    st.session_state.잔여시간 = remaining_time
    
    # 타이머가 종료되었는지 체크
    if remaining_time <= 0:
        st.session_state.running = False
        st.session_state.timer_over = True
        st.experimental_rerun()

def click():
    if st.session_state.running:
        st.session_state.cnt += 1
        st.experimental_rerun()

def reset():
    st.session_state.cnt = 0
    st.session_state.timer_over = False
    st.experimental_rerun()

# 타이머 업데이트 (주기적으로 실행)
if st.session_state.running:
    update_timer()

# UI 구성
st.title('주어진 시간동안 최대한 많이 클릭하세요!')

# 타이머
st.write(f"Time left: {st.session_state.잔여시간} seconds")

# 클릭 횟수
st.write(f"현재 횟수: {st.session_state.cnt}")

# 타이머 종료 후 최종 결과 표시
if st.session_state.timer_over:
    st.write(f"최종 횟수: {st.session_state.cnt}")
    st.button('Restart', on_click=reset)

# 버튼
if st.session_state.running:
    st.button('Button', on_click=click)
else:
    st.button('Start Timer', on_click=start_timer)
