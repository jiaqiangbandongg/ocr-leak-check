import streamlit as st
import pandas as pd

st.title("OCR提交结果leak检查🤡")
st.write("科技金融子赛道——基于文本字符的交易验证码识别 专用")
st.write("比赛地址: https://www.dcic-china.com/competitions/10023/")

uploaded_file = st.file_uploader("提交结果文件")
if uploaded_file is not None:
    sub = pd.read_csv(uploaded_file)
    sub['num'] = sub['num'].astype('int')
    sub = sub.sort_values('num')
    sub['tag'] = sub['tag'].map(lambda x:x.lower())
    num_before = -1
    tag_before = '0'
    result = []
    for _, line in sub.iterrows():
        num  = line['num']
        tag  = line['tag']
        if tag <= tag_before:
            result.append(f"{num}.png")
        num_before = num
        tag_before = tag
    st.write("可能有问题的图片列表（**也可能是前一张或者后一张**）：")
    st.write(" ".join(result))

st.write("预祝各位都能提分🎉！DF平台越办越棒！早日消除leak")
st.write("by lmy")