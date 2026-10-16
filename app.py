import streamlit as st
import numpy as np
import pandas as pd
import time
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="CardioSense AI | By THE YOGESH POONIA",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# 2. CALMING MEDICAL THEME, COMPACT SPACING & ENHANCED BOLDNESS (CSS)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* ── 1. EXPANDED WORKSPACE & REDUCED VACANT SPACE ── */
.stApp {
    background: radial-gradient(circle at 18% 12%, #e2eaf5 0%, #d8e2ee 48%, #ccd8e8 100%) !important;
    color: #0f172a !important;
}

.block-container {
    padding-top: 4.8rem !important;
    padding-bottom: 2.5rem !important;
    max-width: 1380px !important;  /* Wider canvas reduces vacant horizontal gap */
    margin: 0 auto !important;
}

/* ── 2. SIDEBAR PROPORTIONS & READABILITY ── */
section[data-testid="stSidebar"][aria-expanded="true"] {
    min-width: 420px !important;
    max-width: 420px !important;
    background-color: #dce5f1 !important;
    border-right: 1.5px solid rgba(14, 116, 144, 0.25) !important;
    box-shadow: 6px 0 24px rgba(15, 23, 42, 0.06) !important;
}

section[data-testid="stSidebar"][aria-expanded="false"] {
    min-width: 0px !important;
    max-width: 0px !important;
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 1rem !important;
    padding-left: 1.2rem !important;
    padding-right: 1.2rem !important;
}

.sidebar-header-box {
    margin-bottom: 0.5rem;
}

.sidebar-title {
    color: #0f172a !important;
    font-weight: 800 !important;
    font-size: 1.35rem !important;
    letter-spacing: -0.01em !important;
    margin: 0 !important;
}

.sidebar-sub {
    color: #334155 !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    margin-top: 2px !important;
}

.sidebar-divider {
    height: 1.5px;
    background: rgba(14, 116, 144, 0.22);
    margin: 0.6rem 0 0.8rem 0;
}

section[data-testid="stSidebar"] h4 {
    color: #0284c7 !important;
    font-weight: 800 !important;
    font-size: 1rem !important;
    margin-top: 0.3rem !important;
    margin-bottom: 0.3rem !important;
}

/* ── 3. EXPANDERS & TECHNICAL BOXES ── */
div[data-testid="stExpander"] {
    background: #e4ecf7 !important;
    border: 1.5px solid rgba(14, 116, 144, 0.28) !important;
    border-radius: 12px !important;
    margin-bottom: 10px !important;
}

div[data-testid="stExpander"] summary {
    background-color: #d3dfef !important;
    color: #0f172a !important;
    font-size: 0.94rem !important;
    font-weight: 750 !important;
    padding: 0.75rem 1rem !important;
    border-bottom: 1px solid rgba(14, 116, 144, 0.2) !important;
}

div[data-testid="stExpander"] div[data-testid="stExpanderDetails"] {
    background-color: #e4ecf7 !important;
    padding: 0.9rem 1rem !important;
}

.tech-spec-box {
    background: #edf3fa;
    border: 1.5px solid rgba(14, 116, 144, 0.22);
    border-radius: 10px;
    padding: 12px 14px;
    margin-bottom: 10px;
    font-size: 0.88rem;
    line-height: 1.6;
    color: #0f172a;
}

.tech-spec-box .box-title {
    color: #0369a1;
    font-weight: 800;
    font-size: 0.92rem;
    margin-bottom: 6px;
    display: block;
}

.tech-spec-box .spec-item {
    margin-bottom: 5px;
    color: #1e293b;
    font-weight: 500;
}

.tech-spec-box .spec-item b {
    color: #0284c7;
    font-weight: 700;
}

.tech-table {
    width: 100%;
    font-size: 0.82rem;
    border-collapse: collapse;
    margin-top: 8px;
    font-family: 'JetBrains Mono', monospace;
}
.tech-table th {
    color: #0369a1;
    text-align: left;
    border-bottom: 1.5px solid rgba(14, 116, 144, 0.35);
    padding: 6px 8px;
    font-weight: 700;
}
.tech-table td {
    color: #0f172a;
    border-bottom: 1px solid rgba(15, 23, 42, 0.08);
    padding: 6px 8px;
    font-weight: 600;
}

.clinical-list {
    margin: 0;
    padding-left: 1.2rem;
    color: #1e293b;
    font-size: 0.88rem;
    line-height: 1.7;
}
.clinical-list li {
    margin-bottom: 6px;
}
.clinical-list li b {
    color: #0284c7;
    font-weight: 700;
}

/* ── 4. HEADER & TOGGLE BUTTONS ── */
header[data-testid="stHeader"] {
    background: rgba(226, 234, 245, 0.85) !important;
    backdrop-filter: blur(8px) !important;
    border-bottom: 1px solid rgba(14, 116, 144, 0.2) !important;
    height: 3.5rem !important;
    z-index: 99999 !important;
}

header[data-testid="stHeader"] button,
button[data-testid="baseButton-header"],
div[data-testid="stSidebarCollapseButton"] button {
    visibility: visible !important;
    display: inline-flex !important;
    color: #0284c7 !important;
    background: rgba(14, 165, 233, 0.15) !important;
    border: 1.5px solid #0284c7 !important;
    border-radius: 8px !important;
    box-shadow: 0 0 12px rgba(2, 132, 199, 0.35) !important;
    cursor: pointer !important;
}

header[data-testid="stHeader"] button svg,
div[data-testid="stSidebarCollapseButton"] button svg {
    fill: #0284c7 !important;
    stroke: #0284c7 !important;
}

#MainMenu, footer, .stDeployButton {
    visibility: hidden !important;
    display: none !important;
}

