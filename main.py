m1 = input("Enter marks of first student: ")
m2 = input("Enter marks of second student: ")
m3 = input("Enter marks of third student: ")
m4 = input("Enter marks of fourth student: ")
m5 = input("Enter marks of fifth student: ")
m6 = input("Enter marks of sixth student: ")

m1 = int(m1)
m2 = int(m2)
m3 = int(m3)
m4 = int(m4)
m5 = int(m5)
m6 = int(m6)

allmarks = [m1, m2, m3, m4, m5, m6]

allmarks.sort()
print(allmarks)
