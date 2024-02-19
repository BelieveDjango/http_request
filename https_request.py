import requests
import time

def send_request(url):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        print(f"Request sent to {url} | Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending request to {url}: {e}")

def main():
    # Replace 'https://example.com' with the URL you want to send requests to
    target_url = 'https://www.techtechinfra.tech/'
    
    # Set the interval between requests in seconds
    interval_seconds = 5  # 5 Seconds
    
    print(f"Sending periodic requests to {target_url} every {interval_seconds} seconds. Press Ctrl+C to stop.")
    
    try:
        while True:
            send_request(target_url)
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("\nScript terminated by user.")

if __name__ == "__main__":
    main()