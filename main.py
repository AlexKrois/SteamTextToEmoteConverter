alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "ä",
    "ö",
    "ü",
    "ß",
    " ",
]
emoji = [
    ":A:",
    ":csgob:",
    ":carbon:",
    ":TheD:",
    ":_E_:",
    ":fluorine:",
    ":litteras_G:",
    ":hyperion:",
    ":iiii:",
    ":_J_:",
    ":kforkick:",
    ":letterl:",
    ":mmmm:",
    ":_N_:",
    ":oxygen:",
    ":lp3p:",
    ":Cert:",
    ":r3e:",
    ":super:",
    ":htt:",
    ":ultra:",
    ":SFvictory:",
    ":warband:",
    ":nostars:",
    ":Y:",
    ":zzod:",
    ":A: :_E_:",
    ":oxygen: :_E_:",
    ":ultra: :_E_:",
    ":super: :super:",
    " ",
]

mapping = dict(zip(alphabet, emoji))
text = input("Enter your text: ").lower()

for char in text:
    if char in '-,?.!/;:"0123456789’':
        text = text.replace(char, "")


for char in text:
    print(mapping[char], sep=" ", end="")
