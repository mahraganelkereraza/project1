import streamlit as st

st.set_page_config(page_title="page3", layout="wide")


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
def new_func1():
        st.markdown("""
<div style="text-align: center; margin-top: 30px;">
    <h1 style="font-size: 60px; color: #191970; font-weight: bold;">
      : مجمع أفسس (431 م)
    </h1>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div style="text-align: right; margin-top: 30px;">
    <h1 style="font-size: 60px; color: #191970; font-weight: bold;">
     : أسباب انعقاده
    </h1>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div style="text-align: right; margin-top: 1px;">
    <h1 style="font-size: 60px; color: #191970; font-weight: bold;">
   :  بدعة بيلاجيوس
    </h1>
</div>
""", unsafe_allow_html=True)






        st.markdown("""
<div style="text-align: right; margin-top: 1px;">
    <h2 style="font-size: 30px; color: black; font-weight: bold;">
   كان راهب قس من بريطانيا وكان ينادى بأن "خطية آدم قاصرة عليه دون بقية الجنس البشري" وأن "كل إنسان منذ ولادته يكون كآدم قبل سقوطه". ثم قال أن "الإنسان بقوته الطبيعية يستطيع الوصول إلى أسمى درجات القداسة بدون انتظار إلى مساعدة النعمة"...
وبديهي أن هذه التعاليم الفاسدة تهدِم سِرّ الفداء المجيد ويُضْعِف من دم السيد المسيح.
(مز 51: 5) "بإنسان واحد دخلت الخطية إلى العالم وبالخطية الموت".
(رو 2: 12) "كما في آدم يموت الجميع هكذا في المسيح يحيا الجميع".
وبدأ ينشر بدعته بين البلاد حتى حَكَمَ عليه مجمع أفسس الأول بحرمه هو وبدعته.
    </h2>
</div>
""", unsafe_allow_html=True)
new_func1()
#col
def new_func2():
        col1, col2 = st.columns(2)

        with col1:
            st.image("image/cyril.jpg", caption="", width=450)

        with col2:
            st.markdown("""
    <div style="text-align: right; line-height: 2;">
    <h1 style="font-size: 45px; color: #191970; font-weight: bold;">
     بدعة نسطور بطريرك القسطنطينية
    </h1>
    </div>
    """, unsafe_allow_html=True)

            st.markdown("""
    <div style="text-align: right; line-height: 2;">
    <h1 style="font-size: 32px; color: black; font-weight: bold;">
      نادى بأن في المسيح له المجد أقنومين وشخصين وطبيعتين <br>
    "  واستنتج من ذلك أنه لا ينبغي أن نسمي السيدة العذراء بـ"والدة الإله  <br>
    .    كما عاب على المجوس لسجودهم للطفل يسوع <br>
  استقطع الجزء الأخير من كل من الثلاث تقديسات التي ترتلها الكنيسة في صلواتها، وبحكم منصبه بدأ ينشر بدعته وتعاليمه الفاسدة في كل مكان مستخدمًا في ذلك بعض الكهنة والأساقفة. وعندما سمع البابا كيرلس ببدعته كتب يفندها ويثبت التعليم الصحيح، وأرسل رسائل كثيرة إليه، ولكنه رغم ذلك لم يرجع عن فساد تعاليمه    .   <br>    
    </h1>
    </div>
    """, unsafe_allow_html=True)

            st.markdown("""   
    <hr style="border: 0; height: 4px; background: Black; border-radius: 6px; margin: 40px 0;">
    """, unsafe_allow_html=True)

            st.markdown("""
    <div style="text-align: right; line-height: 0;">
    <h1 style="font-size: 45px; color: #191970; font-weight: bold;">
    جلسات المجمع   
    </h1>
    </div>
    """, unsafe_allow_html=True)

            st.markdown("""
    <div style="text-align: right; line-height: 2;">
    <h1 style="font-size: 32px; color: black; font-weight: bold;">
    أرسل البابا كيرلس رسائل كثيرة إلى نسطور ولكنه لم يقبل المناقشة ووقعت هذه الرسائل عليه كوقع المطرقة على السندان بعنف فغضب بشدة وأرسل إلى البابا بخطاب يفيض بالسخط والتوبيخ وقضى رسل البابا شهرًا محاولين مقابلة نسطور أو أن يتحدثوا إليه دون جدوى، إذ رفض مقابلتهم فغادَروا إلى الإسكندرية. 
    </h1>
    </div>
    """, unsafe_allow_html=True)
            st.markdown("""   
    <hr style="border: 0; height: 4px; background: Black; border-radius: 6px; margin: 40px 0;">
    """, unsafe_allow_html=True)
