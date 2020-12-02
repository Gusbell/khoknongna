people = int(input("จำนวนคนในครอบครัว: "))
print(people)
rice = (people*0.3) * 365 * 2
#365 days/year *2เป็นข้าวเปลือก
print("ต้องมีข้าวเปลือก %d กก.ต่อปี" %int(rice))
