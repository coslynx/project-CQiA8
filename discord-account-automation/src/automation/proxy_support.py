import requests
import ProxyBroker

class ProxySupport:
    def __init__(self):
        self.proxy_list = ProxyBroker.get_proxy_list()

    def get_random_proxy(self):
        return random.choice(self.proxy_list)

    def send_request_with_proxy(self, url):
        proxy = self.get_random_proxy()
        try:
            response = requests.get(url, proxies={'http': proxy, 'https': proxy})
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def verify_proxy(self, proxy):
        try:
            response = requests.get("https://www.google.com", proxies={'http': proxy, 'https': proxy})
            if response.status_code == 200:
                return True
            else:
                return False
        except requests.exceptions.RequestException:
            return False

# Usage example:
# proxy_support = ProxySupport()
# random_proxy = proxy_support.get_random_proxy()
# response = proxy_support.send_request_with_proxy("https://www.example.com")
# is_valid = proxy_support.verify_proxy(random_proxy)