import platform
import os

def get_terminal_info():
    term_info = os.popen('echo $SHELL').read().strip()
    term_size = os.get_terminal_size()

    return term_info, term_size

def colorize_text(text, color):
    colors = {
        'HEADER': '\033[95m',
        'OKBLUE': '\033[94m',
        'OKCYAN': '\033[96m',
        'OKGREEN': '\033[92m',
        'WARNING': '\033[93m',
        'FAIL': '\033[91m',
        'ENDC': '\033[0m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m',
    }
    return f"{colors[color]}{text}{colors['ENDC']}"

def whocaresfetch():
    system_info = platform.uname()

    print(colorize_text("Really, who cares?", 'OKBLUE'))
    print(colorize_text(f"System: {system_info.system}", 'OKCYAN'))
    print(colorize_text(f"Node: {system_info.node}", 'OKCYAN'))
    print(colorize_text(f"Release: {system_info.release}", 'OKCYAN'))
    print(colorize_text(f"Version: {system_info.version}", 'OKCYAN'))
    print(colorize_text(f"Machine: {system_info.machine}", 'OKCYAN'))
    print(colorize_text(f"Processor: {system_info.processor}", 'OKCYAN'))

    print(colorize_text("\nDistribution Information:", 'OKGREEN'))
    dist_info = platform.platform()
    print(colorize_text(f"Distribution: {dist_info}", 'OKCYAN'))
    
    print(colorize_text("\nAdditional Information:", 'OKGREEN'))
    print(colorize_text(f"Architecture: {platform.architecture()}", 'OKCYAN'))
    print(colorize_text(f"System Type: {platform.system()} {platform.architecture()[0]}", 'OKCYAN'))
    print(colorize_text(f"Python Version: {platform.python_version()}", 'OKCYAN'))
    print(colorize_text(f"Boot Time: {os.path.getctime('/')}", 'OKCYAN'))  # Using the creation time of the root directory as a substitute for boot time

    print(colorize_text("\nHardware Information:", 'OKGREEN'))
    print(colorize_text(f"CPU Cores: {os.cpu_count()}", 'OKCYAN'))
    print(colorize_text(f"RAM Total: {round(os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / (1024. ** 3), 2)} GB", 'OKCYAN'))

    print(colorize_text("\nStorage Information:", 'OKGREEN'))
    statvfs = os.statvfs('/')
    print(colorize_text(f"Total Size: {round((statvfs.f_frsize * statvfs.f_blocks) / (1024. ** 3), 2)} GB", 'OKCYAN'))

    term_info, term_size = get_terminal_info()
    print(colorize_text("\nTerminal Information:", 'OKGREEN'))
    print(colorize_text(f"Shell: {term_info}", 'OKCYAN'))
    print(colorize_text(f"Terminal Size: {term_size.columns} columns x {term_size.lines}", 'OKCYAN'))

if __name__ == "__main__":
    whocaresfetch()
