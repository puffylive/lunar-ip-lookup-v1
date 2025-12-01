import os
import sys
import time
import json
import requests
from datetime import datetime

PURPLE = "\033[95m"
DARK_PURPLE = "\033[35m"
LIGHT_PURPLE = "\033[38;5;141m"
BRIGHT_PURPLE = "\033[38;5;165m"
NEON_PURPLE = "\033[38;5;129m"
END = "\033[0m"

LOGO = f'''
{BRIGHT_PURPLE},──.                                             ,──. {END}
{DARK_PURPLE}│  │   ,──.,──.,──,──,  ,──,──.,──.──.,──.  ,──.{LIGHT_PURPLE}╱   │{END}
{BRIGHT_PURPLE}│  │   │  ││  ││      ╲' ,─.  ││  .──'{DARK_PURPLE} ╲  `'  ╱ `│  │{END}
{LIGHT_PURPLE}│  '──.'  ''  '│  ││  │╲ '─'  ││  │     {BRIGHT_PURPLE}╲    ╱   │  │{END}
{NEON_PURPLE}`─────' `────' `──''──' `──`──'`──'      `──'    `──' {END}
                                                    
'''

BANNER = f'''
{NEON_PURPLE}╔══════════════════════════════════════════════════════════════╗{END}
{BRIGHT_PURPLE}║                    LUNAR v1 - IP LOOKUP TOOL                 ║{END}
{DARK_PURPLE}║                    By PuffyLive                              ║{END}
{NEON_PURPLE}╚══════════════════════════════════════════════════════════════╝{END}
'''

def set_purple_theme():
    if os.name == 'nt':
        os.system('color 07')
        os.system('mode con: cols=80 lines=30')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    clear_screen()
    set_purple_theme()
    print(f"\n{LOGO}")
    print(f"{BANNER}\n")

def print_purple(text, level=0):
    colors = [LIGHT_PURPLE, BRIGHT_PURPLE, NEON_PURPLE, DARK_PURPLE]
    color = colors[min(level, len(colors)-1)]
    print(f"{color}{text}{END}")

def get_ip_info(ip_address):
    try:
        print_purple(f"\n🔍 Querying IP information...", 1)
        response = requests.get(f'http://ip-api.com/json/{ip_address}', timeout=10)
        response.raise_for_status()
        print_purple("✅ Data retrieved successfully!", 2)
        return response.json()
    except requests.exceptions.ConnectionError:
        print_purple("\n❌ Network Error: Cannot connect to IP API service", 3)
        print_purple("   Please check your internet connection", 0)
        return None
    except requests.exceptions.Timeout:
        print_purple("\n❌ Timeout Error: Request took too long", 3)
        return None
    except requests.exceptions.RequestException as e:
        print_purple(f"\n❌ API Error: {e}", 3)
        return None
    except json.JSONDecodeError:
        print_purple("\n❌ Data Error: Invalid response from server", 3)
        return None

def format_ip_info(data):
    if not data or data.get('status') != 'success':
        error_msg = f"{NEON_PURPLE}┌──────────────────────────────────────────────────────┐{END}\n"
        error_msg += f"{BRIGHT_PURPLE}│               LOOKUP FAILED                         │{END}\n"
        error_msg += f"{NEON_PURPLE}├──────────────────────────────────────────────────────┤{END}\n"
        error_msg += f"{DARK_PURPLE}│  ❌ Invalid IP address or lookup failed              │{END}\n"
        error_msg += f"{NEON_PURPLE}└──────────────────────────────────────────────────────┘{END}"
        return error_msg
    
    info_lines = [
        f"{NEON_PURPLE}┌──────────────────────────────────────────────────────┐{END}",
        f"{BRIGHT_PURPLE}│              IP GEO-LOCATION RESULTS                 │{END}",
        f"{NEON_PURPLE}├──────────────────────────────────────────────────────┤{END}",
        f"{LIGHT_PURPLE}│  Status:    {NEON_PURPLE}{data.get('status', 'N/A'):<44}{END}│",
        f"{LIGHT_PURPLE}│  IP Address: {BRIGHT_PURPLE}{data.get('query', 'N/A'):<43}{END}│",
        f"{NEON_PURPLE}├──────────────────────────────────────────────────────┤{END}",
        f"{LIGHT_PURPLE}│  Country:   {DARK_PURPLE}{data.get('country', 'N/A'):<44}{END}│",
        f"{LIGHT_PURPLE}│  Region:    {data.get('regionName', 'N/A'):<44}{END}│",
        f"{LIGHT_PURPLE}│  City:      {data.get('city', 'N/A'):<44}{END}│",
        f"{LIGHT_PURPLE}│  ZIP Code:  {data.get('zip', 'N/A'):<44}{END}│",
        f"{NEON_PURPLE}├──────────────────────────────────────────────────────┤{END}",
        f"{LIGHT_PURPLE}│  ISP:       {BRIGHT_PURPLE}{data.get('isp', 'N/A'):<44}{END}│",
        f"{LIGHT_PURPLE}│  Organization: {data.get('org', 'N/A'):<39}{END}│",
        f"{NEON_PURPLE}├──────────────────────────────────────────────────────┤{END}",
        f"{LIGHT_PURPLE}│  Timezone:  {data.get('timezone', 'N/A'):<44}{END}│",
        f"{LIGHT_PURPLE}│  Latitude:  {data.get('lat', 'N/A'):<44}{END}│",
        f"{LIGHT_PURPLE}│  Longitude: {data.get('lon', 'N/A'):<44}{END}│",
        f"{NEON_PURPLE}└──────────────────────────────────────────────────────┘{END}",
    ]
    
    if data.get('lat') and data.get('lon'):
        info_lines.append(f"\n{BRIGHT_PURPLE}📍 Map Link: {NEON_PURPLE}https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}{END}")
    
    return "\n".join(info_lines)

