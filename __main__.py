from urllib import request, response


def main():
    google_response = request.urlopen("https://google.com")
    print(google_response.getcode())
    print(google_response.read())


if __name__ == "__main__":
    main()
