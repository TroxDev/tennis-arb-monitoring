import requests
import time
import subprocess

URL = "http://localhost:8080/tennis_arb.html"
FAIL_COUNT = 0
MAX_FAIL = 2

print("Auto-restart monitor started...")
print(f"Monitoring: {URL}")
print("-" * 40)

while True:
    try:
        r = requests.get(URL, timeout=5)
        if r.status_code == 200:
            if FAIL_COUNT > 0:
                print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Site is back UP")
            FAIL_COUNT = 0
        else:
            FAIL_COUNT += 1
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - HTTP {r.status_code} (fail {FAIL_COUNT}/{MAX_FAIL})")
    except Exception as e:
        FAIL_COUNT += 1
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Connection failed (fail {FAIL_COUNT}/{MAX_FAIL})")
    
    if FAIL_COUNT >= MAX_FAIL:
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - MAX FAILS REACHED. Restarting nginx-server...")
        subprocess.run(["docker", "compose", "restart", "nginx-server"], check=True)
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Restart complete. Resetting counter.")
        FAIL_COUNT = 0
    
    time.sleep(30)