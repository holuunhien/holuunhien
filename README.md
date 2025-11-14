

🎮 Python & JavaScript WebGame Toolkit

Bộ công cụ dành cho phát triển web game, bao gồm các script Python và mã JavaScript hỗ trợ gameplay, macro, custom UI và xử lý dữ liệu.


---

📑 Mục lục

Giới thiệu

Cấu trúc dự án

Python Scripts

JavaScript Scripts

Hướng dẫn sử dụng

Đóng góp

Giấy phép



---

🚀 Giới thiệu

Repo này tập hợp những đoạn mã hữu ích cho:

Mini web game hoặc game chạy qua trình duyệt

Tạo macro tự động thao tác

Tùy chỉnh UI/UX của trang game

Xử lý dữ liệu, log, tính toán server-side bằng Python


Tất cả được tối ưu để dễ hiểu, dễ mở rộng và dùng trực tiếp trong các dự án hoặc game browser.


---

📁 Cấu trúc dự án

/python/
    ├── data_handler.py      # Đọc ghi dữ liệu, config
    ├── game_logic.py        # Tính toán gameplay
    ├── utils.py             # Các hàm phụ trợ

/js/
    ├── macro.js             # Macro auto trong web game
    ├── ui-custom.js         # Thay đổi màu, UI, hiệu ứng
    ├── input-handler.js     # Bắt phím, gán hotkey
README.md


---

🐍 Python Scripts

1. data_handler.py

Quản lý đọc / ghi dữ liệu, tối ưu cho log hoặc config.

import json

def load_config(path):
    with open(path, "r") as f:
        return json.load(f)

def write_log(msg):
    with open("log.txt", "a") as f:
        f.write(msg + "\n")


---

2. game_logic.py

Chứa các thuật toán mô phỏng logic game.

def calc_damage(power, armor):
    return max(0, power - armor)


---

3. utils.py

Hỗ trợ chung.

def clamp(n, min_n, max_n):
    return max(min_n, min(n, max_n))


---

🌐 JavaScript Web Scripts

1. macro.js

Macro thao tác nhanh cho web game (ví dụ: auto eject, auto split).

document.addEventListener("keydown", (e) => {
    if (e.key === "E") {
        for (let i = 0; i < 5; i++) {
            window.dispatchEvent(new KeyboardEvent("keydown", { key: "w" }));
        }
    }
});


---

2. ui-custom.js

Thay đổi UI, màu sắc, hiệu ứng trong game.

function setNameColor(color) {
    const name = document.querySelector("#player-name");
    if (name) name.style.color = color;
}


---

3. input-handler.js

Xử lý phím, dùng cho macro hoặc gameplay smooth hơn.

window.addEventListener("keydown", (e) => {
    if (e.key === " ") console.log("Split triggered!");
});


---

⚙️ Hướng dẫn sử dụng

⚡ Dùng Python

python3 yourscript.py

🌐 Dùng JavaScript

Dành cho Tampermonkey hoặc web game:

1. Cài Tampermonkey (Chrome/Firefox)


2. Tạo script mới


3. Dán nội dung file .js


4. Lưu là chạy




---

🤝 Đóng góp

Pull requests luôn được chào đón!
Bạn có thể:

Thêm tính năng

Tối ưu code

Báo lỗi (Issues)

Cải thiện tài liệu



---

📜 Giấy phép

MIT License — tự do sử dụng và phát triển.

