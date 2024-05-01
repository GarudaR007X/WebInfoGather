import socket
import requests
import whois

print("Example: google.com")
domain = input("Enter a Domain Name: ")
print("\n\n")

# Find IP
def getIP(domain):
    try:
        ip = socket.gethostbyname(domain)
        print("| IP Address:", ip)
    except socket.gaierror as e:
        print("IP not Found:", e)

# Get HTTP headers
def getHTTPHeaders(domain):
    try:
        r = requests.get("http://" + domain)  
        if r.status_code == 200: 
            print("| HTTP Headers:")
            for header, value in r.headers.items():
               print("|  - {}: {}".format(header, value))
    except Exception as e:
        print("HTTP Headers not Found:", e)

# Get WHOIS Info
def getWHOISInfo(domain):
    try:
        whois_result = ""
        py = whois.whois(domain)
        
        whois_result += "| Name: {}\n".format(py.name)
        whois_result += "| Registrar: {}\n".format(py.registrar)
        whois_result += "| Creation Date: {}\n".format(py.creation_date)
        whois_result += "| Expiry Date: {}\n".format(py.expiration_date)
        whois_result += "| Registrant: {}\n".format(py.registrant)
        whois_result += "| Registrant Country: {}\n".format(py.registrant_country)
        print(whois_result)
       
    except Exception as e:
       print("WHOIS not found:", e)

# Port scan 
def portScan(domain):
    try:
        ip = socket.gethostbyname(domain)
        open_ports = []

        top_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080, 8443]  
        for port in top_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # Returns an error indicator
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            s.close()

        if open_ports:
            print("| Open ports:" , open_ports)
        else:
            print("| No open ports found.")

    except socket.gaierror as e:
        print("Error resolving domain:", e)
    except KeyboardInterrupt:
        print("\nExiting Program !!!")
    except socket.error:
        print("\nServer not responding !!!")


print("[+] Finding IP...")
getIP(domain)
print("IP Address Found. \n\n")

print("[+] Finding HTTP Headers...")
getHTTPHeaders(domain)  
print("HTTP Headers Found. \n\n")

print("[+] Finding Whois Info... ")
getWHOISInfo(domain)
print("WHOIS Found. \n\n")

print("[+] Finding Port Scan...")
print("Port scanning is starting...")
portScan(domain)
print("Port scanning is complete. \n\n")
