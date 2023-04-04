import random

# Khởi tạo một giải pháp ngẫu nhiên


def generate_random_solution(items):
    solution = []
    # Chọn ngẫu nhiên các vật phẩm để đưa vào giải pháp
    for i in range(len(items)):
        solution.append(random.randint(0, 1))
    return solution

# Tính giá trị và khối lượng của một giải pháp


def calculate_fitness(solution, items, max_weight):
    total_value = 0
    total_weight = 0
    for i in range(len(items)):
        if solution[i] == 1:
            total_value += items[i][1]
            total_weight += items[i][2]
    # Nếu giải pháp đưa ra lớn hơn ràng buộc cho phép sẽ trả về giá trị 0
    if total_weight > max_weight:
        return 0
    return total_value

# Tạo một giải pháp mới bằng cách thay thế một vật phẩm trong túi bằng một vật phẩm khác


def get_neighbour(solution):
    # Copy giải pháp hiện tại
    neighbour = solution.copy()
    # Tạo ra giải pháp mới bằng cách thêm hoặc bớt 1 sản phẩm bất kỳ
    index = random.randint(0, len(solution) - 1)
    neighbour[index] = 1 - neighbour[index]
    return neighbour

# Áp dụng thuật toán Hill Climbing để tìm giải pháp tối ưu


def hill_climbing(items, max_weight):
    # Khởi tạp một giải pháp ngẫu nhiên
    current_solution = generate_random_solution(items)
    # Tính toán giá trị của giải pháp ngẫu nhiên
    current_fitness = calculate_fitness(current_solution, items, max_weight)
    i = 0
    # Chọn số lần thử nghiệm các giải pháp mới
    while i < 99999:
        i += 1
        # Tạo một giải pháp mới dựa trên giải pháp hiện tại
        neighbour = get_neighbour(current_solution)
        # Tính toán giải pháp hiện tại
        neighbour_fitness = calculate_fitness(neighbour, items, max_weight)
        # So sánh giá trị của giải pháp mới với giải pháp hiện tại
        if neighbour_fitness > current_fitness:
            print(current_solution, current_fitness)
            current_solution = neighbour
            current_fitness = neighbour_fitness
    return current_solution, current_fitness

# Giao diện


def interface():
    n = int(input("Hãy nhập số lượng vật phẩm: "))
    w = int(input("Hãy nhập giới hạn khối lượng của túi: "))
    items = []
    for i in range(n):
        while True:
            try:
                name = input("\nNhập tên vật phẩm thứ {0}: ".format(i+1))
                vi = int(input("Nhập giá trị của vật phẩm: "))
                wi = int(input("Nhập khối lượng của vật phẩm: "))
                items.append((name, vi, wi))
                break
            except:
                print("Vui lòng nhập lại.")
    return items, w


while True:
    try:
        check = int(
            input("Nhấn 0 để sử dụng ví dụ có sẵn, 1 để nhập thủ công. Cheers !!! : "))
        if check != 0 and check != 1:
            raise
        else:
            break
    except:
        print("Vui lòng nhập 0 hoặc 1")

if check == 0:
    # Định nghĩa các tham số của bài toán
    items = [("Phone", 10, 5), ("Keyboard", 20, 10), ("Laptop", 15, 15),
             ("PC", 30, 20), ("Fridge", 40, 20), ("Air-conditioner", 25, 25)]
    max_weight = 70
else:
    items, max_weight = interface()

# Chạy thuật toán Hill Climbing và in ra kết quả
best_solution, best_fitness = hill_climbing(items, max_weight)
print("\nBest solution: ", best_solution)
print("Best fitness: ", best_fitness)
for i in range(len(items)):
    if best_solution[i] == 1:
        print("-", items[i][0])
