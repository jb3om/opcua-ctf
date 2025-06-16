from opcua import Server
import time
import datetime
import random

# OPC-UA 서버 초기화
server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4842/freeopcua/output/")

# 네임스페이스 등록
uri = "http://ctf.example.org/output"
idx = server.register_namespace(uri)

# 객체 노드 생성
objects = server.get_objects_node()

# 제어 변수 등록
active_power_control = objects.add_variable(idx, "ActivePowerControl", 100)  # 유효전력 제어
reactive_power_control = objects.add_variable(idx, "ReactivePowerControl", 30)  # 무효전력 제어
power_factor_control = objects.add_variable(idx, "PowerFactorControl", 0.95)  # 역률 제어

# 계측 변수 등록 (읽기 전용)
active_power_measured = objects.add_variable(idx, "ActivePowerMeasured", 100)  # 유효전력 측정
reactive_power_measured = objects.add_variable(idx, "ReactivePowerMeasured", 30)  # 무효전력 측정
power_factor_measured = objects.add_variable(idx, "PowerFactorMeasured", 0.95)  # 역률 측정

# 제어 변수는 쓰기 가능
active_power_control.set_writable()
reactive_power_control.set_writable()
power_factor_control.set_writable()

# flag 노출 노드 (읽기 전용)
flag_node = objects.add_variable(idx, "ControlFlag", "Access Denied")
flag_node.set_writable(False)

print("[+] OPC-UA Output Control Server Started at opc.tcp://0.0.0.0:4840/freeopcua/output/")
server.start()

try:
    while True:
        # 미끼 계측 데이터 랜덤화
        active_power_measured.set_value(random.randint(80, 120))
        reactive_power_measured.set_value(random.randint(10, 50))
        power_factor_measured.set_value(round(random.uniform(0.80, 1.00), 2))

        # 유효전력 제어값 검사 후 flag 제어
        active_val = active_power_control.get_value()
        if active_val == 0:
            flag_node.set_value("flag{output_control_bypass}")
        else:
            flag_node.set_value("Access Denied")

        print(f"{datetime.datetime.now()} - [Control] Active: {active_val}%, Reactive: {reactive_power_control.get_value()}kVAR, PF: {power_factor_control.get_value()}")
        print(f"{datetime.datetime.now()} - [Measured] Active: {active_power_measured.get_value()}%, Reactive: {reactive_power_measured.get_value()}kVAR, PF: {power_factor_measured.get_value()}")
        time.sleep(3)

finally:
    server.stop()
    print("[-] Server stopped")
