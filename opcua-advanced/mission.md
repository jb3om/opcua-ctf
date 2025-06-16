
# 🧠 Mission: Flag Control via Setpoint

You are given 8 OPC-UA servers (server.py and server1~7.py), each exposing:

- Writable Control Variables:
  - ActivePowerControl (integer)
  - ReactivePowerControl (integer)
  - PowerFactorControl (float)

- Readonly Measured Variables:
  - ActivePowerMeasured
  - ReactivePowerMeasured
  - PowerFactorMeasured

- Readonly Flag Node:
  - ControlFlag — usually returns "Access Denied"

## 🎯 Goal
Set `ActivePowerControl` to the correct value so that `ControlFlag` returns a flag.

> Hint: All 8 servers use the same condition: **`ActivePowerControl == 0`** reveals the flag.

This challenge demonstrates logic bypass and variable control in OT protocols.
