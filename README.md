
# 🔐 OPC-UA CTF Challenge Set

This repository provides a collection of OPC-UA (Open Platform Communications - Unified Architecture) based CTF challenges. Players can explore secure communication, protocol analysis, and logic bypass techniques in OT environments.

---

## 📁 Directory Structure

### ✅ `opcua-basic/` – Flag Bitstream Challenge
| File | Description |
|------|-------------|
| `opcua-server.py` | Sends a binary-encoded flag bit-by-bit using the `FlagToggle` variable. |
| `opcua-client.py` | Connects to server, captures the stream, and reconstructs the flag. |
| `mission.md` | Challenge instructions. |

### 🧠 `opcua-advanced/` – Control Logic Bypass Challenges
| File | Description |
|------|-------------|
| `server.py`, `server1.py` ~ `server7.py` | Expose control variables. Setting `ActivePowerControl = 0` reveals the flag in `ControlFlag`. |
| `mission.md` | Challenge instructions. |

---

## ▶️ Quick Start

Install dependencies:
```bash
pip install freeopcua
```

Run a basic or advanced server:
```bash
python opcua-basic/opcua-server.py
python opcua-advanced/server.py
```

---

## 🎯 Challenge Concepts

| Theme | Covered |
|-------|---------|
| OPC-UA Client/Server Basics | ✅ |
| Variable Browsing & Manipulation | ✅ |
| Flag Extraction via Control Logic | ✅ |
| Stream Analysis (Bitwise Flag) | ✅ |

---

## 📜 License

Educational use only. Designed for ethical security training and CTF competitions.
