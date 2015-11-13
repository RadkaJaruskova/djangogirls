jmeno = "Radka"
prijmeni = "Jaruskova"
if prijmeni == "Jaruskova" and jmeno == "Katka":
    if jmeno == "Radka":
        print("Radka")
    else:
        print("Krestni jmeno neznam")
elif jmeno == "Katka":
    print("Katka")
elif 8 > 10:
    print("toto se nemuze vypsat")
elif 10 < 8:
    print("toto je pravda")
else:
    print("Jmeno je " + jmeno + " " + prijmeni)




def hi(jmeno):
    print("Ahoj " + jmeno + "!")


hi("Radko")


girls = ["Marusko", "Evo", "Vladko"]

for girl in girls:
    hi(girl)

for i in range(2, 5):
    hi(str(i))
