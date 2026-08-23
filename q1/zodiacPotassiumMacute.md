birth_year = int(input("Enter your year of birth: "))<br>
<br>
if birth_year < 1900:<br>
    print("Invalid Year, it should not be earlier than 1900")<br>
    exit<br>
<br>
zodiac_animals = [ <br>
    "Rat (鼠 / Shǔ)",<br>
    "Ox (牛 / Niú)", <br>
    "Tiger (虎 / Hǔ)", <br>
    "Rabbit (兔 / Tù)", <br>
    "Dragon (龙 / Lóng)", <br>
    "Snake (蛇 / Shé)", <br>
    "Horse (马 / Mǎ)", <br>
    "Goat (羊 / Yáng)", <br>
    "Monkey (猴 / Hóu)", <br>
    "Rooster (鸡 / Jī)", <br>
    "Dog (狗 / Gǒu)", <br>
    "Pig (猪 / Zhū)" <br>
]<br>
<br>
zodiac_index = (birth_year - 1900) % 12<br>
print("Your Chinese Zodiac Sign is:", zodiac_animals[zodiac_index])<br>
<br>
![A picture of output of this code](zodiac.png)
