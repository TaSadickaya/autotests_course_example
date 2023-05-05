link = "C:\python\work.txt"
link2 = link.replace(":", "").split('\\')
link3 = link2[-1].split(".")
print(link3[0])
print(link2[0])
print(link2[1])