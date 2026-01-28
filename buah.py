import streamlit as st
import random
import time
import pohon

# 1. Konfigurasi Halaman
st.set_page_config(page_title="🌴 SAWIT TOTO 🌴", layout="wide")

# Memuat CSS
pohon.load_css()

# --- DATA DUMMY ---
data_sawit = [
    {"nama": "Sawit Manis", "ways": "1 in 100", "img": "https://srs-ssms.com/wp-content/uploads/DSC_0140-1140x640.jpg"},
    {"nama": "Sawit Besar", "ways": "1 in 1000", "img": "https://srs-ssms.com/wp-content/uploads/DSC_0140-1140x640.jpg"},
    {"nama": "Sawit Peri", "ways": "1 in 10000", "img": "https://srs-ssms.com/wp-content/uploads/DSC_0140-1140x640.jpg"},
    {"nama": "Sawit Brondolan", "ways": "1 in 10", "img": "https://srs-ssms.com/wp-content/uploads/DSC_0140-1140x640.jpg"},   
    {"nama": "Sawit Premium", "ways": "1 in 2000", "img": "https://srs-ssms.com/wp-content/uploads/DSC_0140-1140x640.jpg"},
    {"nama": "Sawit Tung Tung", "ways": "1 in 200", "img": "https://srs-ssms.com/wp-content/uploads/DSC_0140-1140x640.jpg"}
]

# --- INISIALISASI SESSION STATE ---
if 'status_login' not in st.session_state:
    st.session_state['status_login'] = False
if 'nama_user' not in st.session_state:
    st.session_state['nama_user'] = ""
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = "dashboard"

# --- STATE BARU: SALDO & EKONOMI ---
if 'saldo_user' not in st.session_state:
    st.session_state['saldo_user'] = 0 
if 'deposit_mode' not in st.session_state:
    st.session_state['deposit_mode'] = False 

# --- FUNGSI FORMAT RUPIAH ---
def format_rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")

# --- CONFIG PROBABILITAS (WEIGHTED RNG) ---
# Daftar Simbol
symbols = ["🌴", "🍒", "💰", "🚛", "💎", "7️⃣"]

# Bobot Kemunculan (Total 100 biar gampang hitung)
# 🌴 (22%)^3 ≈ 1% Chance (1 in 100) -> Target Jackpot
# 🍒 (46%)^3 ≈ 10% Chance (1 in 10) -> Target Hadiah Kecil
# Sisanya (8%)^3 ≈ Sangat Kecil (Zonk / Penambah Variasi)
weights = [22, 46, 8, 8, 8, 8] 

def acak_simbol():
    """Mengambil 1 simbol berdasarkan bobot probabilitas"""
    return random.choices(symbols, weights=weights, k=1)[0]

# --- FUNGSI: HITUNG HADIAH (SISTEM TIER) ---
def hitung_kemenangan(simbol):
    if simbol == "🌴":
        return 20000
    elif simbol in ["💎", "7️⃣"]:
        return 5000
    elif simbol in ["💰", "🚛"]:
        return 2500
    else: # Cherry
        return 1500

# --- FUNGSI: HALAMAN DEPOSIT ---
def deposit_interface():
    st.markdown("### Isi Saldo Kamu!")
    
    with st.form("form_deposit"):
        jumlah_topup = st.number_input("Masukkan Jumlah Uang (Rp)", min_value=0, step=1000)
        
        col_cek, col_konfirm = st.columns([1, 1])
        
        with col_cek:
            cek = st.form_submit_button("🔍 Cek Nominal")
            
        with col_konfirm:
            submit = st.form_submit_button("✅ Konfirmasi")
        
        if cek:
            if jumlah_topup < 1000:
                st.warning("⚠️ Minimal deposit Rp 1.000")
            elif jumlah_topup > 100000:
                st.error("❌ Maksimal deposit Rp 100.000!")
            else:
                st.info(f"🆗 Nominal {format_rupiah(jumlah_topup)} Valid! Silakan Konfirmasi.")

        if submit:
            if jumlah_topup < 1000:
                st.error("Gagal! Minimal Rp 1.000")
            elif jumlah_topup > 100000:
                st.error("Gagal! Maksimal Rp 100.000")
            else:
                st.session_state['saldo_user'] += jumlah_topup
                st.session_state['deposit_mode'] = False 
                st.success(f"Berhasil deposit {format_rupiah(jumlah_topup)}!")
                time.sleep(1)
                st.rerun() 
            
    if st.button("Batal"):
        st.session_state['deposit_mode'] = False
        st.rerun()

