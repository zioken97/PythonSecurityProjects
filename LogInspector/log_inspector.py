import re
from datetime import datetime

LOG_FILE = "sample_logs/auth.log"  # Replace with actual path if needed
ALERTS_FILE = "alerts.txt"
FAILED_LOGIN_PATTERN = r"Failed password.*from (\d{1,3}(?:\.\d{1,3}){3})"
SSH_ROOT_LOGIN_PATTERN = r"sshd.*session opened for user root"

def analyze_logs():
    alerts = []
    failed_login_counts = {}

    try:
        with open(LOG_FILE, "r") as file:
            for line in file:
                if match := re.search(FAILED_LOGIN_PATTERN, line):
                    ip = match.group(1)
                    failed_login_counts[ip] = failed_login_counts.get(ip, 0) + 1

                if re.search(SSH_ROOT_LOGIN_PATTERN, line):
                    alerts.append(f"[ROOT LOGIN] {line.strip()}")

        for ip, count in failed_login_counts.items():
            if count >= 5:
                alerts.append(f"[ALERT] {ip} failed {count} times")

        with open(ALERTS_FILE, "w") as output:
            for alert in alerts:
                output.write(f"{datetime.now()} - {alert}\n")

        print(f"Analysis complete. Alerts saved to {ALERTS_FILE}")

    except FileNotFoundError:
        print("❌ Log file not found. Check the path.")

if __name__ == "__main__":
    analyze_logs()
