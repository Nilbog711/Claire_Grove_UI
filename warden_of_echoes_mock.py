
import os
from datetime import datetime

# Paths
LOG_FILE = "Logs/echoes_log.txt"
DIGEST_FILE = "Memory/Digests/scroll_digest.md"

# Ensure folders exist
os.makedirs("Logs", exist_ok=True)
os.makedirs("Memory/Digests", exist_ok=True)

def write_log(message):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] {message}\n")

def write_mock_digest():
    with open(DIGEST_FILE, "w", encoding="utf-8") as f:
        f.write("# Scroll Digest\n\n")
        f.write("No real data processed. This is a simulation run by the Warden.\n")

def run_warden():
    write_log("Warden of Echoes invoked in MOCK mode.")
    write_mock_digest()
    write_log("Digest created: No anomalies found (mock).")

# Cloud Function entrypoint
def main(request=None):
    run_warden()
    return "Warden of Echoes (mock) completed memory scan."

# Manual run
if __name__ == "__main__":
    run_warden()
