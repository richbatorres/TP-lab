import csv

vremena=[]
duljine=[]
with open('file_editing', 'r', newline='') as readfile:
    reader = csv.reader(readfile, delimiter=',')
    line=0
    for row in reader:
        if line == 0:
            line += 1
        else:
            vremena.append(row[1])
            duljine.append(row[5])
            line += 1

# print(line)

preveliki=0
for i in range(len(vremena), 0, -1):
    if i-1!=0:
        vremena[i-1]=float(vremena[i-1])-float(vremena[i-2])
        if vremena[i-1]>3:
            preveliki+=1
            # vremena.pop(i-1)
    else:
        vremena[i-1]=float(vremena[i-1])
        if vremena[i-1]>5:
            preveliki+=1
            # vremena.pop(i-1)

print(max(vremena))
print(preveliki)

# print(vremena[0], vremena[1], vremena[2], len(vremena))
# print(duljine[0], duljine[1], duljine[5], len(duljine))

# with open('editing_times.csv', 'w', newline='') as writefile:
#     writer = csv.writer(writefile)
#     for i in range(0, len(vremena)):
#         writer.writerow([vremena[i]])

# with open('editing_lengths.csv', 'w', newline='') as writefile:
#     writer = csv.writer(writefile)
#     for i in range(0, len(duljine)):
#         writer.writerow([duljine[i]])

# vremena=[]
# duljine=[]
# with open('paketi_video', 'r', newline='') as readfile:
#     reader = csv.reader(readfile, delimiter=',')
#     line=0
#     for row in reader:
#         if line == 0:
#             line += 1
#         else:
#             vremena.append(row[1])
#             duljine.append(row[5])
#             line += 1

# # print(line)

# preveliki=0
# for i in range(len(vremena), 0, -1):
#     if i-1!=0:
#         vremena[i-1]=float(vremena[i-1])-float(vremena[i-2])
#         if vremena[i-1]>5:
#             # preveliki+=1
#             vremena.pop(i-1)
#     else:
#         vremena[i-1]=float(vremena[i-1])
#         if vremena[i-1]>5:
#             # preveliki+=1
#             vremena.pop(i-1)

# print(max(vremena))
# # print(preveliki)


# with open('video_times.csv', 'w', newline='') as writefile:
#     writer = csv.writer(writefile)
#     for i in range(0, len(vremena)):
#         writer.writerow([vremena[i]])

# with open('video_lengths.csv', 'w', newline='') as writefile:
#     writer = csv.writer(writefile)
#     for i in range(0, len(duljine)):
#         writer.writerow([duljine[i]])


# vremena=[]
# duljine=[]
# with open('forum_paketi', 'r', newline='') as readfile:
#     reader = csv.reader(readfile, delimiter=',')
#     line=0
#     for row in reader:
#         if line == 0:
#             line += 1
#         else:
#             vremena.append(row[1])
#             duljine.append(row[5])
#             line += 1

# # print(line)

# preveliki=0
# for i in range(len(vremena), 0, -1):
#     if i-1!=0:
#         vremena[i-1]=float(vremena[i-1])-float(vremena[i-2])
#         if vremena[i-1]>3:
#             # preveliki+=1
#             vremena.pop(i-1)
#     else:
#         vremena[i-1]=float(vremena[i-1])
#         if vremena[i-1]>5:
#             # preveliki+=1
#             vremena.pop(i-1)

# print(max(vremena))
# print(preveliki)


# with open('forum_times.csv', 'w', newline='') as writefile:
#     writer = csv.writer(writefile)
#     for i in range(0, len(vremena)):
#         writer.writerow([vremena[i]])

# with open('forum_lengths.csv', 'w', newline='') as writefile:
#     writer = csv.writer(writefile)
#     for i in range(0, len(duljine)):
#         writer.writerow([duljine[i]])