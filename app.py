import streamlit as st
from pathlib import Path

# 1. Page Config
st.set_page_config(
    page_title="Iqra Gulzar | Professional CV",
    page_icon="💎",
    layout="wide"
)

# 2. High-Visibility Dark Mode Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
    
    /* Force Dark Mode and High Contrast */
    .main {
        background-color: #0f172a;
        font-family: 'Outfit', sans-serif;
    }
    
    h1, h2, h3, h4 {
        color: #ffffff !important;
        font-weight: 700 !important;
    }
    
    .stMarkdown p, .stMarkdown li {
        color: #e2e8f0 !important;
        font-size: 1.1rem;
        line-height: 1.7;
    }
    
    /* Highlighted Cards */
    .css-1r6slb0, .stVerticalBlock > div > div {
        background-color: rgba(30, 41, 59, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 1rem;
        padding: 1.5rem;
    }
    
    /* Skill Badges (High Visibility) */
    .skill-tag {
        display: inline-block;
        background-color: #3b82f6;
        color: #ffffff;
        padding: 0.4rem 1rem;
        border-radius: 0.5rem;
        font-size: 0.9rem;
        font-weight: 700;
        margin: 0.3rem;
        box-shadow: 0 0 10px rgba(59, 130, 246, 0.4);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #1e293b;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    hr {
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    if Path("iqra_new_profile.png").exists():
        st.image("iqra_new_profile.png", use_container_width=True)
    
    st.markdown("# Iqra Gulzar")
    st.markdown("### Support Engineer")
    st.divider()
    st.markdown("📍 **Abu Dhabi, UAE**")
    st.markdown("📧 **gulzariqra87@gmail.com**")
    st.markdown("📞 **+971 50 622 4979**")
    st.divider()
    st.markdown("🏆 **Golden Visa Holder**")
    st.markdown("🚗 **UAE Driving License**")
    st.divider()
    st.markdown("### Languages")
    st.write("• English (Native)")
    st.write("• Hindi (Native)")

# 4. Main Content
st.title("Iqra Gulzar")
st.markdown("#### Support Engineer | MSc Data Science & AI Student")

st.success("Motivated IT professional and Support Engineer with expertise in ELV system design, pre-sales engineering, and digital infrastructure. Pursuing MSc in Data Science and AI.")

st.header("Professional Experience")

# Job 1
st.markdown("### Support Engineer — Syssense")
st.markdown("*Abu Dhabi, UAE | 2023 — 2025*")
st.markdown("""
- Designed and estimated **ELV systems** (CCTV, Structured Cabling, Access Control, Intercom, Gate Barriers).
- Prepared layout drawings, **BOQs**, technical submittals, and cost estimations for tenders.
- Coordinated with vendors and clients for project compliance and timely approvals.
- Managed Annual Maintenance Contract (**AMC**) documentation and reporting.
- Developed corporate website and designed company profile.
- Optimized IT infrastructure and troubleshot Windows/Linux systems.
""")

st.divider()

# Job 2
st.markdown("### Cybersecurity Intern — Jamia Bank")
st.markdown("*India | 2022*")
st.markdown("""
- Identified system vulnerabilities and supported implementation of security controls.
- Assisted in maintaining secure network operations and financial infrastructure.
""")

st.divider()

# Skills (The massive list with High Visibility)
st.header("Skills & Expertise")

skills = [
    "SQL", "Pandas", "NumPy", "Scikit-Learn", "TensorFlow", "Java",
    "Predictive Modelling", "Feature Engineering", "NLP", "Computer Vision",
    "RAG System", "ETL Pipeline", "Statistical Analysis", "Regression & Classification",
    "Google Cloud", "Hadoop", "AWS", "Power BI", "Tableau", "Vercel",
    "ELV System Design", "Networking", "Linux", "Cybersecurity", "Python"
]

skill_html = ""
for skill in skills:
    skill_html += f'<span class="skill-tag">{skill}</span>'
st.markdown(skill_html, unsafe_allow_html=True)

st.divider()

# Education
st.header("Education")
st.markdown("#### MSc in Data Science & Artificial Intelligence")
st.write("Middlesex University Dubai | 2025 — Present")
st.markdown("#### B.Tech in Information Systems & Management")
st.write("MAHE Dubai | 2020 — 2023 | GPA: 8.68/10")

st.divider()

# Certifications
st.header("Certifications")
c1, c2 = st.columns(2)
with c1:
    st.write("• IT Essentials")
    st.write("• Cybersecurity Essentials")
    st.write("• Computer Networks")
    st.write("• IoT Connecting Things")
with c2:
    st.write("• Routing & Switching")
    st.write("• Enterprise Security")
    st.write("• Linux Administration")
    st.write("• Database Management")

st.markdown("---")
st.markdown("<p style='text-align:center; color:#94a3b8;'>© 2026 Iqra Gulzar | Built with High-Visibility Python</p>", unsafe_allow_html=True)
