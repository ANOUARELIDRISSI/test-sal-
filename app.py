import streamlit as st

st.set_page_config(
    page_title="E-Learning Platform",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)

# We avoid emoji visuals in the UI and use inline SVG icons for consistency.
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Manrope', sans-serif;
    }

    .stApp {
        background: radial-gradient(1200px 500px at 10% -10%, #e6f4ff 0%, rgba(230, 244, 255, 0) 70%),
                    radial-gradient(800px 300px at 100% 0%, #ffe9d6 0%, rgba(255, 233, 214, 0) 70%),
                    #f8fafc;
    }

    .hero {
        border: 1px solid #dbe4ef;
        border-radius: 20px;
        padding: 28px;
        background: linear-gradient(145deg, #ffffff 0%, #f3f7fb 100%);
        box-shadow: 0 12px 30px rgba(25, 40, 60, 0.08);
        margin-bottom: 18px;
    }

    .title {
        font-size: 2rem;
        font-weight: 800;
        color: #1e293b;
        margin-bottom: 0.35rem;
    }

    .subtitle {
        color: #475569;
        font-size: 1.02rem;
        max-width: 760px;
    }

    .metric-card {
        border: 1px solid #dbe4ef;
        border-radius: 16px;
        padding: 16px;
        background: #ffffff;
        box-shadow: 0 8px 18px rgba(15, 23, 42, 0.05);
        height: 100%;
    }

    .metric-title {
        color: #334155;
        font-weight: 600;
        font-size: 0.95rem;
    }

    .metric-value {
        color: #0f172a;
        font-weight: 800;
        font-size: 1.5rem;
        margin-top: 6px;
    }

    .course-card {
        border: 1px solid #dbe4ef;
        border-radius: 16px;
        padding: 16px;
        background: #ffffff;
        box-shadow: 0 8px 18px rgba(15, 23, 42, 0.05);
        margin-bottom: 14px;
    }

    .course-title {
        color: #0f172a;
        font-weight: 700;
        font-size: 1.05rem;
        margin-bottom: 4px;
    }

    .course-meta {
        color: #475569;
        font-size: 0.92rem;
        margin-bottom: 10px;
    }

    .badge {
        display: inline-block;
        border-radius: 999px;
        padding: 5px 10px;
        font-size: 0.78rem;
        font-weight: 700;
        background: #e2e8f0;
        color: #1e293b;
        margin-right: 8px;
    }

    .progress-wrap {
        background: #e2e8f0;
        border-radius: 99px;
        height: 10px;
        overflow: hidden;
    }

    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #0ea5e9, #0284c7);
    }

    .icon {
        width: 18px;
        height: 18px;
        vertical-align: middle;
        margin-right: 8px;
    }

    .section-head {
        margin-top: 8px;
        margin-bottom: 10px;
        color: #1e293b;
        font-size: 1.22rem;
        font-weight: 800;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def svg_book() -> str:
    return """
    <svg class="icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M4 5.5C4 4.12 5.12 3 6.5 3H19v16H6.5A2.5 2.5 0 0 0 4 21.5V5.5Z" stroke="#0369A1" stroke-width="1.8"/>
      <path d="M7 7h9M7 10h9M7 13h6" stroke="#0369A1" stroke-width="1.8" stroke-linecap="round"/>
    </svg>
    """


def svg_clock() -> str:
    return """
    <svg class="icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <circle cx="12" cy="12" r="8.5" stroke="#0369A1" stroke-width="1.8"/>
      <path d="M12 7.5v5l3 1.7" stroke="#0369A1" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    """


def svg_chart() -> str:
    return """
    <svg class="icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M4 19h16" stroke="#0369A1" stroke-width="1.8" stroke-linecap="round"/>
      <rect x="6" y="11" width="3" height="6" rx="1" fill="#38BDF8"/>
      <rect x="11" y="8" width="3" height="9" rx="1" fill="#0EA5E9"/>
      <rect x="16" y="5" width="3" height="12" rx="1" fill="#0284C7"/>
    </svg>
    """


with st.sidebar:
    st.markdown("### Learning Settings")
    level = st.selectbox("Skill level", ["Beginner", "Intermediate", "Advanced"], index=1)
    track = st.multiselect(
        "Focus tracks",
        ["Data Engineering", "Analytics", "Machine Learning", "Product Thinking"],
        default=["Data Engineering", "Analytics"],
    )
    weekly_goal = st.slider("Weekly study goal (hours)", 2, 20, 8)
    st.markdown("---")
    st.write("Quick Actions")
    st.button("Create learning plan", use_container_width=True)
    st.button("Download syllabus", use_container_width=True)

st.markdown(
    """
    <div class="hero">
      <div class="title">E-Learning Dashboard Interface</div>
      <div class="subtitle">
        A modern learning workspace to manage courses, track progress, and schedule study sessions.
        Designed for a focused, professional e-learning experience.
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(
        f"""
        <div class="metric-card">
          <div class="metric-title">{svg_book()}Active Courses</div>
          <div class="metric-value">6</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        f"""
        <div class="metric-card">
          <div class="metric-title">{svg_clock()}Hours This Week</div>
          <div class="metric-value">{weekly_goal}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        f"""
        <div class="metric-card">
          <div class="metric-title">{svg_chart()}Completion Rate</div>
          <div class="metric-value">74%</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div class='section-head'>Current Learning Path</div>", unsafe_allow_html=True)

courses = [
    {
        "title": "Data Modeling for Analytics",
        "meta": "12 lessons  |  4h 30m  |  Instructor: M. Johnson",
        "status": "In Progress",
        "progress": 68,
    },
    {
        "title": "SQL for Decision Making",
        "meta": "18 lessons  |  6h 10m  |  Instructor: A. Kim",
        "status": "In Progress",
        "progress": 41,
    },
    {
        "title": "Power BI Storytelling",
        "meta": "9 lessons  |  3h 20m  |  Instructor: C. Williams",
        "status": "Planned",
        "progress": 12,
    },
]

for course in courses:
    st.markdown(
        f"""
        <div class="course-card">
          <div class="course-title">{course['title']}</div>
          <div class="course-meta">{course['meta']}</div>
          <span class="badge">{course['status']}</span>
          <div class="progress-wrap" style="margin-top: 10px;">
            <div class="progress-fill" style="width: {course['progress']}%;"></div>
          </div>
          <div style="margin-top: 6px; color: #334155; font-size: 0.86rem;">Progress: {course['progress']}%</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div class='section-head'>Recommended Next Module</div>", unsafe_allow_html=True)
left, right = st.columns([2, 1])
with left:
    st.info(
        "Module: Building a reliable ETL pipeline in Power Query and validating data quality checks."
    )
with right:
    st.button("Start module", use_container_width=True)

st.caption(f"Profile: {level} learner  |  Tracks: {', '.join(track) if track else 'None selected'}")
