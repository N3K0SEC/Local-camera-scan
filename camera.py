from rtsp_scanner import PortScanner

scanner = PortScanner()
results = scanner.scan_network('192.168.1.0/24')
print(f"Found {len(results)} cams")
