import streamlit as st
st.title("BMI Calculation")
st.markdown("---")
bg="""
<style>
.stApp {
    background-image: url("https://rare-gallery.com/livewalls/imgpreview/140388-lone-samurai-sekiro-raven-live-wallpaper.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment:fixed;
}
</style>
"""
st.html(bg)  
kg=st.number_input("Weight(Kg.)",value=60.5,min_value=10.0,max_value=200.0,step=0.5)
cm=st.number_input("Height(Cm.)",value=100,min_value=1,max_value=200,step=1)

xes = st.radio("เพศ",("ชาย","หญิง"))

st.write(xes)
        
if st.button("calculation"): 
        b=kg/(cm/100)**2
        st.subheader(f"ค่าดัชนีของคุณคือ {b:.1f}")
        if  xes=="หญิง":
            if b<18.5:
                st.info("น้อยไป")
                st.warning("เสี่ยงขาดสารอาหาร")
                st.image("1.6.png")
            elif b<23:
                st.info("ปกติ")
                st.success("มีโอกาสเกิดโรคแทรกซ้อนน้อยที่สุด")
                st.image("1.7.png")
            elif b<25:
                st.info("เริ่มอ้วน")
                st.warning("ภาวะน้ำหนักเกินมีโรคแทรกซ้อน")
                st.image("1.8.png")
            elif b<30:
                st.info("อ้วน")
                st.warning("มีโอกาสเกิดโรคสูง")
                st.image("1.9.png")
            else:
                st.info("อ้วนมาก")
                st.error("เสี่ยงต่อโรคร้าย")
                st.image("1.10.png")
        if  xes=="ชาย":
            if b<19:
                st.info("น้อยไป")
                st.warning("เสี่ยงขาดสารอาหาร")
                st.image("1.1.png")
            elif b<24:
                st.info("ปกติ")
                st.success("มีโอกาสเกิดโรคแทรกซ้อนน้อยที่สุด")
                st.image("1.2.png")
            elif b<26:
                st.info("เริ่มอ้วน")
                st.warning("ภาวะน้ำหนักเกินมีโรคแทรกซ้อน")
                st.image("1.3.png")
            elif b<30:
                st.info("อ้วน")
                st.warning("มีโอกาสเกิดโรคสูง")
                st.image("1.4.png")
            else:
                st.info("อ้วนมาก")
                st.error("เสี่ยงต่อโรคร้าย")
                st.image("5.png")    
            
         
    
   




    
