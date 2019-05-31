import laptop


def main():
    lapi_list = []
    for count in range(1, 3):
        name = input("\nEnter laptop name:")
        ram = input("Enter RAM size:")
        hdd = input("Enter hdd size:")

        uknown = laptop.Machine_specs(name, ram, hdd)

        lapi_list.append(uknown)

    for item in lapi_list:
        print("++++++++++++++++++++++++++\n")
        print(item.get_name())
        print(item.get_ram())
        print(item.get_hdd())
        

main()
