#!/usr/bin/env python3
"""
Local development runner for the Telegram Quiz Bot
This script allows you to run the bot locally with polling for development
"""

import os
import sys

def run_local():
    """Run the bot in local development mode with polling"""
    print("🔧 Starting Telegram Quiz Bot in LOCAL DEVELOPMENT mode...")
    print("📡 Using polling instead of webhooks for local testing")
    print("🔄 Press Ctrl+C to stop the bot\n")
    
    # Set environment variable to use polling
    os.environ['ENVIRONMENT'] = 'local'
    
    # Import and run the bot
    try:
        from TelegramBot import bot
        print("✅ Bot initialized successfully!")
        print("🤖 Bot is now running and listening for messages...")
        print("💬 Test it by sending /start to your bot on Telegram\n")
        
        # Remove any existing webhook and start polling
        bot.remove_webhook()
        bot.polling(none_stop=True)
        
    except KeyboardInterrupt:
        print("\n🛑 Bot stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error starting bot: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_local()
