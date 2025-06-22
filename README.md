PythonSecurityProjects

A curated collection of Python scripts focused on security-related tasks. These projects demonstrate practical skills in log analysis, vulnerability detection, and automation of common security operations. Each tool is self-contained, beginner-friendly, and designed to showcase real-world applications of Python in cybersecurity.

⚠️ Disclaimer: All scripts are intended for educational and authorized use only. Never use these tools on systems you do not own or have explicit permission to test.

🔍 Log Inspector
Description: A basic log file analyzer that searches for suspicious patterns in system or application logs.

Language: Python

Dependencies: None (standard library only)

Usage: Customize suspicious_patterns in the script and run it against a .log file.

⚠️ Do not use on unauthorized logs.

🛡 Vulnerability Scanner
Description: A basic scanner that checks for outdated software versions and known CVEs using the CIRCL API.

Language: Python

Dependencies: requests

Usage: Edit the software/version list and run to check known vulnerabilities via public APIs.

⚙️ Update Checker
Description: Automates the check for software updates on a Linux system using apt or dnf, helping ensure systems stay secure and up to date.

Language: Python

Dependencies: None (uses subprocess from standard library)

Usage: Run with sufficient permissions to check for pending updates on the host system.

