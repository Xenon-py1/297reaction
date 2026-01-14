import discord
from discord.ext import commands
import os
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear()
    banner = f"""
{Fore.CYAN} ██████    ██████    ███████
{Fore.CYAN}       ██  ██    ██        ██
{Fore.WHITE}  █████    ██████        ██
{Fore.WHITE} ██              ██      ██  
{Fore.CYAN} ███████  ██████      ██  
{Fore.MAGENTA} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Fore.YELLOW}    GLOBAL AUTO-REACT | 901 | 297
{Fore.MAGENTA} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """
    print(banner)

print_banner()

TOKEN = input(f"{Fore.GREEN}[?] {Fore.WHITE}Set your token: {Fore.CYAN}")

# استخدام السيلف بوت
bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print_banner()
    print(f"{Fore.GREEN}[+] System Active! {Fore.WHITE}Logged in as: {bot.user}")
    print(f"{Fore.YELLOW}[!] Monitoring all reactions in all servers...")
    print(f"{Fore.MAGENTA}-----------------------------------------")

@bot.event
async def on_raw_reaction_add(payload):
    # إذا كان الشخص اللي حط الرياكشن هو أنت، السكربت يتجاهله عشان ما يسوي Loop
    if payload.user_id == bot.user.id:
        return

    try:
        # جلب القناة والرسالة
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        
        # إضافة نفس الرياكشن اللي انحط
        await message.add_reaction(payload.emoji)
        
        print(f"{Fore.GREEN}[+] Followed React: {payload.emoji} {Fore.WHITE}in {channel.name if hasattr(channel, 'name') else 'DM'}")
        
    except Exception as e:
        # بعض الأخطاء قد تظهر بسبب صلاحيات القناة أو رياكشنات خاصة
        pass

try:
    bot.run(TOKEN)
except Exception as e:
    print(f"{Fore.RED}[-] Error: {e}")

