import csv

universityInfo = {}

with open('National Universities Rankings.csv', newline='', encoding='latin1') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        universityInfo[row['Name']] = [int(row['Rank']), row['Location'][-2:], int(row['Tuition and fees'][1:].replace(',',''))]

print (universityInfo)

usableData = []
listOfMajors = ["Finance", "Computer Science", "Computer Engineer", "Biomedical", "Bio", "Chem", "Mechanical", "English", "Electrical",
                "Theater", "Architecture", "Nursing", "Management", "Marketing", "History", "Psychology","Criminal", "Business",
                "Communication", "Industrial", "Sociology", "Economics", "Politic", "Art", "Math", "Language", "Design", "Music",
                "Physics", "Pharma", "Health", "Med", "Social", "Government", "Gender", "Law", "Accounting","Philosophy", "Civil",
                "Aerospace", "Petroleum","Information","Journalism", "Anthropology"]

with open('Most-Recent-Field-Data-Elements.csv', newline='', encoding='latin1') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        uni, earning = row["INSTNM"], row['MD_EARN_WNE']
        if earning != "PrivacySuppressed" and uni in universityInfo and "Bachelor" in row["CREDDESC"]:
            for maj in listOfMajors:
                major = row["CIPDESC"]
                if maj.lower() in major.lower():
                    dataR = [maj, int(earning)]
                    dataR = universityInfo[uni]+dataR
                    usableData.append(dataR)
print(usableData[0])
print("total number of columns: ",len(usableData))

with open('usuable_data_student_success.csv', 'w', newline='') as file:
    file.truncate()
    writer = csv.writer(file)
    writer.writerows(usableData)

