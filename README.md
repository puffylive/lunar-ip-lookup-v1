# 🌙 Lunar v1 - IP Lookup Tool

<div align="center">

![Lunar Logo](https://via.placeholder.com/800x200/5A189A/FFFFFF?text=LUNAR+v1+IP+LOOKUP)  
*[Replace with your actual logo image]*

**A powerful, purple-themed IP geolocation lookup tool with a sleek terminal interface**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)
[![Windows](https://img.shields.io/badge/Windows-11%2C%2010-purple.svg)](https://windows.com)
[![Version](https://img.shields.io/badge/Version-1.0.0-9D4EDD.svg)]()

</div>

## ✨ Features

- 🌐 **IP Geolocation** - Detailed location information for any IP address
- 🎨 **Beautiful Purple UI** - Custom terminal interface with purple theme
- 💾 **Export Results** - Save lookup data as JSON files
- 🚀 **Fast & Lightweight** - Quick API queries with minimal resource usage
- 🔧 **Multiple Modes** - Lookup target IPs or your own public IP
- 🗺️ **Map Integration** - Direct Google Maps links for coordinates
- 📦 **Executable Support** - Run as standalone .exe file
- 🛡️ **Error Handling** - Robust error handling and input validation

## 📸 Screenshots

### Main Interface
![Main Menu](https://via.placeholder.com/800x450/5A189A/FFFFFF?text=Main+Menu+Interface)  
*[Add screenshot of your main menu here]*

### IP Lookup Results
![Results Screen](https://via.placeholder.com/800x450/7B2CBF/FFFFFF?text=IP+Lookup+Results)  
*[Add screenshot of IP lookup results here]*

### Command Line Mode
![CLI Mode](https://via.placeholder.com/800x250/240046/FFFFFF?text=Command+Line+Interface)  
*[Add screenshot of CLI mode here]*

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Windows 10/11 (or Linux/Mac with terminal)
- Internet connection

### Installation

1. **Clone or Download the Repository**
```bash
git clone https://github.com/puffylive/lunar-ip-lookup.git
cd lunar-ip-lookup
Install Required Dependencies

bash
pip install -r requirements.txt
Or install manually:

bash
pip install requests colorama
Run the Tool

bash
python lunar_ip_lookup.py
📖 In-Depth Tutorial
🎮 Part 1: Basic Usage
Step 1: Launch the Application
After installation, simply run the script:

bash
python lunar_ip_lookup.py
You'll be greeted with the main menu:

https://via.placeholder.com/600x300/3C096C/FFFFFF?text=LUNAR+v1+Main+Menu
The purple-themed main interface appears

Step 2: Choose Lookup Type
Use the menu options:

Option 1: Lookup a specific IP address

Option 2: Lookup your own public IP

Option 3-4: Future features (coming in v2)

Option 5: Exit the program

https://via.placeholder.com/600x200/240046/FFFFFF?text=Menu+Options+1-5
Select from the available options

Step 3: Enter IP Address
If you choose Option 1, enter any valid IP address:

text
Enter target IP address: 8.8.8.8
https://via.placeholder.com/600x100/5A189A/FFFFFF?text=Enter+IP+Address+8.8.8.8
Enter the target IP address

Step 4: View Results
The tool queries the IP-API service and displays:

https://via.placeholder.com/700x400/7B2CBF/FFFFFF?text=Detailed+IP+Information
Comprehensive IP information displayed

Step 5: Save Results (Optional)
When prompted, save results to a JSON file:

text
💾 Save results to file? [Y/n]: Y
✅ Results saved to: lunar_ip_lookup_20241215_143022.json
🔧 Part 2: Advanced Features
Command Line Mode
Run lookups directly from command line:

bash
# Lookup specific IP
python lunar_ip_lookup.py --ip 1.1.1.1

# OR
python lunar_ip_lookup.py -i 192.168.1.1
https://via.placeholder.com/600x250/3C096C/FFFFFF?text=Command+Line+Mode+Example
Direct command line lookup

Exporting Data
All saved JSON files include complete API response:

json
{
  "status": "success",
  "country": "United States",
  "countryCode": "US",
  "region": "CA",
  "regionName": "California",
  "city": "Mountain View",
  "zip": "94043",
  "lat": 37.4192,
  "lon": -122.0574,
  "timezone": "America/Los_Angeles",
  "isp": "Google LLC",
  "org": "Google LLC",
  "as": "AS15169 Google LLC",
  "query": "8.8.8.8"
}
Map Integration
Click the generated Google Maps link to see the location:

text
📍 Map Link: https://www.google.com/maps?q=37.4192,-122.0574
https://via.placeholder.com/600x300/4285F4/FFFFFF?text=Google+Maps+Integration
View location on Google Maps

💻 Part 3: Creating an Executable
Generate .exe File
Use the built-in instructions:

bash
python lunar_ip_lookup.py --exe
Or use PyInstaller directly:

bash
# Install PyInstaller
pip install pyinstaller

# Create executable
pyinstaller --onefile --console --name "Lunar_IP_Lookup" lunar_ip_lookup.py

# With custom icon (optional)
pyinstaller --onefile --console --name "Lunar_IP_Lookup" --icon=lunar.ico lunar_ip_lookup.py
Executable Locations
Windows: dist/Lunar_IP_Lookup.exe

Output: Standalone executable (no Python required)

https://via.placeholder.com/400x200/5A189A/FFFFFF?text=Lunar_IP_Lookup.exe
Standalone executable file

🛠️ Technical Details
API Integration
Lunar v1 uses the free ip-api.com service with these rate limits:

45 requests per minute from an IP address

No API key required

Commercial use available

Color System
The purple theme uses ANSI escape codes:

\033[95m - Bright Purple

\033[35m - Dark Purple

\033[38;5;141m - Light Purple

\033[38;5;165m - Bright Purple

\033[38;5;129m - Neon Purple

File Structure
text
lunar_ip_lookup/
├── lunar_ip_lookup.py      # Main application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── lunar.ico              # Icon for executable (optional)
└── examples/              # Example output files
    ├── lookup_google.json
    └── lookup_cloudflare.json
📋 Usage Examples
Example 1: Basic Lookup
bash
> python lunar_ip_lookup.py
[Choose Option 1]
Enter target IP address: 8.8.8.8
[Shows Google's DNS server location]
Example 2: Public IP Check
bash
> python lunar_ip_lookup.py
[Choose Option 2]
[Automatically detects and displays your public IP]
Example 3: Batch Processing (Manual)
Create a batch file lookup.bat:

batch
@echo off
python lunar_ip_lookup.py --ip 1.1.1.1
pause
python lunar_ip_lookup.py --ip 8.8.8.8
pause
🐛 Troubleshooting
Issue	Solution
"Cannot connect to IP API service"	Check internet connection, firewall settings
"Invalid IP address format"	Ensure IP follows xxx.xxx.xxx.xxx format
Colors not displaying	Ensure terminal supports ANSI colors
Executable won't run	Install Visual C++ Redistributable
Permission denied when saving	Run as administrator or choose different save location
🔮 Future Updates (v2 Planned)
Batch IP Processing - Upload CSV files with multiple IPs

Network Scanner Integration - Scan local network IPs

Whois Lookup - Additional domain registration info

Report Generation - PDF/HTML report generation

API Key Support - For higher rate limits

Dark/Light Mode - Toggle between themes

Proxy Support - Use proxies for lookups

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

👤 Author
PuffyLive

GitHub: @puffylive

Tool: Lunar v1 IP Lookup

Version: 1.0.0

🙏 Acknowledgments
ip-api.com for the free geolocation API

Python community for excellent libraries

Contributors and testers

⭐ Support
If you find this tool useful, please:

⭐ Star the repository

🐛 Report issues

🔄 Share with others

