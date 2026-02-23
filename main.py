import product_manager as pm

def main():
    # Tải dữ liệu cũ lên khi mở app
    ds_san_pham = pm.load_data()

    while True:
        print("\n--- MENU QUẢN LÝ KHO HÀNG ---")
        print("1. Hiển thị danh sách")
        print("2. Thêm sản phẩm")
        print("3. Sửa sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Tìm kiếm theo tên")
        print("6. Lưu vào file")
        print("0. Thoát")
        
        chon = input("Chọn chức năng (0-6): ")

        if chon == '1':
            pm.display_all_products(ds_san_pham)
        elif chon == '2':
            ds_san_pham = pm.add_product(ds_san_pham)
        elif chon == '3':
            ds_san_pham = pm.update_product(ds_san_pham)
        elif chon == '4':
            ds_san_pham = pm.delete_product(ds_san_pham)
        elif chon == '5':
            pm.search_product_by_name(ds_san_pham)
        elif chon == '6':
            pm.save_data(ds_san_pham)
        elif chon == '0':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()