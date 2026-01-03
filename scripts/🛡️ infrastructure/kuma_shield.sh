#!/bin/bash
# Title: Kuma-Shield v1.0
# Description: Automated UFW Hardening & VPN KillSwitch for Secure Remote Work.
# Author: Kuma-DoTech

echo "🛡️ Initializing Kuma-Shield..."

# Reset Rules
sudo ufw --force reset

# Default Policies
sudo ufw default deny incoming
sudo ufw default deny outgoing

# Allow Essential Handshaking
sudo ufw allow out 53/udp     # DNS
sudo ufw allow out 67,68/udp  # DHCP
sudo ufw allow out 443/tcp    # HTTPS
sudo ufw allow out 1194/udp   # OpenVPN Standard

# Allow Tunnel Interface (The KillSwitch)
sudo ufw allow out on tun0
sudo ufw allow in on tun0

sudo ufw --force enable
echo "✅ Infrastructure Hardened. Tunnel Ready."
