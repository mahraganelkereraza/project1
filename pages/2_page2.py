import streamlit as st

st.set_page_config(page_title="page2", layout="wide")



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





#tital
def new_func6():
        st.markdown("""
<div style="text-align: center; margin-top: 30px;">
    <h1 style="font-size: 60px; color: #191970; font-weight: bold;">
       مجمع القسطنطينية 381 م
    </h1>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div style="text-align: right; margin-top: 20px; line-height: 5;">
    <h1 style="font-size: 35px; color: #191970; font-weight: bold;">
    Council of Constantinople
    </h1>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div style="text-align: right; margin-top: 23px; line-height: 2;">
    <h2 style="font-size: 28px; color: black; font-weight: bold;">
        بعد أن جاهد البابا أثناسيوس ضد البدعة الآريوسية سنينًا عديدة، وبعده استراحت الكنيسة من هذه البدعة الوخيمة والخطيرة جدًا على الكنيسة، 
        ظهرت عدة بِدَع في نهاية القرن الرابع الميلادي. وكان ذلك في زمان الإمبراطور المسيحي الأرثوذكسي ثيئودوسيوس الكبير، 
        الذي أصدر مرسومًا إمبراطوري سنة 381 م. يأمر فيه بهدم المعابد الوثنية وتحويلها إلى كنائس.
    </h2>
</div>
""", unsafe_allow_html=True)
new_func6()
#col
def new_func5():
        col1, col2 = st.columns(2)

        with col1:
            st.image("image/www-St-Takla-org--Council-of-Constantinople.jpg" , use_container_width=True)

        with col2:
            st.markdown("""
    <div style="text-align: right; line-height: 2;">
        <h1 style="font-size: 35px; color: black; font-weight: bold;">
        :أما البدع التي ظهرت في ذلك الوقت وهي <br>
        بدعة أبوليناريوس أسقف اللاذقية <br>
        بدعة أوسابيوس مجدد تعاليم سابليوس <br>
        بدعة مكدونيوس أسقف القسطنطينية المعزول <br>
        </h1>
    </div>
    """, unsafe_allow_html=True)

            st.markdown("""
    <hr style="border: 0; height: 8px; background: Black; border-radius: 6px; margin: 40px 0;">
    """, unsafe_allow_html=True)
            st.markdown("""
    <div style="text-align: right; line-height: 2;">
        <h1 style="font-size: 45px; color: #191970; font-weight: bold;">
      :  مكان انعقاد المجمع 
        </h1>
    </div>
    """, unsafe_allow_html=True)
            st.markdown("""
    <div style="text-align: right; line-height: 2;">
        <h1 style="font-size: 25px; color: black; font-weight: bold;">
      انعقد المجمع المسكوني الثاني في القسطنطينية العاصمة الجديدة للإمبراطورية الرومانية التي أقامها قسطنطين مكان بيزنطة وأسس فيها أول حكومة مسيحية في 11/5/330 م.، ثم جعلها أركاديوس عاصمة الإمبراطورية الشرقية سنة 395 م. وقد اختيرت مقرًا للمجمع المسكوني الثاني لموقعها الجغرافي في شهر مايو سنة 381 م. برئاسة القديس ميلاتيوس بطريرك إنطاكية وكان عدد الذين حضروا فيه 150 أسقفًا يتقدمهم تيموثاوس بابا الإسكندرية مع بعض أساقفته وكيرلس أسقف أورشليم ونكتاريوس وغريغوريوس النيصي أسقف نيصص وغريغوريوس الناطق بالإلهيات وبلاجيوس أسقف اللاذقية.
    وقد أمتنع عن الحضور أسقف روما ولكنه خضع لقرارات المجمع وقوانينه، فكان العدد الإجمالي للحاضرين بالمجمع 150 أسقفًا.
        </h1>
    </div>
    """, unsafe_allow_html=True)
new_func5()
#line 
st.markdown("""
    <hr style="border: 0; height: 4px; background: Black; border-radius: 6px; margin: 40px 0;">
    """, unsafe_allow_html=True)
#tital
def new_func4():
        st.markdown("""
<div style="text-align: right; margin-top: 20px; line-height: 5;">
    <h1 style="font-size: 35px; color:  #191970; font-weight: bold;">
      :  مشكلة في رئاسة المجمع 
    </h1>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div style="text-align: right; margin-top: 20px; line-height: 5;">
    <h2 style="font-size: 25px; color: black; font-weight: bold;">
      حدث في بداية المجمع عند ترشيح الرئيس أن البعض رشح القديس غريغوريوس الثيؤلوغوس وذلك بعد نياحة القديس ملاتيوس الذي رشح قبل بداية المجمع ورقد في الرب قبل جلسات المجمع. (انظر المزيد عن هذا الموضوع هنا في موقع الأنبا تكلا في أقسام المقالات والكتب الأخرى). فعارض البابا السكندري وأساقفة مصر على الترشيح فعندما رأى القديس غريغوريوس ذلك قال قولًا شهيرًا.... ألقوني في البحر كيونان حتى يهدأ الغَلَيَان... وتنازل عن الرئاسة للأسقف نكتاريوس الذي حاز رضى الجميع.
    </h2>
</div>
""", unsafe_allow_html=True)
new_func4()
#line
st.markdown("""
    <hr style="border: 0; height: 4px; background: Black; border-radius: 6px; margin: 40px 0;">
    """, unsafe_allow_html=True)
