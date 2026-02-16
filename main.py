import streamlit as st
import sys
import os

utils_path = os.path.join(os.path.dirname(__file__), 'utils')
if utils_path not in sys.path:
    sys.path.append(utils_path)

st.set_page_config(
    page_title="APEX Suite Demo | ESNV",
    page_icon="⚛️",
    layout="wide"
)

if 'page' not in st.session_state:
    st.session_state.page = "Home"

st.markdown("""
<style>
    /* Tombol Sidebar Rata Kiri */
    [data-testid="stSidebarContent"] .stButton > button {
        width: 100% !important; border: none !important; background-color: transparent !important;
        text-align: left !important; justify-content: flex-start !important;
        padding: 10px 20px !important; display: flex !important; align-items: center !important;
        gap: 15px !important; color: #b0a8c2 !important;
    }
    /* Warna Ikon Ungu */
    [data-testid="stSidebarContent"] .stButton button span[data-testid="stIconMaterial"],
    [data-testid="stSidebarContent"] [data-testid="stIconMaterial"] {
        color: #9d4edd !important;
    }
    /* Hover Effect Sidebar */
    [data-testid="stSidebarContent"] .stButton > button:hover {
        background-color: rgba(157, 78, 221, 0.1) !important;
        color: #ffffff !important;
    }
    /* Branding Style */
    .brand-title { 
        color: #9d4edd; font-weight: 800; font-size: 1.6em; padding: 20px 20px 10px 20px;
    }
    .nav-label {
        color: #6c5f82; font-size: 0.75em; font-weight: bold;
        padding: 15px 20px 5px 22px; letter-spacing: 1.5px; text-transform: uppercase;
    }
    /* Hover Effect untuk Kartu Home */
    [data-testid="stVerticalBlock"] > [data-testid="stHorizontalBlock"] > [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
        transition: background-color 0.3s ease;
    }
    [data-testid="stVerticalBlock"] > [data-testid="stHorizontalBlock"] > [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"]:hover {
        background-color: rgba(157, 78, 221, 0.05);
    }
    /* --- PERBAIKAN: CSS untuk mensejajarkan tombol --- */
    .card-caption {
        min-height: 40px; /* Memberi ruang yang cukup untuk 2 baris teks */
        font-size: 0.9em;
        color: rgba(255, 255, 255, 0.6);
    }
</style>
""", unsafe_allow_html=True)


def navigate(page_name):
    st.session_state.page = page_name
    st.rerun()

with st.sidebar:
    st.markdown("<div class='brand-title'>APEX Suite</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    if st.button("Home", icon=":material/home:", use_container_width=True): navigate("Home")
    
    st.markdown("<p class='nav-label'>Ads Overview</p>", unsafe_allow_html=True)
    
    if st.button("Product Analyzer", icon=":material/inventory_2:", use_container_width=True): navigate("analyzer_product") 
    if st.button("Business Analyzer", icon=":material/storefront:", use_container_width=True): navigate("analyzer_business")
    if st.button("ROI Analyzer", icon=":material/lan:", use_container_width=True): navigate("analyzer_roi")
    
    st.markdown("<p class='nav-label'>Ads Forecasting</p>", unsafe_allow_html=True)
    if st.button("Product Optimizer", icon=":material/auto_fix:", use_container_width=True): navigate("optimizer_product")
    if st.button("Business Optimizer", icon=":material/storefront:", use_container_width=True): navigate("optimizer_business")
    
    st.markdown("<p class='nav-label'>Ads Evaluation</p>", unsafe_allow_html=True)
    if st.button("Content Ranker", icon=":material/rocket_launch:", use_container_width=True): navigate("content_ranker")
    
    st.markdown("<br>---", unsafe_allow_html=True)
    st.caption("v1.3.2 // Powered by ESNV ")


# 4. CONTENT AREA & ROUTING
def execute_module(page_name):
    try:
        # Mengimpor modul secara dinamis
        module = __import__(page_name)
        # Menjalankan fungsi utama dalam modul (misal: run())
        if hasattr(module, 'run'):
            module.run()
        else:
            st.info(f"For a demonstration of the full features, please contact me at: elangelano@tujuhcahaya.com")
    except ModuleNotFoundError:
        st.info(f"For a demonstration of the full features, please contact me at: elangelano@tujuhcahaya.com")
    except Exception as e:
        st.info(f"For a demonstration of the full features, please contact me at: elangelano@tujuhcahaya.com")

# Halaman Home
if st.session_state.page == "Home":
    st.header("⚛️ APEX Suite")
    st.markdown("Select the tools you want to use to analyze and plan marketing strategies.")
    st.divider()
    st.subheader("📊 Ads Overview")
    st.caption("Performance analysis of existing campaigns.")
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.markdown("##### :material/inventory_2: Product Analyzer")
            st.markdown('<div class="card-caption">Profitability analysis for one type of product.</div>', unsafe_allow_html=True)
            if st.button("Launch", key="launch_pa", use_container_width=True): navigate("analyzer_product")
    with c2:
        with st.container(border=True):
            st.markdown("##### :material/storefront: Business Analyzer")
            st.markdown('<div class="card-caption">Monthly profit and loss analysis for visits.</div>', unsafe_allow_html=True)
            if st.button("Launch", key="launch_ba", use_container_width=True): navigate("analyzer_business")
    with c3:
        with st.container(border=True):
            st.markdown("##### :material/lan: ROI Analyzer")
            st.markdown('<div class="card-caption">Compare ROAS and CPA from different advertising channels.</div>', unsafe_allow_html=True)
            if st.button("Launch", key="launch_ra", use_container_width=True): navigate("analyzer_roi")
    st.divider()
    st.subheader("🎯 Ads Forecasting")
    st.caption("Project budget and targets for future campaigns.")
    c4, c5, c6 = st.columns(3)
    with c4:
        with st.container(border=True):
            st.markdown("##### :material/auto_fix: Product Optimizer")
            st.markdown('<div class="card-caption">Ideal advertising budget for product profit targets.</div>', unsafe_allow_html=True)
            if st.button("Launch", key="launch_po", use_container_width=True): navigate("optimizer_product")
    with c5:
        with st.container(border=True):
            st.markdown("##### :material/coffee: Business Optimizer")
            st.markdown('<div class="card-caption">Find the ideal advertising budget for your target audience.</div>', unsafe_allow_html=True)
            if st.button("Launch", key="launch_bo", use_container_width=True): navigate("optimizer_business")
    st.divider()
    st.subheader("🏆 Ads Evaluation")
    st.caption("Evaluate and rank creative/content performance.")
    c7, c8, c9 = st.columns(3)
    with c7:
        with st.container(border=True):
            st.markdown("##### :material/rocket_launch: Content Ranker")
            st.markdown('<div class="card-caption">Rank ad content from most to most profitable.</div>', unsafe_allow_html=True)
            if st.button("Launch", key="launch_cr", use_container_width=True): navigate("content_ranker")


# --- LANGKAH 3: ROUTING KE MODUL DI DALAM 'utils' ---
elif st.session_state.page != "Home":
    execute_module(st.session_state.page)

