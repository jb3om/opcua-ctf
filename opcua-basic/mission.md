
# 📡 Mission: Flag Stream Capture

This challenge simulates an OPC-UA server that transmits a binary flag one bit per second.

- Writable Variables: None
- Readable Variable:
  - `FlagToggle` (value alternates between 0 and 1 every second)

The flag transmitted is: `flag{opc_ua_game_is_fun!!}` (in binary)

## 🎯 Goal
Build or use an OPC-UA client to:
1. Connect to the server.
2. Monitor `FlagToggle` every second.
3. Detect the flag start/end pattern (10 zeros).
4. Reconstruct the flag by decoding binary to ASCII.

A reference `opcua-client.py` is provided.
