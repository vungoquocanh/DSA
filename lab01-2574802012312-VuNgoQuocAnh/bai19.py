def search_student(students, target_id):
    for student in students:
        if student["maSV"] == target_id:
            print("Thông tin sinh viên tìm thấy:")
            print(f"Mã SV: {student['maSV']}")
            print(f"Họ tên: {student['ho_ten']}")
            print(f"Điểm trung bình: {student['dtb']}")
            return
    print("Không tìm thấy sinh viên có mã tương ứng.")

students_list = [
    {"maSV": "VLU01", "ho_ten": "Nguyen Van A", "dtb": 7.5},
    {"maSV": "VLU02", "ho_ten": "Tran Thi B", "dtb": 8.2},
    {"maSV": "VLU03", "ho_ten": "Le Van C", "dtb": 6.8}
]

search_student(students_list, "VLU02")