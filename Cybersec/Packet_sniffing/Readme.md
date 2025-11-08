In this project I'll be sniffing packets of other devices connected in my network. In short I'll be doing **Man in the middle attack**

## Adress Resolution Protocol(ARP)
Address Resolution Protocol (ARP) is a network protocol used to map an IP address to a physical MAC address within a local area network (LAN).

## A simple Example of how ARP works
If your computer wants to send data to 192.168.1.10:

1. It checks its ARP cache.

2. If not found, it broadcasts an ARP request.

3. The device with IP 192.168.1.10 replies with its MAC address.

4. Your computer sends the data directly to that MAC address.

## ARP poisoning 
ARP poisoning (also called ARP spoofing) is a trick used by attackers to fool devices on a network into sending data to the wrong place (usually to the attacker).

### Before performing such attacks, you need to know some networking ie

**Switch** - A switch connects devices within the same network(Mac Address)
**Router** - Connects your home network to the internet
**Hub** - A hub is a simple network device that connects multiple computers or devices in a local area network (LAN). 
When one device sends data, the hub copies it and sends it to all other devices.
It doesn’t know who the data is meant for, so everyone gets it, even if only one device needs it.

## Tools used in this MITM attack
1. Wireshark
2. Nmap
3. Ettercap

## Steps I used to conduct this MITM attack
1. I did some recon in order to identify the ip address of the device I want to attack.
I run this Nmap command

```
sudo nmap -sn 192.168.1.0/24
```
This will return all devices connected in the network and I can choose the one I want to attack

![alt text](https://github.com/GERRY-01/Cybersecurity-Projects-/blob/main/Cybersec/Packet_sniffing/nmapsnan.png?raw=true)

2. I'll run this command to start the attack 
```
sudo ettercap -T -S -i wlan0 -M arp:remote /router_ip/ /target_ip/
```

**What it does**
sudo: Runs the command with administrative privileges.

ettercap: The tool being used.

-T: Text-only interface (no GUI).

-S: Silent mode (less output).

-i wlan0: Specifies the network interface (in this case, Wi-Fi).

-M arp:remote: Tells Ettercap to perform ARP poisoning between two remote hosts.

/router_ip/ /target_ip/: These are the two devices you want to intercept:

By running that command, you will start capturing traffic for that device

![alt text](https://github.com/GERRY-01/Cybersecurity-Projects-/blob/main/Cybersec/Packet_sniffing/ettercat.png?raw=true)

3. Open Wireshark
After opening wireshark you can just filter traffic by ip address


![alt text](https://github.com/GERRY-01/Cybersecurity-Projects-/blob/main/Cybersec/Packet_sniffing/wireshark.png?raw=true)
