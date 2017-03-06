def alt(s1, s2):

    if s1  == " ":
        return " "
    elif s2 == "":
        return " "
    else:
        return s1[0] + s2[0] + alt(s1[1:], s2[1:])
