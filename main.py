# FOR
sentence = input("Jumlani kiriting: ")

words = sentence.split()
secret_code = "".join(word[0] for word in words)

print("Maxfiy kod:", secret_code)
