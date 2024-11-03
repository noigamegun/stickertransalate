try:
    import requests
    from colorama import Fore, Style
except ImportError:
    print("[!] Failed to import required libraries. Please run 'pip install -r requirements.txt' to install the required libraries.")
    exit()

print(Fore.WHITE + "=" * 40)
print(Fore.GREEN + "Welcome to Sticker Translate!")
print(Fore.GREEN + "This tool will help you find the name and stock of a sticker from its non-human-readable SKUs.")
print(Fore.GREEN + "Please enter the SKU of the sticker you want to find.")
print(Fore.WHITE + "=" * 40)
# reset color
print(Style.RESET_ALL)


debug = False

api_url = 'https://arcade-stickers.hackclub.dev/api/skus/all'


try:
    print("Fetching data from the API...")
    json = requests.get(url=api_url).json()

    if debug:
        with open('debugfetch.json', 'w') as f:
            print(Fore.YELLOW + "[DEBUG] Writing API response to debugfetch.json")
            f.write(json)

except requests.exceptions.RequestException as e:
    print(Fore.RED + "[!] Failed to fetch data from the API. Please try again later. If the api URL has changed, Change the 'api_url' variable in the script.")
    if debug:
        print(Fore.RED + "[DEBUG] Error:")
        print(e)
        print(Fore.RED + "[DEBUG] Writing error to debugerror.txt")
        with open ('debugerror.txt', 'w') as f:
            f.write(e)
    exit()

if debug:
    print(Fore.YELLOW + "[DEBUG] API Response:")
    print(json)

try:
    while True:
        print("\n")
        sku_input = input("Enter the SKU of the sticker. (Something Like Sti/Foo/Bar) or type 'all' to list every stickers fetched or type 'exit' to quit: ")
        if sku_input.lower().strip() == 'exit':
            break
        if sku_input.lower().strip() == 'all':
            print("\n")
            print(Fore.GREEN + "Listing all stickers...")
            print(Style.RESET_ALL)
            for item in json['items']:
                print(f"SKU: {item['sku']}")
                print(f"Name: {item['name']}")
                print(f"Stock: {item['stock']}")
                print(f"Sticker Preview: {item['picture']}")
                if item['stock'] == 0:
                    print(Fore.RED + "This sticker is out of stock. You will likely have to wait for a restock. But, it could also be discontinued. :(")
                elif item['stock'] < 100:
                    print(Fore.YELLOW + "This sticker is low in stock. You should get it soon before it runs out.")
                print("\n")
                print(Style.RESET_ALL)
            continue

        print("Finding Sticker...")
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
            print(Fore.RED + "[!] SKU not found.")
        print(Style.RESET_ALL)
except KeyboardInterrupt:
    print("\n")
    print(Fore.RED + "[!] Exiting...")
    exit()

print(Fore.GREEN + "Thank you for using Sticker Translate!")
print(Fore.GREEN + "Goodbye!")
print(Style.RESET_ALL)
exit()

print(Fore.RED + "[!] Script call 'exit()' but failed. Something is very wrong with your python installation. Please check your python installation.")
print(Fore.RED + "Please terminate the script manually.")   
print(Style.RESET_ALL)