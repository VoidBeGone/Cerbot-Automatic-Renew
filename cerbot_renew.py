import time
import subprocess

while True:
    subprocess.run(["certbot", "renew", "--quiet", "--post-hook", "systemctl reload nginx"])
    time.sleep(24 * 60 * 60 * 30)
