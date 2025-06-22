from datetime import datetime
import subprocess
import platform

def check_updates():
    system = platform.system()
    distro = platform.linux_distribution()[0].lower() if hasattr(platform, 'linux_distribution') else ""

    log_file = "update_log.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[+] Checking for updates at {timestamp}")
    updates = []

    try:
        if "ubuntu" in distro or "debian" in distro:
            result = subprocess.run(["apt", "list", "--upgradable"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            updates = result.stdout.splitlines()
        elif "redhat" in distro or "centos" in distro or "fedora" in distro:
            result = subprocess.run(["yum", "check-update"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            updates = result.stdout.splitlines()
        else:
            print("[-] Unsupported or unrecognized Linux distribution.")
            return
    except Exception as e:
        print(f"[!] Error checking updates: {e}")
        return

    with open(log_file, "a") as log:
        log.write(f"\n=== {timestamp} ===\n")
        if updates:
            for line in updates:
                log.write(line + "\n")
            print(f"[+] Updates found and logged in {log_file}")
        else:
            log.write("No updates available.\n")
            print("[+] System is up to date.")

check_updates()
