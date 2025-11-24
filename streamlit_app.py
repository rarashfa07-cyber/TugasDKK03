import streamlit as st

st.title("Tugas DKK")
st.markdown(
    """ 
   Airah Shifa (03)
   x TJKT !
    """
)

import streamlit as st

st.title("Kalkulator BMI")

berat = st.number_input("Berat Badan (kg):", min_value=0)
tinggi = st.number_input("Tinggi Badan (cm):", min_value=0)

if st.button("Hitung"):
    if berat == 0 or tinggi == 0:
        st.error("Lengkapi data anda!")
    else:
        bmi = berat / ((tinggi / 100) ** 2)
        st.write("BMI kamu:", round(bmi, 2))

        # Kategori BMI
        if bmi < 18.5:
            st.write("Kategori: Kekurangan berat badan")
        elif bmi < 24.9:
            st.write("Kategori: Normal")
        elif bmi < 29.9:
            st.write("Kategori: Kelebihan berat badan")
        else:
            st.write("Kategori: Obesitas")
