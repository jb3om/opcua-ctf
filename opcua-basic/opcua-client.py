from opcua import Client
import time

client = Client("opc.tcp://localhost:4840/freeopcua/server/")
client.connect()
print("[+] Connected to OPC-UA Server")

# 동적 탐색으로 FlagToggle 변수 찾기
objects = client.get_objects_node()
flag_node = None

for child in objects.get_children():
    browse_name = child.get_browse_name().Name
    if browse_name == "FlagToggle":
        flag_node = child
        print(f"[+] Found FlagToggle Node: {flag_node.nodeid}")
        break

if flag_node is None:
    print("[-] FlagToggle node not found. Check server namespace and variable name.")
    client.disconnect()
    exit(1)

# 이후는 동일
recent_bits = ""
flag_bits = ""
recording = False
zero_threshold = 10

try:
    while True:
        bit = str(flag_node.get_value())
        recent_bits += bit
        recent_bits = recent_bits[-zero_threshold:]

        print(bit, end="", flush=True)

        if not recording:
            if recent_bits == "0" * zero_threshold:
                print("\n[!] Start sequence detected → begin recording flag...")
                flag_bits = ""
                recording = True
                continue
        else:
            if recent_bits == "0" * zero_threshold:
                print("\n[!] End sequence detected → stop recording.")
                break
            flag_bits += bit

        time.sleep(1)

    flag_bytes = [flag_bits[i:i+8] for i in range(0, len(flag_bits), 8)]
    flag = ''.join(chr(int(b, 2)) for b in flag_bytes if len(b) == 8)
    print(f"\n\n[FLAG] {flag}")

finally:
    client.disconnect()