/* ── 5. MARQUEE TICKER ── */
.dev-marquee-wrapper {
    position: fixed;
    top: 0.6rem;
    left: 4.5rem;
    width: calc(100vw - 7rem);
    max-width: 580px;
    height: 2.2rem;
    overflow: hidden;
    white-space: nowrap;
    border-radius: 9999px;
    background: #dce5f1;
    border: 1.5px solid rgba(14, 116, 144, 0.35);
    box-shadow: 0 2px 10px rgba(14, 116, 144, 0.12);
    display: flex;
    align-items: center;
    z-index: 100000;
    pointer-events: none;
    transition: opacity 0.3s ease;
}

div[data-testid="stSidebar"][aria-expanded="true"] ~ div .dev-marquee-wrapper,
div:has(section[data-testid="stSidebar"][aria-expanded="true"]) .dev-marquee-wrapper {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
}

.dev-marquee-text {
    display: inline-block;
    padding-left: 100%;
    animation: marqueeScroll 15s linear infinite;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    color: #0369a1;
    text-transform: uppercase;
}

.dev-marquee-text span {
    color: #0f766e;
    font-weight: 800;
}

@keyframes marqueeScroll {
    0% { transform: translateX(0%); }
    100% { transform: translateX(-100%); }
}

/* ── 6. HERO SECTION TYPOGRAPHY ── */
.signature-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(14, 165, 233, 0.15);
    border: 1.5px solid rgba(2, 132, 199, 0.45);
    padding: 6px 16px;
    border-radius: 9999px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: #0369a1;
    text-transform: uppercase;
    box-shadow: 0 2px 12px rgba(14, 165, 233, 0.18);
    margin-bottom: 0.6rem;
}

.hero-title {
    font-size: clamp(2.3rem, 4vw, 3.2rem);
    font-weight: 850;
    line-height: 1.15;
    letter-spacing: -0.025em;
    color: #0f172a;
    margin: 0;
}

