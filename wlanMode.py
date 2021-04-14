import argparse
import subprocess
import sys


def enable_monitor(iface):
    subprocess.run(["sudo", "ifconfig", iface, "down"])
    subprocess.run(["sudo", "iwconfig", iface, "mode", "monitor"])
    subprocess.run(["sudo", "ifconfig", iface, "up"])


def enable_managed(iface):
    subprocess.run(["sudo", "ifconfig", iface, "down"])
    subprocess.run(["sudo", "iwconfig", iface, "mode", "managed"])
    subprocess.run(["sudo", "ifconfig", iface, "up"])


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-mo", "--monitor", help="Enables monitor mode", action="store_true")
    group.add_argument("-ma", "--managed", help="Emables managed mode", action="store_true")
    group.add_argument("-rs", "--restart", help="Restarts network manager", action="store_true")
    parser.add_argument("iface", help="Current wireless interface", type=str)
    args = parser.parse_args()
    out = subprocess.check_output(["iwconfig", args.iface]).decode(sys.stdout.encoding)

    if args.monitor:
        if "Monitor" in out:
            print("The interface is already set to monitor")
        else:
            subprocess.run(["systemctl", "start", "NetworkManager"])
            enable_monitor(args.iface)
            print("Monitor mode enabled.")
    elif args.managed:
        if "Managed" in out:
            print("The interface is already set to managed")
        else:
            enable_managed(args.iface)
            subprocess.run(["systemctl", "start", "NetworkManager"])
            print("Managed mode enabled")
    elif args.restart:
        subprocess.run(["systemctl", "start", "NetworkManager"])
    else:
        print("Invalid operation argument error.")


if __name__ == "__main__":
    main()
