from flask import Flask  
lemon = Flask(__name__)  
 # ☕ 建立一本「咖啡護照」叫做 lemon @是門鈴， `/` 貼上門牌配對了喔 
@lemon.route('/')  
def waiter():  
    return "🍋 Hello from Lemon! 歡迎光臨咖啡館！"  
 # 🛎️ 加一個 API 路由 `/api/hi`，會有另一位接待員出來打招呼  
@lemon.route('/api/hi')  
def say_hi():  
    return "👋 Hi there! 我是 Lemon API 的接待員"  
 # 🚦 這段是讓程式「啟動」，就像店門開張  
if __name__ == '__main__': 
lemon.run(host='0.0.0.0', port=5000)  
