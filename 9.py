names = ["isafi", "rajin", "tamim", "saleh"]

def check_for_name(name, names):
    return (name in names)

names.remove("rajin")

print(check_for_name("rajin", names))
