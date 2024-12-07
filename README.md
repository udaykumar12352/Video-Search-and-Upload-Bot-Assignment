# 🎥 Video Search and Upload Bot

A Python-based bot to search, download, and upload videos from social media platforms such as Instagram, TikTok, and Reddit. The bot integrates with Empowerverse's API to upload videos to the Super Feed category.

---

## 📋 Project Description

This bot automates the process of:
1. Searching and downloading videos from specified platforms.
2. Uploading videos to a server using provided API endpoints.
3. Monitoring a directory (`/videos`) for new `.mp4` files and processing them automatically.

Key features:
- Async operations for concurrent uploads.
- Auto-deletion of local files after upload.
- Comprehensive error handling and retry mechanisms.

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or above
- `pip` (Python package manager)
- Internet connection

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/video-bot.git
   cd video-bot
2.Install dependencies:
    pip install -r requirements.txt
3.Set up your Flic-Token:
    Obtain your token by messaging the Empowerverse Telegram bot with your username.
▶️ How to Run the Bot
1.Run the bot:
    python main.py
2.Follow the on-screen prompts to:
    Search for videos on specified platforms.
    Monitor the /videos directory for .mp4 files.
    Automatically upload videos to the Super Feed.
📖 Usage Guidelines
Testing Features
    1.Search and Download:
        Provide a valid URL from Instagram, TikTok, or Reddit.
        Verify the video is downloaded to the /videos directory.
    2.Upload Videos:
        Place an .mp4 file in the /videos directory.
        Confirm the bot uploads it using the Empowerverse API.
    3.Super Feed Verification:
        Open the Empowerverse app and navigate to the Super Feed category.
        Verify the uploaded video is visible.
🤝 Contribution
Feel free to fork the repository, create a new branch, and submit a pull request for any improvements or fixes.
📞 Support
    For issues or questions, please contact:
        Email:udaykumarvakacharla@gmail.com
📜 License
    This project is licensed under the MIT License. See the LICENSE file for details.