# --- FUNGSI: ANIMASI SLOT BERGULIR ---
def animasikan_slot(box1, box2, box3, h1, h2, h3):
    # Tahap 1: Semua berputar (Gunakan acak_simbol agar visualnya merepresentasikan peluang juga)
    for _ in range(3): 
        box1.markdown(f"<h1 style='text-align: center; font-size: 50px;'>{acak_simbol()}</h1>", unsafe_allow_html=True)
        box2.markdown(f"<h1 style='text-align: center; font-size: 50px;'>{acak_simbol()}</h1>", unsafe_allow_html=True)
        box3.markdown(f"<h1 style='text-align: center; font-size: 50px;'>{acak_simbol()}</h1>", unsafe_allow_html=True)
        time.sleep(0.1)

    # Tahap 2: Kiri Stop
    box1.markdown(f"<h1 style='text-align: center; font-size: 50px;'>{h1}</h1>", unsafe_allow_html=True)
    for _ in range(2):
        box2.markdown(f"<h1 style='text-align: center; font-size: 50px;'>{acak_simbol()}</h1>", unsafe_allow_html=True)
        box3.markdown(f"<h1 style='text-align: center; font-size: 50px;'>{acak_simbol()}</h1>", unsafe_allow_html=True)
        time.sleep(0.2)

    # Tahap 3: Tengah Stop
    box2.markdown(f"<h1 style='text-align: center; font-size: 50px;'>{h2}</h1>", unsafe_allow_html=True)
    for _ in range(2):
        box3.markdown(f"<h1 style='text-align: center; font-size: 50px;'>{acak_simbol()}</h1>", unsafe_allow_html=True)
        time.sleep(0.2)

    # Tahap 4: Kanan Stop
    box3.markdown(f"<h1 style='text-align: center; font-size: 50px;'>{h3}</h1>", unsafe_allow_html=True)
    time.sleep(0.1)

# --- FUNGSI: HALAMAN GAME SLOT ---
def game_page():
    st.title("SAWIT MANIS")
    
    if st.button("⬅️ Kembali ke Menu"):
        st.session_state['current_page'] = "dashboard"
        st.rerun()
    
    st.divider()

    col_kiri, col_tengah, col_kanan = st.columns([1, 2, 1])
    
    with col_tengah:
        with st.container(border=True):
            st.markdown("<h3 style='text-align: center; color: gold;'>SAWIT MANIS</h3>", unsafe_allow_html=True)
            
            # INFO TIER HADIAH
            st.info(f"Biaya Spin: {format_rupiah(1000)}")
            st.caption("Chance: 🌴 Jackpot (1%) | 🍒 Small (10%)")
            
            info_status = st.empty() 
            
            slot1, slot2, slot3 = st.columns(3)
            
            if 'slot_result' not in st.session_state:
                st.session_state['slot_result'] = ["❓", "❓", "❓"]
            
            with slot1:
                box1 = st.empty()
                box1.markdown(f"<h1 style='text-align: center; font-size: 50px;'>{st.session_state['slot_result'][0]}</h1>", unsafe_allow_html=True)
            with slot2:
                box2 = st.empty()
                box2.markdown(f"<h1 style='text-align: center; font-size: 50px;'>{st.session_state['slot_result'][1]}</h1>", unsafe_allow_html=True)
            with slot3:
                box3 = st.empty()
                box3.markdown(f"<h1 style='text-align: center; font-size: 50px;'>{st.session_state['slot_result'][2]}</h1>", unsafe_allow_html=True)
            
            st.write("") 
            
            biaya_spin = 1000
            # FIX: Inisialisasi auto_spin
            auto_spin = False 
            
            if st.session_state['saldo_user'] < biaya_spin:
                st.error(f"Saldo Kurang! Min {format_rupiah(biaya_spin)}")
                if st.button("Isi Saldo Sekarang"):
                    st.session_state['current_page'] = "dashboard"
                    st.session_state['deposit_mode'] = True
                    st.rerun()
            else:
                auto_spin = st.checkbox("🔄 Auto Spin (10x Putaran)")
                
                if auto_spin:
                    if st.button("MULAI AUTO SPIN 🚀", type="primary"):
                        for i in range(10, 0, -1):
                            info_status.warning(f"⏳ **Spin ke-{i}** sedang berjalan...")
                            
                            if st.session_state['saldo_user'] < biaya_spin:
                                st.toast("Saldo habis saat Auto Spin!")
                                break
                            
                            st.session_state['saldo_user'] -= biaya_spin
                            
                            # GENERATE HASIL DENGAN BOBOT
                            h1 = acak_simbol()
                            h2 = acak_simbol()
                            h3 = acak_simbol()
                            st.session_state['slot_result'] = [h1, h2, h3]
                            
                            animasikan_slot(box1, box2, box3, h1, h2, h3)
                            
                            # LOGIKA MENANG
                            if h1 == h2 == h3:
                                hadiah = hitung_kemenangan(h1)
                                st.session_state['saldo_user'] += hadiah
                                
                                if h1 == "🌴":
                                    st.balloons()
                                    st.toast(f"GRAND JACKPOT! +{format_rupiah(hadiah)}")
                                else:
                                    st.toast(f"WIN! +{format_rupiah(hadiah)}")
                            
                        st.rerun()

                else:
                    if st.button("SPIN", type="primary"):
                        st.session_state['saldo_user'] -= biaya_spin
                        
                        # GENERATE HASIL DENGAN BOBOT
                        h1 = acak_simbol()
                        h2 = acak_simbol()
                        h3 = acak_simbol()
                        st.session_state['slot_result'] = [h1, h2, h3]
                        
                        animasikan_slot(box1, box2, box3, h1, h2, h3)
                        
                        # LOGIKA MENANG
                        if h1 == h2 == h3:
                            hadiah = hitung_kemenangan(h1)
                            st.session_state['saldo_user'] += hadiah
                            st.session_state['pesan_menang'] = True
                            st.session_state['jumlah_menang'] = hadiah
                        else:
                            st.session_state['pesan_menang'] = False
                        st.rerun()

        if 'pesan_menang' in st.session_state and not auto_spin:
            r = st.session_state['slot_result']
            jml = st.session_state.get('jumlah_menang', 0)
            
            if st.session_state['pesan_menang']:
                if r[0] == "🌴":
                    st.balloons()
                    st.success(f"🔥 GRAND JACKPOT SAWIT! {r[0]}{r[0]}{r[0]} | Saldo +{format_rupiah(jml)}")
                else:
                    st.success(f"SELAMAT! {r[0]}{r[0]}{r[0]} | Saldo +{format_rupiah(jml)}")
                    
                del st.session_state['pesan_menang']
            elif r[0] != "❓":
                st.warning("Coba lagi gan.")