def save_to_file(data, filename=None):
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"lunar_ip_lookup_{timestamp}.json"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print_purple(f"\n💾 Results saved to: {filename}", 2)
        return True
    except PermissionError:
        print_purple(f"\n❌ Permission denied: Cannot write to {filename}", 3)
        return False
    except Exception as e:
        print_purple(f"\n❌ Error saving file: {e}", 3)
        return False

def display_menu():
    print_purple("═" * 60, 1)
    print_purple(" MENU OPTIONS:", 2)
    print_purple("═" * 60, 1)
    print_purple("  [1] 🔍 Lookup Target IP Address", 0)
    print_purple("  [2] 🌐 Lookup Your Public IP", 0)
    print_purple("  [3] 💾 View Previous Lookups", 0)
    print_purple("  [4] 🛠️  Settings", 0)
    print_purple("  [5] ❌ Exit", 0)
    print_purple("═" * 60, 1)

def validate_ip(ip):
    if not ip:
        return False
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False

def main():
    if os.name == 'nt':
        os.system('title 🌙 Lunar v1 - IP Lookup Tool - By PuffyLive')
    
    while True:
        display_header()
        display_menu()
        
        choice = input(f"\n{LIGHT_PURPLE}Select option [1-5]: {BRIGHT_PURPLE}").strip()
        print(END, end="")
        
        if choice == '5':
            print_purple("\n👋 Farewell! Thank you for using Lunar v1", 2)
            time.sleep(1.5)
            break
        
        elif choice == '1':
            ip_address = input(f"\n{LIGHT_PURPLE}Enter target IP address: {BRIGHT_PURPLE}").strip()
            print(END, end="")
            
            if not validate_ip(ip_address):
                print_purple("\n⚠️  Invalid IP address format (use: xxx.xxx.xxx.xxx)", 3)
                time.sleep(2)
                continue
        
        elif choice == '2':
            ip_address = ""
            print_purple("\n🌐 Detecting your public IP address...", 1)
        
        elif choice == '3':
            print_purple("\n📁 Feature coming soon in v2!", 1)
            time.sleep(2)
            continue
        
        elif choice == '4':
            print_purple("\n⚙️  Settings menu coming soon in v2!", 1)
            time.sleep(2)
            continue
        
        else:
            print_purple("\n❌ Invalid choice. Please select 1-5", 3)
            time.sleep(1.5)
            continue
        
        data = get_ip_info(ip_address)
        
        if data:
            clear_screen()
            print(f"\n{LOGO}")
            print("\n" + format_ip_info(data))
            
            print_purple("\n" + "─" * 60, 0)
            save_choice = input(f"{LIGHT_PURPLE}💾 Save results to file? [Y/n]: {BRIGHT_PURPLE}").strip().lower()
            print(END, end="")
            
            if save_choice not in ['n', 'no']:
                save_to_file(data)
            
            print_purple("\n" + "─" * 60, 0)
            again = input(f"{LIGHT_PURPLE}🔄 Perform another lookup? [Y/n]: {BRIGHT_PURPLE}").strip().lower()
            print(END, end="")
            
            if again in ['n', 'no']:
                print_purple("\n👋 Returning to main menu...", 1)
                time.sleep(1.5)
        else:
            input(f"\n{LIGHT_PURPLE}Press Enter to continue...{END}")

def create_exe_instructions():
    instructions = f"""
{BRIGHT_PURPLE}══════════════════════════════════════════════════════════════{END}
{NEON_PURPLE}                 CREATING EXECUTABLE (.exe){END}
{BRIGHT_PURPLE}══════════════════════════════════════════════════════════════{END}

{LIGHT_PURPLE}To create an executable file from this script:{END}

1. {DARK_PURPLE}Install PyInstaller:{END}
   {BRIGHT_PURPLE}pip install pyinstaller{END}

2. {DARK_PURPLE}Create the executable:{END}
   {BRIGHT_PURPLE}pyinstaller --onefile --windowed --name "Lunar_v1" lunar_ip_lookup.py{END}

3. {DARK_PURPLE}Additional options for better executable:{END}
   {BRIGHT_PURPLE}pyinstaller --onefile --console --name "Lunar_IP_Lookup" ^
              --add-data ".;." --icon=icon.ico lunar_ip_lookup.py{END}

{NEON_PURPLE}The executable will be created in the 'dist' folder.{END}
"""
    return instructions

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            if sys.argv[1] in ['--exe', '-e', '--build']:
                print(create_exe_instructions())
                input(f"\n{LIGHT_PURPLE}Press Enter to exit...{END}")
                sys.exit(0)
            elif sys.argv[1] in ['--ip', '-i'] and len(sys.argv) > 2:
                set_purple_theme()
                print(f"\n{LOGO}")
                data = get_ip_info(sys.argv[2])
                if data:
                    print("\n" + format_ip_info(data))
                sys.exit(0)
        
        main()
        
    except KeyboardInterrupt:
        print_purple(f"\n\n⚠️  Program interrupted by user", 3)
        sys.exit(0)
    except Exception as e:
        print_purple(f"\n❌ Unexpected error: {e}", 3)
        sys.exit(1)
