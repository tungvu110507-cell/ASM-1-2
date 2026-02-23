import json
import os

def load_data():
    """Đọc dữ liệu từ file products.json."""
    try:
        if os.path.exists("products.json"):
            with open("products.json", "r", encoding="utf-8") as f:
                return json.load(f)
        return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(products):
    """Lưu danh sách vào file JSON."""
    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)
    print("\n[ Đã lưu dữ liệu vào file thành công!")

def add_product(products):
    print("\n--- NHẬP THÔNG TIN SẢN PHẨM MỚI ---")
    name = input("Tên sản phẩm: ")
    brand = input("Thương hiệu: ")
    try:
        price = int(input("Giá: "))
        quantity = int(input("Số lượng tồn: "))
    except ValueError:
        print("Lỗi: Giá và số lượng phải là số nguyên!")
        return products

    # Tự động tạo ID dựa trên số lượng hiện có
    new_id = f"LT{len(products) + 1:02d}"
    
    new_item = {
        "id": new_id,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity
    }
    products.append(new_item)
    print(f"Thêm thành công! Mã SP là: {new_id}")
    return products

def display_all_products(products):
    if not products:
        print("\n[!] Kho hàng trống.")
        return
    print("\n" + "="*70)
    print(f"{'ID':<6} | {'Tên sản phẩm':<25} | {'Hiệu':<10} | {'Giá':<10} | {'SL'}")
    print("-" * 70)
    for p in products:
        print(f"{p['id']:<6} | {p['name']:<25} | {p['brand']:<10} | {p['price']:<10} | {p['quantity']}")
    print("="*70)

def search_product_by_name(products):
    keyword = input("\Vui lòng nhập tên sản phẩm: ").lower()
    results = [p for p in products if keyword in p['name'].lower()]
    display_all_products(results)

def update_product(products):
    target_id = input("\nNhập mã ID sản phẩm cần sửa: ").upper()
    for p in products:
        if p['id'] == target_id:
            print(f"Đang sửa: {p['name']}")
            p['name'] = input("Tên mới: ") or p['name']
            p['brand'] = input("Thương hiệu mới: ") or p['brand']
            try:
                p['price'] = int(input("Giá mới: ") or p['price'])
                p['quantity'] = int(input("Số lượng mới: ") or p['quantity'])
            except ValueError:
                print("Lỗi định dạng số!")
            return products
    print("Không tìm thấy ID!")
    return products

def delete_product(products):
    target_id = input("\nNhập mã ID cần xóa: ").upper()
    for i, p in enumerate(products):
        if p['id'] == target_id:
            products.pop(i)
            print("Đã xóa sản phẩm.")
            return products
    print("Không tìm thấy ID để xóa.")

    return products