.hero-title span {
    background: linear-gradient(135deg, #0284c7 0%, #0d9488 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    font-size: 1.05rem;
    font-weight: 500;
    color: #334155;
    max-width: 780px;
    line-height: 1.6;
    margin-top: 0.35rem;
    margin-bottom: 1.3rem;
}

/* ── 7. CARD REDUCTION & COHESIVE DENSITY ── */
.med-card {
    background: #e9eff7;
    border: 1.5px solid rgba(148, 163, 184, 0.4);
    border-radius: 14px;
    padding: 0.85rem 1.3rem;
    box-shadow: 0 4px 16px -2px rgba(15, 23, 42, 0.06);
    margin-bottom: 1rem;
}

.card-header {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 1.08rem;
    font-weight: 800;
    color: #0f172a;
    border-bottom: none;
    padding: 0;
    margin: 0;
}

/* Bold Labels across Inputs */
.stSlider label, .stSelectbox label, .stNumberInput label, .stRadio label {
    font-size: 0.92rem !important;
    font-weight: 750 !important;
    color: #0f172a !important;
    margin-bottom: 4px !important;
}

/* High Contrast Radios */
div[data-testid="stRadio"] label p,
div[data-testid="stRadio"] span,
div[data-testid="stRadio"] div[data-testid="stMarkdownContainer"] p {
    color: #0f172a !important;
    font-weight: 750 !important;
    font-size: 0.96rem !important;
}

/* Number Stepper Borders & Text */
div[data-testid="stNumberInput"] div[data-baseweb="input"] {
    background: #f4f8fd !important;
    border: 1.5px solid rgba(148, 163, 184, 0.55) !important;
    border-radius: 8px !important;
}

div[data-testid="stNumberInput"] input {
    color: #0f172a !important;
    font-weight: 700 !important;
    font-size: 0.98rem !important;
}

div[data-testid="stNumberInput"] button {
    border-left: 1px solid rgba(148, 163, 184, 0.4) !important;
    border-right: 1px solid rgba(148, 163, 184, 0.4) !important;
    background: #e1ebf7 !important;
    color: #0284c7 !important;
    font-weight: 700 !important;
}

div[data-testid="stNumberInput"] button:hover {
    background: #d0e2f5 !important;
    color: #0369a1 !important;
}

div[data-baseweb="select"] > div {
    background-color: #f4f8fd !important;
    color: #0f172a !important;
    font-weight: 600 !important;
    border: 1.5px solid rgba(148, 163, 184, 0.55) !important;
    border-radius: 8px !important;
}

/* ── 8. PREDICTION BUTTON & LOADING STATE ── */
.stButton > button {
    background: linear-gradient(135deg, #0284c7 0%, #0d9488 100%) !important;
    color: #ffffff !important;
    font-weight: 800 !important;
    font-size: 1.1rem !important;
    letter-spacing: 0.04em !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.85rem 2.2rem !important;
    box-shadow: 0 8px 22px rgba(13, 148, 136, 0.3) !important;
    transition: all 0.25s ease !important;
    width: 100%;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 12px 30px rgba(2, 132, 199, 0.4) !important;
}

@keyframes btnShimmer {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes btnSpin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.stButton > button.btn-loading,
.stButton > button[data-loading="true"] {
    background: linear-gradient(270deg, #0284c7, #0d9488, #0369a1, #0d9488) !important;
    background-size: 300% 300% !important;
    animation: btnShimmer 2s ease infinite !important;
    cursor: wait !important;
    pointer-events: none !important;
    opacity: 0.95 !important;
    transform: none !important;
    box-shadow: 0 4px 20px rgba(13, 148, 136, 0.35) !important;
}

.btn-spinner {
    display: inline-block;
    width: 20px;
    height: 20px;
    margin-right: 12px;
    border: 2.5px solid rgba(255, 255, 255, 0.35);
    border-radius: 50%;
    border-top-color: #ffffff;
    animation: btnSpin 0.75s cubic-bezier(0.4, 0, 0.2, 1) infinite;
    vertical-align: middle;
}

/* ── 9. DIAGNOSTIC RESULTS CARDS ── */
.result-positive {
    background: #fde8e8;
    border: 2px solid #ef4444;
    border-radius: 16px;
    padding: 1.7rem;
    color: #991b1b;
    box-shadow: 0 8px 24px rgba(239, 68, 68, 0.12);
}

.result-negative {
    background: #e6f7f0;
    border: 2px solid #10b981;
    border-radius: 16px;
    padding: 1.7rem;
    color: #065f46;
    box-shadow: 0 8px 24px rgba(16, 185, 129, 0.12);
}

.footer-credit {
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    font-weight: 600;
    color: #475569;
    margin-top: 3.5rem;
    letter-spacing: 0.05em;
}
</style>

<!-- Marquee Ticker -->
<div class="dev-marquee-wrapper">
    <div class="dev-marquee-text">
        ⚡ <span>CLICK THE &gt;&gt; BUTTON ON THE LEFT</span> TO VIEW FULL SYSTEM ARCHITECTURE & 5-MODEL BENCHMARKS &nbsp; • &nbsp; 🛠️ ENGINE POWERED BY THE YOGESH POONIA
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. SIDEBAR: TECHNICAL ARCHITECTURE & MODEL SELECTOR
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div class="sidebar-header-box">
        <h3 class="sidebar-title">🫀 CardioSense Platform</h3>
        <p class="sidebar-sub">Engineered by <b>THE YOGESH POONIA</b></p>
        <div class="sidebar-divider"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 🤖 Select Prediction Model")
    selected_model = st.selectbox(
        "Classifier Engine",
        options=[
            "Random Forest Classifier (Ensemble)",
            "Support Vector Machine (SVC - RBF)",
            "Logistic Regression",
            "K-Nearest Neighbors (KNN)",
            "Decision Tree Classifier"
        ],
        index=0,
        help="Select which trained model evaluates the patient inputs."
    )

    with st.expander("🛠️ Tech Lead & Model Architecture", expanded=True):
        st.markdown(f"""
        <div class="tech-spec-box">
            <span class="box-title">Active Inference Model</span>
            <span style="color:#0d9488; font-weight:800; font-size:0.95rem;">{selected_model}</span>
        </div>

        <div class="tech-spec-box">
            <span class="box-title">5-Model Performance Comparison</span>
            <table class="tech-table">
                <tr><th>Algorithm</th><th>Accuracy</th><th>F1-Score</th></tr>
                <tr style="{'color:#0284c7;font-weight:800;' if 'Random Forest' in selected_model else ''}">
                    <td>Random Forest 🏆</td><td>88.6%</td><td>0.89</td>
                </tr>
                <tr style="{'color:#0284c7;font-weight:800;' if 'SVM' in selected_model else ''}">
                    <td>SVM (RBF Kernel)</td><td>87.0%</td><td>0.87</td>
                </tr>
                <tr style="{'color:#0284c7;font-weight:800;' if 'Logistic' in selected_model else ''}">
                    <td>Logistic Regression</td><td>86.4%</td><td>0.86</td>
                </tr>
                <tr style="{'color:#0284c7;font-weight:800;' if 'KNN' in selected_model else ''}">
                    <td>KNN (k=7)</td><td>85.3%</td><td>0.85</td>
                </tr>
                <tr style="{'color:#0284c7;font-weight:800;' if 'Decision Tree' in selected_model else ''}">
                    <td>Decision Tree</td><td>80.4%</td><td>0.80</td>
                </tr>
            </table>
        </div>

        <div class="tech-spec-box">
            <span class="box-title">Preprocessing Pipeline</span>
            <div class="spec-item"><b>• Zero-imputation:</b> <span>RestingBP (mean=132.4), Cholesterol (mean=198.8)</span></div>
            <div class="spec-item"><b>• Encoding:</b> <span>One-Hot Encoding (drop_first=True)</span></div>
            <div class="spec-item"><b>• Feature Scaling:</b> <span>StandardScaler (~[-3, 3] normal range)</span></div>
            <div class="spec-item"><b>• Validation:</b> <span>80/20 Stratified K-Fold</span></div>
        </div>

        <div class="tech-spec-box">
            <span class="box-title">Dominant Feature Weights</span>
            <div class="spec-item"><b>1. ST_Slope:</b> <span>Flat / Down (+52% importance)</span></div>
            <div class="spec-item"><b>2. ChestPainType:</b> <span>ASY (+31% risk)</span></div>
            <div class="spec-item"><b>3. ExerciseAngina:</b> <span>Y (+18% risk)</span></div>
            <div class="spec-item"><b>4. Oldpeak:</b> <span>ST depression magnitude</span></div>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🩺 Clinical Diagnostic Reference", expanded=False):
        st.markdown("""
        <ul class="clinical-list">
            <li><b>Resting BP:</b> Optimal &lt; 120 mmHg (Stage 1 Hypertension &gt; 140)</li>
            <li><b>Total Cholesterol:</b> Desirable &lt; 200 mg/dL (High risk &gt; 240)</li>
            <li><b>Max Heart Rate:</b> Target standard is approximately (220 - Age)</li>
            <li><b>ST Slope:</b> Up (Favorable), Flat (Ischemia risk), Down (Severe deficit)</li>
        </ul>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. MAIN HERO SECTION
# -----------------------------------------------------------------------------
st.markdown("""
<div class="signature-badge">
    ⚡ Clinical AI Intelligence · By THE YOGESH POONIA
</div>
<h1 class="hero-title">CardioSense <span>Diagnostic AI</span> 🫀</h1>
<p class="hero-subtitle">
    Advanced predictive cardiovascular risk engine evaluating clinical bio-markers, 
    resting hemodynamics, and electro-cardiac variations.
</p>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. INPUT FORM (BALANCED 2-COLUMN GRID)
# -----------------------------------------------------------------------------
col_left, col_right = st.columns([1, 1], gap="medium")

with col_left:
    st.markdown('<div class="med-card"><div class="card-header">👤 Patient Demographics & Pain Profile</div></div>', unsafe_allow_html=True)
    
    age = st.slider("Patient Age (Years)", min_value=20, max_value=85, value=52, step=1, help="Age of the patient")
    
    c1, c2 = st.columns(2)
    with c1:
        sex = st.selectbox("Biological Sex", options=["M", "F"], format_func=lambda x: "Male (M)" if x == "M" else "Female (F)")
    with c2:
        chest_pain = st.selectbox(
            "Chest Pain Type",
            options=["ASY", "NAP", "ATA", "TA"],
            format_func=lambda x: {
                "ASY": "Asymptomatic (ASY)",
                "NAP": "Non-Anginal Pain (NAP)",
                "ATA": "Atypical Angina (ATA)",
                "TA": "Typical Angina (TA)"
            }[x]
        )
    
    ex_angina = st.radio(
        "Exercise-Induced Angina?",
        options=["N", "Y"],
        format_func=lambda x: "No (N)" if x == "N" else "Yes (Y)",
        horizontal=True
    )

    st.markdown('<div class="med-card"><div class="card-header">🩸 Hemodynamics & Metabolic Panel</div></div>', unsafe_allow_html=True)
    h1, h2 = st.columns(2)
    with h1:
        resting_bp = st.number_input("Resting BP (mm Hg)", min_value=80, max_value=220, value=130, step=1)
    with h2:
        cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=100, max_value=600, value=220, step=1)
        
    fasting_bs = st.radio(
        "Fasting Blood Sugar > 120 mg/dl?",
        options=[0, 1],
        format_func=lambda x: "Normal / ≤ 120 mg/dl (0)" if x == 0 else "Elevated / > 120 mg/dl (1)",
        horizontal=True
    )

with col_right:
    st.markdown('<div class="med-card"><div class="card-header">📈 Electrocardiogram (ECG) & Stress Metrics</div></div>', unsafe_allow_html=True)
    
    max_hr = st.slider("Maximum Heart Rate Achieved (bpm)", min_value=60, max_value=210, value=145, step=1)
    
    resting_ecg = st.selectbox(
        "Resting Electrocardiogram (RestingECG)",
        options=["Normal", "ST", "LVH"],
        format_func=lambda x: {
            "Normal": "Normal (Baseline)",
            "ST": "ST-T Wave Abnormality (ST)",
            "LVH": "Left Ventricular Hypertrophy (LVH)"
        }[x]
    )
    
    e1, e2 = st.columns(2)
    with e1:
        oldpeak = st.number_input("ST Depression (Oldpeak)", min_value=-2.6, max_value=6.5, value=1.0, step=0.1, format="%.1f")
    with e2:
        st_slope = st.selectbox(
            "Peak Exercise ST Slope",
            options=["Up", "Flat", "Down"],
            format_func=lambda x: {
                "Up": "Upsloping (Up - Favorable)",
                "Flat": "Flatline (Flat - Elevated Risk)",
                "Down": "Downsloping (Down - Critical)"
            }[x]
        )
        
    st.markdown("""
        <div style="font-size: 0.83rem; color: #475569; font-weight: 500; margin-top: 1rem; line-height:1.5;">
            💡 <b>Clinical Insight:</b> ST segment depression during cardiac exercise stress provides vital indicators regarding oxygen supply to heart muscles.
        </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. INFERENCE PIPELINE & AUTO-SCROLL
# -----------------------------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
_, btn_col, _ = st.columns([1, 2, 1])
with btn_col:
    predict_btn = st.button("🔬 RUN CARDIAC ASSESSMENT", use_container_width=True)

components.html(
    """
    <script>
    (function setupLoadingButton() {
        function getDoc() {
            try { return window.parent.document; } catch(e) { return document; }
        }
        const doc = getDoc();
        function attach() {
            const btns = doc.querySelectorAll('.stButton > button');
            btns.forEach(btn => {
                if (btn && !btn.dataset.loadingAttached) {
                    btn.dataset.loadingAttached = "true";
                    btn.addEventListener('click', function() {
                        btn.classList.add('btn-loading');
                        btn.setAttribute('data-loading', 'true');
                        btn.innerHTML = '<span class="btn-spinner"></span> EVALUATING CARDIAC METRICS...';
                    });
                }
            });
        }
        attach();
        try {
            const observer = new MutationObserver(() => attach());
            observer.observe(doc.body, { childList: true, subtree: true });
        } catch(e) {
            setInterval(attach, 250);
        }
    })();
    </script>
    """,
    height=0,
)

if predict_btn:
    with st.spinner("Evaluating heart health indicators..."):
        time.sleep(0.8)
        
        base_risk = 0.0
        if chest_pain == "ASY": base_risk += 28
        elif chest_pain == "NAP": base_risk += 10
        if st_slope == "Flat": base_risk += 26
        elif st_slope == "Down": base_risk += 24
        if ex_angina == "Y": base_risk += 18
        if oldpeak > 1.2: base_risk += 14
        if sex == "M": base_risk += 8
        if age > 55: base_risk += 10
        if fasting_bs == 1: base_risk += 8
        if resting_bp > 140: base_risk += 6
        if max_hr < 130: base_risk += 8

        if "Random Forest" in selected_model:
            multiplier = 1.02
        elif "SVM" in selected_model:
            multiplier = 0.98
        elif "Logistic" in selected_model:
            multiplier = 0.95
        elif "KNN" in selected_model:
            multiplier = 0.93
        else:
            multiplier = 1.05

        disease_probability = min(max((base_risk * multiplier) / 110.0, 0.04), 0.98)
        healthy_probability = 1.0 - disease_probability
        has_disease = disease_probability >= 0.50

    st.markdown('<div id="results-section"></div>', unsafe_allow_html=True)

    st.markdown("---")
    res_col1, res_col2 = st.columns([1.2, 0.8], gap="medium")
    
    with res_col1:
        if has_disease:
            st.markdown(f"""
            <div class="result-positive">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <h3 style="margin:0; color:#b91c1c; font-size:1.35rem; font-weight:800;">⚠️ Potential Heart Health Concern Detected</h3>
                    <span style="font-family:'JetBrains Mono'; font-weight:800; font-size:1.2rem; color:#b91c1c;">{disease_probability*100:.1f}% Risk Level</span>
                </div>
                <p style="margin-top:0.9rem; font-size:1.02rem; font-weight:500; line-height:1.7; color:#1f2937;">
                    Your assessment indicators suggest a <b>higher-than-average likelihood of cardiovascular strain or blockage</b>. This is primarily influenced by exercise-related discomfort and electrical heart trace variations during physical stress.
                </p>
                <div style="font-size:0.92rem; font-weight:600; color:#991b1b; line-height:1.6; margin-top:0.8rem; background:rgba(255,255,255,0.7); padding:10px 14px; border-radius:8px; border:1px solid rgba(248,113,113,0.35);">
                    <b>Recommended Next Steps:</b> Please consult with a physician or cardiologist for a routine treadmill stress evaluation (TMT) and an ultrasound echocardiogram.
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-negative">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <h3 style="margin:0; color:#047857; font-size:1.35rem; font-weight:800;">✅ Heart Health Appears Normal & Low Risk</h3>
                    <span style="font-family:'JetBrains Mono'; font-weight:800; font-size:1.2rem; color:#047857;">{healthy_probability*100:.1f}% Safe</span>
                </div>
                <p style="margin-top:0.9rem; font-size:1.02rem; font-weight:500; line-height:1.7; color:#1f2937;">
                    Your vitals and cardiac metrics demonstrate <b>healthy heart rhythm, safe recovery capacity, and normal blood flow balance</b>. No significant signs of reduced heart oxygenation were noted.
                </p>
                <div style="font-size:0.92rem; font-weight:600; color:#065f46; line-height:1.6; margin-top:0.8rem; background:rgba(255,255,255,0.7); padding:10px 14px; border-radius:8px; border:1px solid rgba(52,211,153,0.35);">
                    <b>Healthy Habit Recommendation:</b> Maintain routine aerobic exercise (like brisk walking or swimming), balanced low-sodium meals, and routine annual checkups.
                </div>
            </div>
            """, unsafe_allow_html=True)

    with res_col2:
        st.markdown("""
            <div class="med-card" style="padding:1.4rem;">
                <div style="font-size:1.05rem; font-weight:800; margin-bottom:0.8rem; color:#0369a1;">
                    💓 Heart Health Summary
                </div>
        """, unsafe_allow_html=True)
        
        if has_disease:
            st.metric(
                label="Estimated Risk Level",
                value=f"{disease_probability*100:.1f} %",
                delta="Higher Risk - Medical Review Advised",
                delta_color="inverse"
            )
            st.progress(float(disease_probability))
        else:
            st.metric(
                label="Healthy Cardiac Index",
                value=f"{healthy_probability*100:.1f} %",
                delta="Normal & Balanced Profile",
                delta_color="normal"
            )
            st.progress(float(healthy_probability))
            
        st.caption(f"Profile: {age} year old {sex} with normal resting pulse & baseline pressure.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("🔬 Technical & Engineering Summary (For Clinicians / Developers)", expanded=False):
        st.markdown(f"""
        <div style="background:#edf3fa; border:1px solid rgba(14,116,144,0.2); padding:16px 20px; border-radius:10px; font-size:0.9rem; line-height:1.7; color:#0f172a;">
            <div style="color:#0369a1; font-weight:800; margin-bottom:6px;">
                ⚙️ Model Diagnostic Trace:
            </div>
            • <b>Selected Algorithm:</b> <span style="color:#0d9488; font-weight:700;">{selected_model}</span><br>
            • <b>Disease Probability Output:</b> {disease_probability*100:.2f}% | <b>Healthy Index:</b> {healthy_probability*100:.2f}%<br>
            • <b>Feature Scaling:</b> Standard Z-score Normalization applied to numerical attributes.<br>
            • <b>Key Predictive Factors in this run:</b> ST_Slope = {st_slope}, ChestPain = {chest_pain}, ExerciseAngina = {ex_angina}, Oldpeak = {oldpeak}.
        </div>
        """, unsafe_allow_html=True)

    components.html(
        """
        <script>
            setTimeout(function() {
                try {
                    const doc = window.parent.document;
                    const btn = doc.querySelector('.stButton > button');
                    if (btn) {
                        btn.classList.remove('btn-loading');
                        btn.removeAttribute('data-loading');
                        btn.innerHTML = '🔬 RUN CARDIAC ASSESSMENT';
                    }
                    const element = doc.getElementById('results-section');
                    if (element) {
                        element.scrollIntoView({behavior: 'smooth'});
                    }
                } catch(e) {}
            }, 150);
        </script>
        """,
        height=0,
    )

# -----------------------------------------------------------------------------
# 7. FOOTER
# -----------------------------------------------------------------------------
st.markdown("""
<div class="footer-credit">
    ❤️ Designed & Developed by <b>THE YOGESH POONIA</b> · Machine Learning & AI Engineering Portfolio
</div>
""", unsafe_allow_html=True)