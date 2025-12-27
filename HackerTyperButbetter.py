import time
import random
import sys

# ================= CONFIG =================
TYPING_SPEED = (0.002, 0.01)
MODULES = [
    "Initializing neural interface",
    "Bypassing firewall layer",
    "Scanning open ports",
    "Injecting polymorphic payload",
    "Decrypting AES-256 tunnel",
    "Hijacking packet stream",
    "Escalating privileges",
    "Masking IP signature",
    "Accessing core node"
]

FAKE_IPS = [
    "192.168.4.23",
    "10.0.0.77",
    "172.16.32.5",
    "45.133.12.201",
    "8.34.91.6"
]

# ================= UTILS =================
def type_print(text, newline=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(*TYPING_SPEED))
    if newline:
        print()

def progress_bar(task, length=25):
    sys.stdout.write(task + " [")
    sys.stdout.flush()
    for _ in range(length):
        sys.stdout.write("#")
        sys.stdout.flush()
        time.sleep(random.uniform(0.02, 0.07))
    print("] DONE")

def glitch():
    junk = "".join(random.choice("01#$%&@") for _ in range(random.randint(10, 25)))
    print(junk)

# ================= CORE =================
def boot_sequence():
    print("R3VAI :: SIMULATED INFILTRATION TERMINAL")
    print("--------------------------------------")
    time.sleep(0.5)

    for m in MODULES:
        type_print(f"[+] {m}...")
        if random.random() < 0.3:
            glitch()
        time.sleep(random.uniform(0.2, 0.6))

    progress_bar("Establishing secure session")
    print()

def fake_scan():
    ip = random.choice(FAKE_IPS)
    type_print(f"Scanning target {ip}")
    for port in random.sample(range(20, 9000), 6):
        type_print(f"Port {port} :: OPEN", newline=True)
        time.sleep(0.1)

def fake_decrypt():
    type_print("Decrypting data stream...")
    progress_bar("Running brute-force heuristic")
    type_print("Encryption key resolved: **REDACTED**")

def fake_inject():
    type_print("Injecting payload...")
    for i in range(0, 101, random.randint(7, 15)):
        sys.stdout.write(f"\rPayload upload: {i}%")
        sys.stdout.flush()
        time.sleep(0.15)
    print("\nPayload active.")

def fake_status():
    print("\n--- SYSTEM STATUS ---")
    print("Firewall: DISABLED")
    print("Trace Risk:", random.choice(["LOW", "MODERATE", "CRITICAL"]))
    print("Access Level:", random.choice(["USER", "ROOT", "SYSTEM"]))
    print("---------------------\n")

# ================= INTERFACE =================
def terminal():
    while True:
        try:
            cmd = input(">>> ").lower().strip()
        except KeyboardInterrupt:
            print("\nSession terminated.")
            break

        if cmd in ("exit", "quit"):
            print("Disconnecting...")
            break
        elif cmd == "scan":
            fake_scan()
        elif cmd == "decrypt":
            fake_decrypt()
        elif cmd == "inject":
            fake_inject()
        elif cmd == "status":
            fake_status()
        elif cmd == "":
            continue
        else:
            type_print(f"Unknown command: {cmd}")

# ================= RUN =================
if __name__ == "__main__":
    boot_sequence()
    print("Type commands: scan | decrypt | inject | status | exit\n")
    terminal()
