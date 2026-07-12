
def main():
    print("Malaria Dosing Program")
    print()
    print("What drug do you prefer?")
    print()
    list_1 = ["Coartem", "Lufart", "Lonart", "Malar 2"]
    list_2 = ["D-Artepp", "P-Alaxin"]
    list_3 = ["Sunat", "TesquinCare"]

    while True:
        print()
        what_drug1 = input("1)Artesunate/Amodiaquine ,2)Artemether/Lumefantrine ,3)Dihydroartemisin-Piperaquine? ")

        if what_drug1 == "2":
            print()
            what_weight = float(input("What is the weight in kg? "))
            print()
            if 5 <= what_weight < 14.5:
                print("One 20/120mg tablet 2 times daily for 3 days")
            elif 14.5 <= what_weight < 24.5:
                print("One 40/240mg tablet 2 times daily for 3 days")
            elif 24.5 <= what_weight < 34.5:
                print("One 60/360mg tablet 2 times daily for 3 days")
            elif what_weight >= 34.5:
                print("One 80/480mg tablet 2 times daily for 3 days")
            print("Brands:" + str(list_1))

        elif what_drug1 == "1":
            print()
            what_weight = float(input("What is the weight in kg? "))
            print()
            if what_weight < 9:
                print("One 25/67.5mg tablet once daily for 3 days")
            elif 9 <= what_weight < 18:
                print("One 50/135mg tablet once daily for 3 days")
            elif 18 <= what_weight < 35.5:
                print("One 100/270mg tablet once daily for 3 days")
            elif what_weight >= 35.5:
                print("Two 100/270mg tablets once daily for 3 days")
            print("Brands:" + str(list_3))

        elif what_drug1 == "3":
            print()
            what_weight = float(input("What is the weight in kg? "))
            print()
            if 17 <= what_weight < 25:
                print("One 60/480mg tablet per day for 3 days")
            elif 25 <= what_weight < 36:
                print("Option 1)40MG/320MG Option 2)80/640mg")
                which_dose_DHAP = input("Which option do you prefer? ")
                if which_dose_DHAP == "1":
                    print("Two 40/320mg tablets per day for 3 days")
                elif which_dose_DHAP == "2":
                    print("One 80/640mg tablet per day for 3 days")
            elif 36 <= what_weight < 60:
                print("Option 1)40MG/320MG Option 2)60/480mg Option 3)80/640mg")
                which_dose_DHAP = input("Which option do you prefer? ")
                if which_dose_DHAP == "1":
                    print("Three 40/320mg tablets per day for 3 days")
                elif which_dose_DHAP == "2":
                    print("Two 60/480mg tablets for 3 days")
                elif which_dose_DHAP == "3":
                    print("One and half tablet of 80/640mg per day for 3 days")
            elif 60 <= what_weight < 80:
                print("Option 1)40MG/320MG Option 2)80/640mg")
                which_dose_DHAP = input("Which option do you prefer? ")
                if which_dose_DHAP == "1":
                    print("Four 40/320mg tablets per day for 3 days")
                elif which_dose_DHAP == "2":
                    print("Two 80/640mg tablets per day for 3 days")
            elif what_weight >= 80:
                print("Option 1)80/640mg Option 2)40/320mg")
                which_dose_DHAP = input("Which option do you prefer? ")
                if which_dose_DHAP == "1":
                    print("Two and a half tablets of 80/640mg per day for 3 days")
                elif which_dose_DHAP == "2":
                    print("Five 40/320mg tablets per day for 3 days")
            print("Brands:" + str(list_2))



if __name__ == "__main__":
    main()