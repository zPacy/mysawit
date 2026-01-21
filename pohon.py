import streamlit as st

def load_css():
    st.markdown("""
        <style>
        /* --- DEFINISI ANIMASI (Bounce & Glow) --- */
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

        /* --- SETTING BACKGROUND GAMBAR (GIF) --- */
        .stApp {
            background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                              url("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bjFlM2Rqenh2ZTIyY2ptZmlxaTU1eDZ5YjhmazkwcTg2Y2x0dnozMSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/aRZ4vTsHnyW6A/giphy.gif");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        
        /* --- UPDATE: STYLE CONTAINER (SOLID / TIDAK TRANSPARAN) --- */
        /* Menggunakan selector khusus untuk st.container(border=True) */
        [data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #111111 !important; /* Hitam Pekat */
            opacity: 1 !important; /* Memastikan tidak pudar */
            border-radius: 15px;
            border: 1px solid #444; /* Garis tepi abu-abu */
            padding: 15px;
        }

        /* Memastikan bagian dalam container juga mengikuti warna solid */
        [data-testid="stVerticalBlockBorderWrapper"] > div {
            background-color: #111111 !important;
        }
        
        /* --- Style untuk Tombol --- */
        .stButton button {
            width: 100%;
            border-radius: 10px;
            font-weight: bold;
            transition: transform 0.2s;
            background-color: #ffcc00; 
            color: black;
            border: none;
        }
        .stButton button:hover {
            transform: scale(1.05);
            background-color: #e6b800;
        }
        
        /* --- Style Text Input --- */
        /* Label (Judul input) berwarna putih */
        .stTextInput label {
            color: white !important;
            font-weight: bold;
        }
        /* Kolom ketikan berwarna abu gelap biar kontras dengan background hitam */
        .stTextInput input {
            color: white !important;
            background-color: #333333 !important; 
            border: 1px solid #555;
        }
        
        /* --- Style untuk Angka Saldo --- */
        [data-testid="stMetricValue"] {
            font-size: 24px;
            color: #ff6b6b;
        }
        
        /* --- JUDUL LOGIN ANIMASI --- */
        .judul-login {
            text-align: center !important;
            font-size: 3.5rem;
            font-weight: 900;
            margin-bottom: 20px;
            text-transform: uppercase;
            animation: bounce 2s infinite, glow 1.5s infinite alternate;
        }
        
        /* Menyembunyikan menu bawaan */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)