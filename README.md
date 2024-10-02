# -Activity-Tracker-App-using-Streamlit


### Code Overview

This code creates an **Activity Tracker App** using **Streamlit** that allows users to "punch in" and "punch out" to track time spent on an activity, as well as monitor system metrics like **CPU usage** and **memory usage**. The app uses **psutil** to gather system information and **time** to track the activity duration.

Here’s a step-by-step breakdown of how the code works:

### 1. **Page Configuration**
- `st.set_page_config()` sets up the Streamlit app with the following parameters:
  - **page_title**: Sets the app's title to "Activity Tracker App."
  - **page_icon**: Sets a chart icon using `:chart_with_upwards_trend:`.
  - **layout**: Configures the layout to "wide" so the content stretches across the screen.
  - **initial_sidebar_state**: Automatically shows or hides the sidebar as needed.

### 2. **Custom CSS Styling**
- **Custom CSS** is defined in the `custom_css` string to modify the appearance of the app:
  - Sets the **background color** of the app to black and the **text color** to neon green.
  - Customizes the buttons with **neon green background** and **black text**.

- `st.markdown(custom_css, unsafe_allow_html=True)` applies the custom CSS styles to the Streamlit app.

### 3. **Tracking Time**
- The app allows users to punch in and out to track active time:
  - **Session State**: The session state (`st.session_state`) stores the following:
    - `start_time`: The time the user punches in (saved as a timestamp).
    - `punched_in`: A boolean flag indicating if the user has punched in.
    - `punched_out`: A boolean flag indicating if the user has punched out.
  
- **Buttons**:
  - `punch_in_button` lets the user start tracking their active time.
  - `punch_out_button` stops the time tracking.

- When the user punches in, the `start_time` is stored, and the `punched_in` state is set to `True`.
- When the user punches out:
  - The app calculates the **active time** by subtracting the start time from the current time (`end_time - st.session_state.start_time`).
  - The app converts the active time into **hours, minutes, and seconds** using the `format_time()` function.

### 4. **Displaying System Metrics**
- **Memory and CPU Usage**: 
  - The app uses `psutil.virtual_memory().percent` to get the current memory usage percentage.
  - It also uses `psutil.cpu_percent()` to get the CPU usage percentage.

- These metrics are displayed alongside the total active time tracked.

### 5. **Output**
- If the user punches out, the app displays:
  - The **total active time** in hours, minutes, and seconds.
  - The **memory usage** and **RAM usage** during the activity.

### Project Name Suggestions:
Here are some potential names for this project:
1. **TrackTime**
2. **PunchTracker**
3. **WorkLog Pro**
4. **Time & Metrics Tracker**
5. **ActivityPulse**
6. **Effort Monitor**
7. **TaskTime Manager**
8. **ActiveClock**
9. **FocusTrack**
10. **MemoryTracker**

These names reflect the functionality of tracking time and system performance.


https://github.com/user-attachments/assets/e3daf246-de83-414e-b65e-9ee97d4613bb




