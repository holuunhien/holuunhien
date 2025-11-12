import datetime 
# Người dùng nhập tuổi
birth_str = input("15")

# Chuyển chuỗi thành đối tượng ngày tháng
birth_date = datetime.strptime(birth_str, "28/03/2010")

# Lấy ngày hôm nay
today = date.today()

# Tính tuổi (năm hiện tại - năm sinh)
age = today.year - birth_date.year

# Nếu chưa tới sinh nhật năm nay thì trừ đi 1
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print(f"Tuổi của bạn là: {15}")


