import gradio as gr
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import tempfile
import requests
from prophet import Prophet
from datetime import datetime, timedelta
import logging

# 設置日誌
logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')

# 字體設置
def setup_font():
    try:
        url_font = "https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_"
        response_font = requests.get(url_font)
        
        with tempfile.NamedTemporaryFile(delete=False, suffix='.ttf') as tmp_file:
            tmp_file.write(response_font.content)
            tmp_file_path = tmp_file.name
        
        fm.fontManager.addfont(tmp_file_path)
        mpl.rc('font', family='Taipei Sans TC Beta')
    except Exception as e:
        logging.error(f"字體設置失敗: {str(e)}")
        # 使用備用字體
        mpl.rc('font', family='SimHei')

def predict_stock_price(stock_code, period, prediction_days):
    try:
        # 下載股票數據
        df = yf.download(stock_code, period=period)
        if df.empty:
            return "無法獲取股票數據", None
        
        # 準備數據
        data = df.reset_index()
        data = data[['Date', 'Close']]
        data.columns = ['ds', 'y']
        
        # 訓練 Prophet 模型
        model = Prophet(daily_seasonality=True)
        model.fit(data)
        
        # 創建未來日期
        future = model.make_future_dataframe(periods=prediction_days)
        forecast = model.predict(future)
        
        # 繪製圖表
        plt.figure(figsize=(12, 6))
        
        # 繪製實際數據
        plt.plot(data['ds'], data['y'], 
                label='實際收盤價', 
                color='blue')
        
        # 繪製預測數據
        plt.plot(forecast['ds'], forecast['yhat'],
                label='預測收盤價',
                color='orange',
                linestyle='--')
        
        # 添加預測區間
        plt.fill_between(forecast['ds'],
                        forecast['yhat_lower'],
                        forecast['yhat_upper'],
                        color='orange',
                        alpha=0.2)
        
        # 設置圖表格式
        plt.title(f'{stock_code} 股價預測', pad=20)
        plt.xlabel('日期')
        plt.ylabel('股價')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        
        # 返回預測結果和圖表
        return forecast.tail(prediction_days).to_string(), plt.gcf()
        
    except Exception as e:
        logging.error(f"預測過程發生錯誤: {str(e)}")
        return f"預測過程發生錯誤: {str(e)}", None

# 初始化字體
setup_font()

# Gradio 介面
with gr.Blocks() as demo:
    gr.Markdown("# 股票價格 Stock Price 預測系統 Prophet")
    
    with gr.Column():
        # 輸入區域
        with gr.Row():
            stock_input = gr.Textbox(
                label="股票代碼",
                placeholder="例如: 2330.TW",
                value="2330.TW"
            )
            
            period_dropdown = gr.Dropdown(
                choices=["1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "max"],
                label="歷史數據期間",
                value="1y"
            )
            
            prediction_days = gr.Slider(
                minimum=5,
                maximum=30,
                value=5,
                step=1,
                label="預測天數"
            )
        
        predict_button = gr.Button("開始預測", variant="primary")
        
        # 輸出區域（垂直排列）
        output_plot = gr.Plot(label="股價預測圖")
        output_text = gr.Textbox(label="預測結果", lines=10)
    
    predict_button.click(
        predict_stock_price,
        inputs=[stock_input, period_dropdown, prediction_days],
        outputs=[output_text, output_plot]
    )

# 啟動應用
if __name__ == "__main__":
    demo.launch()