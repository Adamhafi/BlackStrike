# 🛡️ BlackStrike - Unified XSS Scanner

![Python Version](https://img.shields.io/badge/python-3.7+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macos-orange.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**BlackStrike** is a powerful, all-in-one XSS (Cross-Site Scripting) vulnerability scanner featuring both an elegant GUI interface and command-line capabilities. Built entirely in Python with an integrated scanning engine, BlackStrike requires no external tools—everything you need is in a single file.

![BlackStrike Screenshot](https://i.ibb.co/whYJcgXc/Screenshot-20251108-134549.png)

---

## ✨ Key Features

### 🎯 **All-in-One Solution**
- **Single File Deployment** - No separate XSStrike installation needed
- **Dual Interface** - Use GUI or command-line interface
- **Integrated Engine** - Built-in XSS detection with 20+ payloads
- **Zero External Tools** - Completely self-contained

### 🎨 **Luxury GUI Interface**
- **Professional Orange & Black Theme** - Eye-friendly dark mode
- **5 Comprehensive Tabs** - Scan, Advanced, Console, Tutorial, Examples
- **Real-time Logging** - Color-coded console output
- **Interactive Tutorials** - Built-in learning resources
- **10 Practical Examples** - Real-world scanning scenarios

### ⚡ **Powerful Scanning Engine**
- **GET & POST Support** - Test both HTTP methods
- **20+ XSS Payloads** - Comprehensive attack vectors
- **Multi-threaded** - Fast, concurrent testing
- **Parameter Detection** - Automatic parameter parsing
- **Reflection Analysis** - Smart vulnerability detection
- **Payload Encoding** - Base64 and custom encoding
- **Configurable Options** - Timeout, threads, delays

### 📚 **Educational Resources**
- **Step-by-step Tutorials** - Learn as you scan
- **Practical Examples** - Real-world scenarios
- **Best Practices** - Professional testing guidelines
- **Troubleshooting Guide** - Common issues solved

---

## 📋 Requirements

- **Python 3.7+** (Python 3.8+ recommended)
- **Tkinter** (included with most Python installations)
- **Standard Library Only** - No external dependencies required!

---

## 🚀 Installation

### Quick Install

```bash
# Clone the repository
git clone https://github.com/yourusername/blackstrike.git
cd blackstrike

# Make executable (Linux/Mac)
chmod +x blackstrike.py

# Run GUI mode
python3 blackstrike.py

# Or run CLI mode
python3 blackstrike.py -u http://target.com/page?param=test
```

### Verify Installation

```bash
# Check Python version
python3 --version

# Verify Tkinter (GUI) is available
python3 -c "import tkinter; print('Tkinter OK')"

# Test BlackStrike
python3 blackstrike.py --help
```

---

## 🎯 Quick Start Guide

### GUI Mode (Recommended for Beginners)

1. **Launch BlackStrike**
   ```bash
   python3 blackstrike.py
   ```

2. **Basic Scan**
   - Navigate to **SCAN** tab
   - Enter target URL: `http://testphp.vulnweb.com/search.php?test=query`
   - Click **START SCAN**
   - View results in **CONSOLE** tab

3. **Advanced Scan**
   - Configure options in **ADVANCED** tab
   - Enable **Crawl**, **Fuzzer**, or **Blind XSS**
   - Adjust threads, timeout, and delay
   - Return to **SCAN** tab and start

### CLI Mode (For Automation & Scripts)

```bash
# Basic GET request scan
python3 blackstrike.py -u "http://example.com/search.php?q=test"

# POST request scan
python3 blackstrike.py -u "http://example.com/login.php" --data "user=admin&pass=test"

# Advanced scan with options
python3 blackstrike.py -u "http://example.com" --fuzzer --crawl -t 4 --timeout 10

# Multi-threaded scan
python3 blackstrike.py -u "http://example.com/page?id=1" -t 8 --delay 1
```

---

## 📖 Usage Examples

### Example 1: Basic Vulnerability Scan
**Scenario:** Test a search parameter for XSS

```bash
# GUI Mode
Target URL: http://testphp.vulnweb.com/search.php?test=query
POST Data: [Empty]
Options: [None]

# CLI Mode
python3 blackstrike.py -u "http://testphp.vulnweb.com/search.php?test=query"
```

**Expected Output:**
- Parameter detection
- Payload injection
- Vulnerability confirmation (if vulnerable)

---

### Example 2: POST Request Testing
**Scenario:** Test login form for XSS

```bash
# GUI Mode
Target URL: http://example.com/login.php
POST Data: username=admin&password=test&remember=1
Options: [None]

# CLI Mode
python3 blackstrike.py -u "http://example.com/login.php" \
  --data "username=admin&password=test&remember=1" \
  -t 4
```

---

### Example 3: Multi-Parameter Testing
**Scenario:** Test multiple parameters simultaneously

```bash
# GUI Mode
Target URL: http://example.com/search.php?q=test&cat=all&sort=date
Quick Options: Enable "Fuzzer"
Advanced: Threads: 6

# CLI Mode
python3 blackstrike.py -u "http://example.com/search.php?q=test&cat=all&sort=date" \
  --fuzzer -t 6
```

---

### Example 4: JSON API Testing
**Scenario:** Test modern API endpoint

```bash
# GUI Mode
Target URL: http://api.example.com/search
POST Data: {"query":"test","filter":"all"}
Advanced: Enable "JSON Data"

# CLI Mode
python3 blackstrike.py -u "http://api.example.com/search" \
  --data '{"query":"test","filter":"all"}'
```

---

### Example 5: Comprehensive Deep Scan
**Scenario:** Full security assessment

```bash
# GUI Mode
Target URL: http://example.com
Quick Options: ✓ Crawl, ✓ Fuzzer, ✓ Blind XSS
Advanced: Threads: 4, Delay: 2, Crawl Level: 3

# CLI Mode
python3 blackstrike.py -u "http://example.com" \
  --crawl --fuzzer -t 4 --delay 2 -l 3
```

---

## 🛠️ Configuration Options

### GUI Options

| Tab | Option | Description | Default |
|-----|--------|-------------|---------|
| **Scan** | Target URL | URL to test | - |
| **Scan** | POST Data | POST parameters | - |
| **Scan** | Crawl | Auto-discover pages | Off |
| **Scan** | Fuzzer | Advanced payload testing | Off |
| **Scan** | Blind XSS | Test stored XSS | Off |
| **Scan** | Skip DOM | Skip DOM checks | Off |
| **Advanced** | Encoding | Payload encoding | None |
| **Advanced** | Timeout | Request timeout (sec) | 7 |
| **Advanced** | Threads | Concurrent threads | 2 |
| **Advanced** | Delay | Request delay (sec) | 0 |
| **Advanced** | Crawl Level | Crawl depth | 2 |
| **Advanced** | Use Proxy | Enable proxy | Off |
| **Advanced** | JSON Data | Treat as JSON | Off |
| **Advanced** | Path Injection | Test URL paths | Off |

### CLI Options

```bash
python3 blackstrike.py [options]

Required:
  -u, --url URL              Target URL to scan

Optional:
  --data DATA                POST data to send
  --fuzzer                   Enable fuzzer mode
  --crawl                    Enable crawling
  -t, --threads NUM          Number of threads (default: 2)
  --timeout SEC              Request timeout (default: 7)
  --delay SEC                Delay between requests (default: 0)
  -l, --level NUM            Crawl level 1-3 (default: 2)
  -h, --help                 Show help message
```

---

## 📊 Understanding Console Output

### Color Coding

- 🟢 **Green** - Successful operations, vulnerabilities found
- 🔴 **Red** - Errors, critical issues
- 🟡 **Yellow** - Warnings, potential issues
- 🔵 **Blue** - Informational messages
- ⚪ **Gray** - Timestamps

### Sample Output

```
[14:23:45] ============================================================
[14:23:45] BlackStrike XSS Scanner v3.1.5 Initiated
[14:23:45] ============================================================
[14:23:45] Target: http://example.com/search.php?q=test
[14:23:45] Target host: example.com
[14:23:45] Target path: /search.php
[14:23:45] Query parameters detected: q=test
[14:23:45] Testing 1 parameter(s)
[14:23:46] Testing parameter: q
[14:23:46]   Testing payload 1/5: <script>alert(1)</script>...
[14:23:47] 🚨 Vulnerability confirmed!
[14:23:47] ✓ Vulnerable parameter found: q
```

---

## ⚠️ Legal Disclaimer

**CRITICAL: Read Before Using**

BlackStrike is designed exclusively for **legal security testing and educational purposes**.

### ✅ Authorized Use
- Testing applications you own
- Testing with explicit written permission
- Educational environments and labs
- Security research with proper authorization
- Bug bounty programs (follow their rules)

### ❌ Prohibited Use
- Unauthorized testing of websites/applications
- Testing without explicit permission
- Malicious activities or attacks
- Violation of computer fraud laws
- Any illegal purposes

### 📜 Legal Notice

**Unauthorized access to computer systems is illegal** under laws including but not limited to:
- Computer Fraud and Abuse Act (CFAA) - USA
- Computer Misuse Act - UK
- Similar legislation in other jurisdictions

**The creator (Adam) and contributors:**
- Assume NO liability for misuse
- Are NOT responsible for any damages
- Do NOT endorse illegal activities
- Provide this tool "AS IS" without warranty

**By using BlackStrike, you agree:**
- You have permission to test the target
- You accept full responsibility for your actions
- You will comply with all applicable laws
- You release the creators from all liability

---

## 🐛 Troubleshooting

### Issue: GUI won't launch

**Symptoms:**
```
ImportError: No module named 'tkinter'
```

**Solutions:**
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora/RHEL
sudo dnf install python3-tkinter

# macOS (Homebrew)
brew install python-tk

# Windows
# Reinstall Python with "tcl/tk and IDLE" option checked
```

---

### Issue: "Invalid URL" error

**Symptoms:**
```
Invalid URL - missing scheme (http/https)
```

**Solution:**
Always include `http://` or `https://`:
```bash
# Wrong
python3 blackstrike.py -u example.com

# Correct
python3 blackstrike.py -u http://example.com
```

---

### Issue: No vulnerabilities found

**Possible Causes:**
1. Target is actually secure
2. WAF/firewall blocking requests
3. Payloads not suited for target

**Solutions:**
- Enable **Fuzzer** mode for more payloads
- Try **Encoded** payloads in Advanced tab
- Increase **Timeout** for slow servers
- Check **Console** for detailed results

---

### Issue: Scan is too slow

**Solutions:**
```bash
# Increase threads
-t 8

# Enable Skip DOM
# (GUI: Check "Skip DOM" option)

# Reduce timeout
--timeout 5

# Add delay to prevent blocks
--delay 1
```

---

### Issue: Connection errors

**Symptoms:**
```
Connection timeout
Connection refused
```

**Solutions:**
1. Verify target is accessible: `curl http://target.com`
2. Increase timeout: `--timeout 30`
3. Check firewall/proxy settings
4. Ensure proper URL format

---

## 🤝 Contributing

Contributions are welcome! BlackStrike is open-source and community-driven.

### How to Contribute

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/blackstrike.git
   cd blackstrike
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Make Changes**
   - Add new payloads
   - Improve detection logic
   - Enhance UI/UX
   - Fix bugs
   - Update documentation

4. **Test Thoroughly**
   ```bash
   # Test GUI mode
   python3 blackstrike.py
   
   # Test CLI mode
   python3 blackstrike.py -u http://testphp.vulnweb.com/search.php?test=query
   ```

5. **Commit Changes**
   ```bash
   git commit -m 'Add: Amazing new feature'
   ```

6. **Push and Create PR**
   ```bash
   git push origin feature/AmazingFeature
   ```

### Contribution Ideas

- 🎯 Additional XSS payload templates
- 🔐 New encoding/obfuscation methods
- 🎨 UI/UX improvements
- ⚡ Performance optimizations
- 📚 Documentation enhancements
- 🌐 Internationalization (i18n)
- 🧪 Unit tests and CI/CD
- 🐛 Bug fixes

---

## 📝 Changelog

### Version 1.0.0 (2025)
**Initial Release - Unified Architecture**

✨ **New Features:**
- Complete GUI interface with 5 tabs
- Integrated XSS scanning engine
- 20+ XSS payload templates
- Dual mode operation (GUI/CLI)
- Real-time console logging
- Color-coded output
- Multi-threaded scanning
- Parameter parsing (GET/POST)
- Payload encoding support
- Built-in tutorials and examples
- Professional orange/black theme

🛡️ **Security:**
- Safe payload handling
- Input validation
- Error handling
- Legal disclaimers

📚 **Documentation:**
- Comprehensive README
- Usage examples
- Troubleshooting guide
- Contributing guidelines

---

## 🏆 Credits & Acknowledgments

### Creator
**Adam** - Original BlackStrike concept and implementation

### Inspiration
- **XSStrike** by [@s0md3v](https://github.com/s0md3v) - Original CLI scanner
- **OWASP** - XSS testing methodologies
- **PortSwigger** - Web security research

### Technologies
- **Python 3** - Core language
- **Tkinter** - GUI framework
- **Threading** - Concurrent execution

### Community
- Security researchers worldwide
- Open-source contributors
- Bug hunters and testers

---

## 📜 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 Adam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📧 Contact & Support

### Get Help
- 📖 **Documentation**: Read this README thoroughly
- 💬 **Issues**: [GitHub Issues](https://github.com/adamhafi/blackstrike/issues)
- 🐛 **Bug Reports**: Use issue template
- 💡 **Feature Requests**: Submit via GitHub

### Stay Connected
- 🌐 **GitHub**: [@AdamHafi](https://github.com/adamhafi)
- 📦 **Project**: [BlackStrike Repository](https://github.com/adamhafi/blackstrike)
- ⭐ **Star**: If you find this useful!

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/adamhafi/blackstrike?style=social)
![GitHub forks](https://img.shields.io/github/forks/adamhafi/blackstrike?style=social)
![GitHub issues](https://img.shields.io/github/issues/adamhafi/blackstrike)
![GitHub pull requests](https://img.shields.io/github/issues-pr/adamhafi/blackstrike)

---

## 🎯 Roadmap

### Planned Features
- [ ] Custom payload import
- [ ] Export scan reports (PDF/HTML/JSON)
- [ ] Proxy support (HTTP/HTTPS/SOCKS)
- [ ] WAF detection and bypass
- [ ] Browser automation (Selenium)
- [ ] Database storage for results
- [ ] API endpoint for integration
- [ ] Plugin system
- [ ] Advanced fuzzing algorithms
- [ ] Machine learning payload generation

### Future Enhancements
- [ ] Support for other injection types (SQLi, CSRF)
- [ ] Mobile app version
- [ ] Cloud-based scanning
- [ ] Team collaboration features
- [ ] Compliance reporting (PCI-DSS, OWASP)

---

<div align="center">

## 🛡️ BlackStrike by Adam

**The Ultimate Unified XSS Scanner**

![Made with Python](https://img.shields.io/badge/Made%20with-Python-orange.svg?style=for-the-badge)
![Made with Love](https://img.shields.io/badge/Made%20with-❤-orange.svg?style=for-the-badge)

### ⭐ Star this repo if you find it useful!

**[Download](https://github.com/adamhafi/blackstrike/archive/refs/heads/main.zip) • [Report Bug](https://github.com/adamhafi/blackstrike/issues) • [Request Feature](https://github.com/adamhafi/blackstrike/issues)**

</div>

---

## 📌 Quick Reference Card

```bash
# Launch GUI
python3 blackstrike.py

# Basic scan
python3 blackstrike.py -u http://target.com/page?param=test

# POST scan
python3 blackstrike.py -u http://target.com/login --data "user=test&pass=test"

# Advanced scan
python3 blackstrike.py -u http://target.com --fuzzer --crawl -t 4 -l 2

# Fast scan
python3 blackstrike.py -u http://target.com/page?q=test -t 8 --timeout 5

# Help
python3 blackstrike.py --help
```

---

**Remember: With great power comes great responsibility. Use BlackStrike ethically and legally.**

© 2025 Adam | Licensed under MIT
