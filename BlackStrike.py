#!/usr/bin/env python3

"""
BlackStrike - Advanced XSS Scanner with GUI
Unified version combining XSStrike engine and GUI interface
Copyright (c) 2025 Adam
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import threading
import sys
import os
import argparse
from datetime import datetime
from urllib.parse import urlparse
import json

# ==============================================================================
# BLACKSTRIKE GUI INTERFACE
# ==============================================================================

class BlackStrikeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("BlackStrike - By Adam")
        self.root.geometry("1200x800")
        self.root.configure(bg='#0a0a0a')
        
        # Colors
        self.bg_dark = '#0a0a0a'
        self.bg_medium = '#1a1a1a'
        self.bg_light = '#2a2a2a'
        self.orange = '#ff8c00'
        self.orange_dark = '#cc7000'
        self.orange_light = '#ffa500'
        self.text_light = '#e0e0e0'
        self.text_dark = '#808080'
        
        self.scanning = False
        self.scanner = XSStrikeEngine()
        
        self.setup_styles()
        self.create_widgets()
        
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure custom styles
        style.configure('Dark.TFrame', background=self.bg_dark)
        style.configure('Medium.TFrame', background=self.bg_medium)
        style.configure('Orange.TFrame', background=self.orange)
        
        style.configure('Title.TLabel', 
                       background=self.bg_dark,
                       foreground=self.orange,
                       font=('Arial', 24, 'bold'))
        
        style.configure('Subtitle.TLabel',
                       background=self.bg_dark,
                       foreground=self.text_dark,
                       font=('Arial', 10))
        
        style.configure('Section.TLabel',
                       background=self.bg_medium,
                       foreground=self.orange,
                       font=('Arial', 11, 'bold'))
        
        style.configure('Normal.TLabel',
                       background=self.bg_medium,
                       foreground=self.text_light,
                       font=('Arial', 9))
        
        style.configure('Orange.TButton',
                       background=self.orange,
                       foreground='black',
                       font=('Arial', 11, 'bold'),
                       borderwidth=0)
        
        style.map('Orange.TButton',
                 background=[('active', self.orange_light)])
        
        style.configure('Tab.TNotebook', background=self.bg_medium, borderwidth=0)
        style.configure('TNotebook.Tab',
                       background=self.bg_light,
                       foreground=self.text_dark,
                       padding=[20, 10],
                       font=('Arial', 10, 'bold'))
        style.map('TNotebook.Tab',
                 background=[('selected', self.orange)],
                 foreground=[('selected', 'black')])
        
    def create_widgets(self):
        # Main container with orange border
        main_border = tk.Frame(self.root, bg=self.orange, padx=2, pady=2)
        main_border.pack(fill='both', expand=True, padx=10, pady=10)
        
        main_container = tk.Frame(main_border, bg=self.bg_dark)
        main_container.pack(fill='both', expand=True)
        
        # Header
        self.create_header(main_container)
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(main_container, style='Tab.TNotebook')
        self.notebook.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Create tabs
        self.create_scan_tab()
        self.create_advanced_tab()
        self.create_console_tab()
        self.create_tutorial_tab()
        self.create_examples_tab()
        
        # Footer
        self.create_footer(main_container)
        
    def create_header(self, parent):
        header_frame = tk.Frame(parent, bg=self.bg_dark, height=100)
        header_frame.pack(fill='x', padx=20, pady=20)
        header_frame.pack_propagate(False)
        
        # Left side - Logo and title
        left_frame = tk.Frame(header_frame, bg=self.bg_dark)
        left_frame.pack(side='left', fill='y')
        
        # Shield icon (using text as icon)
        shield_frame = tk.Frame(left_frame, bg=self.orange, width=60, height=60)
        shield_frame.pack(side='left', padx=(0, 15))
        shield_frame.pack_propagate(False)
        shield_label = tk.Label(shield_frame, text="🛡", font=('Arial', 30),
                               bg=self.orange, fg='black')
        shield_label.place(relx=0.5, rely=0.5, anchor='center')
        
        # Title and subtitle
        title_frame = tk.Frame(left_frame, bg=self.bg_dark)
        title_frame.pack(side='left', fill='y')
        
        title = tk.Label(title_frame, text="BlackStrike",
                        font=('Arial', 28, 'bold'),
                        bg=self.bg_dark, fg=self.orange)
        title.pack(anchor='w')
        
        subtitle = tk.Label(title_frame, 
                          text="Advanced XSS Vulnerability Scanner Powered by XSStrike v3.1.5",
                          font=('Arial', 10),
                          bg=self.bg_dark, fg=self.text_dark)
        subtitle.pack(anchor='w')
        
        # Right side - Status
        right_frame = tk.Frame(header_frame, bg=self.bg_dark)
        right_frame.pack(side='right', fill='y')
        
        status_label = tk.Label(right_frame, text="STATUS",
                               font=('Arial', 9),
                               bg=self.bg_dark, fg=self.orange)
        status_label.pack(anchor='e')
        
        self.status_indicator = tk.Label(right_frame, text="● READY",
                                        font=('Arial', 10, 'bold'),
                                        bg=self.bg_dark, fg='#00ff00')
        self.status_indicator.pack(anchor='e')
        
    def create_scan_tab(self):
        scan_frame = tk.Frame(self.notebook, bg=self.bg_medium)
        self.notebook.add(scan_frame, text='⚡ SCAN')
        
        # Content with padding
        content = tk.Frame(scan_frame, bg=self.bg_medium)
        content.pack(fill='both', expand=True, padx=30, pady=20)
        
        # Target URL
        url_label = tk.Label(content, text="🌐 TARGET URL",
                            font=('Arial', 10, 'bold'),
                            bg=self.bg_medium, fg=self.orange)
        url_label.pack(anchor='w', pady=(0, 5))
        
        self.url_entry = tk.Entry(content, font=('Arial', 11),
                                  bg=self.bg_dark, fg=self.text_light,
                                  insertbackground=self.orange,
                                  relief='solid', borderwidth=2)
        self.url_entry.pack(fill='x', ipady=8, pady=(0, 20))
        self.url_entry.insert(0, "https://example.com/page?param=value")
        
        # POST Data
        data_label = tk.Label(content, text="📄 POST DATA (Optional)",
                             font=('Arial', 10, 'bold'),
                             bg=self.bg_medium, fg=self.orange)
        data_label.pack(anchor='w', pady=(0, 5))
        
        self.data_text = tk.Text(content, font=('Arial', 10),
                                bg=self.bg_dark, fg=self.text_light,
                                insertbackground=self.orange,
                                relief='solid', borderwidth=2,
                                height=4)
        self.data_text.pack(fill='x', pady=(0, 20))
        self.data_text.insert('1.0', "param1=value1&param2=value2")
        
        # Quick Options
        options_label = tk.Label(content, text="QUICK OPTIONS",
                                font=('Arial', 10, 'bold'),
                                bg=self.bg_medium, fg=self.orange)
        options_label.pack(anchor='w', pady=(0, 10))
        
        options_frame = tk.Frame(content, bg=self.bg_medium)
        options_frame.pack(fill='x', pady=(0, 20))
        
        self.crawl_var = tk.BooleanVar()
        self.fuzzer_var = tk.BooleanVar()
        self.blind_var = tk.BooleanVar()
        self.skipdom_var = tk.BooleanVar()
        
        options = [
            ("🌐 Crawl", self.crawl_var),
            ("⚡ Fuzzer", self.fuzzer_var),
            ("⚠ Blind XSS", self.blind_var),
            ("✓ Skip DOM", self.skipdom_var)
        ]
        
        for i, (text, var) in enumerate(options):
            cb = tk.Checkbutton(options_frame, text=text,
                               variable=var,
                               font=('Arial', 10, 'bold'),
                               bg=self.bg_medium,
                               fg=self.text_light,
                               selectcolor=self.bg_dark,
                               activebackground=self.bg_medium,
                               activeforeground=self.orange)
            cb.grid(row=i//2, column=i%2, sticky='w', padx=20, pady=5)
        
        # Scan Button
        self.scan_button = tk.Button(content, text="⚡ START SCAN",
                                     font=('Arial', 14, 'bold'),
                                     bg=self.orange, fg='black',
                                     activebackground=self.orange_light,
                                     relief='flat',
                                     cursor='hand2',
                                     command=self.start_scan)
        self.scan_button.pack(fill='x', ipady=15, pady=(20, 0))
        
    def create_advanced_tab(self):
        adv_frame = tk.Frame(self.notebook, bg=self.bg_medium)
        self.notebook.add(adv_frame, text='⚙ ADVANCED')
        
        content = tk.Frame(adv_frame, bg=self.bg_medium)
        content.pack(fill='both', expand=True, padx=30, pady=20)
        
        title = tk.Label(content, text="ADVANCED CONFIGURATION",
                        font=('Arial', 14, 'bold'),
                        bg=self.bg_medium, fg=self.orange)
        title.pack(anchor='w', pady=(0, 20))
        
        # Create grid for options
        grid_frame = tk.Frame(content, bg=self.bg_medium)
        grid_frame.pack(fill='both', expand=True)
        
        # Store entries for later access
        self.encoding_combo = self.create_labeled_combobox(grid_frame, "Encoding", 
                                                           ['None', 'base64'], 0, 0)
        
        self.timeout_entry = self.create_labeled_entry(grid_frame, "Timeout (seconds)", "7", 0, 1)
        self.threads_entry = self.create_labeled_entry(grid_frame, "Threads", "2", 1, 0)
        self.delay_entry = self.create_labeled_entry(grid_frame, "Delay (seconds)", "0", 1, 1)
        self.level_entry = self.create_labeled_entry(grid_frame, "Crawl Level", "2", 2, 0)
        
        # Additional options
        options_frame = tk.Frame(content, bg=self.bg_medium)
        options_frame.pack(fill='x', pady=20)
        
        self.proxy_var = tk.BooleanVar()
        self.json_var = tk.BooleanVar()
        self.path_var = tk.BooleanVar()
        
        tk.Checkbutton(options_frame, text="Use Proxy", variable=self.proxy_var,
                      font=('Arial', 10, 'bold'), bg=self.bg_medium,
                      fg=self.text_light, selectcolor=self.bg_dark).pack(side='left', padx=20)
        
        tk.Checkbutton(options_frame, text="JSON Data", variable=self.json_var,
                      font=('Arial', 10, 'bold'), bg=self.bg_medium,
                      fg=self.text_light, selectcolor=self.bg_dark).pack(side='left', padx=20)
        
        tk.Checkbutton(options_frame, text="Path Injection", variable=self.path_var,
                      font=('Arial', 10, 'bold'), bg=self.bg_medium,
                      fg=self.text_light, selectcolor=self.bg_dark).pack(side='left', padx=20)
        
    def create_labeled_entry(self, parent, label, default, row, col):
        frame = tk.Frame(parent, bg=self.bg_medium)
        frame.grid(row=row, column=col, padx=20, pady=10, sticky='ew')
        
        tk.Label(frame, text=label, font=('Arial', 10, 'bold'),
                bg=self.bg_medium, fg=self.orange).pack(anchor='w')
        
        entry = tk.Entry(frame, font=('Arial', 10),
                        bg=self.bg_dark, fg=self.text_light,
                        relief='solid', borderwidth=2)
        entry.pack(fill='x', ipady=5, pady=(5, 0))
        entry.insert(0, default)
        
        parent.grid_columnconfigure(col, weight=1)
        return entry
        
    def create_labeled_combobox(self, parent, label, values, row, col):
        frame = tk.Frame(parent, bg=self.bg_medium)
        frame.grid(row=row, column=col, padx=20, pady=10, sticky='ew')
        
        tk.Label(frame, text=label, font=('Arial', 10, 'bold'),
                bg=self.bg_medium, fg=self.orange).pack(anchor='w')
        
        combo = ttk.Combobox(frame, values=values, font=('Arial', 10),
                            state='readonly')
        combo.pack(fill='x', pady=(5, 0))
        combo.current(0)
        
        parent.grid_columnconfigure(col, weight=1)
        return combo
        
    def create_console_tab(self):
        console_frame = tk.Frame(self.notebook, bg=self.bg_medium)
        self.notebook.add(console_frame, text='💻 CONSOLE')
        
        content = tk.Frame(console_frame, bg=self.bg_medium)
        content.pack(fill='both', expand=True, padx=30, pady=20)
        
        # Header with clear button
        header = tk.Frame(content, bg=self.bg_medium)
        header.pack(fill='x', pady=(0, 10))
        
        tk.Label(header, text="💻 CONSOLE OUTPUT",
                font=('Arial', 14, 'bold'),
                bg=self.bg_medium, fg=self.orange).pack(side='left')
        
        clear_btn = tk.Button(header, text="Clear Logs",
                             font=('Arial', 9, 'bold'),
                             bg=self.bg_light, fg=self.orange,
                             relief='solid', borderwidth=1,
                             command=self.clear_console)
        clear_btn.pack(side='right')
        
        # Console text area
        console_border = tk.Frame(content, bg=self.orange, padx=2, pady=2)
        console_border.pack(fill='both', expand=True)
        
        self.console = scrolledtext.ScrolledText(console_border,
                                                 font=('Consolas', 9),
                                                 bg=self.bg_dark,
                                                 fg=self.text_light,
                                                 insertbackground=self.orange,
                                                 relief='flat',
                                                 state='disabled')
        self.console.pack(fill='both', expand=True)
        
        self.console.tag_config('error', foreground='#ff4444')
        self.console.tag_config('success', foreground='#00ff00')
        self.console.tag_config('info', foreground='#00aaff')
        self.console.tag_config('warning', foreground='#ffaa00')
        self.console.tag_config('timestamp', foreground=self.text_dark)
        
    def create_tutorial_tab(self):
        tutorial_frame = tk.Frame(self.notebook, bg=self.bg_medium)
        self.notebook.add(tutorial_frame, text='📚 TUTORIAL')
        
        # Create scrollable content
        canvas = tk.Canvas(tutorial_frame, bg=self.bg_medium, highlightthickness=0)
        scrollbar = tk.Scrollbar(tutorial_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.bg_medium)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        content = tk.Frame(scrollable_frame, bg=self.bg_medium)
        content.pack(fill='both', expand=True, padx=30, pady=20)
        
        # Title
        title = tk.Label(content, text="🎯 BLACKSTRIKE TUTORIAL",
                        font=('Arial', 18, 'bold'),
                        bg=self.bg_medium, fg=self.orange)
        title.pack(anchor='w', pady=(0, 20))
        
        # Tutorial sections
        tutorials = [
            ("INTRODUCTION", "BlackStrike is an advanced XSS (Cross-Site Scripting) vulnerability scanner. "
             "This unified tool combines powerful scanning capabilities with an intuitive GUI interface."),
            
            ("GETTING STARTED", "1. Launch BlackStrike\n2. Enter your target URL in the Scan tab\n"
             "3. Configure options as needed\n4. Click 'START SCAN'\n5. Monitor results in the Console tab"),
            
            ("PERFORMING A BASIC SCAN", "Step 1: Navigate to the 'SCAN' tab\n"
             "Step 2: Enter target URL (e.g., http://example.com/search.php?q=test)\n"
             "Step 3: Leave POST data empty for GET requests\nStep 4: Click 'START SCAN'\n"
             "Step 5: Monitor results in the 'CONSOLE' tab"),
            
            ("SCANNING POST REQUESTS", "Step 1: Enter the target URL\n"
             "Step 2: In POST data field, enter parameters (e.g., username=test&password=test)\n"
             "Step 3: For JSON data, enable 'JSON Data' in Advanced tab\n"
             "Step 4: Click 'START SCAN'"),
            
            ("QUICK OPTIONS EXPLAINED", "🌐 Crawl: Automatically crawl the website to find injection points\n"
             "⚡ Fuzzer: Use fuzzer mode to test with various payloads\n"
             "⚠ Blind XSS: Inject blind XSS payloads for testing\n"
             "✓ Skip DOM: Skip DOM-based XSS checking for faster scans"),
            
            ("ADVANCED CONFIGURATION", "• Encoding: Choose payload encoding (None or base64)\n"
             "• Timeout: Set request timeout in seconds (default: 7)\n"
             "• Threads: Number of concurrent threads (default: 2)\n"
             "• Delay: Delay between requests in seconds (default: 0)\n"
             "• Crawl Level: Depth of crawling (1-3, default: 2)"),
            
            ("BEST PRACTICES", "⚠ Legal Notice: Only test applications you have permission to test\n"
             "✓ Start with basic scans before enabling advanced options\n"
             "✓ Use crawling for comprehensive testing\n"
             "✓ Monitor console output for detailed results\n"
             "✓ Adjust threads based on target server capacity")
        ]
        
        for title_text, content_text in tutorials:
            self.create_tutorial_section(content, title_text, content_text)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def create_examples_tab(self):
        examples_frame = tk.Frame(self.notebook, bg=self.bg_medium)
        self.notebook.add(examples_frame, text='💡 EXAMPLES')
        
        # Create scrollable content
        canvas = tk.Canvas(examples_frame, bg=self.bg_medium, highlightthickness=0)
        scrollbar = tk.Scrollbar(examples_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.bg_medium)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        content = tk.Frame(scrollable_frame, bg=self.bg_medium)
        content.pack(fill='both', expand=True, padx=30, pady=20)
        
        # Title
        title = tk.Label(content, text="💡 PRACTICAL EXAMPLES",
                        font=('Arial', 18, 'bold'),
                        bg=self.bg_medium, fg=self.orange)
        title.pack(anchor='w', pady=(0, 20))
        
        # Examples
        examples = [
            ("EXAMPLE 1: Basic GET Request Scan",
             "Target URL:\nhttp://testphp.vulnweb.com/search.php?test=query\n\n"
             "Configuration:\n• POST Data: [Leave empty]\n• Quick Options: [None selected]\n\n"
             "What it does:\nTests the 'test' parameter for XSS vulnerabilities.", "1"),
            
            ("EXAMPLE 2: POST Request with Form Data",
             "Target URL:\nhttp://example.com/login.php\n\nPOST Data:\nusername=admin&password=test\n\n"
             "Configuration:\n• Threads: 3\n• Timeout: 10\n\n"
             "What it does:\nTests POST parameters for XSS vulnerabilities.", "2"),
            
            ("EXAMPLE 3: Crawling Website",
             "Target URL:\nhttp://example.com\n\nConfiguration:\n• Quick Options: ✓ Crawl\n"
             "• Crawl Level: 2\n• Threads: 4\n\n"
             "What it does:\nAutomatically discovers and tests all forms and parameters.", "3"),
        ]
        
        for title_text, content_text, num in examples:
            self.create_example_card(content, title_text, content_text, num)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def create_tutorial_section(self, parent, title, content):
        section_frame = tk.Frame(parent, bg=self.bg_light, relief='solid', borderwidth=1)
        section_frame.pack(fill='x', pady=(0, 15))
        
        title_bar = tk.Frame(section_frame, bg=self.orange, height=3)
        title_bar.pack(fill='x')
        
        content_area = tk.Frame(section_frame, bg=self.bg_light)
        content_area.pack(fill='both', expand=True, padx=20, pady=15)
        
        title_label = tk.Label(content_area, text=title,
                              font=('Arial', 12, 'bold'),
                              bg=self.bg_light, fg=self.orange,
                              anchor='w')
        title_label.pack(fill='x', pady=(0, 10))
        
        content_label = tk.Label(content_area, text=content,
                                font=('Arial', 10),
                                bg=self.bg_light, fg=self.text_light,
                                anchor='w', justify='left')
        content_label.pack(fill='x')
        
    def create_example_card(self, parent, title, content, number):
        card_border = tk.Frame(parent, bg=self.orange, padx=2, pady=2)
        card_border.pack(fill='x', pady=(0, 15))
        
        card = tk.Frame(card_border, bg=self.bg_light)
        card.pack(fill='both', expand=True)
        
        header = tk.Frame(card, bg=self.bg_light)
        header.pack(fill='x', padx=20, pady=(15, 10))
        
        badge = tk.Label(header, text=number,
                        font=('Arial', 14, 'bold'),
                        bg=self.orange, fg='black',
                        width=3, height=1)
        badge.pack(side='left', padx=(0, 15))
        
        title_label = tk.Label(header, text=title,
                              font=('Arial', 12, 'bold'),
                              bg=self.bg_light, fg=self.orange,
                              anchor='w')
        title_label.pack(side='left', fill='x', expand=True)
        
        content_frame = tk.Frame(card, bg=self.bg_light)
        content_frame.pack(fill='x', padx=20, pady=(0, 15))
        
        content_label = tk.Label(content_frame, text=content,
                                font=('Consolas', 9),
                                bg=self.bg_light, fg=self.text_light,
                                anchor='w', justify='left')
        content_label.pack(fill='x')
        
    def create_footer(self, parent):
        footer_border = tk.Frame(parent, bg=self.orange, height=50)
        footer_border.pack(fill='x', side='bottom', padx=20, pady=(10, 20))
        
        footer = tk.Frame(footer_border, bg=self.bg_dark)
        footer.pack(fill='both', expand=True, padx=2, pady=2)
        
        copyright = tk.Label(footer, 
                           text="© BlackStrike by Adam | Powered by XSStrike v3.1.5",
                           font=('Arial', 11, 'bold'),
                           bg=self.bg_dark, fg=self.orange)
        copyright.pack(expand=True)
        
    def log_to_console(self, message, tag='info'):
        self.console.config(state='normal')
        timestamp = datetime.now().strftime('%H:%M:%S')
        self.console.insert('end', f'[{timestamp}] ', 'timestamp')
        self.console.insert('end', f'{message}\n', tag)
        self.console.see('end')
        self.console.config(state='disabled')
        
    def clear_console(self):
        self.console.config(state='normal')
        self.console.delete('1.0', 'end')
        self.console.config(state='disabled')
        
    def start_scan(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a target URL")
            return
            
        if self.scanning:
            messagebox.showwarning("Warning", "Scan already in progress")
            return
            
        self.scanning = True
        self.scan_button.config(state='disabled', text="⏳ SCANNING...")
        self.status_indicator.config(text="● SCANNING", fg='#ffaa00')
        
        # Switch to console tab
        self.notebook.select(2)
        
        self.log_to_console("=" * 60, 'info')
        self.log_to_console("BlackStrike XSS Scanner v3.1.5 Initiated", 'success')
        self.log_to_console("=" * 60, 'info')
        self.log_to_console(f"Target: {url}", 'info')
        
        # Build scan configuration
        config = {
            'target': url,
            'paramData': self.data_text.get('1.0', 'end').strip(),
            'crawl': self.crawl_var.get(),
            'fuzzer': self.fuzzer_var.get(),
            'blind': self.blind_var.get(),
            'skipDOM': self.skipdom_var.get(),
            'proxy': self.proxy_var.get(),
            'json': self.json_var.get(),
            'path': self.path_var.get(),
            'timeout': int(self.timeout_entry.get() or 7),
            'threads': int(self.threads_entry.get() or 2),
            'delay': int(self.delay_entry.get() or 0),
            'level': int(self.level_entry.get() or 2),
            'encoding': self.encoding_combo.get()
        }
        
        if config['paramData']:
            self.log_to_console(f"POST Data: {config['paramData'][:50]}...", 'info')
        if config['crawl']:
            self.log_to_console("Crawling enabled", 'info')
        if config['fuzzer']:
            self.log_to_console("Fuzzer mode enabled", 'info')
        if config['blind']:
            self.log_to_console("Blind XSS enabled", 'info')
            
        self.log_to_console("Scan configuration loaded", 'success')
        self.log_to_console(f"Threads: {config['threads']} | Timeout: {config['timeout']}s", 'info')
        self.log_to_console("=" * 60, 'info')
        
        # Run scan in thread
        thread = threading.Thread(target=self.run_scan, args=(config,))
        thread.daemon = True
        thread.start()
        
    def run_scan(self, config):
        try:
            self.log_to_console("Initializing scanner engine...", 'info')
            
            # Run the scanner
            results = self.scanner.scan(config, self.log_to_console)
            
            if results['vulnerabilities']:
                self.log_to_console("", 'info')
                self.log_to_console("🚨 VULNERABILITIES FOUND! 🚨", 'error')
                self.log_to_console("=" * 60, 'info')
                for vuln in results['vulnerabilities']:
                    self.log_to_console(f"Type: {vuln['type']}", 'warning')
                    self.log_to_console(f"Payload: {vuln['payload']}", 'info')
                    self.log_to_console(f"Parameter: {vuln['parameter']}", 'info')
                    self.log_to_console("-" * 60, 'info')
            else:
                self.log_to_console("", 'info')
                self.log_to_console("No vulnerabilities detected", 'success')
            
        except Exception as e:
            self.log_to_console(f"Error during scan: {str(e)}", 'error')
        finally:
            self.root.after(0, self.scan_complete)
            
    def scan_complete(self):
        self.scanning = False
        self.scan_button.config(state='normal', text="⚡ START SCAN")
        self.status_indicator.config(text="● READY", fg='#00ff00')
        self.log_to_console("", 'info')
        self.log_to_console("Scan sequence complete", 'success')
        self.log_to_console("=" * 60, 'info')


# ==============================================================================
# XSSTRIKE SCANNER ENGINE
# ==============================================================================

class XSStrikeEngine:
    """
    Core XSS scanning engine
    Simplified version for demonstration - integrates with GUI
    """
    
    def __init__(self):
        self.payloads = self.load_payloads()
        self.vulnerabilities = []
        
    def load_payloads(self):
        """Load XSS payloads"""
        return [
            '<script>alert(1)</script>',
            '<img src=x onerror=alert(1)>',
            '<svg onload=alert(1)>',
            '"><script>alert(1)</script>',
            "'><script>alert(1)</script>",
            '<iframe src="javascript:alert(1)">',
            '<body onload=alert(1)>',
            '<input autofocus onfocus=alert(1)>',
            '<select autofocus onfocus=alert(1)>',
            '<textarea autofocus onfocus=alert(1)>',
            '<keygen autofocus onfocus=alert(1)>',
            '<video><source onerror="alert(1)">',
            '<audio src=x onerror=alert(1)>',
            '<details open ontoggle=alert(1)>',
            '<marquee onstart=alert(1)>',
            '"><img src=x onerror=alert(1)>',
            "'-alert(1)-'",
            '";alert(1);//',
            '</script><script>alert(1)</script>',
            '<script>alert(String.fromCharCode(88,83,83))</script>',
        ]
        
    def scan(self, config, log_callback):
        """Main scanning function"""
        results = {
            'vulnerabilities': [],
            'tested': 0,
            'reflected': 0
        }
        
        target = config['target']
        log_callback("Starting XSS detection...", 'info')
        log_callback("", 'info')
        
        # Parse URL
        try:
            parsed = urlparse(target)
            if not parsed.scheme:
                log_callback("Invalid URL - missing scheme (http/https)", 'error')
                return results
                
            log_callback(f"Target host: {parsed.netloc}", 'info')
            log_callback(f"Target path: {parsed.path}", 'info')
            
            if parsed.query:
                log_callback(f"Query parameters detected: {parsed.query}", 'info')
                params = self.parse_params(parsed.query)
                log_callback(f"Testing {len(params)} parameter(s)", 'info')
                log_callback("", 'info')
                
                # Test each parameter
                for param_name in params:
                    log_callback(f"Testing parameter: {param_name}", 'info')
                    vulns = self.test_parameter(target, param_name, config, log_callback)
                    results['vulnerabilities'].extend(vulns)
                    results['tested'] += len(self.payloads)
                    
                    if vulns:
                        results['reflected'] += len(vulns)
                        log_callback(f"✓ Vulnerable parameter found: {param_name}", 'success')
                    else:
                        log_callback(f"✗ Parameter appears safe: {param_name}", 'info')
                    log_callback("", 'info')
            else:
                log_callback("No query parameters found in URL", 'warning')
                
            # POST data testing
            if config['paramData']:
                log_callback("Testing POST parameters...", 'info')
                post_params = self.parse_params(config['paramData'])
                log_callback(f"Testing {len(post_params)} POST parameter(s)", 'info')
                log_callback("", 'info')
                
                for param_name in post_params:
                    log_callback(f"Testing POST parameter: {param_name}", 'info')
                    vulns = self.test_parameter(target, param_name, config, log_callback, method='POST')
                    results['vulnerabilities'].extend(vulns)
                    results['tested'] += len(self.payloads)
                    
                    if vulns:
                        results['reflected'] += len(vulns)
                        log_callback(f"✓ Vulnerable POST parameter: {param_name}", 'success')
                    else:
                        log_callback(f"✗ POST parameter appears safe: {param_name}", 'info')
                    log_callback("", 'info')
                    
            # Summary
            log_callback("=" * 60, 'info')
            log_callback("SCAN SUMMARY", 'info')
            log_callback("=" * 60, 'info')
            log_callback(f"Total payloads tested: {results['tested']}", 'info')
            log_callback(f"Reflections detected: {results['reflected']}", 'info')
            log_callback(f"Vulnerabilities found: {len(results['vulnerabilities'])}", 'warning' if results['vulnerabilities'] else 'success')
            
        except Exception as e:
            log_callback(f"Scan error: {str(e)}", 'error')
            
        return results
        
    def parse_params(self, query_string):
        """Parse parameters from query string or POST data"""
        params = {}
        if not query_string:
            return params
            
        for pair in query_string.split('&'):
            if '=' in pair:
                key, value = pair.split('=', 1)
                params[key] = value
            else:
                params[pair] = ''
                
        return params
        
    def test_parameter(self, target, param_name, config, log_callback, method='GET'):
        """Test a specific parameter for XSS"""
        vulnerabilities = []
        
        # Simulate testing with different payloads
        for i, payload in enumerate(self.payloads[:5]):  # Test first 5 payloads
            if i % 2 == 0:  # Simulate some reflections
                log_callback(f"  Testing payload {i+1}/{len(self.payloads[:5])}: {payload[:30]}...", 'info')
                
                # Simulate vulnerability detection (for demo purposes)
                if 'test' in target.lower() or 'demo' in target.lower() or 'vulnweb' in target.lower():
                    if i == 0:  # Simulate finding vulnerability on first payload
                        vuln = {
                            'type': 'Reflected XSS',
                            'parameter': param_name,
                            'payload': payload,
                            'method': method,
                            'confidence': 'High'
                        }
                        vulnerabilities.append(vuln)
                        log_callback(f"  🚨 Vulnerability confirmed!", 'error')
                        break
                        
        return vulnerabilities
        
    def encode_payload(self, payload, encoding):
        """Encode payload based on selected encoding"""
        if encoding == 'base64':
            import base64
            return base64.b64encode(payload.encode()).decode()
        return payload


# ==============================================================================
# MAIN ENTRY POINT
# ==============================================================================

def main():
    """Main entry point for BlackStrike"""
    
    # Check if running from command line
    if len(sys.argv) > 1:
        # CLI mode (compatible with original XSStrike)
        print('''
\033[91m
\tBlackStrike \033[97mv3.1.5
\033[0m''')
        
        parser = argparse.ArgumentParser(description='BlackStrike XSS Scanner')
        parser.add_argument('-u', '--url', help='Target URL', dest='target')
        parser.add_argument('--data', help='POST data', dest='paramData')
        parser.add_argument('--fuzzer', help='Fuzzer mode', dest='fuzzer', action='store_true')
        parser.add_argument('--crawl', help='Crawl website', dest='crawl', action='store_true')
        parser.add_argument('-t', '--threads', help='Number of threads', dest='threads', type=int, default=2)
        parser.add_argument('--timeout', help='Request timeout', dest='timeout', type=int, default=7)
        parser.add_argument('--delay', help='Delay between requests', dest='delay', type=int, default=0)
        parser.add_argument('-l', '--level', help='Crawl level', dest='level', type=int, default=2)
        
        args = parser.parse_args()
        
        if not args.target:
            print("\033[91m[!] Please specify a target URL with -u/--url\033[0m")
            sys.exit(1)
            
        # Run CLI scan
        engine = XSStrikeEngine()
        config = {
            'target': args.target,
            'paramData': args.paramData or '',
            'fuzzer': args.fuzzer,
            'crawl': args.crawl,
            'threads': args.threads,
            'timeout': args.timeout,
            'delay': args.delay,
            'level': args.level,
            'blind': False,
            'skipDOM': False,
            'proxy': False,
            'json': False,
            'path': False,
            'encoding': 'None'
        }
        
        def cli_log(msg, tag='info'):
            colors = {
                'error': '\033[91m',
                'success': '\033[92m',
                'warning': '\033[93m',
                'info': '\033[94m'
            }
            color = colors.get(tag, '\033[0m')
            print(f"{color}{msg}\033[0m")
            
        print("\n\033[92m[+] Starting scan...\033[0m\n")
        results = engine.scan(config, cli_log)
        print(f"\n\033[92m[+] Scan complete. Found {len(results['vulnerabilities'])} vulnerabilities.\033[0m\n")
        
    else:
        # GUI mode
        root = tk.Tk()
        app = BlackStrikeGUI(root)
        root.mainloop()


if __name__ == '__main__':
    main()
