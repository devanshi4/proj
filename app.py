import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="JP Morgan 2014 Data Breach Dashboard", layout="wide")

# =============================
# TITLE
# =============================
st.title("JP Morgan Chase 2014 Data Breach — Dashboard")

st.write("This dashboard summarizes the 2014 JP Morgan data breach, its impact, failures, and how analytics could have prevented it.")

# =============================
# SECTION 1 — KPIs
# =============================
st.subheader("Breach Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Accounts Affected", "83 Million")
col2.metric("Households Impacted", "76 Million")
col3.metric("Undetected For", "60 Days")
col4.metric("Financial Fraud", "$0")

# =============================
# SECTION 2 — ATTACK TIMELINE
# =============================
st.subheader("Attack Timeline")

timeline = pd.DataFrame({
    "Event": [
        "Breach begins",
        "Attackers active",
        "External detection",
        "Breach contained",
        "Public disclosure"
    ],
    "Date": [
        "June 2014",
        "Jun–Aug 2014",
        "Late July 2014",
        "Mid-Aug 2014",
        "Oct 2, 2014"
    ]
})

st.table(timeline)

# =============================
# SECTION 3 — ATTACK FLOW
# =============================
st.subheader("How the Attack Happened")

st.markdown("""
➡️ **Phishing email compromises employee**  
➡️ **Credentials stolen**  
➡️ **Server without 2FA exploited**  
➡️ **Privilege escalation to admin level**  
➡️ **Lateral movement across 90+ servers**  
➡️ **Gradual data exfiltration for 60 days**
""")

# =============================
# SECTION 4 — SECURITY FAILURES
# =============================
st.subheader("Critical Security Failures")

f1, f2, f3, f4, f5 = st.columns(5)
f1.error("Missing 2FA")
f2.error("Weak Monitoring")
f3.error("No DLP")
f4.error("Poor Segmentation")
f5.error("Human Error")

# =============================
# SECTION 5 — BUSINESS IMPACT
# =============================
st.subheader("Business Impact")

with st.expander("Financial Impact"):
    st.write("""
    - Security budget doubled ($250M → $500M)
    - Total long-term cost: $300M–$500M
    - No direct financial losses to customers
    """)

with st.expander("Reputational Impact"):
    st.write("""
    - Heavy media coverage
    - No major customer loss
    - Public trust restored after security investments
    """)

with st.expander("Operational Impact"):
    st.write("""
    - 200+ employees reassigned for breach response
    - Security team expanded from 1,000 → 2,000+
    - Major system-wide security overhaul
    """)

# =============================
# SECTION 6 — ANALYTICS PREVENTION
# =============================
st.subheader("How Analytics Could Have Prevented the Breach")

analytics_table = pd.DataFrame({
    "Analytics Tool": ["2FA Scanner", "UEBA", "Network Analytics", "DLP", "Threat Intelligence"],
    "Prevention": [
        "Find non-compliant server",
        "Catch unusual credential use",
        "Detect lateral movement",
        "Spot slow data exfiltration",
        "Match known attack patterns"
    ]
})

st.table(analytics_table)

# =============================
# SECTION 7 — RECOMMENDATIONS
# =============================
st.subheader("Strategic Recommendations")

st.checkbox("Emergency audit and 2FA verification")
st.checkbox("24/7 SOC monitoring with SIEM")
st.checkbox("Zero-trust architecture rollout")
st.checkbox("Vendor risk management program")
st.checkbox("Automated incident response systems")
st.checkbox("Continuous compliance monitoring")
st.checkbox("Threat hunting team development")

st.success("Dashboard Loaded Successfully.")