import streamlit as st
st.set_page_config(page_title="Home", layout="wide")
def new_func3():
    titles = [
    ("Home", 60),
    ("ما هي المجامع المسكونيه ؟", 55),
]


    for text, size in titles:
            st.markdown(
        f"<h1 style='text-align: center; font-size: {size}px; color: #191970;'>{text}</h1>",
        unsafe_allow_html=True)
new_func3()

import streamlit.components.v1 as components

st.set_page_config(layout="wide")

html = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8"/>
<style>
body { margin:0; padding:0; }
.container{
  direction: rtl;
  text-align: right;
  margin:0; padding:0;
  font-size: 28px; line-height: 1.9; color: black;
}
.container .title{ font-size: 40px; font-weight:800; margin:0 0 8px 0; }
</style>
</head>
<body>
<div class="container">
  <div>المجامع المسكونية الثلاثة التي تقبلها الكنائس الأرثوذكسية الشرقية هي:
  مجمع نيقية الأول (325م)، ومجمع القسطنطينية الأول (381م)، ومجمع أفسس (431م).
  هذه المجامع الأولى حددت العقائد المسيحية الأساسية مثل قانون الإيمان النيقاوي
  وأدانت تعاليم هرطقات مثل الأريوسية.</div>

  <div class="title">مجمع نيقية الأول (325م)</div>
  <div>عُقد في مدينة نيقية، وأكد فيه على عقيدة ألوهية المسيح ضد هرطقة آريوس.</div>

  <div class="title">مجمع القسطنطينية الأول (381م)</div>
  <div>وافق على الصيغة الحالية لعقيدة نيقية، وعزز الأرثوذكسية ضد تعاليم آريوس وأبوليناريس، ودعم مكانة القسطنطينية.</div>

  <div class="title">مجمع أفسس (431م)</div>
  <div>أكّد على الإيمان الأصلي، وأدان تعاليم نسطور بطريرك القسطنطينية، وأعلن أن مريم هي والدة الإله (ثيوتوكس).</div>

  <div>تُعد هذه المجامع الثلاثة علامات فارقة في التاريخ المسيحي، حيث وضعت أسساً للعقيدة المسيحية وتحديداً في طبيعة المسيح و«تجسده».</div>
</div>
</body>
</html>
"""
components.html(html, height=800, scrolling=True)


import streamlit as st
import base64
from pathlib import Path

# -----------------------------
# دالة لتحويل الصورة لBase64
# -----------------------------
def get_base64_of_bin_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# -----------------------------
# دالة لتعيين الخلفية
# -----------------------------
def set_background(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# مسار الصورة
# -----------------------------
image_path = "image/pngtree-high-quality-blue-sky-background-wallpapers-high-resolution-blue-sky-backgrounds-image_13267110.jpg"  # ضع هنا اسم الصورة أو المسار الصحيح
set_background(image_path)
def new_func():
    cols = st.columns(3, gap="large")

    with cols[0]:
        st.text("")
            

    with cols[1]:
        st.image("image/d.png", width=500)
        if st.button("about", key="btn_page9"):
            st.switch_page("pages/about.py")

    with cols[2]:
        st.text("")


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




    cols = st.columns(3, gap="large")

    with cols[0]:
                st.image("image/a.jpg", width=500)
                if st.button("(325 م):مجمع نيقية الأول ", key="btn_page1"):
                    st.switch_page("pages/1_page1.py")

    with cols[1]:
                st.image("image/b.jpg", width=500)
                if st.button("مجمع القسطنطينية 381 م ", key="btn_page2"):
                    st.switch_page("pages/2_page2.py")

    with cols[2]:
                st.image("image/c.jpg", width=500)
                if st.button("مجمع أفسس (431 م) ", key="btn_page3"):
                    st.switch_page("pages/3_page3.py")
new_func()  

  


