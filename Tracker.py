import streamlit as st
import psutil
import time

# Set Streamlit page configuration
st.set_page_config(
    page_title="Activity Tracker App",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",  # You can adjust the layout as needed
    initial_sidebar_state="auto",
)

# Define custom CSS styles
custom_css = """
<style>
body {
    background-color: black;
    color: neongreen;
}
button {
    background-color: neongreen;
    color: black;
    border-radius: 5px;
    padding: 10px 20px;
}
</style>
"""

# Apply custom CSS styles
st.markdown(custom_css, unsafe_allow_html=True)


def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return hours, minutes, seconds

def main():
    st.title("Activity Tracker App")
    
    if 'start_time' not in st.session_state:
        st.session_state.start_time = None
    if 'punched_in' not in st.session_state:
        st.session_state.punched_in = False
    if 'punched_out' not in st.session_state:
        st.session_state.punched_out = False

    punch_in_button = st.button("Punch in")
    punch_out_button = st.button("Punch out")

    if punch_in_button and not st.session_state.punched_in:
        st.session_state.start_time = time.time()
        st.session_state.punched_in = True
        st.session_state.punched_out = False
        st.success("Punch in successful")

    if punch_out_button and st.session_state.punched_in and not st.session_state.punched_out:
        end_time = time.time()
        active_time_seconds = end_time - st.session_state.start_time
        st.session_state.punched_out = True
        
        memory_usage = psutil.virtual_memory().percent
        ram_usage = psutil.cpu_percent()
        st.write(f"Memory Usage: {memory_usage}%")
        st.write(f"RAM Usage: {ram_usage}%")
        
        active_hours, active_minutes, active_seconds = format_time(active_time_seconds)
        st.write(f"Total Active Time: {active_hours} hours, {active_minutes} minutes, {active_seconds} seconds")

if __name__ == "__main__":
    main()
