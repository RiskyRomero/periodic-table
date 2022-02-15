import os

from dict import periodic_elements


def main():
    os.system("cls")

    val = input("element: ")

    def search(arg):

        is_num = None

        if arg.isnumeric():
            is_num = True
            arg = int(arg)

        if is_num:
            for element in periodic_elements:
                if arg == element["atomic_num"]:
                    return element
        else:
            for element in periodic_elements:
                if arg.lower() in element["chem_sym"].lower():
                    return element

    value = search(val) or None

    if value:
        print("\n原子番号: {}\n記号: {}\n名前: {}\n名前 (英語): {}\n原子量: {}".format(value["atomic_num"], value["chem_sym"], value["chem_name_ja"], value["chem_name"], value["atomic_mass"]))
    else:
        print("\nみつからない; もういちどやってみて")

    input("\n続けるにはどれかキーを押してください")

    return main()


main()
