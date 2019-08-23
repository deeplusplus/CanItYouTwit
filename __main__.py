import requests


def main():
    google_response = requests.get("https://google.com")
    print(google_response.status_code)
    print(google_response.text)


if __name__ == "__main__":
    main()