new_func2()
#tital
def new_func3():
        st.markdown("""
<div style="text-align: right; margin-top: 30px;">
    <h1 style="font-size: 60px; color: #191970; font-weight: bold;">
     : مجمع مكاني
    </h1>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div style="text-align: right; margin-top: 30px;">
<h1 style="font-size: 35px; color: black; font-weight: bold;">
     عقد البابا السكندري مجمع مكاني مع الأساقفة لاتخاذ موقف واضح وصريح لحفظ الإيمان أمام المجمع وصدر منه بالإجماع أمر بالتمسك بدستور الإيمان النيقاوي ووضعوا له مقدمة مأخوذة من الكتاب المقدس "نعظمك يا أم النور الحقيقي". (انظر المزيد عن هذا الموضوع هنا في موقع الأنبا تكلا في أقسام المقالات والكتب الأخرى). وأرسل البابا رسائل إلى زوجة الإمبراطور وبليكاريا وأركاريا ومارينا أخوات الإمبراطور يشرح لهم حقائق الإيمان وبذلك لكي لا يؤثر نسطور على الإمبراطور ثيئودسيوس الصغير صديقه وأرسل رسائل أخرى إلى يوحنا أسقف إنطاكية وبونيياس أسقف أورشليم وأكاكيوس أسقف حلب وكتب البابا الحرمان وأرسلها أباء المجمع السكندري إلى نسطور يطالبونه بان يرجع إلى الإيمان المستقيم ويوقع على الحروم.
كما أرسل البابا إلى كهنة ورهبان القسطنطينية خطابين. والحروم الاثنا عشر تُبَرْهِن على عُمْق العقيدة الأرثوذكسية وإيمان الكنيسة القبطية. ورَفَضَ نسطور التوقيع على الحروم بل وكتب ضدها بنود تؤيد بدعته، وساعده على ذلك بعض أساقفة إنطاكية.
وبدأ الانقسام بين الكنيسة الواحدة "رومية أورشليم وأسيا الصغرى إلى جانب البابا الإسكندري وإنطاكية إلى جانب نسطور ومما زاد الموقف تعقيدًا استثارة نسطور للإمبراطور ضد البابا لكتابه خطابات لأخواته وزوجته دون إذنه فأرسل الملك للبابا خطابًا شديد اللهجة ودعى الأساقفة لعقد مجمع مسكوني وكان ذلك في 19 نوفمبر سنة 430 م.
</h1>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div style="text-align: right; margin-top: 30px;">
<h1 style="font-size: 35px; color: black; font-weight: bold;">
     وسافر البابا السكندري ومعه خمسون أسقفًا والأنبا شنودة رئيس المتوحدين والأنبا بقطر السوهاجي رئيس الأديرة الباخومية وديسقوروس مدير مدرسة الإسكندرية اللاهوتية وتبعهم أسقف أورشليم.
 وبالرغم من تهديده رحب بهم أسقف أفسس.
 وأرسل أسقف روما أسقفين وقسًا وأيدهم برسالة بأن يعلموا بقوانين وقرارات البابا السكندري.
 كما حضر نسطور ومعه 140 أسقفًا مع رجال مسلحين ظنًا منه أنه سيرهب المجتمعين لكي لا يتخذوا قرارا ضده.
</h1>
</div>
""", unsafe_allow_html=True)
new_func3()
#line
st.markdown("""   
    <hr style="border: 0; height: 4px; background: Black; border-radius: 6px; margin: 40px 0;">
    """, unsafe_allow_html=True)
#tital
def new_func4():
        st.markdown("""
<div style="text-align: right; margin-top: 30px;">
    <h1 style="font-size: 60px; color: #191970; font-weight: bold;">
    : مجمع أفسس الأول
    </h1>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div style="text-align: right; margin-top: 30px;">
    <h1 style="font-size: 40px; color: black; font-weight: bold;">
     بدأت جلسات المجمع في كنيسة السيدة العذراء في أفسس 7 يونيو سنة 431 م. في عيد حلول الروح القدس وحضر المجمع 200 أسقف مؤيدين بنعمة الروح القدس.
وكان من أنصار نسطور أيريناس أحد رجال البلاط الإمبراطوري وكنديديان مندوب الإمبراطور.
    </h1>
</div>
""", unsafe_allow_html=True)
new_func4()
#line
st.markdown("""   
    <hr style="border: 0; height: 4px; background: Black; border-radius: 6px; margin: 40px 0;">
    """, unsafe_allow_html=True)
