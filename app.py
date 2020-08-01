while True:
    words = input("Sag etwas!\n").lower()
    if "hallo" in words:
        print("Hallo dir auch!")
    elif "wie geht's" in words:
        print("Alles gut, danke!")
    elif "tschuss" in words:
        print("Bis bald!")
        break
    else:
        print("He?")
