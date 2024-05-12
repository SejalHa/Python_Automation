
# Instagram Bot

Overview

This Python script is designed to automate interactions on Instagram, including liking posts, commenting, and following users based on specified tags. It utilizes the Selenium library for web automation.

 Prerequisites

- Python 3.x installed
- Chrome WebDriver installed (compatible with your Chrome version)
- Required Python packages installed (`requests`, `selenium`)

 Installation

1. Clone or download the repository to your local machine.
2. Install Python 3.x if not already installed.
3. Install required Python packages using pip:
   ```
   pip install requests selenium
   ```
4. Download Chrome WebDriver compatible with your Chrome version and set its path in the script.

 Configuration

1. Create a `creds.txt` file in the same directory as the script.
2. Add your Instagram username and password in the `creds.txt` file, separated by a space.

 Usage

1. Run the script using Python:
   ```
   python instagram_bot.py
   ```
2. Follow the on-screen instructions to configure the bot:
   - Enter the tags you want to search for (separated by commas).
   - Specify the number of posts to interact with per tag.
   - Set the follow percentage (0 for no follows).
   - Enter a list of comments to post (separated by commas).
   - Confirm the configurations.

Important Notes

- Ensure that your internet connection is stable before running the script.
- The bot will simulate human-like behavior to avoid detection by Instagram's anti-bot measures, including random wait times.
- Use the bot responsibly and within Instagram's terms of service to avoid account suspension or banning.

Disclaimer

This script is provided for educational purposes only. The developers are not responsible for any misuse or damage caused by the script.

---

Feel free to customize the README further to include additional information or instructions specific to your use case!
