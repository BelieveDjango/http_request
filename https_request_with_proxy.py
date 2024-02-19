import requests
import random
from urllib3.exceptions import NewConnectionError
import time

def send_request(url, proxy_list):
    try:
        # Randomly select a proxy for each request
        proxy_string = random.choice(proxy_list)
        response = requests.get(url, proxies={'http': proxy_string, 'https': proxy_string}, verify=False, timeout=5)
        response.raise_for_status()
        print(f"Request sent to {url} using proxy {proxy_string} | Status code: {response.status_code}")
    except (requests.exceptions.RequestException, NewConnectionError) as e:
        print(f"Error sending request to {url} using proxy {proxy_string}: {e}")

def main():
    # Replace 'https://example.com' with the URL you want to send requests to
    target_url = 'https://wwww.techtechinfra.tech/'

    # Set the interval between requests in seconds
    interval_seconds = 20  # 5 Seconds

    # Set proxy details
    proxy_host = 'gate.smartproxy.com'
    proxy_ports = list(range(10000, 10113))

    # Create a list of proxies without authentication
    proxy_list = [
        f"http://{proxy_host}:{port}" for port in proxy_ports
    ]

    print(f"Sending periodic requests to {target_url} using proxies every {interval_seconds} seconds. Press Ctrl+C to stop.")

    try:
        while True:
            send_request(target_url, proxy_list)
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("\nScript terminated by user.")

if __name__ == "__main__":
    main()
