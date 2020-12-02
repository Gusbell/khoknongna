import main

def rain():
    rain_input = int(input("ปริมาณน้ำฝนเฉลี่ยต่อปี(มม.): "))
    rain_per_year = rain_input / 1000
    return rain_per_year

def receive_rain():
    print("***พื้นที่ทั้งหมด***")
    land = main.square_meter()
    rain_all = (land * rain_avarge)
    print("พื้นที่ทั้งหมด: %d ตร.ม." %land)
    print("ปริมาณน้ำฝนที่ตกในพื้นที่ตลอดปี %d ลบ.ม." %int(rain_all))
    return rain_all

def khok():
    print("***โคก***")
    land = main.square_meter()
    khok_save = int(land * (70/100) * rain_avarge)
    print("ปริมาณน้ำที่เก็บไว้ใต้ดิน = %.2f ลบ.ม." %khok_save)
    return khok_save

def na():
    print("***นา***")
    land = main.square_meter()
    na_high = float(input("ความสูงคันนา(ม.): "))
    na_save = (land * na_high * (80/100))
    print("ปริมาณน้ำในนาที่เก็บได้ %.2f ลบ.ม." %na_save)
    return na_save

def nong():
    print("***หนอง***")
    land = main.square_meter()
    nong_deep = (((all_rain_receive - (save_from_khok+save_from_na))) / (land*(70/100))) + 3
    save_from_nong = ((land*0.7) * (nong_deep-3))
    total_save = save_from_khok + save_from_na + save_from_nong
    total_percent_save = (total_save / all_rain_receive) * 100
    print("หนองต้องลึก %.2f ม." %nong_deep)
    print("ปริมาณน้ำในหนองที่เก็บได้ %.2f ลบ.ม." %save_from_nong)
    print("ปริมาณน้ำที่เก็บได้ทั้งหมด %.2f ลบ.ม." %total_save)
    print("คิดเป็น %.2f%% ของปริมาณน้ำฝนที่ตกทั้งหมด" %total_percent_save)

    

rain_avarge = rain()

all_rain_receive = receive_rain()
save_from_khok = khok()
save_from_na = na()
nong()