import streamlit as st
import pandas as pd

def run():

    st.markdown("""
        <style>
        div[data-testid="stMetric"] {
            border: 2px solid #9d4edd !important; padding: 20px; border-radius: 15px;
            background: rgba(157, 78, 221, 0.1) !important;
            box-shadow: 0px 4px 15px rgba(157, 78, 221, 0.3) !important;
        }
        .brand-glow { color: #7d39eb; font-weight: bold; text-shadow: 0px 0px 5px rgba(0, 242, 255, 0.5); }
        .footer-right {
            display: flex; justify-content: flex-end; align-items: center; gap: 8px;
            margin-top: 50px; color: #666; font-size: 0.72em;
            border-top: 0.5px solid #333; padding-top: 15px;
        }
        [data-testid="stAppViewContainer"] [data-testid="stIconMaterial"] { color: #9d4edd !important; }
        [data-testid="stAppViewContainer"] [data-testid="stIconMaterial"] svg { fill: currentColor !important; }
        [data-testid="stSidebarContent"] [data-testid="stIconMaterial"] svg { fill: #00f2ff !important; }
        </style>
        """, unsafe_allow_html=True)

    st.title(":material/query_stats: Product Campaign Performance")
    st.markdown("Measure the Profitability and ROI of a Single Campaign")
    st.divider()

    st.subheader(":material/database: Campaign Data")
    st.caption("Input all actual data from campaigns that have been running.")
    col_in1, col_in2, col_in3 = st.columns(3)

    with col_in1:
        st.markdown("### :material/payments: Financials")
        ad_spend = st.number_input("Total Ad Spend", min_value=0, value=250_000, step=50_000)
        creative_cost = st.number_input("Creative & Other Cost", min_value=0, value=50_000)
        admin_fee_pct = st.number_input("Admin/Tax Fee (%)", min_value=0.0, value=5.0)

    with col_in2:
        st.markdown("### :material/inventory_2: Product")
        cogs_per_unit = st.number_input("COGS per Unit", min_value=0, value=50_000, step=10_000)
        price_per_unit = st.number_input("Price per Unit", min_value=0, value=120_000, step=10_000)

    with col_in3:
        st.markdown("### :material/analytics: Performance")
        impressions = st.number_input("Total Impressions", min_value=1, value=15_000)
        clicks = st.number_input("Total Clicks", min_value=1, value=300)
        conversions = st.number_input("Total Conversions", min_value=0, value=15)

    st.divider()

    # 4. LOGIKA KALKULASI (BERDASARKAN DATA AKTUAL)
    total_investment = ad_spend + creative_cost
    gross_revenue = conversions * price_per_unit
    fee_amount = gross_revenue * (admin_fee_pct / 100)
    net_revenue = gross_revenue - fee_amount
    total_cogs = conversions * cogs_per_unit
    gross_profit = net_revenue - total_cogs - total_investment
    ctr = (clicks / impressions) * 100 if impressions > 0 else 0
    cpc = ad_spend / clicks if clicks > 0 else 0
    cpa = total_investment / conversions if conversions > 0 else 0
    conv_rate = (conversions / clicks) * 100 if clicks > 0 else 0
    roas = gross_revenue / ad_spend if ad_spend > 0 else 0
    roi = (gross_profit / total_investment) * 100 if total_investment > 0 else 0
    margin_per_unit = (price_per_unit * (1 - admin_fee_pct/100)) - cogs_per_unit
    bep_units = total_investment / margin_per_unit if margin_per_unit > 0 else 0
    aov = gross_revenue / conversions if conversions > 0 else 0
    target_bep_units = int(bep_units) + 1 if bep_units > 0 else 0
    break_even_revenue = target_bep_units * price_per_unit

    st.subheader(":material/emoji_events: Executive Summary")
    st.caption("Summary of the most important financial metrics from campaign performance results.")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("NET REVENUE", f"Rp {net_revenue:,.0f}")
    col2.metric("GROSS PROFIT", f"Rp {gross_profit:,.0f}", delta=f"{roi:.1f}% ROI")
    col3.metric("ROAS", f"{roas:.2f}x")
    col4.metric("CPA (Cost per Sale)", f"Rp {cpa:,.0f}")
    st.divider()
    c_left, c_right = st.columns(2)

    with c_left:
        st.subheader(":material/track_changes: Efficiency Analysis")
        st.caption("Measuring the effectiveness and efficiency of campaign operations.")
        metrics_df = pd.DataFrame({
            "Metric": ["CTR", "CPC", "Conversion Rate", "AOV (Avg. Order Value)"],
            "Value": [f"{ctr:.2f}%", f"Rp {cpc:,.0f}", f"{conv_rate:.2f}%", f"Rp {aov:,.0f}"]
        })
        st.table(metrics_df)

    with c_right:
        st.subheader(":material/security: Break-Even Point Analysis")
        st.caption("Break-even analysis based on costs and prices on this campaign.")
        if conversions >= target_bep_units:
            st.success(f":material/check_circle: STATUS: PROFIT // Passing BEP by {conversions - target_bep_units} units")
        else:
            st.error(f":material/cancel: STATUS: CRITICAL // Less {target_bep_units - conversions} units to reach BEP")
        st.info(f":material/flag: Sales Target BEP: **{target_bep_units} unit**")
        st.info(f":material/monetization_on: Revenue Target BEP: **Rp {break_even_revenue:,.0f}**")

    st.divider()
    with st.expander("📚 Glossary", expanded=False):
        st.write("""
    Berikut adalah penjelasan untuk setiap metrik yang dihitung dan ditampilkan dalam analyzer ini, dikelompokkan berdasarkan bagiannya.

    ### Ringkasan Eksekutif
    *   **Net Revenue (Pendapatan Bersih):** Total Omzet setelah dipotong biaya platform atau pajak (Admin/Tax Fee). Ini adalah uang bersih yang diterima sebelum dikurangi biaya operasional.
    *   **Operating Profit (Laba Operasional):** Angka keuntungan akhir bisnis Anda. Dihitung dari `Net Revenue` dikurangi **SEMUA** biaya: HPP (Biaya Variabel), Biaya Iklan, dan Biaya Tetap (Gaji, Sewa, dll).
    *   **ROAS (Return on Ad Spend):** Pengembalian atas Belanja Iklan. Mengukur berapa banyak **Omzet** (pendapatan kotor) yang dihasilkan untuk setiap Rupiah yang dihabiskan untuk iklan. Semakin tinggi, semakin baik.
    *   **CPA (Cost Per Acquisition):** Biaya per Akuisisi. Dalam konteks ini, ini adalah rata-rata biaya iklan (`Ad Spend`) yang dikeluarkan untuk menghasilkan **satu transaksi**. Semakin rendah, semakin efisien.
    *   **Delta (▲/▼):** Menunjukkan nilai perubahan (naik atau turun) dari periode sebelumnya. Untuk CPA, delta negatif (berwarna hijau) adalah hal yang baik karena berarti biaya per transaksi Anda menurun.

    ### Analisis Margin dan Efisiensi
    *   **Net Profit Margin:** Persentase Laba Bersih. Mengukur berapa persen keuntungan akhir (`Operating Profit`) yang Anda dapatkan dari setiap `Net Revenue`. Ini adalah indikator utama kesehatan finansial bisnis.
    *   **Gross Profit Margin:** Persentase Laba Kotor. Mengukur efisiensi HPP Anda. Dihitung dari (Omzet - HPP) / Omzet.
    *   **AOV (Average Order Value):** Nilai Pesanan Rata-rata. Rata-rata jumlah uang yang dibelanjakan pelanggan dalam satu transaksi.
    *   **CTR (Click-Through Rate):** Persentase klik dari total tayangan iklan. Mengukur seberapa menarik iklan Anda bagi audiens.
    *   **CPC (Cost Per Click):** Biaya per Klik. Rata-rata biaya yang Anda bayar setiap kali seseorang meng-klik iklan Anda.

    ### Analisis Titik Impas (Break-Even)
    *   **Sales Target BEP (Transactions):** Jumlah **transaksi** minimum yang harus Anda capai dalam satu periode agar total pendapatan bisa menutupi semua biaya (impas).
    *   **Revenue Target BEP:** Jumlah **pendapatan** minimum yang harus Anda capai agar bisnis tidak merugi.
    """)
        
    st.markdown("""
        <div class="footer-right">
            <span>APEX Suite by</span>
            <span class="brand-glow">ESNV</span>
            <span>| © 2025</span>
        </div>
        """, unsafe_allow_html=True)
