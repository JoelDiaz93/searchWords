file = open("libro.txt", encoding="utf")
libro = file.read()
harry = libro.count("Harry")
potter = libro.count("Potter")
nino = libro.count("child")
file.close()
print("Harry: ",harry)
print("Potter: ",potter)
print("niño: ",nino)