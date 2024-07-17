import json

import requests
from bs4 import BeautifulSoup


class EbayScrapper:
    def __init__(self, link):
        self.__link = link
        self.__page = requests.get(self.__link).text
        self.__soup = BeautifulSoup(self.__page, "html.parser")
        self.data = {}
        pass

    def print_data(self):
        name_tag = self.__soup.find('h1', class_="x-item-title__mainTitle").find('span')
        price_tag = self.__soup.find('div', class_='x-price-primary').find('span')
        shipping_tag = self.__soup.find('div', class_='ux-layout-section ux-layout-section--shipping').find('span', class_="ux-textspans ux-textspans--BOLD ux-textspans--NEGATIVE")

        self.data["name"] = name_tag.text
        self.data["price"] = float(price_tag.text[4:])
        self.data["shipping"] = shipping_tag.text

        print(self.data)

    def write_to_file(self, filename):
        with open(filename + ".json", 'w') as file:
            json.dump(self.data, file)


es = EbayScrapper("https://www.ebay.com/itm/116195101560?itmmeta=01J30P7TZ05EN64DH0A12MTYKW&hash=item1b0dc48b78:g:~v8AAOSw7lFmUrxQ&itmprp=enc%3AAQAJAAAA0DxBkgil%2FBmh5h%2FPMZIG3yc9%2FpYnyM2LOtJsi2IrdCzwXdxQHGPqQgmDjZY8qYqpf7LK9Yz8yTsV2LmPCg8qoxxdrnkRdwPby0YlO3bYjjZUzVMo%2FMfWQ7eB6vhOSVF6Tjo5iZbukwAXaER%2FX5DWK7gymlA8jheOrXfDYGKONK14AKOH3id2NaUnHL%2B8U22xeHlvJBl3niu3kH4uy05t0UAdTT%2B2m6HimCDuJ%2FNdZ0BpJKaDufPtrClVXd9Xh8EhaGzKuqIid6%2FvG6D0bn4IkVc%3D%7Ctkp%3ABFBM6q-flphk")
es.print_data()
es.write_to_file("data")