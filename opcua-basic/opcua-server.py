from opcua import Server
import datetime
import time

# OPC-UA 서버 초기화
server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

# 네임스페이스 설정
uri = "http://ctf.example.org"
idx = server.register_namespace(uri)

# 객체 생성
objects = server.get_objects_node()

# 값이 교차하는 변수 생성
flag_variable = objects.add_variable(idx, "FlagToggle", 0)
flag_variable.set_writable()

# 서버 시작
server.start()

print("OPC-UA Server started at {}".format(server.endpoint))

try:
    # flag를 이진으로 변환 (flag{opc_ua_game})
    flag_binary = ''.join(format(ord(c), '08b') for c in 'flag{opc_ua_game_is_fun!!}')
    index = 0

    while True:
        if index >= len(flag_binary):
            # 10초간 0 반복 후 다시 시작
            for _ in range(10):
                flag_variable.set_value(0)
                print(f"{datetime.datetime.now()} - FlagToggle: 0 (reset)")
                time.sleep(1)
            index = 0
        else:
            value = int(flag_binary[index])
            flag_variable.set_value(value)
            print(f"{datetime.datetime.now()} - FlagToggle: {value}")
            index += 1
            time.sleep(1)

finally:
    # 종료 시 서버 정리
    server.stop()
    print("Server stopped")