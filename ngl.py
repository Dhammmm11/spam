#!/data/data/com.termux/files/usr/bin/python3
# -*- coding: utf-8 -*-
"""
██╗   ██╗ ██████╗ ██╗██████╗    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
██║   ██║██╔═══██╗██║██╔══██╗   ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
██║   ██║██║   ██║██║██║  ██║   ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
╚██╗ ██╔╝██║   ██║██║██║  ██║   ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
 ╚████╔╝ ╚██████╔╝██║██████╔╝   ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
  ╚═══╝   ╚═════╝ ╚═╝╚═════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
VOID NUKER - Ultimate NGL Spammer v4.0
Developer: Marr | Termux Optimized
"""

import subprocess
import sys
import os

# ========== AUTO-INSTALL DEPENDENCIES ==========
def install_dependencies():
    """Auto-install required packages"""
    print("[*] Checking dependencies...")
    
    required = {
        'requests': 'requests',
        'colorama': 'colorama'
    }
    
    for module, package in required.items():
        try:
            __import__(module)
            print(f"✅ {module} already installed")
        except ImportError:
            print(f"⚠️ Installing {module}...")
            try:
                subprocess.check_call([
                    sys.executable, 
                    "-m", 
                    "pip", 
                    "install", 
                    package,
                    "--quiet"
                ])
                print(f"✅ {module} installed successfully")
            except Exception as e:
                print(f"❌ Failed to install {module}: {e}")
                print("Please run manually: pip install requests colorama")
                sys.exit(1)

# Run auto-install
install_dependencies()

# ========== NOW IMPORT EVERYTHING ==========
import requests
import json
import time
import threading
import random
from datetime import datetime

# ========== CONFIGURATION ==========
VERSION = "4.0"
DEVELOPER = "Marr"
BANNER = f"""
{chr(27)}[91m
╦  ╦╔═╗╔╦╗╔╦╗  ╔═╗╦ ╦╔═╗╦═╗╔═╗
╚╗╔╝╠═╣║║║ ║   ║ ╦║ ║╠═╣╠╦╝║╣ 
 ╚╝ ╩ ╩╩ ╩ ╩   ╚═╝╚═╝╩ ╩╩╚═╚═╝
{chr(27)}[96m
╔═╗╔╦╗╔═╗╔═╗╦═╗╔═╗╔═╗╦  ╔═╗╦═╗
╠═╣ ║║╠═╣║ ║╠╦╝╠═╣║  ║  ║╣ ╠╦╝
╩ ╩═╩╝╩ ╩╚═╝╩╚═╩ ╩╚═╝╩═╝╚═╝╩╚═
{chr(27)}[93m
Termux Edition v{VERSION}
Developer: {DEVELOPER}
{chr(27)}[0m"""

# User Agents
USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 12; SM-S901U) AppleWebKit/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 10) AppleWebKit/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
]

# Colors
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

# ========== CORE FUNCTIONS ==========
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    clear_screen()
    print(BANNER)

def print_colored(text, color=Colors.WHITE):
    print(f"{color}{text}{Colors.END}")

