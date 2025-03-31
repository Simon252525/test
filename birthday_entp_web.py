import streamlit as st
import random
import time

# 페页面配置
st.set_page_config(
    page_title="生日快乐，张嘉蔚！",
    page_icon="🎂",
    layout="centered"
)

# 页面标题
st.markdown("""
# 🎉🎂 **HAPPY BIRTHDAY** 🎂🎉  
### 给宇宙独一份的张嘉蔚 (a.k.a Vicky) 🌌🌟
---
""")

# ENTP 检测模块
with st.spinner('🧟‍♂️ SYSTEM CHECK: Scanning for ENTP energy...'):
    time.sleep(1.2)
st.success("🧠 ENTP detected in your life system")
st.info("✨ 唯一实例: ME (你生命里唯一的 ENTP)")

# 出场分段效果
st.markdown("---")
st.subheader("📦 Initializing BirthdayProtocol()...")

wishes = [
    "🌟 Vicky，生日快乐！你是少数可以让互联网维持转速的女孩。",
    "🌌 愿你每天依旧是新版本，稳定、充满更新。",
    "📚 你是统统规则中的特例，也是社交系统里的惊喜带。",
    "✨ 愿你的生活每一小节，都是被 if 分支选中的喜悦。",
    "📂 愿你像栈一样被亲成，像堆一样被加载。",
    "🛠️ 你对世界的应用，是 return True，是一类永远可以调用的常量。",
    "🪨 当然，你也值得 ENTP 混乱而热点的深情。"
]

# 分段输出
for line in wishes:
    st.markdown(f"> {line}")
    time.sleep(0.8)

# 插入照片
st.image(
    "https://raw.githubusercontent.com/Simon252525/test/main/jiawei.JPG",
    caption="🌸 这位太原女孩兼川渝后裔，是被宇宙缓存的限量角色，正不断自我进化、版本升级，每次出现都是更新后的闪光体。",
    use_container_width=True
)

# 二次元风结语
st.markdown("""
<div style="font-family: 'Lucida Console', monospace; font-size: 18px; line-height: 1.8">

🚀 星线已连接。<br>
🌙 你是太原雪里的松，是川湘火锅里的灰糖，是宇宙端点的光点，名叫 Vicky。<br>
📁 恭喜你！你已被 ENTP 系统识别，后续将被无限调用。<br>
🛡️ 在漫长的时间线中，你是一段无法拿离散表表示的重要定量。<br>
🫰 此软件已成功编译，版本号 v∞，已送达张嘉蔚或更高级存储单元。

</div>
""", unsafe_allow_html=True)

# 落款
st.markdown("""
### 🩵 来自你的朋友 ～～  
### 🧠 你生命中唯一的贱宝 ENTP ❤️  
""")

st.markdown("""
<div style='text-align: center; font-size: 24px;'>
🎁 <code>return "Happy Birthday, Zhang Jiawei 🎂💫✨"</code>
</div>
""", unsafe_allow_html=True)
