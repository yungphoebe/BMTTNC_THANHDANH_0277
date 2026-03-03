def dao_nguoi_chuoi(chuoi):
    return chuoi[::-1]
input_string = input("Moi nhap chuoi can dao nguoc: ")
print("chuoi dao nguoc la:", dao_nguoi_chuoi(input_string))