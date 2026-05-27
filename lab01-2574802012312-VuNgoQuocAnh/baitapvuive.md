# Vu Ngo Quoc Anh-2574802012312
# bai 1

Thuật toán tìm kiếm tuyến tính:
-
- Hoạt động bằng cách duyệt lần lượt từng phần tử trong mảng 
từ đầu đến cuối để kiểm tra phần tử cần tìm có xuất hiện trong mảng hay không.
- Khi duyệt gặp phần từ bằng giá trị cần tìm thì trả về vị trí của phần tử đó.
- Khi duyệt hết mảng vẫn không tìm thấy sẽ trả kết luận phần tử không tồn tại trong mảng.

INPUT: 
- Mảng a = [7, 3, 9, 12, 5]
- Giá trị cần tìm x = 12

OUTPUT: 
- Vị trí của giá trị x trong mảng nếu tìm thấy.
- Nếu không tìm thấy sẽ trả về -1

-> Vị trí của giá trị 12 trong mảng nếu tìm thấy là: 3

Thuật toán dừng: 
- Thuật toán sẽ dừng trong hai trường hợp:
	+ Trường hợp 1: Tìm thấy phần tử.
	+ Trường hợp 2: Duyệt hết mảng nhưng không tìm thấy phần tử.

# Bai 2
-
- Mô phỏng tìm x = 5 trong mảng A = [7, 3, 9, 12, 5, 8, 1]:

- Bước 1: Chỉ số i = 0, giá trị A[0] = 7. So sánh 7 == 5 (Sai). Kết luận: Tiếp tục tìm kiếm.

- Bước 2: Chỉ số i = 1, giá trị A[1] = 3. So sánh 3 == 5 (Sai). Kết luận: Tiếp tục tìm kiếm.

- Bước 3: Chỉ số i = 2, giá trị A[2] = 9. So sánh 9 == 5 (Sai). Kết luận: Tiếp tục tìm kiếm.

- Bước 4: Chỉ số i = 3, giá trị A[3] = 12. So sánh 12 == 5 (Sai). Kết luận: Tiếp tục tìm kiếm.

- Bước 5: Chỉ số i = 4, giá trị A[4] = 5. So sánh 5 == 5 (Đúng). Kết luận: Tìm thấy phần tử. Thuật toán dừng.

-> Giá trị hàm trả về là: 4

# bai 3 
Số phép so sánh cần thực hiện với mảng A = [7, 3, 9, 12, 5, 8, 1]:

- (a) Với x = 7: Số phép so sánh là 1 (vì 7 nằm ở ngay vị trí đầu tiên).

- (b) Với x = 1: Số phép so sánh là 7 (vì 1 nằm ở vị trí cuối cùng).

- (c) Với x = 100: Số phép so sánh là 7 (vì phải duyệt qua toàn bộ mảng mà không thấy).

Nhận xét:

Vị trí của phần tử quyết định số phép so sánh. Phần tử nằm càng gần đầu mảng thì số phép so sánh càng ít. Phần tử nằm ở cuối mảng hoặc không có trong mảng thì số phép so sánh là nhiều nhất.
# bai 4
-Số phép so sánh cần thực hiện với mảng A = [7, 3, 9, 12, 5, 8, 1]:

- (a) Với x = 7: Số phép so sánh là 1 (vì 7 nằm ở ngay vị trí đầu tiên).

- (b) Với x = 1: Số phép so sánh là 7 (vì 1 nằm ở vị trí cuối cùng).

- (c) Với x = 100: Số phép so sánh là 7 (vì phải duyệt qua toàn bộ mảng mà không thấy).

Nhận xét:

Vị trí của phần tử quyết định số phép so sánh. Phần tử nằm càng gần đầu mảng thì số phép so sánh càng ít. Phần tử nằm ở cuối mảng hoặc không có trong mảng thì số phép so sánh là nhiều nhất.
# bai 5 Tìm kiếm tuyến tính:

- Không bắt buộc mảng phải được sắp xếp trước.

- Giải thích: Vì thuật toán hoạt động theo cách kiểm tra tuần tự từng phần tử từ đầu đến cuối mảng, nên dữ liệu lộn xộn hay đã sắp xếp thì thuật toán vẫn chạy được bình thường.

- So sánh ngắn gọn với tìm kiếm nhị phân:

- Tìm kiếm tuyến tính:

- Điều kiện áp dụng: Mảng bất kỳ, không cần sắp xếp.

- Độ phức tạp thời gian: O(n)

- Tìm kiếm nhị phân:

- Điều kiện áp dụng: Mảng bắt buộc phải được sắp xếp trước.

- Độ phức tạp thời gian: O(log n)