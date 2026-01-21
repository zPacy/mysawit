import streamlit as st 

#Judul
st.title ("STUS NYAWIT NIH ORANG")

#gambar_web
st.image("https://originalhome.nl/wp-content/uploads/2021/08/RSPO-logo.png",caption="Tersertifikasi Sawit Premium")

#h1
st.header("SELAMAT DATANG")

#deskrippsi
st.write("ANDA NYAWIT, KAMI DAPET DUIT")

#sidebar
st.sidebar.title("PILIH SAWIT TERBAIK AGAN")
st.sidebar.selectbox("SAWIT TERSEDIA: ",["Sawit Manis","Sawit Besar","Sawit Brondolan"]) #pilihan sidebar

#Judul
#st.title("Macam-Macam Sawit yang Tersedia")

#tabulasi
#tab1, tab2 = st.tabs(["Menu 1", "Menu 2"])
#tab1.write("Isi konten Menu 1 di sini")
#tab2.write("Isi konten Menu 2 di sini")

#tombol
if st.title("Pilih Sawit"):
    
    #proggram_sidebar
    col1, col2, col3=st.columns(3)
    col1.write("Sawit Manis")
    col2.write("Sawit Besar")
    col3.write("Sawit Brondolan")
    
    sawit = st.text_input("Pilih Sawit: ", placeholder="Masukkan Jenis Sawit")
    if st.button("OK"):
        if not sawit:
            st.error("Agan Belum Memilih Sawit")
        elif not (sawit.startswith ("Sawit Manis") or sawit.startswith ("Sawit Besar") or sawit.startswith ("Sawit Brondolan")):
            st.error("Masukkan Jenis Sawit yang Valid!")
        else:
            st.success(f"Sawit yang agan pilih: {sawit}")

#pemanggil_css
with open("pohon.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#dashboard_pengguna
st.metric(label="Total Penyawit",value="1000",delta="10%")

#penyembunyi_konten
with st.expander("Info Data Sawit Terikini"):

#checkbox
        st.checkbox("Lihat Semua Sawit")
        
#tabel_data
        st.dataframe({"Sawit Manis": [11,21,13], "Sawit Besar": [14,2,34], "Sawit Brondolan": [110,320,34]})

#chart
        st.line_chart([0,9,29,11,15,30,78,94,121])

#slider
        st.slider("Cek Harga",0,100)

st.code("print('Hello World')", language='python')

#menampilkan_kode        
#st.json({"nama": "User", "role": "Developer", "status": "Active"})

#pilih_banyak
#st.multiselect("Pilih Skill", ["Python", "C++", "Java", "SQL"])

#pilihan_langsung
#st.radio("Pilih Kategori", ["Pilihan A", "Pilihan B", "Pilihan C"])

#catatan
#st.text_area("Catatan Tambahan", " ")

#file_upload
#st.file_uploader("Upload Data Diri Anda")

#file_dwonload
#st.download_button("Unduh File", "Hai", file_name="Laporan Sawit.txt")

#tanggal
#st.date_input("Tanggal Hari ini: ")

#warna
#st.color_picker("Pilih Warna: ","#12f1d0")

#bar
#st.progress()