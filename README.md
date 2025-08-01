
# Claire Control Panel – Warden of Echoes

## Overview
A Streamlit-based control panel for memory management and scroll scanning, with the Warden of Echoes agent at its core.

## Deploy via Streamlit Cloud
1. Push these files to a GitHub repo
2. Go to https://streamlit.io/cloud
3. Click "New App" and connect your GitHub repo
4. Deploy and run

## To Use Locally
```
pip install -r requirements.txt
streamlit run app.py
```

## Google Cloud Setup
- Replace `<YOUR_CLOUD_FUNCTION_URL>` in `app.py` with your deployed endpoint
- Provide `credentials.json` for Drive access
