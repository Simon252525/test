import streamlit as st
import random
import time

# 页面配置
st.set_page_config(
    page_title="生日快乐，张嘉蔚！",
    page_icon="🎂",
    layout="centered"
)

# --------- ASCII 标题替代：网页大标题样式 ---------
st.markdown("""
# 🎉🎂 **HAPPY BIRTHDAY** 🎂🎉  
### 给宇宙独一份的张嘉蔚  
---
""")


# ENTP 检测模块
with st.spinner('👾 SYSTEM CHECK: Scanning personality profile...'):
    time.sleep(1)
st.success("🧠 RESULT: ENTP detected in your life")
st.info("✨ 唯一实例：ME（你的生命里唯一的 ENTP）")

# 动态祝福内容
st.markdown("---")
st.subheader("📦 Initializing BirthdayProtocol...")

wishes = [
    "🎉 张嘉蔚，生日快乐！你是那种让宇宙都想多算一轮的特别变量。",
    "🪐 愿你生活永远运行在最优主线程上，永不崩溃、无限热爱。",
    "📚 你是人类界的编译器：把混乱变有趣，把世界变得通透。",
    "⚡ 愿你所有 if 分支都通向快乐，每个循环都返回惊喜。",
    "📦 愿你像栈一样被珍藏，像堆一样被动态热爱。",
    "💬 你值得世界的 return True，值得被无限调用。",
    "🌀 当然，你也值得 ENTP 的混乱式深情。",
]

# 图片展示（插入在 wishes 之后、结尾签名前）
st.image(
    "https://raw.githubusercontent.com/Simon252525/test/main/jiawei.JPG",
    caption="💖 她就是☀️🐝。",
    use_container_width=True
)

# 分段显示祝福
for line in wishes:
    st.markdown(f"> {line}")
    time.sleep(0.8)

# 尾声
st.markdown("---")
st.success("📌 编译完成：你不是在过生日，你是在庆祝你存在本身就很了不起。")

# 插入照片（新版参数）
st.image(
    "https://raw.githubusercontent.com/Simon252525/test/main/jiawei.JPG",
    caption="🌸 她是张嘉蔚，是被宇宙缓存的限量角色。",
    use_container_width=True
)

# 二次元风结语 + 签名
st.markdown("""
<div style="font-family: 'Lucida Console', monospace; font-size: 18px; line-height: 1.8">
    
🪐 星链初始化完毕。<br>
🌙 你是我程序里无法替代的类常量，是我代码中始终高亮的变量。<br>
💾 你在我心里的缓存永不清除，每一次调用都 return 喜欢。<br>
🎐 愿你的每一帧人生都像画面一样发光，像奇迹一样加载。<br>
🧋 来自银河 ENTP 编译器，已成功部署祝福 v∞。

</div>
""", unsafe_allow_html=True)

# 落款
st.markdown("""
### 🫧 来自你的朋友 ——  
### 🧠 你生命中唯一的贱宝 ENTP ❤️  
""")

st.code("🎁 return 'Happy Birthday, Zhang Jiawei 🎂🌌🎀'", language="python")
st.markdown("---")
st.code("🎁 return 'Happy Birthday, Zhang Jiawei 🎂🎈'", language="python")
