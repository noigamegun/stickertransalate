import requests
from colorama import Fore, Back, Style

print(Fore.GREEN + "Welcome to Sticker Transalate!")
print(Fore.GREEN + "This tool will help you find the name and stock of a sticker from its non-human-readable SKUs.")
print(Fore.GREEN + "Please enter the SKU of the sticker you want to find.")
# reset color
print(Style.RESET_ALL)


debug = False
api_url = 'https://arcade-stickers.hackclub.dev/api/skus/all'
try:
    print("Fetching data from the API...")
    json = requests.get(url=api_url).json()
except requests.exceptions.RequestException as e:
    print(Fore.RED + "Failed to fetch data from the API. Please try again later.")
    if debug:
        print(e)
    exit()

if debug:
    print(json)

while True:
    print("\n")
    sku_input = input("Enter the SKU of the sticker. (Something Like Sti/Foo/Bar) or type 'exit' to quit: ")
    if sku_input.lower() == 'exit':
        break

    print("Finding Sticker")
    print("\n")

    # Iterate through the items to find the matching SKU
    item_found = False
    for item in json['items']:
        if item['sku'] == sku_input:
            print(Fore.GREEN + "Item Found!")
            print(Style.RESET_ALL)
            print(f"Name: {item['name']}")
            print(f"Stock: {item['stock']}")
            print(f"Sticker Preview: {item['picture']}")
            if item['stock'] == 0:
                print(Fore.RED + "This sticker is out of stock. You will likely have to wait for a restock. But, it could also be discontinued. :()")
            elif item['stock'] < 30:
                print(Fore.YELLOW + "This sticker is low in stock. You should get it soon before it runs out.")
            item_found = True
            break

    if not item_found:
        print(Fore.RED + "SKU not found.")
    print(Style.RESET_ALL)