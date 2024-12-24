print("Menu quản lý môn học")
print("1. Xem môn học")
print("2. Thêm môn học")
print("3. Chỉnh sửa môn học")
print("4. Tìm kiếm môn học")
print("5. Xóa môn học")
print("6. Đọc và lưu danh sách vào file ds_mon_hoc.csv")
ds_mon_hoc = []
while True:
    try:
        lua_chon = input("Nhập lựa chọn: ")
        lua_chon = int(lua_chon)
    except:
        print("Nhap sai yêu cầu, vui lòng nhập lại")
    else:
        if lua_chon == 1:
            print("Xem môn học")
            print("ma_mon","\t","ten_mon","\t","tong_so_sv")
            for mh in ds_mon_hoc:
                print(mh["ma_mon"],"\t",mh["ten_mon"],"\t",mh["tong_so_sv"])
        elif lua_chon == 2:
            print("Thêm môn học")
            n = input("Nhập vào số môn học cần cập nhật: ")
            n = int(n)
            for mh in range(n):
                mon_hoc = {"ma_mon": "",
                "ten_mon": "",
                "tong_so_sv": ""
                }
                print(f"Nhập mã môn học thứ {mh + 1}")
                while True:
                    mon_hoc['ma_mon'] = input("Nhập mã môn học: ")
                    if len(mon_hoc['ma_mon']) == 10:
                        break
                    else:
                        print("Mã môn học phải đúng 10 kí tự, vui lòng nhập lại")
                while True:
                    mon_hoc['ten_mon'] = input("Nhập tên môn: ")
                    if len(mon_hoc['ten_mon']) <= 20:
                        break
                    else:
                        print("Tên môn học chỉ được tối đa 20 kí tự, vui lòng nhập lại")
                while True:
                    mon_hoc['tong_so_sv'] = int(input("Nhập tổng số sinh viên: "))
                    if mon_hoc['tong_so_sv'] <= 60:
                        break
                    else:
                        print("Giới hạn tổng số sinh viên là 60, vui lòng nhập số sinh viên hợp lệ")                  
                ds_mon_hoc.append(mon_hoc)
            print("Hoàn thành nhập danh sách môn học")
        elif lua_chon == 3:
            print("Chỉnh sửa môn học")
            n = input("Nhập vào mã môn học hoặc tên môn học muốn sửa: ")
            index = -1
            if len(ds_mon_hoc) == 0:
                print("Danh sách rỗng")
            else:
                for i in range(len(ds_mon_hoc)):
                    if ds_mon_hoc[i]["ma_mon"] == n or ds_mon_hoc[i]["ten_mon"] == n:
                        print("Môn học có tồn tại")
                        index = i
                        break
                else:
                    print("Môn học không tồn tại")
                
                if index != -1:
                    print("Sua thông tin môn học:")
                    ds_mon_hoc[index]['ma_mon'] = input("Nhập mã môn học: ")
                    ds_mon_hoc[index]['ten_mon'] = input("Nhập tên môn học: ")
                    ds_mon_hoc[index]['tong_so_sv'] = input("Nhập mã tổng số sinh viên: ")
        elif lua_chon == 4:
            print("Tìm kiếm môn học")
            n = input("Nhập vào mã môn học hoặc tên môn học muốn tìm kiếm: ")
            for mh in ds_mon_hoc:
                if n in mh['ma_mon'] or n in mh['ten_mon']:
                    print(f"Môn học tìm thấy: Mã môn: {mh['ma_mon']}, Tên môn: {mh['ten_mon']}, Tổng số sinh viên: {mh['tong_so_sv']}")
                    break
            else:
                print("Không tìm thấy môn học")
        elif lua_chon == 5:
            print("Xóa thông tin môn học")
            n = input("Nhập vào mã môn học hoặc tên môn học muốn xóa: ")
            index = -1
            if len(ds_mon_hoc) == 0:
                print("Danh sách rỗng")
            else:
                for i in range(len(ds_mon_hoc)):
                    if ds_mon_hoc[i]["ma_mon"] == n or ds_mon_hoc[i]["ten_mon"] == n:
                        print("Môn học có tồn tại")
                        index = i
                        break
                else:
                    print("Môn học không tồn tại")
                    
                if index != -1:
                    ds_mon_hoc.remove(ds_mon_hoc[index])   
                    print("Tiến hành xóa môn học thành công")
        else:
            print("Đọc và lưu danh sách vào file ds_mon_hoc.csv")