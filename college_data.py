import csv

universityInfo = [['INSTNM', 'DEBT_MDN', 'COSTT4_A', 'ADM_RATE', 'SAT_AVG', 'UGDS', 'AVGFACSAL', 'MD_EARN_WNE_P10']]

with open('Data/MERGED2013_14_PP.csv', newline='', encoding='latin1') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        universityInfo.append(
            [row['INSTNM'], (row['DEBT_MDN']), (row['COSTT4_A']), row["ADM_RATE"], row["SAT_AVG"], row["UGDS"],
             row["AVGFACSAL"], (row["MD_EARN_WNE_P10"])])
print(universityInfo)

with open('college_data_processed.csv', 'w', newline='') as file:
    file.truncate()
    writer = csv.writer(file)
    writer.writerows(universityInfo)

with open('Data/MERGED2013_14_PP.csv', newline='', encoding='latin1') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        universityInfo.append(
            [row['INSTNM'], (row['DEBT_MDN']), (row['COSTT4_A']), row["ADM_RATE"], row["SAT_AVG"], row["UGDS"],
             row["AVGFACSAL"], (row["MD_EARN_WNE_P10"])])
print(universityInfo)