# ========== NGL SPAMMER CLASS ==========
class VoidNuker:
    def __init__(self):
        self.stats = {
            'sent': 0,
            'success': 0,
            'failed': 0,
            'running': False,
            'start_time': None
        }
        self.threads = []
        
    def send_message(self, username, message):
        """Send single message to NGL"""
        url = f"https://ngl.link/api/submit"
        
        headers = {
            'User-Agent': random.choice(USER_AGENTS),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://ngl.link',
            'Referer': f'https://ngl.link/{username}',
            'X-Requested-With': 'XMLHttpRequest'
        }
        
        payload = {
            'username': username,
            'question': message,
            'deviceId': f"void_{random.randint(1000000, 9999999)}",
            'gameSlug': '',
            'referrer': ''
        }
        
        try:
            response = requests.post(url, data=payload, headers=headers, timeout=10)
            self.stats['sent'] += 1
            
            if response.status_code == 200:
                self.stats['success'] += 1
                return True
            else:
                self.stats['failed'] += 1
                return False
        except Exception:
            self.stats['failed'] += 1
            return False
    
    def worker(self, worker_id, username, messages, delay, quantity):
        """Worker thread"""
        sent_count = 0
        
        while self.stats['running'] and (quantity == 0 or sent_count < quantity):
            try:
                message = random.choice(messages)
                self.send_message(username, message)
                sent_count += 1
                
                # Update display every 5 messages
                if sent_count % 5 == 0:
                    self.display_stats()
                
                # Random delay
                time.sleep(delay + random.uniform(0, 0.3))
                
            except Exception as e:
                print_colored(f"[Thread-{worker_id}] Error: {e}", Colors.RED)
                time.sleep(2)
        
        print_colored(f"[Thread-{worker_id}] Finished - {sent_count} sent", Colors.GREEN)
    
    def display_stats(self):
        """Display live statistics"""
        if not self.stats['start_time']:
            return
            
        elapsed = time.time() - self.stats['start_time']
        success_rate = (self.stats['success'] / self.stats['sent'] * 100) if self.stats['sent'] > 0 else 0
        
        clear_screen()
        show_banner()
        
        print_colored(f"\n╔══════════════════════════════════════════╗", Colors.CYAN)
        print_colored(f"║         LIVE ATTACK STATISTICS         ║", Colors.WHITE)
        print_colored(f"╠══════════════════════════════════════════╣", Colors.CYAN)
        print_colored(f"║ 🎯 Target: {self.config['username']:28} ║", Colors.YELLOW)
        print_colored(f"║ 📤 Sent: {self.stats['sent']:<6} ✅ Success: {self.stats['success']:<6} ║", Colors.GREEN)
        print_colored(f"║ ❌ Failed: {self.stats['failed']:<5} 📊 Rate: {success_rate:6.1f}% ║", Colors.RED)
        print_colored(f"║ ⏱️  Time: {elapsed:6.1f}s 🧵 Threads: {len(self.threads):<4} ║", Colors.BLUE)
        
        if elapsed > 0:
            speed = self.stats['sent'] / elapsed
            print_colored(f"║ 🚀 Speed: {speed:6.1f}/s{' ' * 19}║", Colors.MAGENTA)
        
        print_colored(f"╚══════════════════════════════════════════╝", Colors.CYAN)
        print_colored(f"\n[!] Press Ctrl+C to stop", Colors.YELLOW)
    
    def start_attack(self, config):
        """Start the attack"""
        self.config = config
        self.stats = {
            'sent': 0,
            'success': 0,
            'failed': 0,
            'running': True,
            'start_time': time.time()
        }
        
        print_colored(f"\n[+] Starting attack on @{config['username']}", Colors.GREEN)
        print_colored(f"[+] Threads: {config['threads']} | Delay: {config['delay']}s", Colors.CYAN)
        print_colored(f"[+] Quantity: {'Unlimited' if config['quantity'] == 0 else config['quantity']}", Colors.YELLOW)
        
        time.sleep(2)
        
        # Create threads
        for i in range(config['threads']):
            thread = threading.Thread(
                target=self.worker,
                args=(i+1, config['username'], config['messages'], 
                      config['delay'], config['quantity']),
                daemon=True
            )
            thread.start()
            self.threads.append(thread)
        
        try:
            # Monitor attack
            while self.stats['running'] and any(t.is_alive() for t in self.threads):
                time.sleep(0.5)
                self.display_stats()
                
                # Check quantity limit
                if config['quantity'] > 0 and self.stats['sent'] >= config['threads'] * config['quantity']:
                    break
                    
        except KeyboardInterrupt:
            print_colored("\n[!] Stopping attack...", Colors.RED)
        
        finally:
            self.stop_attack()
    
    def stop_attack(self):
        """Stop the attack"""
        self.stats['running'] = False
        time.sleep(1)
        
        # Final stats
        elapsed = time.time() - self.stats['start_time']
        success_rate = (self.stats['success'] / self.stats['sent'] * 100) if self.stats['sent'] > 0 else 0
        
        print_colored(f"\n════════════════════════════════════════", Colors.CYAN)
        print_colored(f"           ATTACK COMPLETED           ", Colors.GREEN)
        print_colored(f"════════════════════════════════════════", Colors.CYAN)
        print_colored(f"🎯 Target: {self.config['username']}", Colors.YELLOW)
        print_colored(f"✅ Success: {self.stats['success']}", Colors.GREEN)
        print_colored(f"❌ Failed: {self.stats['failed']}", Colors.RED)
        print_colored(f"📤 Total: {self.stats['sent']}", Colors.CYAN)
        print_colored(f"📊 Rate: {success_rate:.1f}%", Colors.MAGENTA)
        print_colored(f"⏱️  Time: {elapsed:.1f}s", Colors.BLUE)
        
        if elapsed > 0:
            speed = self.stats['sent'] / elapsed
            print_colored(f"🚀 Speed: {speed:.1f}/s", Colors.GREEN)
        
        print_colored(f"════════════════════════════════════════", Colors.CYAN)
        
        # Save results
        self.save_results(elapsed, success_rate)
    
    def save_results(self, elapsed, success_rate):
        """Save results to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"void_results_{timestamp}.txt"
        
        try:
            with open(filename, 'w') as f:
                f.write(f"VOID NUKER Attack Results\n")
                f.write(f"Time: {timestamp}\n")
                f.write(f"Target: {self.config['username']}\n")
                f.write(f"Success: {self.stats['success']}\n")
                f.write(f"Failed: {self.stats['failed']}\n")
                f.write(f"Total: {self.stats['sent']}\n")
                f.write(f"Success Rate: {success_rate:.1f}%\n")
                f.write(f"Duration: {elapsed:.1f}s\n")
                f.write(f"Threads: {self.config['threads']}\n")
                f.write(f"Developer: {DEVELOPER}\n")
            
            print_colored(f"[+] Results saved to {filename}", Colors.GREEN)
        except Exception as e:
            print_colored(f"[!] Failed to save: {e}", Colors.RED)

# ========== MAIN MENU ==========
def main_menu():
    """Main menu interface"""
    spammer = VoidNuker()
    
    while True:
        show_banner()
        
        print_colored(f"\n╔══════════════════════════════════════╗", Colors.CYAN)
        print_colored(f"║            MAIN MENU               ║", Colors.WHITE)
        print_colored(f"╠══════════════════════════════════════╣", Colors.CYAN)
        print_colored(f"║ 1️⃣  Quick Attack                   ║", Colors.GREEN)
        print_colored(f"║ 2️⃣  Custom Attack                  ║", Colors.YELLOW)
        print_colored(f"║ 3️⃣  View Results                   ║", Colors.BLUE)
        print_colored(f"║ 4️⃣  Exit                          ║", Colors.RED)
        print_colored(f"╚══════════════════════════════════════╝", Colors.CYAN)
        
        choice = input(f"\n{Colors.CYAN}[?] Select (1-4): {Colors.END}").strip()
        
        if choice == '1':
            username = input(f"{Colors.CYAN}[?] NGL Username: {Colors.END}").strip()
            if username:
                config = {
                    'username': username,
                    'messages': [
                        "VOID NUKER ACTIVATED 🚀",
                        "TERMUX POWER ⚡",
                        "MARRIAGE OF CHAOS 💀",
                        "UNLIMITED SPAM 🔥"
                    ],
                    'threads': 10,
                    'delay': 0.5,
                    'quantity': 0  # Unlimited
                }
                
                print_colored(f"\n[!] Starting attack on @{username}", Colors.YELLOW)
                print_colored(f"[!] Press Ctrl+C to stop anytime", Colors.RED)
                time.sleep(2)
                
                spammer.start_attack(config)
                input(f"\n{Colors.CYAN}[?] Press Enter to continue...{Colors.END}")
        
        elif choice == '2':
            show_banner()
            
            username = input(f"{Colors.CYAN}[?] NGL Username: {Colors.END}").strip()
            if not username:
                continue
            
            # Messages
            print_colored(f"\n[*] Messages (Enter empty to use default)", Colors.YELLOW)
            messages = []
            while True:
                msg = input(f"{Colors.CYAN}[?] Message {len(messages)+1}: {Colors.END}").strip()
                if not msg:
                    if not messages:
                        messages = ["VOID ATTACK 🌀", "TERMUX EDITION 📱", "MARRIAGE 👑"]
                    break
                messages.append(msg)
            
            # Threads
            try:
                threads = int(input(f"{Colors.CYAN}[?] Threads (1-50): {Colors.END}") or "10")
                threads = max(1, min(50, threads))
            except:
                threads = 10
            
            # Delay
            try:
                delay = float(input(f"{Colors.CYAN}[?] Delay (seconds): {Colors.END}") or "0.5")
                delay = max(0.1, delay)
            except:
                delay = 0.5
            
            # Quantity
            try:
                quantity = int(input(f"{Colors.CYAN}[?] Messages per thread (0=unlimited): {Colors.END}") or "0")
            except:
                quantity = 0
            
            config = {
                'username': username,
                'messages': messages,
                'threads': threads,
                'delay': delay,
                'quantity': quantity
            }
            
            print_colored(f"\n[!] Starting attack with {threads} threads", Colors.YELLOW)
            time.sleep(2)
            
            spammer.start_attack(config)
            input(f"\n{Colors.CYAN}[?] Press Enter to continue...{Colors.END}")
        
        elif choice == '3':
            show_banner()
            print_colored(f"\n[*] Saved Results", Colors.CYAN)
            
            # List result files
            result_files = [f for f in os.listdir('.') if f.startswith('void_results_') and f.endswith('.txt')]
            
            if not result_files:
                print_colored("[!] No results found", Colors.YELLOW)
            else:
                for i, f in enumerate(sorted(result_files, reverse=True)[:5], 1):
                    print_colored(f"{i}. {f}", Colors.WHITE)
            
            input(f"\n{Colors.CYAN}[?] Press Enter to continue...{Colors.END}")
        
        elif choice == '4':
            print_colored(f"\n[*] Exiting VOID NUKER...", Colors.RED)
            time.sleep(1)
            clear_screen()
            break
        
        else:
            print_colored(f"\n[!] Invalid choice", Colors.RED)
            time.sleep(1)

# ========== MAIN EXECUTION ==========
if __name__ == "__main__":
    try:
        # Welcome message
        show_banner()
        print_colored(f"\n[*] VOID NUKER v{VERSION} - Ready for Action!", Colors.GREEN)
        print_colored(f"[*] Developer: {DEVELOPER}", Colors.CYAN)
        print_colored(f"[*] Platform: Termux (Android)", Colors.YELLOW)
        print_colored(f"[!] For educational purposes only", Colors.RED)
        time.sleep(2)
        
        # Start main menu
        main_menu()
        
    except KeyboardInterrupt:
        print_colored(f"\n[!] Interrupted by user", Colors.RED)
    except Exception as e:
        print_colored(f"\n[!] Error: {e}", Colors.RED)
