import subprocess

def stop_vpn():
    """Para a VPN."""
    subprocess.run(["taskkill", "/F", "/IM", "openvpn.exe"])
