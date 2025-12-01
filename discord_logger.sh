#!/bin/bash

source .env

# Configuration
WEBHOOK_URL="$(WEBHOOK_URL_ENV)"
LOG_FILE="/home/luis/arch-daemon/discord.log"

# Function to send to Discord
send_discord() {
    # Escape special characters for JSON
    CONTENT=$(echo "$1" | sed 's/"/\\"/g' | sed ':a;N;$!ba;s/\n/\\n/g')
    
    # Send via curl
    curl -H "Content-Type: application/json" \
         -X POST \
         -d "{\"content\": \"\`\`\`$CONTENT\`\`\`\"}" \
         $WEBHOOK_URL
}

send_discord "Logger started up"

# Monitor the log file
# -F ensures it follows even if the file is rotated/recreated
tail -F -n 0 "$LOG_FILE" | while read line; do
    send_discord "$line"
done
