dec = int(input("Enter a decimal number: ")) # รับค่าเลขฐาน 10 จากคีย์บอร์ด

# แปลงเลขฐาน และเติม [2:] เพื่อตัดสัญลักษณ์ 0b, 0o, 0x ด้านหน้าออก
conv_to1 = bin(dec)[2:] # แปลงเป็นเลขฐาน 2
conv_to2 = oct(dec)[2:] # แปลงเป็นเลขฐาน 8
conv_to3 = hex(dec)[2:] # แปลงเป็นเลขฐาน 16

print("Binary Number :", conv_to1) # แสดงผลลัพธ์ฐาน 2
print("Octal Number :", conv_to2) # แสดงผลลัพธ์ฐาน 8
print("Hexadecimal Number :", conv_to3) # แสดงผลลัพธ์ฐาน 16
print("สร้างโดย : นายณรงค์ฤทธิ์ อาจองค์ รหัส 694245003")