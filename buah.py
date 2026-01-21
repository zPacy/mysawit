import streamlit as st
import pohon  # Memanggil file styles.py

# 1. Konfigurasi Halaman
st.set_page_config(page_title=" 🌴 SELAMAT DATANG DI SAWIT TOTO 🌴 ", layout="wide")

# Memuat CSS
pohon.load_css()

# --- DATA DUMMY (6 JENIS SAWIT) ---
data_sawit = [
    {"nama": "Sawit Manis", "ways": "1 in 100 ", "img": "https://srs-ssms.com/wp-content/uploads/DSC_0140-1140x640.jpg"},
    {"nama": "Sawit Besar", "ways": "1 in 1000 ", "img": "https://srs-ssms.com/wp-content/uploads/DSC_0140-1140x640.jpg"},
    {"nama": "Sawit Peri", "ways": "1 in 10000 ", "img": "https://srs-ssms.com/wp-content/uploads/DSC_0140-1140x640.jpg"},
    {"nama": "Sawit Brondolan", "ways": "1 in 10 ", "img": "https://srs-ssms.com/wp-content/uploads/DSC_0140-1140x640.jpg"},   
    {"nama": "Sawit Premium", "ways": "1 in 2000 ", "img": "https://srs-ssms.com/wp-content/uploads/DSC_0140-1140x640.jpg"},
    {"nama": "Sawit Tung Tung", "ways": "1 in 200 ", "img": "https://srs-ssms.com/wp-content/uploads/DSC_0140-1140x640.jpg"}
]

# --- INISIALISASI SESSION STATE ---
if 'status_login' not in st.session_state:
    st.session_state['status_login'] = False
if 'nama_user' not in st.session_state:
    st.session_state['nama_user'] = "" # Siapkan wadah kosong untuk nama

# --- HALAMAN LOGIN ---
def login_page():
    # Menggunakan class CSS dari styles.py
    st.markdown('<h1 class="judul-login">DAFTAR SEKARANG!</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        with st.container(border=True):
            username = st.text_input("Username", placeholder="Masukkan nama anda")
            password = st.text_input("Password", type="password", placeholder="Masukkan password anda")
            
            if st.button("Masuk"):
                # Validasi Input
                if not username or not password:
                    st.error("Kamu belum memasukkan nama atau password!")
                elif len(password) < 8:
                    st.error("Password terlalu pendek! Minimal 8 karakter.")
                elif not any(char.isdigit() for char in password):
                    st.error("Password harus mengandung setidaknya satu angka!")
                else:
                    # --- BAGIAN PENTING: MENYIMPAN DATA ---
                    st.success("Login Berhasil!")
                    st.session_state['status_login'] = True
                    st.session_state['nama_user'] = username # Simpan nama input ke memori
                    st.rerun()

# --- HALAMAN UTAMA (SAWIT TOTO) ---
def main_page():
    # Ambil nama yang tersimpan di memori
    nama_aktif = st.session_state['nama_user']
    
    # --- SIDEBAR (INFO PENGGUNA DINAMIS) ---
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
        
        # TAMPILKAN NAMA DARI INPUT USER
        st.title(nama_aktif.upper()) # Ubah jadi huruf besar semua
        st.write("**Status:** Member Baru")
        
        st.divider()
        
        st.metric(label="Saldo Dompet", value="Rp 0", delta="Belum Deposit")
        
        st.divider()
        st.button("Deposit")
        st.button("Riwayat Penarikan")
        
        if st.button("Log Out", type="primary"):
            st.session_state['status_login'] = False
            st.session_state['nama_user'] = "" # Kosongkan nama saat logout
            st.rerun()

    # --- KONTEN UTAMA ---
    st.title("🌴 SAWIT TOTO")
    st.caption(f"Selamat datang, {nama_aktif}! Jangan Asal Pilih Sawit!")

    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]

    for i, item in enumerate(data_sawit):
        with cols[i % 3]:
            with st.container(border=True):
                st.image(item["img"], use_container_width=True)
                st.subheader(item["nama"])
                st.info(f"Ways: {item['ways']}")
                if st.button(f"Pilih {item['nama']}", key=f"btn_{i}"):  
                    st.toast(f"{nama_aktif} memilih: {item['nama']}")

    st.divider()

# --- LOGIKA KONTROL UTAMA ---
if st.session_state['status_login'] == False:
    login_page()
else:
    main_page()