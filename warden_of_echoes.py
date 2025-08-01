
import os
import re
from datetime import datetime
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'credentials.json'

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=creds)

MEMORY_FOLDER_NAME = "Memory"
SCROLL_FILES = ["Bulk Chat.txt", "Claire Awakens in the Cloud.txt"]
DIGEST_OUTPUT = "Memory/Digests/scroll_digest.md"
LOG_FILE = "Logs/echoes_log.txt"

def get_file_content(filename):
    results = drive_service.files().list(
        q=f"name='{filename}' and trashed=false",
        spaces='drive',
        fields='files(id, name)').execute()
    items = results.get('files', [])
    if not items:
        return ""
    file_id = items[0]['id']
    request = drive_service.files().get_media(fileId=file_id)
    from io import BytesIO
    from googleapiclient.http import MediaIoBaseDownload
    fh = BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    return fh.getvalue().decode("utf-8")

def clean_and_parse(text):
    lines = text.splitlines()
    parsed = []
    seen_lines = set()
    for line in lines:
        if line.strip() == "" or line in seen_lines:
            continue
        seen_lines.add(line)
        timestamp_match = re.match(r"^\*\*🕰️ (.*?)\*\*", line)
        if timestamp_match:
            timestamp = timestamp_match.group(1)
        else:
            timestamp = ""
        parsed.append(f"{timestamp} {line.strip()}")
    return parsed

def write_digest(parsed_lines):
    os.makedirs("Memory/Digests", exist_ok=True)
    with open(DIGEST_OUTPUT, "w", encoding="utf-8") as f:
        f.write("# Scroll Digest\n\n")
        for line in parsed_lines:
            f.write(f"{line}\n")

def write_log(message):
    os.makedirs("Logs", exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {message}\n")

def run_warden():
    write_log("Warden of Echoes invoked.")
    all_parsed = []
    for filename in SCROLL_FILES:
        content = get_file_content(filename)
        if content:
            parsed = clean_and_parse(content)
            all_parsed.extend(parsed)
            write_log(f"Parsed {filename}, {len(parsed)} lines.")
        else:
            write_log(f"Failed to retrieve {filename}.")
    all_parsed = sorted(set(all_parsed))
    write_digest(all_parsed)
    write_log(f"Digest written: {DIGEST_OUTPUT}")

def main(request=None):
    run_warden()
    return "Warden of Echoes completed memory scan."

if __name__ == "__main__":
    run_warden()