#tital
def new_func5():
        st.markdown("""
<div style="text-align: right; margin-top: 30px;">
    <h1 style="font-size: 60px; color: #191970; font-weight: bold;">
     :   مشكلة تأخر الوفد الأنطاكي
    </h1>
</div>
""", unsafe_allow_html=True)



        st.markdown("""
<div style="text-align: right; margin-top: 30px;">
    <h1 style="font-size: 45px; color: black; font-weight: bold;">
     تأخر الوفد الأنطاكي فرأى الأساقفة تأجيل بدء الافتتاح لحين وصولهم، وفي أثناء ذلك كانت مباحثات جانبيه مع نسطور لرجوعه ولكن ذهبت جهودهم أدراج الرياح.
وتأخرت المباحثات 16 يومًا لطول المسافة ومرض الخيول، وقد أرسل الوفد الأنطاكي أسقفين ومعهما مشورة للمجمع ألا يؤجِّل الاجتماعات، وفُهِمَ من ذلك بأن يوحنا الأنطاكي لا يرغب في الحضور لكي لا يشارك في الحكم على صديقه نسطور. وبدأت جلسات المجمع، وذلك في كاتدرائية أفسس المُسمّاة باسم "العذراء والدة الإله":
    </h1>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div style="text-align: right; margin-top: 30px;">
    <h1 style="font-size: 45px; color: black; font-weight: bold;">
     تم اختيار البابا السكندري رئيسًا للمجمع (البابا كيرلس).
لم يحضر نسطور وأرسلوا له ثلاث مرات، ورأى أنه لا لزوم لحضوره ثم أرسل رسالة بأنه لا يحضر إلا بحضور صديقه يوحنا بطريرك إنطاكية.
عقدت الجلسة الأولى وقُرِأَت قرارات مجمع الإسكندرية وبدعة نسطور، فوافق المجمع على القرارات، وحكم المجمع على نسطور بقطعه من درجته ومن أي شركة كهنوتية.
أرسل المجمع إلى نسطور كتابًا بحرمه.
ثم قرر المجمع بأن سر التجسد المجيد القائم من اتحاد اللاهوت بالناسوت في أقنوم الكلمة الأزلي بدون انفصال ولا امتزاج ولا تغيير.
وإن السيدة العذراء مريم هي "والدة الإله".
ووضع الآباء مقدمة قانون الإيمان "نعظمك يا أم النور الحقيقي".
ثم استعرض المجمع بدعة بلاجيوس وناقشه المجمع ولم يرجع فحرمه وبدعته.
وأعلن المجمع قراراته على الشعب ففرح وهتفوا للقديس كيرلس.
ولم يقبل نسطور الحكم وأرسلوا إلى الملك وكنديديان.
    </h1>
</div>
""", unsafe_allow_html=True)
new_func5()
#line
st.markdown("""   
    <hr style="border: 0; height: 4px; background: Black; border-radius: 6px; margin: 40px 0;">
    """, unsafe_allow_html=True)
#tital
def new_func6():
        st.markdown("""
<div style="text-align: right; margin-top: 30px;">
    <h1 style="font-size: 60px; color: #191970; font-weight: bold;">
   :  مشكلة وصول بطريرك إنطاكية، وعدم اعترافه بالقرارات لعدم حضوره، وطلب من الأساقفة إعادة المجمع(1) <br> 
    </h1>
</div>
""", unsafe_allow_html=True)


        st.markdown("""
<div style="text-align: right; margin-top: 30px;">
    <h1 style="font-size: 40px; color: black; font-weight: bold;">
     تم عقد جلسة المجمع الثانية في 10 يوليو سنة 431 م. ورفض بطريرك إنطاكية الحضور معهم بالرغم من استدعاءه عدة مرات، مما اضطر المجمع لحرم بطريرك إنطاكية، وكتب المجمع رسالة للإمبراطور كتب فيها كل أعماله.
    </h1>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div style="text-align: right; margin-top: 30px;">
    <h1 style="font-size: 40px; color: black; font-weight: bold;">
    . وكتب المجمع ثمانية قرارات أخرى تخص الكنيسة وانفض المجمع بعد أن اختير مكسيميانوس أسقفًا للقسطنطينية محل نسطور المخلوع <br> 
    .ورجع الأساقفة إلى كراسيهم والبابا إلى الإسكندرية واستقبله شعبه بفرح عظيم        <br>
    . وافق الآباء على قرار الإمبراطور بنفي نسطور في مصر في جبل قسقام لِتَمَسُّك أهلها بالإيمان. ولا زال حتى الآن تل نسطور <br>
    </h1>
</div>
""", unsafe_allow_html=True)
new_func6()
#Buttons

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
                st.subheader("Home")
                if st.button("Back", key="btn_page1"):
                    st.switch_page("Home.py")

with cols[1]:
                st.subheader("page1")
                if st.button("Back", key="btn_page2"):
                    st.switch_page("pages/1_page1.py")

with cols[2]:
                st.subheader("page2 ")
                if st.button("Back", key="btn_page3"):
                    st.switch_page("pages/2_page2.py")





