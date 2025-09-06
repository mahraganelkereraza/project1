import streamlit as st

image_path = "./image/hhgghjhjh.jpg"
col1, col2, col3 = st.columns([1,2,1])
with col2:
                st.image(image_path, width=400)
def new_func(): #B:\new\last\project1\image
        st.markdown("""
<div style="text-align: center; margin-top: 50px;">
    <h1 style="font-size: 60px; color: black; font-weight: bold;">
        Cyril remon nageh
    </h1>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div style="text-align: center; margin-top: 50px;">
    <h1 style="font-size: 60px; color: black; font-weight: bold;">
       prairamy 5
    </h1>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div style="text-align: center; margin-top: 50px;">
    <h1 style="font-size: 60px; color: black; font-weight: bold;">
        Salam Language School
    </h1>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div style="text-align: center; margin-top: 50px;">
    <h1 style="font-size: 60px; color: black; font-weight: bold;">
       01554939909
    </h1>
</div>
""", unsafe_allow_html=True)
new_func()

import base64
import os
def new_func1():
        def add_bg_from_local(image_file):
            if not os.path.exists(image_file):
                st.error(f"❌ ملف الصورة غير موجود: {image_file}")
                return
    
            with open(image_file, "rb") as file:
                encoded_string = base64.b64encode(file.read()).decode()
    
            st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# ✨ هنا غير المسار واسم الصورة حسب مكانها عندك
        add_bg_from_local("./image/pngtree-high-quality-blue-sky-background-wallpapers-high-resolution-blue-sky-backgrounds-image_13267110.jpg")
new_func1()
   


st.markdown("""
<style>
.big-btn .stButton>button {
    width: 100%;
    padding: 24px 20px;
    font-size: 26px;
    font-weight: 800;
    border-radius: 18px;
    border: 0;
    background: linear-gradient(135deg, #7C3AED, #EC4899);
    color: white;
    box-shadow: 0 12px 24px rgba(0,0,0,.18);
    transition: transform .08s ease, box-shadow .2s ease, filter .2s ease;
}
.big-btn .stButton>button:hover {
    transform: translateY(-2px) scale(1.01);
    box-shadow: 0 16px 28px rgba(0,0,0,.22);
    filter: brightness(1.05);
    cursor: pointer;
}
.big-btn .stButton>button:active {
    transform: translateY(0) scale(.99);
}
</style>
""", unsafe_allow_html=True)




cols = st.columns(2, gap="large")

with cols[0]:
                st.subheader("Home")
                if st.button("Back", key="btn_page1"):
                    st.switch_page("Home.py")

with cols[1]:
                st.subheader("page1")
                if st.button("go", key="btn_page2"):
                    st.switch_page("pages/1_page1.py")







