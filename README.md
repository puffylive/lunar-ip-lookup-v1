# 🌙 Lunar v1 — IP Lookup Tool
<div align="center">


Replace this with your actual logo once uploaded

A purple-themed IP lookup tool with a clean and simple terminal interface.








</div>
✨ Features

🌐 Look up any IP address

🟣 Clean purple-themed UI

💾 Save lookups as JSON files

⚡ Fast API requests

🔍 Check your own public IP

🗺️ Google Maps coordinate links

🛡️ Great error handling

📦 Works as .exe if you want

📸 Screenshots
🟪 Main Interface

🟪 IP Lookup Results

🟪 Command Line Mode

🚀 Quick Start
1. Install Python Requirements
pip install -r requirements.txt


Or install manually:

pip install requests colorama

2. Run the Tool
python lunar_ip_lookup.py

📖 How to Use
⭐ Step 1 — Start the Program
python lunar_ip_lookup.py


You’ll see the purple main menu:

⭐ Step 2 — Choose an Option

1 → Look up an IP

2 → View your public IP

3 → View saved logs (coming soon)

4 → Settings (coming soon)

5 → Exit

⭐ Step 3 — Enter an IP

Example:

Enter target IP address: 8.8.8.8


⭐ Step 4 — View Results

You get:

City

State

Country

Timezone

ISP / Org

Coordinates

Google Maps link

⭐ Step 5 — Save If You Want
💾 Save results to file? [Y/n]:


Creates:

lunar_ip_lookup_20251201_143022.json

💻 Advanced Usage
🎯 Direct CLI Lookup
python lunar_ip_lookup.py --ip 1.1.1.1

🎯 Build an Executable (.exe)

Install:

pip install pyinstaller


Build:

pyinstaller --onefile --console lunar_ip_lookup.py


Add an icon:

pyinstaller --onefile --console --icon=lunar.ico lunar_ip_lookup.py

🗂 Project Structure
lunar_ip_lookup/
│── lunar_ip_lookup.py
│── requirements.txt
│── README.md
│── lunar.ico (optional)
└── examples/
    ├── lookup_google.json
    └── lookup_cloudflare.json

🔧 Technical Info

Uses ip-api.com

Does not require an API key

45 requests/min limit

Purple theme uses ANSI escape codes

JSON output is standardized

🔮 Planned for v2

Batch IP uploads

Local network scanner

WHOIS lookup

PDF/HTML report generation

Proxy support

Multiple color themes

Saved lookup history

👤 Author

PuffyLive
GitHub: https://github.com/puffylive

⭐ Support

If you like this project:

⭐ Star the repo

🐛 Report bugs

🔄 Suggest features
