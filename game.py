#10 Question Game
print("Welcome to the 10 questions game! ")
total_count = 0
playing = input("Do you want to play - Yes or No: ").lower()
if playing == "Yes".lower():
    name = (input("What is your Name: ").title())
    print(f"welcome to the 10 question game {name}!")
    language = (input("Here is your first question: What language is this compiler using: "))
    if language == "Python".lower():
        total_count += 1
        print("It can bite and swallow you whole i hear, you have added 1 point")
    else:
        total_count = 0
        print("It slithers, the answer is Python")

    sponge = (input("What is full of holes but still holds water?: "))
    if sponge == "a sponge".lower() or "sponge".lower():
        total_count += 1
        print(f"So you do watch sponge bob haha, who would have figured! your total is {total_count}")
    else:
        total_count -= 1
        print(f"Its Mr. Squarepants, remember. your total is {total_count}")

    java = (input("Here is your third question: Apart from python, which other language is famous: "))
    if java == "Java".lower():
        total_count += 1
        print(f"I dont knw but, yeah sure! One point for you making it {total_count}")
    else:
        total_count -= 1
        print(f"Sorry, that is the wrong answer, the answer is Java, your total is {total_count}")

    all_of_them = (input("What month of the year has 28 days: "))
    if all_of_them == "all".lower() or "all of them".lower():
        total_count += 1
        print(f"All of them,.. now you get it! Hehe your total is {total_count}")
    else:
        total_count -= 1
        print(f"All of them hehe,.. now you getting it! Hehe, your total is {total_count}")

    doctor_away = (input("I doubt it but is it true that an apple a day keeps the....: "))
    if doctor_away == "Doctor Away".lower():
        total_count += 1
        print(f"Then we have found the cure for cancer, a mere APPLE huh! your total is {total_count}")
    else:
        total_count -= 1
        print(f"It keeps the doctor away, i still doubt it cause i still see the doctor. Your total is {total_count}")

    www = (input("Here is your sixth question: What is the short form of World Wide Web?: "))
    if www == "www".lower():
        total_count += 1
        print(f"You are a genious!. Here is another point, your total is {total_count}")
    else:
        total_count -= 1
        print(f"Sorry, that is the wrong answer, the answer is www. Your total is {total_count}")

    past_midday = (input("Here is your seventh question: On a clock, what does PM stand for?: "))
    if past_midday == "Past Midday".lower():
        total_count += 1
        print(f"It is time, Ha ha!, you have added another point time master, your total is {total_count}")
    else:
        total_count -= 1
        print(f"Sorry, that is the wrong answer, the correct answer is Past Midday. Your total is {total_count}")

    do_without = (input("Here is your eighth question: They say, when in doubt -: "))
    if do_without == "do without".lower():
        total_count += 1
        print(f"Yes, do without, cause never doubt! Another point for you youngling! your total is {total_count}")
    else:
        total_count -= 1
        print(f"Sorry, that is the wrong answer, the answer is water. Your total is {total_count}")

    harry_potter = (input("Here is your nineth question: Remember that movie about Howgwarts and the teens, what was it?: "))
    if harry_potter == "Harry Potter".lower():
        total_count += 1
        print(f"Ah yes! thanks. Been scratching my head. Also, i want a broom to fly on! Your total is {total_count}")
    else:
        total_count -= 1
        print(f"Sorry, not everyone knows 'Harry Potter', my bad!. Your total is {total_count}")

    candle = (input("Riddle me a flame cause I’m tall when I’m young, and I’m short when I’m old. What am I?: "))
    if candle == "Candle".lower():
        total_count += 1
        print(f"Yes, the wax hath burnt as shadows grow longer! your total is {total_count}")
    else:
        total_count -= 1
        print(f"Sorry, electricity makes us forget, its a candle. Your total is {total_count}")
    if total_count >= 7:
        print(f"""Thanks for playing the 10 question game.
        You have {total_count} points!""")
    else:
        print(f"""So far you have accumulated {total_count} points! 
    You can always restart and do better""")
    if playing == "No".lower():
        quit()
