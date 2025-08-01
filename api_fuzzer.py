import requests
import sys
def loop():
    for word in sys.stdin:
        word = word.strip()
        if not word:
            continue
        try:
            res = requests.get(f"http://10.10.11.161/{word}")
            if res.status_code != 404:
                try:
                    data = res.json()
                except ValueError:
                    data = res.text
                print(f"[{res.status_code}] Found: /{word}")
                print(data)
        except requests.RequestException as e:
            print(f"Error requesting /{word}: {e}")

loop()
