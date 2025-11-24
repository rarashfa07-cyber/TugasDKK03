import streamlit as st
import time

# === STYLE TOMBOL ===
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #7AA874;
    color: white !important;
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 16px;
    border: none;
}
div.stButton > button:first-child:hover {
    background-color: #6B9468;
}
</style>
""", unsafe_allow_html=True)

# === HEADER ===
st.title("Tugas DKK")
st.markdown("Airah Shifa (03)  \nX TJKT !")

st.title("Kalkulator BMI")

# === INPUT ===
berat = st.number_input("Berat Badan (kg):", min_value=0)
tinggi = st.number_input("Tinggi Badan (cm):", min_value=0)

# === BUTTON ===
if st.button("Hitung"):
    if berat == 0 or tinggi == 0:
        st.error("Lengkapi data anda!")
    else:
        with st.spinner("Tunggu hasilmu…"):
            time.sleep(1.3)

        bmi = berat / ((tinggi / 100) ** 2)

        # === BMI RATA TENGAH ===
        st.markdown(
            f"<h3 style='color:#7C9273; text-align:center;'>BMI kamu: {round(bmi, 2)}</h3>",
            unsafe_allow_html=True
        )

        # KATEGORI + WARNA
        if bmi < 18.5:
            warna = "#EED676"
            kategori = "Kekurangan berat badan"

        elif bmi < 24.9:
            warna = "#8CCD92"
            kategori = "Normal"
            st.balloons()

        elif bmi < 29.9:
            warna = "#F2A86D"
            kategori = "Kelebihan berat badan"

        else:
            warna = "#E86F6F"
            kategori = "Obesitas"

        # === BOX HASIL RATA TENGAH ===
        st.markdown(
            f"""
            <div style="
                background-color:{warna}20;
                padding:12px;
                border-radius:10px;
                margin-top:10px;
                border:1px solid {warna};
                text-align:center;
            ">
                <h4 style="color:{warna}; font-weight:600; margin:0;">
                    {kategori}
                </h4>
            </div>
            """,
            unsafe_allow_html=True
    )
