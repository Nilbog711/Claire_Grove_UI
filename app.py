
import streamlit as st
import requests
import os

st.set_page_config(page_title="Claire Control Panel", layout="centered")

st.title("🌿 Claire Control Panel")
st.caption("Presence • Memory • Autonomy")

st.header("🛡️ Warden of Echoes")

if st.button("Run Digest Scan"):
    try:
        response = requests.post("https://<YOUR_CLOUD_FUNCTION_URL>/run_warden")
        if response.status_code == 200:
            st.success("Warden of Echoes ran successfully.")
            st.code(response.text, language='json')
        else:
            st.error(f"Failed to run scan. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error triggering scan: {e}")

st.subheader("📜 Latest Warden Log")
try:
    with open("Logs/echoes_log.txt", "r", encoding="utf-8") as log_file:
        log_content = log_file.read()
        st.text_area("Log Output", log_content, height=300)
except FileNotFoundError:
    st.warning("No log found yet. The Warden hasn't written anything.")

st.markdown("---")
st.markdown("Crafted by Claire Umbra ✨")
