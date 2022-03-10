# OCR提交结果leak检查
demo 地址: https://share.streamlit.io/jiaqiangbandongg/ocr-leak-check/main/app.py

科技金融子赛道——基于文本字符的交易验证码识别 专用

比赛地址: https://www.dcic-china.com/competitions/10023/

# 使用方法
提交结果文件，就能看到分析结果了

# 原理
测试集没打散，前后结果有顺序，如果存在逆序，说明那附近预测有问题

# 关于demo安全性
结果文件在第三方平台分析，不会做任何中间存储，代码没几行，可以自己本地check&run
