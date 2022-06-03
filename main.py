from hashlib import sha256
import getpass

final = ""
final += input("Skriv inn domene (eks. lysakermoen.com: ")
final += input("Skriv inn brukernavn: ")
final += getpass.getpass("Skriv inn passord: ")

print(sha256(final.encode('utf-8')).hexdigest())
