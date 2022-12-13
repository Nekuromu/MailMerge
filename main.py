with open("Input/Names/invited_names.txt", mode="r") as invited_names:
    raw_names = invited_names.readlines()
    names = []
    for name in raw_names:
        names.append(name.strip())

    for name in names:

        with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
            lines = starting_letter.readlines()
            lines[0] = lines[0].replace("[name]", name)
            with open("Output/ReadyToSend/" + name + "_letter.txt", mode="w") as new_letter:
                new_letter.writelines(lines)
