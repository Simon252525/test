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

# 图片展示（插入在 wishes 之后、结尾签名前）
st.image(
    "https://raw.githubusercontent.com/Simon252525/test/main/jiawei.JPG",
    caption="💖 她就是☀️🐝。",
    use_column_width=True
)

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

# 分段显示祝福
for line in wishes:
    st.markdown(f"> {line}")
    time.sleep(0.8)

# 尾声
st.markdown("---")
st.success("📌 编译完成：你不是在过生日，你是在庆祝你存在本身就很了不起。")

# 结尾签名
st.markdown("""
### 💌 来自你的朋友 ——  
### 🧠 你生命中唯一的贱宝 ENTP ❤️  
""")

st.markdown("---")
st.code("🎁 return 'Happy Birthday, Zhang Jiawei 🎂🎈'", language="python")
