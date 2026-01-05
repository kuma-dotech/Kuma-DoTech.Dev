from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Kuma-Scan: Privacy Auditor</title>
    <style>
        body { font-family: 'Courier New', monospace; background: #0d1117; color: #58a6ff; padding: 20px; }
        .container { border: 1px solid #30363d; padding: 20px; border-radius: 10px; background: #161b22; }
        h1 { color: #f0f6fc; border-bottom: 1px solid #30363d; padding-bottom: 10px; }
        .data-label { color: #7d8590; font-weight: bold; }
        .data-value { color: #aff5b4; margin-bottom: 10px; word-break: break-all; }
        #canvas-status { color: #ffa657; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🦉 Kuma-Scan | Device Fingerprint Audit</h1>
        
        <div class="data-label">Your IP (Detected by Server):</div>
        <div class="data-value">{{ ip }}</div>

        <div class="data-label">User-Agent:</div>
        <div class="data-value">{{ user_agent }}</div>

        <div class="data-label">Accept-Language:</div>
        <div class="data-value">{{ language }}</div>

        <hr style="border: 0.5px solid #30363d;">
        
        <h3>Client-Side Analysis (JavaScript):</h3>
        <div class="data-label">Screen Resolution:</div>
        <div id="screen-res" class="data-value">Detecting...</div>

        <div class="data-label">Timezone:</div>
        <div id="timezone" class="data-value">Detecting...</div>

        <div class="data-label">Canvas Fingerprint Hash (Simulated):</div>
        <div id="canvas-hash" class="data-value">Generating...</div>
    </div>

    <script>
        // Screen Resolution
        document.getElementById('screen-res').innerText = window.screen.width + "x" + window.screen.height + " (" + window.devicePixelRatio + "x)";
        
        // Timezone
        document.getElementById('timezone').innerText = Intl.DateTimeFormat().resolvedOptions().timeZone;

        // Simple Canvas Fingerprinting Simulation
        function getCanvasFingerprint() {
            var canvas = document.createElement('canvas');
            var ctx = canvas.getContext('2d');
            ctx.textBaseline = "top";
            ctx.font = "14px 'Arial'";
            ctx.textBaseline = "alphabetic";
            ctx.fillStyle = "#f60";
            ctx.fillRect(125,1,62,20);
            ctx.fillStyle = "#069";
            ctx.fillText("Kuma-Sentinel-Audit-Test", 2, 15);
            ctx.fillStyle = "rgba(102, 204, 0, 0.7)";
            ctx.fillText("Kuma-Sentinel-Audit-Test", 4, 17);
            
            var b64 = canvas.toDataURL().replace("data:image/png;base64,","");
            var hash = 0;
            for (var i = 0; i < b64.length; i++) {
                var char = b64.charCodeAt(i);
                hash = ((hash << 5) - hash) + char;
                hash = hash & hash;
            }
            return hash;
        }
        document.getElementById('canvas-hash').innerText = getCanvasFingerprint();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    language = request.headers.get('Accept-Language')
    ip = request.remote_addr
    return render_template_string(HTML_TEMPLATE, user_agent=user_agent, language=language, ip=ip)

if __name__ == '__main__':
    print("🦉 Kuma-Scan is starting on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
