import streamlit as st
import pandas as pd
import pickle  # Library untuk memuat file model.pkl
import base64

# --- KODE LATAR BELAKANG BINTANG BERGERAK ---
# --- KODE CSS: BINTANG BERVARIASI + EFEK JUDUL GLOWING ---
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #050914 !important;
        background-image: 
            radial-gradient(1px 1px at 25px 50px, #ffffff, transparent),
            radial-gradient(2px 2px at 75px 150px, #ffffff, transparent),
            radial-gradient(1.5px 1.5px at 120px 300px, rgba(255, 255, 255, 0.8), transparent),
            radial-gradient(2.5px 2.5px at 200px 80px, #ffe4d6, transparent), 
            radial-gradient(1px 1px at 280px 220px, #ffffff, transparent),
            radial-gradient(3px 3px at 350px 40px, #d6e8ff, transparent),  
            radial-gradient(1px 1px at 420px 180px, rgba(255, 255, 255, 0.4), transparent), 
            radial-gradient(2px 2px at 480px 320px, #ffffff, transparent) !important;
        
        background-size: 550px 550px !important; 
        animation: jalanBintang 35s linear infinite !important; 
    }

    @keyframes jalanBintang {
        from { background-position: 0 0; }
        to { background-position: 550px 550px; }
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }

    /* Mengubah semua efek banyangan/glow menjadi warna putih (#ffffff) */
    .judul-glowing {
        color: #ffffff !important;
        font-size: 3rem !important;
        font-weight: 700 !important;
        text-shadow: 0 0 5px #ffffff, 0 0 10px #ffffff, 0 0 10px #ffffff, 0 0 20px rgba(230, 230, 230, 0.6) !important;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# -----------------------------------------------------------------------

# Judul Utama Aplikasi dengan Efek Glowing Putih (Sesuai panduan wajib) [cite: 28]
st.markdown('<h1 class="judul-glowing">My Portfolio with Streamlit</h1>', unsafe_allow_html=True)

# 2. Deskripsi Singkat di Awal Halaman
st.write("Selamat datang di portofolio saya! Di sini Anda dapat melihat informasi diri, proyek yang telah saya kerjakan, serta implementasi model machine learning.")

# 3. Membuat Menu Navigasi di Samping (Sidebar)
st.sidebar.title("Navigasi")
halaman = st.sidebar.radio(
    "Pilih Halaman:",
    ["Tentang Saya", "Proyek Saya", "Prediksi Model", "Visualisasi & Performa"]
)

# --- LOGIKA PERPINDAHAN HALAMAN ---
if halaman == "Tentang Saya":
    # Bagian Atas / Ringkasan
    st.write("") # Memberi sedikit jarak atas
    
    # 1. Membuat 2 Kolom (Kolom kiri untuk foto, kolom kanan untuk teks profil)
    kolom_kiri, kolom_kanan = st.columns([1, 2])
    
    with kolom_kiri:
        link_foto_kamu = r"D:\portofolio_streamlit_elmira\10.jpeg"
    
    with open(link_foto_kamu, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    link_foto_kamu = f"data:image/jpeg;base64,{encoded_string}"
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="{link_foto_kamu}" style="
                border-radius: 50%;
                border: 6px solid #d81b60; 
                width: 170px;
                height: 170px;
                object-fit: cover;
                box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            ">
        </div>
        """,
        unsafe_allow_html=True
    )
        
    with kolom_kanan:
        # Nama, Tagline, dan Tombol Kontak
        st.markdown(
            """
            <div style="margin-top: 10px;">
                <h1 style="color: #ffffff; margin-bottom: 5px; font-size: 2.5rem; font-weight: 700;">
                    Elmira Adi Mazaya Muntaz
                </h1>
                <p style="color: #b0bec5; font-size: 1.1rem; line-height: 1.4; margin-bottom: 20px;">
                    First-year undergraduate student at IPB University, majoring in SSMI, with a focused aspiration to pursue a career in data analysis. Demonstrates a strong commitment to academic growth, analytical thinking, and collaborative learning. Actively developing problem-solving competencies and data literacy to generate meaningful insights. Seeking opportunities to engage in research-driven environments and contribute to intellectually stimulating projects
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Membuat tombol "Contact Me" yang stylish dengan ikon amplop
        st.link_button("✉️ Contact Me", "mailto:email_kamu@gmail.com")

    st.write("---")

    # 1. Experience & Qualifications
    st.markdown("## Experience & Qualifications")
    st.markdown("""
    * ✔️ Memiliki pemahaman kuat dalam dasar-dasar statistika, matematika, dan aplikasinya pada data.
    * ✔️ Berpengalaman praktis dalam pemrograman Python dan manipulasi data menggunakan Pandas & NumPy.
    * ✔️ Memahami alur kerja MLOps (End-to-End) mulai dari pelatihan model hingga deployment.
    * ✔️ Mampu bekerja sama dengan baik di dalam tim serta memiliki inisiatif tinggi dalam pemecahan masalah.
    """)
    st.write("---")

    # 2. Hard Skills
    st.markdown("## Hard Skills")
    st.markdown("""
    * 💻 **Programming:** Python (Scikit-learn, Pandas), SQL, VBA
    * 📊 **Data Visualization:** Streamlit, Matplotlib, Seaborn, Plotly
    * 🤖 **Modeling:** Linear Regression, Logistic Regression, Decision Trees
    * 🗄️ **Databases:** MySQL, PostgreSQL
    """)
    st.write("---")

    # 3. History & Education (Pengganti Work History agar cocok dengan profilmu)
    st.markdown("## History & Education")
    
    # Riwayat 1
    st.markdown("⏳ **Data Science & Machine Learning Bootcamp | Dibimbing.id**")
    st.caption("2026 - Present") # Mengikuti waktu saat ini
    st.markdown("""
    * Mengembangkan rancangan aplikasi portofolio berbasis web menggunakan Streamlit.
    * Membangun pipeline Machine Learning siap produksi untuk proyek prediksi harga rumah.
    """)
    
    st.write("") # Jarak vertikal kosong
    
    # Riwayat 2
    st.markdown("🎓 **S1 Matematika | IPB University**")
    st.caption("2022 - Present")
    st.markdown("""
    * Mempelajari pemodelan matematika, analisis data kuantitatif, dan statistika inferensial.
    """)

# Bagian 2: Proyek Saya
elif halaman == "Proyek Saya":
    st.header("📁 Proyek Saya")
    st.write("Berikut adalah 3 proyek utama yang telah saya selesaikan:")
    st.write("---")
    
    # --- CONTOH PROYEK 1 ---
    # Proyek 1
    st.subheader("1. Time Series Forecasting: Prediksi Transaksi Harian")
    st.write("""
    Secara keseluruhan, projek ini mencakup eksplorasi data menggunakan Python seperti Pandas dan Seaborn dari dataset Telco_customer_churn.csv, serta pembuatan visualisasi grafik untuk melihat pola seperti distribusi tagihan bulanan dan skor risiko. Langkah ini membantu kita mengidentifikasi kelompok pelanggan yang rawan berhenti, misalnya fenomena "High Value, High Risk" di mana pelanggan bertagihan mahal yang baru berlangganan rentan untuk pergi. Pada akhirnya, semua langkah ini difokuskan untuk memecahkan masalah bisnis secara nyata dengan memberikan rekomendasi pencegahan seperti layanan VIP sejak awal, diskon berkala, atau menghubungi pelanggan langsung saat skor risikonya menyentuh angka 70 sebagai strategi mempertahankan pelanggan melalui data.
    """)
    
    # Menampilkan Gambar/Visualisasi hasil prediksi dari Google Colab
    try:
        st.image("newplot.png", caption="Grafik Prediksi Time Series", use_container_width=True)
    except:
        st.info("📷 Tampilan Gambar: ")
    st.write("") # Memberi sedikit jarak antar gambar
    
    # Menampilkan grafik kedua (bawah)
    try:
        st.image("oo.png", caption="Plot ACF & PACF", use_container_width=True)
    except:
        st.info("📷 Tampilan Gambar 2:")

    st.write("") # Memberi sedikit jarak sebelum tombol

    # Tombol interaktif untuk menghubungkan langsung ke Google Colab kamu
    st.link_button("🚀 Lihat Kode di Google Colab", "https://colab.research.google.com/drive/1xLA5vJb9xYYvxFZdkV404Dux0QG-EEiv?usp=sharing")
    
    # Proyek 2
    st.subheader("2.E-commerce Sales Analytics & Forecasting: Time Series, Bundling, dan Rekomendasi Strategis")
    st.write("""
    Proyek ini bertujuan untuk menganalisis data transaksi e-commerce sepanjang tahun 2019 guna mengungkap pola penjualan, perilaku pelanggan, serta peluang bisnis melalui pendekatan time series dan machine learning. Dengan melakukan pembersihan data, agregasi harian/mingguan/bulanan, serta visualisasi tren dan musim, proyek ini mengidentifikasi produk terlaris, kombinasi bundling potensial, kota dengan volume dan nilai transaksi tertinggi, serta jam-jam puncak penjualan. Selanjutnya, dibangun dua model forecasting (ARIMA dan LSTM) untuk memprediksi jumlah order 30 hari ke depan, dievaluasi dengan MAE, dan dipilih model terbaik. Tujuan akhirnya adalah memberikan rekomendasi strategis bagi tim bisnis, seperti optimalisasi stok, efisiensi iklan, peningkatan nilai keranjang belanja, serta prioritas logistik di kota-kota kunci.
    """)
    
    # Menampilkan grafik pertama (atas)
    try:
        st.image("download.png", caption="Grafik Prediksi Time Series", use_container_width=True)
    except:
        st.info("📷 Tampilan Gambar 1: ")
        
    st.write("") # Memberi sedikit jarak antar gambar
    
    # Menampilkan grafik kedua (bawah)
    try:
        st.image("88.png", caption="Plot ACF & PACF", use_container_width=True)
    except:
        st.info("📷 Tampilan Gambar 2: )")

    try:
        st.image("44.png", caption="Plot ACF & PACF", use_container_width=True)
    except:
        st.info("📷 Tampilan Gambar 2:")

    st.write("") # Memberi sedikit jarak sebelum tombol
    
    # Tombol interaktif untuk menghubungkan langsung ke Google Colab kamu
    st.link_button("🚀 Lihat Kode di Google Colab", "https://colab.research.google.com/drive/1vkuH__STdGVcrsdC6RCdmR6Nxhwnle3S?usp=sharing")

    #projek 3
    st.subheader("3. Customer Churn Prediction for Telecom: Model Comparison, Business Insights, and ROI Simulation")
    st.write("""
    Proyek ini bertujuan untuk memprediksi churn pelanggan perusahaan telekomunikasi menggunakan dataset Telco Customer Churn dengan 7.043 pelanggan. Melalui serangkaian proses pembersihan data, eksplorasi fitur (tenure, monthly charges, kontrak, layanan internet, metode pembayaran), encoding kategorikal, scaling numerik, dan transformasi log pada TotalCharges, dibangun tiga model klasifikasi—Decision Tree, Random Forest, dan XGBoost—yang dievaluasi menggunakan akurasi, presisi, recall, F1-score, dan AUC-ROC. Random Forest memberikan keseimbangan terbaik dengan akurasi 78,7% dan AUC 0,827, sementara XGBoost memiliki recall tertinggi (49,7%) yang penting untuk mendeteksi pelanggan berisiko. Simulasi dampak bisnis menunjukkan bahwa dengan biaya insentif $50 per pelanggan yang diprediksi churn dan tingkat efektivitas 30%, program retensi berpotensi menyelamatkan 58 pelanggan dari total 374 churn aktual, menghasilkan net gain sekitar $29.463 dalam 12 bulan. Proyek ini menghasilkan rekomendasi strategis seperti mengonversi kontrak bulanan ke tahunan, memperbaiki kualitas layanan Fiber optic, serta memprioritaskan intervensi pada pelanggan baru dan pengguna metode pembayaran Electronic check.
    """)
    
    # Menampilkan grafik pertama (atas)
    try:
        st.image("22.png", caption="Grafik Prediksi Time Series", use_container_width=True)
    except:
        st.info("📷 Tampilan Gambar 1: ")
        
    st.write("") # Memberi sedikit jarak antar gambar
    
    # Menampilkan grafik kedua (bawah)
    try:
        st.image("33.png", caption="Plot ACF & PACF", use_container_width=True)
    except:
        st.info("📷 Tampilan Gambar 2: )")
    st.write("") # Memberi sedikit jarak sebelum tombol
    
    # Tombol interaktif untuk menghubungkan langsung ke Google Colab kamu
    st.link_button("🚀 Lihat Kode di Google Colab", "https://colab.research.google.com/drive/1Kmf6dQAYKw70erXMXSKtqC7RLHW8Wed2?usp=sharing")

# Bagian 3: Prediksi Model (SEKARANG MENGGUNAKAN MODEL ASLI KAMU)
elif halaman == "Prediksi Model":
    st.header("⚙️ Implementasi Prediksi Model")
    st.write("Halaman ini terintegrasi langsung dengan **model.pkl** dari proyek MLOps Anda.")
    
    # Fitur Upload File CSV
    file_diunggah = st.file_uploader("Unggah file data rumah baru (Format .csv)", type=["csv"])
    
    if file_diunggah is not None:
        df = pd.read_csv(file_diunggah)
        st.write("### Data yang Berhasil Diunggah:")
        st.dataframe(df.head())
        
        # Tombol untuk Trigger Pipeline Prediksi
        tombol_prediksi = st.button("Mulai Prediksi Harga Rumah")
        
        if tombol_prediksi:
            st.write("Memproses prediksi...")
        try:
            # Membuka dan memuat model.pkl asli kamu
            with open("model.pkl", "rb") as file_model:
                model_asli = pickle.load(file_model)
            
            # --- KODE PINTAR PEMILIH KOLOM ---
            # 1. Tanya ke model, kolom apa saja yang dia butuhkan
            kolom_wajib = model_asli.feature_names_in_
            
            # 2. Paksa dataframe untuk HANYA mengambil kolom-kolom tersebut
            df_siap_prediksi = df[kolom_wajib]
            
            # 3. Melakukan prediksi sesungguhnya menggunakan data yang sudah difilter
            hasil_prediksi = model_asli.predict(df_siap_prediksi)
            
            # Memasukkan hasil prediksi ke dalam tabel agar bisa dilihat user
            df['Hasil Prediksi Harga'] = hasil_prediksi
            
            st.success("✨ Proses Prediksi dengan Model Asli Selesai!")
            st.write("### Hasil Prediksi:")
            st.dataframe(df[['Hasil Prediksi Harga']].head())

        except Exception as e:
            st.error(f"Terjadi kendala saat memproses model: {e}")
            st.info("Catatan: Pastikan file CSV yang kamu unggah memiliki struktur kolom yang sama persis seperti saat kamu melatih model dulu ya!")

# Bagian 4: Visualisasi Data
# Bagian: Visualisasi & Performa Model (Interaktif)
elif halaman == "Visualisasi & Performa":
    st.header("📊 Analisis Data & Performa Model")
    st.write("Halaman ini menyediakan visualisasi interaktif dataset dan perbandingan performa model evaluasi.")
    st.write("---")

    # PILIHAN UTAMA: Memilih antara Visualisasi Data atau Performa Model
    # ==========================================

    opsi_utama = st.sidebar.selectbox(
        "Pilih Halaman:", 
        ["1. Visualisasi Dataset", "2. Performa Model"]
    )

    if opsi_utama == "1. Visualisasi Dataset":
        st.subheader("🌌 Visualisasi Dataset Utama")
        pilihan_grafik = st.selectbox(
            "Pilih jenis grafik yang ingin ditampilkan:",
            [
                "Pengaruh Kualitas Bangunan terhadap Harga",
                "Tren Harga Berdasarkan Tahun Dibangun",
                "Jumlah Rumah Berdasarkan Tipe Desain",
                "Distribusi Harga Berdasarkan Kapasitas Garasi"
            ]
        )

        # Pastikan path ini sesuai dengan hasil Copy Path lu tadi
        if pilihan_grafik == "Pengaruh Kualitas Bangunan terhadap Harga":
            st.image(r"11.png", caption="Boxplot Kualitas vs Harga")
        elif pilihan_grafik == "Tren Harga Berdasarkan Tahun Dibangun":
            st.image(r"12.png", caption="Scatter Plot Tahun Dibangun vs Harga")
        elif pilihan_grafik == "Jumlah Rumah Berdasarkan Tipe Desain":
            st.image(r"13.png", caption="Countplot Tipe Desain Rumah")
        elif pilihan_grafik == "Distribusi Harga Berdasarkan Kapasitas Garasi":
            st.image(r"14.png", caption="Violin Plot Kapasitas Garasi vs Harga")

    elif opsi_utama == "2. Performa Model":
        st.subheader("📊 Rapor Akurasi Model")
        
        # Dropdown pilihan model (Pastikan cuma ada SATU selectbox ini biar gak eror dobel)
        pilihan_model = st.selectbox("Pilih Model:", ["Linear Regression", "Random Forest"])
        # Ganti bagian ini di halaman "Visualisasi & Performa"
        if pilihan_model == "Linear Regression":
            st.write("### Evaluasi Linear Regression")
            col1, col2, col3 = st.columns(3)
            col1.metric(label="R² Score", value="0.904")
            col2.metric(label="MAE", value="18,487")
            col3.metric(label="RMSE", value="27,501")
            st.image("16.png", caption="Grafik Evaluasi: Linear Regression")

        elif pilihan_model == "Random Forest":
            st.write("### Evaluasi Random Forest")
            col1, col2, col3 = st.columns(3)
            col1.metric(label="R² Score", value="0.910")
            col2.metric(label="MAE", value="16,785")
            col3.metric(label="RMSE", value="26,556")
            st.image("17.png", caption="Grafik Evaluasi: Random Forest")
            st.image("18.png", caption="Grafik Evaluasi: Random Forest")
            
