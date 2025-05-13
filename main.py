from password_generator import GeneratePassword


password = GeneratePassword(length=8, letters_p=50, digits_p=30, punctuation_p=20)
print(password.generate())
password.save_to_file(lines_num=100)