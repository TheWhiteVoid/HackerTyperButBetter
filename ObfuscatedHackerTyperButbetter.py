import time as _t
import random as _r
import sys as _s

# ===== CFG =====
_A = (0.002, 0.01)

_B = list(map(lambda x: "".join(chr(c) for c in x), [
    [73,110,105,116,105,97,108,105,122,105,110,103,32,110,101,117,114,97,108,32,105,110,116,101,114,102,97,99,101],
    [66,121,112,97,115,115,105,110,103,32,102,105,114,101,119,97,108,108,32,108,97,121,101,114],
    [83,99,97,110,110,105,110,103,32,111,112,101,110,32,112,111,114,116,115],
    [73,110,106,101,99,116,105,110,103,32,112,111,108,121,109,111,114,112,104,105,99,32,112,97,121,108,111,97,100],
    [68,101,99,114,121,112,116,105,110,103,32,65,69,83,45,50,53,54,32,116,117,110,110,101,108],
    [72,105,106,97,99,107,105,110,103,32,112,97,99,107,101,116,32,115,116,114,101,97,109],
    [69,115,99,97,108,97,116,105,110,103,32,112,114,105,118,105,108,101,103,101,115],
    [77,97,115,107,105,110,103,32,73,80,32,115,105,103,110,97,116,117,114,101],
    [65,99,99,101,115,115,105,110,103,32,99,111,114,101,32,110,111,100,101]
]))

_C = ["192.168.4.23", "10.0.0.77", "172.16.32.5", "45.133.12.201", "8.34.91.6"]

# ===== UTIL =====
def _w(x, n=True):
    for c in x:
        _s.stdout.write(c)
        _s.stdout.flush()
        _t.sleep(_r.uniform(*_A))
    if n:
        print()

def _p(x, l=25):
    _s.stdout.write(x + " [")
    _s.stdout.flush()
    for _ in range(l):
        _s.stdout.write("#")
        _s.stdout.flush()
        _t.sleep(_r.uniform(0.02, 0.07))
    print("] DONE")

def _g():
    print("".join(_r.choice("01#$%&@") for _ in range(_r.randint(10, 25))))

# ===== CORE =====
def _b():
    print("R3VAI :: SIMULATED INFILTRATION TERMINAL")
    print("-" * 38)
    _t.sleep(0.5)

    for m in _B:
        _w(f"[+] {m}...")
        if _r.random() < 0.3:
            _g()
        _t.sleep(_r.uniform(0.2, 0.6))

    _p("Establishing secure session")
    print()

def _s1():
    ip = _r.choice(_C)
    _w(f"Scanning target {ip}")
    for p in _r.sample(range(20, 9000), 6):
        _w(f"Port {p} :: OPEN")

def _s2():
    _w("Decrypting data stream...")
    _p("Running brute-force heuristic")
    _w("Encryption key resolved: **REDACTED**")

def _s3():
    _w("Injecting payload...")
    i = 0
    while i <= 100:
        _s.stdout.write(f"\rPayload upload: {i}%")
        _s.stdout.flush()
        i += _r.randint(7, 15)
        _t.sleep(0.15)
    print("\nPayload active.")

def _s4():
    print("\n--- SYSTEM STATUS ---")
    print("Firewall: DISABLED")
    print("Trace Risk:", _r.choice(["LOW", "MODERATE", "CRITICAL"]))
    print("Access Level:", _r.choice(["USER", "ROOT", "SYSTEM"]))
    print("---------------------\n")

# ===== UI =====
def _ui():
    while True:
        try:
            c = input(">>> ").strip().lower()
        except KeyboardInterrupt:
            print("\nSession terminated.")
            break

        if c in ("exit", "quit"):
            print("Disconnecting...")
            break
        elif c == "scan":
            _s1()
        elif c == "decrypt":
            _s2()
        elif c == "inject":
            _s3()
        elif c == "status":
            _s4()
        elif c:
            _w(f"Unknown command: {c}")

# ===== RUN =====
if __name__ == "__main__":
    _b()
    print("Type commands: scan | decrypt | inject | status | exit\n")
    _ui()
