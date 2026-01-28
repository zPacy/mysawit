import streamlit as st

def load_css():
    st.markdown("""
        <style>
        /* --- 1. DEFINISI ANIMASI (Bounce & Glow) --- */
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-20px); }
            60% { transform: translateY(-10px); }
        }
        @keyframes glow {
            0% { text-shadow: 0 0 5px #fff; color: white; }
            50% { text-shadow: 0 0 20px #ffd700; color: #ffd700; }
            100% { text-shadow: 0 0 5px #fff; color: white; }
        }

        /* --- 2. CLASS JUDUL KHUSUS (Dipanggil di main.py) --- */
        .judul-login {
            text-align: center !important; /* Rata Tengah */
            font-size: 3.5rem;
            font-weight: 900;
            margin-bottom: 20px;
            text-transform: uppercase;
            /* Terapkan Animasi */
            animation: bounce 2s infinite, glow 1.5s infinite alternate;
        }

        /* --- 3. BACKGROUND UTAMA (Hijau Sawit Polos) --- */
        .stApp {
            background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                              url("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bjFlM2Rqenh2ZTIyY2ptZmlxaTU1eDZ5YjhmazkwcTg2Y2x0dnozMSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/aRZ4vTsHnyW6A/giphy.gif");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        
        /* --- 4. STYLE TOMBOL --- */
        .stButton button {
            width: 100%;
            border-radius: 10px;
            font-weight: bold;
            background-color: #ffcc00; /* Kuning Emas */
            color: black;
            border: none;
        }
        .stButton button:hover {
            transform: scale(1.02);
            background-color: #e6b800;
        }

        /* --- 5. STYLE WARNA SALDO --- */
        [data-testid="stMetricValue"] {
            font-size: 24px;
            color: #ff6b6b; /* Merah Muda */
        }
        
        /* --- 6. MEMBERSIHKAN TAMPILAN --- */
        /* Hanya menyembunyikan menu pojok kanan atas & footer */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* CATATAN: Saya TIDAK menyembunyikan 'header' agar tombol sidebar tetap aman */

        /* --- 7. MENGHILANGKAN IKON RANTAI (ANCHOR) --- */
/* Menghilangkan elemen anchor secara spesifik menggunakan selektor atribut */
[data-testid="stHeaderActionElements"], 
.st-emotion-cache-15zrgzn, 
a.header-anchor {
    display: none !important;
}

/* Menggunakan global selector untuk menyembunyikan semua link di dalam heading */
h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
    display: none !important;
}

/* Tambahan: Menghilangkan padding berlebih agar judul tetap di tengah */
[data-testid="stMarkdownContainer"] h1, 
[data-testid="stMarkdownContainer"] h2, 
[data-testid="stMarkdownContainer"] h3 {
    padding-top: 0px !important;
}
        </style>
    """, unsafe_allow_html=True)