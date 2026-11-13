from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

PACKAGES = {
    "Global": "com.tencent.ig",
    "KR": "com.pubg.krmobile",
    "VN": "com.vng.pubgmobile",
    "TW": "com.recom.pubgmobile",
    "Lite": "com.tencent.iglite",
    "China": "com.tencent.tmgp.pubgmhd"
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PUBG Pro Loader</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #0b0f19;
            color: #f8fafc;
            text-align: center;
            padding: 8px;
            margin: 0;
        }
        .container {
            background-color: #1e293b;
            padding: 12px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.7);
            max-width: 400px;
            margin: 0 auto;
        }
        h2 { color: #38bdf8; font-size: 17px; margin: 4px 0; }
        .status { color: #22c55e; font-size: 11px; margin-bottom: 8px; font-weight: bold; }
        .section-title { color: #fbbf24; font-size: 12px; text-align: right; margin-top: 6px; border-bottom: 1px solid #334155; padding-bottom: 2px; }
        
        select, .btn-feature {
            width: 100%;
            padding: 8px;
            margin: 4px 0;
            border-radius: 6px;
            border: none;
            font-size: 13px;
        }
        select { background-color: #0f172a; color: white; border: 1px solid #475569; }
        .btn-feature { background-color: #334155; color: #f8fafc; text-align: right; cursor: pointer; }
        
        .btn-launch {
            background-color: #16a34a;
            color: white;
            font-size: 14px;
            font-weight: bold;
            width: 100%;
            padding: 10px;
            margin-top: 8px;
            border-radius: 6px;
            border: none;
            cursor: pointer;
        }
        .btn-launch:hover { background-color: #15803d; }
    </style>
</head>
<body>
    <div class="container">
        <h2>⚡ PUBG LOADER PRO</h2>
        <div class="status">● السيرفر متصل وجاهز</div>
        
        <div class="section-title">اختر نسخة اللعبة:</div>
        <select id="game_version">
            <option value="Global">ببجي العالمية (Global)</option>
            <option value="KR">ببجي الكورية (KR)</option>
            <option value="VN">ببجي الفيتنامية (VN)</option>
            <option value="TW">ببجي التايوانية (TW)</option>
            <option value="Lite">ببجي لايت (Lite)</option>
            <option value="China">ببجي الصينية (Game For Peace)</option>
        </select>

        <div class="section-title">المميزات المفعلة:</div>
        <button class="btn-feature">🛡️ تفعيل الباس والحماية</button>
        <button class="btn-feature">🎯 ثبات السلاح وفريمات عالية</button>
        <button class="btn-feature">👤 كشف الأماكن واللوت (ESP)</button>

        <button class="btn-launch" onclick="launchGame()">🚀 تشغيل ودخول اللعبة الآن</button>
    </div>

    <script>
        function launchGame() {
            var version = document.getElementById("game_version").value;
            fetch('/launch?ver=' + version)
            .then(response => response.text())
            .then(data => alert(data));
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/launch')
def launch():
    ver = request.args.get('ver', 'Global')
    pkg = PACKAGES.get(ver, "com.tencent.ig")
    try:
        os.system(f"am start --user 0 -n {pkg}/$(cmd package resolve-activity --brief {pkg} | tail -n 1)")
        return f"🚀 تم إرسال أمر فتح لعبة ببجي ({ver}) بنجاح!"
    except Exception as e:
        return f"خطأ في التشغيل: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

