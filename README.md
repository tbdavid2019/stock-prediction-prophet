---
title: Stock Predict Prophet
emoji: 🏢
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 5.7.1
app_file: app.py
pinned: false
short_description: 使用 Prophet 來預測股價, 如台積電輸入 2330.tw
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference


# Stock Price Prediction System

A web-based stock price prediction system built with Python, utilizing the Prophet model for time series forecasting.

## Features

- Real-time Taiwan stock data retrieval
- Time series prediction using Facebook Prophet
- Interactive web interface with Gradio
- Supports custom prediction timeframes
- Visualization of predictions with confidence intervals
- Chinese font support for Taiwan stock market

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tbdavid2019/stock-prediction-prophet.git
cd stock-prediction-prophet
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Note: For Prophet installation on Windows, you might need Microsoft Visual C++ Build Tools.

## Usage

1. Run the application:
```bash
python app.py
```

2. Open your browser and navigate to the provided local URL
3. Enter a Taiwan stock code (e.g., 2330.TW)
4. Select historical data period
5. Set prediction days
6. Click "Start Prediction"

## Dependencies

- gradio >= 4.0.0
- yfinance >= 0.2.3
- pandas >= 1.3.0
- numpy >= 1.21.0
- matplotlib >= 3.4.3
- prophet >= 1.1.4

---

# 台股預測系統

使用 Python 建立的網頁版股票預測系統，採用 Prophet 模型進行時間序列預測。

## 功能特點

- 即時獲取台股資料
- 使用 Facebook Prophet 進行時間序列預測
- 基於 Gradio 的互動式網頁界面
- 支援自訂預測時間範圍
- 預測結果視覺化與信賴區間
- 支援中文字型顯示

## 安裝方式

1. 克隆專案：
```bash
git clone https://github.com/tbdavid2019/stock-prediction-prophet.git
cd stock-prediction-prophet
```

2. 安裝依賴套件：
```bash
pip install -r requirements.txt
```

注意：在 Windows 環境下安裝 Prophet 可能需要 Microsoft Visual C++ Build Tools。

## 使用方法

1. 執行應用程式：
```bash
python app.py
```

2. 開啟瀏覽器，前往提供的本地網址
3. 輸入台股代碼（例如：2330.TW / TSLA ）
4. 選擇歷史資料期間
5. 設定預測天數
6. 點擊「開始預測」

## 系統需求

- Python 3.7 或更高版本
- 相關套件版本要求請參考 requirements.txt

## 注意事項

- 股票預測結果僅供參考，不作為投資建議
- 建議使用穩定的網路連線以確保資料獲取
- 預測結果的準確性會受到多種因素影響

## 贊助與支持

如果您覺得這個專案對您有幫助，歡迎給予 Star ⭐️

## 聯絡方式

若有任何問題或建議，歡迎提出 Issue 或直接聯繫專案維護者。
