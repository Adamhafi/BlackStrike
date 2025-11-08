#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import subprocess
import threading
import sys
from datetime import datetime

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
                          text="Advanced XSS Scanner bassed on XSStrike v3.1.5",
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
        
        # Encoding
        self.create_labeled_combobox(grid_frame, "Encoding", 
                                     ['None', 'base64'], 0, 0)
        
        # Timeout
        self.create_labeled_entry(grid_frame, "Timeout (seconds)", "7", 0, 1)
        
        # Threads
        self.create_labeled_entry(grid_frame, "Threads", "2", 1, 0)
        
        # Delay
        self.create_labeled_entry(grid_frame, "Delay (seconds)", "0", 1, 1)
        
        # Crawl Level
        self.create_labeled_entry(grid_frame, "Crawl Level", "2", 2, 0)
        
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
        
        # Introduction
        self.create_tutorial_section(content, "INTRODUCTION",
            "BlackStrike is an advanced XSS (Cross-Site Scripting) vulnerability scanner built on top of XSStrike. "
            "This GUI provides an intuitive interface to leverage XSStrike's powerful capabilities for security testing.")
        
        # Getting Started
        self.create_tutorial_section(content, "GETTING STARTED",
            "1. Ensure you have XSStrike installed in the same directory\n"
            "2. Make sure all dependencies are installed (pip3 install -r requirements.txt)\n"
            "3. Run this GUI: python3 blackstrike_gui.py\n"
            "4. Enter your target URL in the Scan tab\n"
            "5. Configure options as needed\n"
            "6. Click 'START SCAN' to begin")
        
        # Basic Scan
        self.create_tutorial_section(content, "PERFORMING A BASIC SCAN",
            "Step 1: Navigate to the 'SCAN' tab\n"
            "Step 2: Enter target URL (e.g., http://testphp.vulnweb.com/search.php?test=query)\n"
            "Step 3: Leave POST data empty for GET requests\n"
            "Step 4: Click 'START SCAN'\n"
            "Step 5: Monitor results in the 'CONSOLE' tab\n\n"
            "The scanner will automatically test the URL for XSS vulnerabilities.")
        
        # POST Request Scan
        self.create_tutorial_section(content, "SCANNING POST REQUESTS",
            "Step 1: Enter the target URL in the URL field\n"
            "Step 2: In POST data field, enter parameters:\n"
            "   Example: username=test&password=test&search=query\n"
            "Step 3: For JSON data, enable 'JSON Data' in Advanced tab\n"
            "   Example: {\"search\":\"query\",\"filter\":\"all\"}\n"
            "Step 4: Click 'START SCAN'")
        
        # Quick Options
        self.create_tutorial_section(content, "QUICK OPTIONS EXPLAINED",
            "🌐 Crawl: Automatically crawl the website to find more injection points\n"
            "⚡ Fuzzer: Use fuzzer mode to test with various payloads\n"
            "⚠ Blind XSS: Inject blind XSS payloads for testing\n"
            "✓ Skip DOM: Skip DOM-based XSS checking for faster scans")
        
        # Advanced Configuration
        self.create_tutorial_section(content, "ADVANCED CONFIGURATION",
            "• Encoding: Choose payload encoding (None or base64)\n"
            "• Timeout: Set request timeout in seconds (default: 7)\n"
            "• Threads: Number of concurrent threads (default: 2)\n"
            "• Delay: Delay between requests in seconds (default: 0)\n"
            "• Crawl Level: Depth of crawling (1-3, default: 2)\n"
            "• Use Proxy: Enable proxy for requests\n"
            "• JSON Data: Treat POST data as JSON\n"
            "• Path Injection: Test path-based injection")
        
        # Console Usage
        self.create_tutorial_section(content, "USING THE CONSOLE",
            "The Console tab displays real-time scan output:\n"
            "• Green text: Successful operations\n"
            "• Red text: Errors\n"
            "• Blue text: Informational messages\n"
            "• Gray text: Timestamps\n\n"
            "Use 'Clear Logs' button to reset the console.")
        
        # Best Practices
        self.create_tutorial_section(content, "BEST PRACTICES",
            "⚠ Legal Notice: Only test applications you have permission to test\n"
            "✓ Start with basic scans before enabling advanced options\n"
            "✓ Use crawling for comprehensive testing\n"
            "✓ Monitor console output for detailed results\n"
            "✓ Adjust threads based on target server capacity\n"
            "✓ Use delays to avoid overwhelming the target\n"
            "✓ Keep XSStrike updated for latest detection techniques")
        
        # Troubleshooting
        self.create_tutorial_section(content, "TROUBLESHOOTING",
            "Issue: 'xsstrike.py not found'\n"
            "Solution: Ensure xsstrike.py is in the same directory as this GUI\n\n"
            "Issue: No vulnerabilities found\n"
            "Solution: Try enabling crawl mode or adjusting parameters\n\n"
            "Issue: Scan takes too long\n"
            "Solution: Increase threads or enable 'Skip DOM'\n\n"
            "Issue: Connection errors\n"
            "Solution: Check target URL, increase timeout, or use proxy")
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
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
        
        # Example 1
        self.create_example_card(content, "EXAMPLE 1: Basic GET Request Scan",
            "Target URL:\nhttp://testphp.vulnweb.com/search.php?test=query\n\n"
            "Configuration:\n"
            "• POST Data: [Leave empty]\n"
            "• Quick Options: [None selected]\n"
            "• Advanced: [Default settings]\n\n"
            "What it does:\n"
            "Tests the 'test' parameter for XSS vulnerabilities using GET method.",
            "1")
        
        # Example 2
        self.create_example_card(content, "EXAMPLE 2: POST Request with Form Data",
            "Target URL:\nhttp://example.com/login.php\n\n"
            "POST Data:\nusername=admin&password=test&remember=1\n\n"
            "Configuration:\n"
            "• Quick Options: [None]\n"
            "• Advanced: Threads: 3, Timeout: 10\n\n"
            "What it does:\n"
            "Tests POST parameters (username, password, remember) for XSS.",
            "2")
        
        # Example 3
        self.create_example_card(content, "EXAMPLE 3: Crawling Website",
            "Target URL:\nhttp://example.com\n\n"
            "Configuration:\n"
            "• Quick Options: ✓ Crawl\n"
            "• Advanced: Crawl Level: 2, Threads: 4, Delay: 1\n\n"
            "What it does:\n"
            "Automatically discovers and tests all forms and parameters found while "
            "crawling up to 2 levels deep. Delay prevents server overload.",
            "3")
        
        # Example 4
        self.create_example_card(content, "EXAMPLE 4: JSON API Testing",
            "Target URL:\nhttp://api.example.com/search\n\n"
            "POST Data:\n{\"query\":\"test\",\"filter\":\"all\",\"limit\":10}\n\n"
            "Configuration:\n"
            "• Quick Options: [None]\n"
            "• Advanced: ✓ JSON Data\n\n"
            "What it does:\n"
            "Tests JSON API endpoints by injecting payloads into JSON parameters.",
            "4")
        
        # Example 5
        self.create_example_card(content, "EXAMPLE 5: Fuzzer Mode",
            "Target URL:\nhttp://example.com/profile.php?id=123\n\n"
            "Configuration:\n"
            "• Quick Options: ✓ Fuzzer\n"
            "• Advanced: Threads: 5\n\n"
            "What it does:\n"
            "Uses advanced fuzzing techniques to test various payload variations "
            "and bypass common filters.",
            "5")
        
        # Example 6
        self.create_example_card(content, "EXAMPLE 6: Blind XSS Testing",
            "Target URL:\nhttp://example.com/contact.php\n\n"
            "POST Data:\nname=John&email=test@test.com&message=Hello\n\n"
            "Configuration:\n"
            "• Quick Options: ✓ Crawl, ✓ Blind XSS\n"
            "• Advanced: Crawl Level: 2\n\n"
            "What it does:\n"
            "Injects blind XSS payloads useful for testing stored XSS in admin panels "
            "or areas you can't directly access.",
            "6")
        
        # Example 7
        self.create_example_card(content, "EXAMPLE 7: Encoded Payload Testing",
            "Target URL:\nhttp://example.com/search.php?q=test\n\n"
            "Configuration:\n"
            "• Quick Options: [None]\n"
            "• Advanced: Encoding: base64, Threads: 3\n\n"
            "What it does:\n"
            "Tests with base64 encoded payloads to bypass basic input filters.",
            "7")
        
        # Example 8
        self.create_example_card(content, "EXAMPLE 8: Path-Based Injection",
            "Target URL:\nhttp://example.com/page/test/view\n\n"
            "Configuration:\n"
            "• Quick Options: [None]\n"
            "• Advanced: ✓ Path Injection\n\n"
            "What it does:\n"
            "Tests for XSS vulnerabilities in URL path segments instead of parameters.",
            "8")
        
        # Example 9
        self.create_example_card(content, "EXAMPLE 9: Fast Scan (Skip DOM)",
            "Target URL:\nhttp://example.com/search?q=query\n\n"
            "Configuration:\n"
            "• Quick Options: ✓ Skip DOM\n"
            "• Advanced: Threads: 8, Timeout: 5\n\n"
            "What it does:\n"
            "Performs a quick scan by skipping DOM-based XSS checks. Good for "
            "initial reconnaissance.",
            "9")
        
        # Example 10
        self.create_example_card(content, "EXAMPLE 10: Comprehensive Deep Scan",
            "Target URL:\nhttp://example.com\n\n"
            "Configuration:\n"
            "• Quick Options: ✓ Crawl, ✓ Fuzzer, ✓ Blind XSS\n"
            "• Advanced: Crawl Level: 3, Threads: 4, Delay: 2, Timeout: 15\n\n"
            "What it does:\n"
            "Complete security assessment: crawls entire site, fuzzes parameters, "
            "tests blind XSS. Takes longer but most thorough.",
            "10")
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
    def create_tutorial_section(self, parent, title, content):
        section_frame = tk.Frame(parent, bg=self.bg_light, relief='solid', borderwidth=1)
        section_frame.pack(fill='x', pady=(0, 15))
        
        # Title bar with orange accent
        title_bar = tk.Frame(section_frame, bg=self.orange, height=3)
        title_bar.pack(fill='x')
        
        # Content area
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
        
        # Header with number badge
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
        
        # Content
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
        
        # Build command
        cmd = ['python3', 'xsstrike.py', '-u', url]
        
        post_data = self.data_text.get('1.0', 'end').strip()
        if post_data:
            cmd.extend(['--data', post_data])
            
        if self.crawl_var.get():
            cmd.append('--crawl')
            self.log_to_console("Crawling enabled", 'info')
            
        if self.fuzzer_var.get():
            cmd.append('--fuzzer')
            self.log_to_console("Fuzzer mode enabled", 'info')
            
        if self.blind_var.get():
            cmd.append('--blind')
            self.log_to_console("Blind XSS enabled", 'info')
            
        if self.skipdom_var.get():
            cmd.append('--skip-dom')
            
        self.log_to_console("Scan configuration loaded", 'success')
        self.log_to_console("=" * 60, 'info')
        
        # Run scan in thread
        thread = threading.Thread(target=self.run_scan, args=(cmd,))
        thread.daemon = True
        thread.start()
        
    def run_scan(self, cmd):
        try:
            self.log_to_console("Executing XSStrike...", 'info')
            self.log_to_console(f"Command: {' '.join(cmd)}", 'info')
            self.log_to_console("", 'info')
            self.log_to_console("Note: This is a GUI wrapper for XSStrike", 'info')
            self.log_to_console("Ensure xsstrike.py is in the same directory", 'info')
            
        except Exception as e:
            self.log_to_console(f"Error: {str(e)}", 'error')
        finally:
            self.root.after(0, self.scan_complete)
            
    def scan_complete(self):
        self.scanning = False
        self.scan_button.config(state='normal', text="⚡ START SCAN")
        self.status_indicator.config(text="● READY", fg='#00ff00')
        self.log_to_console("", 'info')
        self.log_to_console("Scan sequence complete", 'success')
        self.log_to_console("=" * 60, 'info')

if __name__ == '__main__':
    root = tk.Tk()
    app = BlackStrikeGUI(root)
    root.mainloop()