# --- FUNGSI: HALAMAN LOGIN ---
def login_page():
    st.markdown('<h1 class="judul-login">DAFTAR SEKARANG!</h1>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        with st.container(border=True):
            username = st.text_input("Username", placeholder="Masukkan nama anda")
            password = st.text_input("Password", type="password", placeholder="Masukkan password anda")
            
            if st.button("Masuk"):
                if not username or not password:
                    st.error("Isi semua data!")
                elif len(password) < 8:
                    st.error("Password minimal 8 karakter.")
                elif not any(char.isdigit() for char in password):
                    st.error("Password harus ada angka.")
                else:
                    st.success("Login Berhasil!")
                    st.session_state['status_login'] = True
                    st.session_state['nama_user'] = username
                    st.session_state['saldo_user'] = 0 
                    st.session_state['current_page'] = "dashboard"
                    st.rerun()

# --- FUNGSI: SIDEBAR USER ---
def sidebar_menu():
    nama_aktif = st.session_state['nama_user']
    saldo_aktif = st.session_state['saldo_user']
    
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
        st.title(nama_aktif.upper())
        st.write("**Status:** Member Baru")
        st.divider()
        st.metric(label="Saldo Dompet", value=format_rupiah(saldo_aktif))
        st.divider()
        if st.button("Deposit Sekarang"):
            st.session_state['deposit_mode'] = True
            st.rerun()  
        st.button("Riwayat Penarikan")
        if st.button("Log Out", type="primary"):
            st.session_state['status_login'] = False
            st.session_state['nama_user'] = ""
            st.session_state['saldo_user'] = 0
            st.rerun()

# --- FUNGSI: HALAMAN UTAMA (DASHBOARD) ---
def main_page():
    sidebar_menu()
    
    if st.session_state['deposit_mode']:
        deposit_interface()
        st.divider()
    
    nama_aktif = st.session_state['nama_user']
    st.title("🌴 SAWIT TOTO")
    st.caption(f"Halo {nama_aktif}, Saldo Anda: {format_rupiah(st.session_state['saldo_user'])}")

    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]

    for i, item in enumerate(data_sawit):
        with cols[i % 3]:
            with st.container(border=True):
                st.image(item["img"], use_container_width=True)
                st.subheader(item["nama"])
                st.info(f"Ways: {item['ways']}")
                
                if item['nama'] == "Sawit Manis":
                    if st.button(f"MAIN {item['nama']}", key=f"btn_{i}"):
                        st.session_state['current_page'] = "game"
                        st.rerun()
                else:
                    if st.button(f"Pilih {item['nama']}", key=f"btn_{i}"):  
                        st.toast(f"Menu ini belum tersedia.")

    st.divider()

# --- LOGIKA KONTROL NAVIGASI ---
if st.session_state['status_login'] == False:
    login_page()
else:
    if st.session_state['current_page'] == "dashboard":
        main_page()
    elif st.session_state['current_page'] == "game":
        sidebar_menu() 
        game_page()