#tital
def new_func3():
        st.markdown("""
<div style="text-align: right; margin-top: 20px; line-height: 5;">
    <h1 style="font-size: 35px; color:#191970; font-weight: bold;">
     :  بدعة مكدونيوس
    </h1>
</div>
""", unsafe_allow_html=True)
        st.markdown("""
<div style="text-align: right; margin-top: 20px; line-height: 5;">
    <h1 style="font-size: 35px; color: black; font-weight: bold;">
     قال مكدونيوس أمام المجمع عندما دُعِيَ لِعَرْض بدعته: "أن الروح القدس عمل إلهي منتشر في الكون، وليس بأقنوم متميز عن الآب والابن، بل هو مخلوق يشبه الملائكة وليس ذو رتبة أسمى منهم".
وقد فند هذه البدعة من قبل القديس أثناسيوس بعد رجوعه من منفاه سنة 362 م. وأظهر فسادها وحكم بحرمه وحرم بدعته وحاول الأساقفة بعد ذلك إقناع مكدونيوس بخطأه وخطأ عقيدته الفاسدةـ لكنه رفض وأصرَّ على التمسك بمعتقده.
فحكم عليه المجمع بالحرم وفرزه من شركة الكنيسة وحكم عليه الإمبراطور بالنفي وقرر الآباء أن الروح القدس هو الأقنوم الثالث من الثالوث القدوس وإنه مساو للآب وللابن، ثم قرروا تكميل قانون الإيمان النيقاوي: "نعم نؤمن بالروح القدس الرب المُحيي المُنْبَثِق من الآب".
    </h1>
</div>
""", unsafe_allow_html=True)
new_func3()
#line
st.markdown("""
    <hr style="border: 0; height: 4px; background: Black; border-radius: 6px; margin: 40px 0;">
    """, unsafe_allow_html=True)
#tital
def new_func2():
        st.markdown("""
<div style="text-align: right; margin-top: 35px; line-height: 5;">
    <h1 style="font-size: 35px; color: #191970; font-weight: bold;">
    : بدعة أبوليناريوس أسقف اللاذقية
    </h1>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div style="text-align: right; margin-top: 35px; line-height: 5;">
    <h1 style="font-size: 35px; color: black; font-weight: bold;">
            وقد أشتهر بمهاجمته للآريوسية وشدة دفاعه عن لاهوت السيد المسيح له والمجد وفيما هو يدافع سقط في بدعة شنيعة إذ قال بأن "لاهوت السيد المسيح قد قام مقام الروح الجسدية وتحمل الآلام والصلب والموت مع الجسد، كما إنه اعتقد أيضًا بوجود تفاوت بين الأقانيم فقال: الروح القدس عظيم والابن أعظم، أما الآب فهو الأعظم.
وقد فند أيضًا القديس أثناسيوس هذه البدعة في مجمع مكاني بالإسكندرية سنة 362 م. وأظهر فساد هذه البدعة غير أن أبوليناريوس لم يرجع عن رأيه.
وبعد أن ناقشهُ القديس في المجمع ولم يرجع عن رأيه وظل على عِناده، حكم عليه بالحَرْم، وجرَّدوه من رتبتهُ.
    </h1>
</div>
""", unsafe_allow_html=True)
new_func2()
#line
st.markdown("""
    <hr style="border: 0; height: 4px; background: Black; border-radius: 6px; margin: 40px 0;">
    """, unsafe_allow_html=True)
#tital
def new_func1():
        st.markdown("""
<div style="text-align: right; margin-top: 35px; line-height: 5;">
    <h1 style="font-size: 35px; color:#191970; font-weight: bold;">
   : بدعة أوسابيوس
    </h1>
</div>
""", unsafe_allow_html=True)
        st.markdown("""
<div style="text-align: right; margin-top: 25px; line-height: 5;">
    <h1 style="font-size: 35px; color: black; font-weight: bold;">
   أعتقد أوسابيوس أن الثالوث ذاتًا واحدة وأقنوم واحد.... وقد حاول البابا تيموثاوس لإقناعه فلم يرجع عن رأيه، فأمر المجمع بتجريدهُ من رتبتهُ، وإظهار فساد بدعته. وقد أصدر المجمع سبعة قوانين أخرى جديدة لسياسة الكنيسة.
    </h1>
</div>
""", unsafe_allow_html=True)
new_func1()
#line
st.markdown("""
    <hr style="border: 0; height: 4px; background: Black; border-radius: 6px; margin: 40px 0;">
    """, unsafe_allow_html=True)
#Buttons
def new_func():
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


        st.markdown ('<div class="big-btn">', unsafe_allow_html=True)

        cols = st.columns(3, gap="large")

        with cols[0]:
            st.subheader("Home")
            if st.button("Back", key="btn_page1"):
                st.switch_page("Home.py")

        with cols[1]:
            st.subheader("page1")
            if st.button("Back", key="btn_page2"):
                st.switch_page("pages/1_page1.py")

        with cols[2]:
            st.subheader("page3")
            if st.button("Go", key="btn_page3"):
                st.switch_page("pages/3_page3.py")
new_func()


