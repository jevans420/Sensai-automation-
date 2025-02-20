import time
import json
import requests
from automation_utils import post_to_twitter, post_to_reddit, post_to_fansly, send_auto_dms

# Load configuration settings
with open("config.json", "r") as config_file:
    config = json.load(config_file)

def run_automation():
    while True:
        print("🔄 Running automation cycle...")
        
        # Auto-posting to platforms
        post_to_twitter(config)
        post_to_reddit(config)
        post_to_fansly(config)
        
        # Auto-send DMs to subscribers
        send_auto_dms(config)
        
        # Sleep before next cycle
        time.sleep(config["posting_interval"])

if __name__ == "__main__":
    print("🚀 SensAI Automation System Starting...")
    run_automation()
