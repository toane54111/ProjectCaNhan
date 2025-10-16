# 🎓 BÀI TẬP LỚN CÁ NHÂN MÔN TRÍ TUỆ NHÂN TẠO
## Bài toán 8 Quân Hậu - 16 Thuật toán AI

**Sinh viên thực hiện:** Trần Quang Toản  
**MSSV:** 23110158  
**Lớp:** ARIN330585_04CLC  
**Môn học:** Trí tuệ nhân tạo  
**Giảng viên hướng dẫn:** Phan Thị Huyền Trang

---

## 📋 THÔNG TIN BÀI TẬP

### Yêu cầu đề bài:
Triển khai bài toán 8 quân hậu sử dụng **16 thuật toán AI** khác nhau bao gồm:
- ✅ Tìm kiếm không có thông tin
- ✅ Tìm kiếm có thông tin  
- ✅ Thỏa mãn ràng buộc (CSP)
- ✅ Tìm kiếm cục bộ
- ✅ Tìm kiếm tiến hóa
- ✅ Tìm kiếm đồ thị

### Mục tiêu bài toán:
Đặt **8 quân hậu** trên bàn cờ 8x8 sao cho không có quân nào tấn công được quân nào khác. Quân hậu có thể di chuyển theo:
- ↔️ Hàng ngang
- ↕️ Hàng dọc  
- ↗️ Đường chéo

---

## 🚀 HƯỚNG DẪN CHẠY CHƯƠNG TRÌNH

### Bước 1: Kiểm tra yêu cầu hệ thống
```bash
# Kiểm tra Python (cần Python 3.7+)
python --version

# Kiểm tra pip
pip --version
```

### Bước 2: Cài đặt thư viện cần thiết
```bash
# Không cần cài đặt thư viện bên ngoài
# Chỉ dùng thư viện có sẵn: tkinter, time, heapq, collections, random, math, csv
```

### Bước 3: Tải code từ GitHub
```bash
# Clone repository
git clone [link-github-của-bạn]

# Di chuyển vào thư mục
cd 8-quan-hau-ai
```

---

## 🎮 CÁCH CHẠY CHƯƠNG TRÌNH

### Chạy trực tiếp file Python (KHUYẾN NGHỊ)
```bash
python 8_quan_hau.py
```

### Tính năng giao diện:
- 🖱️ **Click chuột trái** vào bàn cờ bên trái để đặt/xóa quân hậu
- 🎯 **Chọn thuật toán** bằng cách nhấn nút tương ứng
- 📊 **Xem lịch sử** các lần chạy thuật toán
- 💾 **Xuất CSV** để phân tích kết quả

---

## 📊 16 THUẬT TOÁN ĐÃ TRIỂN KHAI

### 🔍 TÌM KIẾM KHÔNG CÓ THÔNG TIN
| STT | Thuật toán | Mô tả | Đặc điểm |
|-----|-----------|-------|----------|
| 1 | **BFS** - Breadth-First Search | Tìm kiếm theo chiều rộng | Đảm bảo tìm được nghiệm ngắn nhất |
| 2 | **DFS** - Depth-First Search | Tìm kiếm theo chiều sâu | Tiết kiệm bộ nhớ |
| 3 | **DLS** - Depth-Limited Search | Tìm kiếm sâu có giới hạn | Tránh vòng lặp vô hạn |
| 4 | **IDS** - Iterative Deepening Search | Tìm kiếm sâu dần | Kết hợp ưu điểm BFS và DFS |
| 5 | **UCS** - Uniform Cost Search | Tìm kiếm chi phí đồng nhất | Tối ưu với chi phí |

### 🎯 TÌM KIẾM CÓ THÔNG TIN
| STT | Thuật toán | Mô tả | Heuristic |
|-----|-----------|-------|-----------|
| 6 | **Best-First Search** | Tham lam theo heuristic | Số xung đột |
| 7 | **A\*** - A-star Search | Tối ưu với f(n) = g(n) + h(n) | Chi phí + xung đột |

### 🔒 THỎA MÃN RÀNG BUỘC (CSP)
| STT | Thuật toán | Mô tả | Đặc điểm |
|-----|-----------|-------|----------|
| 8 | **Backtracking** | Quay lui cơ bản | Đơn giản, hiệu quả |
| 9 | **Forward Checking** | Kiểm tra tiến | Loại bỏ giá trị sớm |
| 10 | **AC-3** - Arc Consistency | Tính nhất quán cung | Thu hẹp miền giá trị |

### 🏔️ TÌM KIẾM CỤC BỘ
| STT | Thuật toán | Mô tả | Yêu cầu |
|-----|-----------|-------|---------|
| 11 | **Hill Climbing** | Leo đồi | Cần 8 quân hậu ban đầu |
| 12 | **Simulated Annealing** | Luyện kim mô phỏng | Cần 8 quân hậu ban đầu |
| 13 | **Beam Search** | Tìm kiếm chùm (k=100) | Giữ k trạng thái tốt nhất |

### 🧬 TÌM KIẾM TIẾN HÓA
| STT | Thuật toán | Mô tả | Tham số |
|-----|-----------|-------|---------|
| 14 | **Genetic Algorithm** | Thuật toán di truyền | Pop=100, Gen=1000 |

### 🌳 TÌM KIẾM ĐỒ THỊ & ĐẶCBIỆT
| STT | Thuật toán | Mô tả | Đặc điểm |
|-----|-----------|-------|----------|
| 15 | **Belief State Search** | Tìm kiếm không gian niềm tin | Cho bài toán không chắc chắn |
| 16 | **AND-OR Search** | Tìm kiếm đồ thị AND-OR | Tìm tất cả lời giải |

---

## 🎯 CÁCH SỬ DỤNG CHƯƠNG TRÌNH

### 1. Đặt trạng thái ban đầu
- Click vào **bàn cờ bên trái** để đặt quân hậu
- Click lại vào ô đã có quân hậu để xóa
- Ô màu **cam** = vị trí không an toàn

### 2. Chọn thuật toán
- Nhấn vào nút thuật toán bạn muốn thử nghiệm
- Chương trình sẽ tự động tìm kiếm nghiệm

### 3. Xem kết quả
- **Bàn cờ bên phải** hiển thị nghiệm tìm được
- Kết quả được animate từng bước
- Thông tin chi tiết hiển thị trong popup

### 4. Xem thống kê
- Nhấn **"Xem lịch sử"** để xem tất cả lần chạy
- Nhấn **"Xuất CSV"** để lưu kết quả ra file

---

## 📈 THỐNG KÊ & SO SÁNH

### Các chỉ số đo lường:
- ⏱️ **Thời gian thực thi** (giây)
- 🔢 **Số nodes explored** (số trạng thái đã duyệt)
- ✅ **Thành công/Thất bại**
- 📅 **Timestamp** (thời gian chạy)

### File CSV xuất ra bao gồm:
```csv
STT,Timestamp,Thuật toán,Số nodes,Thời gian (s),Thành công,Trạng thái ban đầu
1,2025-10-16 14:41:49,BFS,118878,6.1826,Có,0
2,2025-10-16 14:41:57,DFS,1970,4.4317,Có,0
3,2025-10-16 14:42:04,DLS,1970,3.8849,Có,0
4,2025-10-16 14:42:10,IDS,388841,10.0016,Có,0
5,2025-10-16 14:42:22,UCS,118878,6.7771,Có,0
6,2025-10-16 14:42:30,Best-First,118878,5.9232,Có,0
7,2025-10-16 14:42:37,A*,118878,6.7904,Có,0
8,2025-10-16 14:42:58,Hill Climbing,2,4.7190,Không,8
9,2025-10-16 14:43:05,Simulated Annealing,73,4.1099,Có,8
10,2025-10-16 14:43:17,Beam Search,474,4.2211,Có,1
11,2025-10-16 14:43:25,Genetic Algorithm,18100,4.4421,Có,0
12,2025-10-16 14:43:31,Belief State,1965,3.6465,Không,0
13,2025-10-16 14:43:47,AND-OR,2057,0.0409,Có,0
14,2025-10-16 14:43:53,Backtracking,114,16.3793,Có,0
15,2025-10-16 14:44:14,Forward Checking,54,13.3097,Có,0
16,2025-10-16 14:44:29,AC-3,56,16.3256,Có,0
```

---

## 📁 CẤU TRÚC FILE CODE
```
ProjectCaNhan/
├── 8Hau.py          # File chính - chạy file này
├── README.md              # Hướng dẫn (file này)
└── ket_qua_*.csv          # File kết quả (tự động tạo khi xuất)
```

### File chính bao gồm:
- ✅ 16 thuật toán AI hoàn chỉnh
- ✅ Giao diện Tkinter với 2 bàn cờ
- ✅ Hệ thống tracking (nodes, time)
- ✅ Xuất CSV và xem lịch sử
- ✅ Animate từng bước giải pháp

---

## ⚠️ LƯU Ý QUAN TRỌNG

### Yêu cầu đặc biệt của một số thuật toán:

#### 🏔️ Hill Climbing & Simulated Annealing:
- ⚠️ **Bắt buộc** phải đặt đủ **8 quân hậu ban đầu**
- Có thể đặt các quân hậu xung đột nhau (cho phép khi popup hỏi)
- Thuật toán sẽ di chuyển các quân hậu để giảm xung đột

#### 🧬 Genetic Algorithm:
- Không cần trạng thái ban đầu
- Tự sinh quần thể ngẫu nhiên

#### 🌳 AND-OR Search:
- Không dùng trạng thái ban đầu
- Luôn bắt đầu từ bàn cờ trống
- Tìm **tất cả** lời giải

#### 🔍 Beam Search:
- Cần đặt ít nhất 1 quân hậu ban đầu
- Đặt hậu theo cột tuần tự

---

## 🎨 GIAO DIỆN CHƯƠNG TRÌNH

### Layout chính:
```
┌─────────────────────────────────────────────────────┐
│  Bàn cờ BÊN TRÁI        │  Bàn cờ BÊN PHẢI          │
│  (Đặt trạng thái        │  (Hiển thị kết quả)       │
│   ban đầu)              │                            │
├─────────────────────────────────────────────────────┤
│  [BFS] [DFS] [DLS] [IDS] [UCS] [Best] [A*]         │
├─────────────────────────────────────────────────────┤
│  [Hill] [SA] [Beam] [GA] [Belief] [AND-OR]         │
│  [Backtrack] [Forward] [AC-3]                       │
├─────────────────────────────────────────────────────┤
│  [Xem lịch sử]  [Xuất CSV]                         │
└─────────────────────────────────────────────────────┘
```

### Màu sắc:
- ⬜ **Trắng/Đen**: Ô bàn cờ
- 🟧 **Cam**: Vùng không an toàn
- 👑 **Hồng**: Quân hậu (#fe37a1)

---

## ⚙️ XỬ LÝ LỖI THƯỜNG GẶP

### Lỗi 1: "No module named 'tkinter'"
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# MacOS (đã có sẵn)
# Windows (đã có sẵn với Python từ python.org)
```

### Lỗi 2: Không đặt được quân hậu
- ✅ Kiểm tra đã có dòng `ban_trai.bind("<Button-1>", an_chuot)`
- ✅ Click vào bàn cờ **bên trái**

### Lỗi 3: Thuật toán không chạy
- ✅ Chờ thuật toán trước đó chạy xong
- ✅ Các nút bị disable khi đang chạy

### Lỗi 4: Hill Climbing báo lỗi
- ✅ Đảm bảo đã đặt **đủ 8 quân hậu** trước khi chạy
- ✅ Chấp nhận đặt quân hậu xung đột khi popup hỏi

---

## 📊 KẾT QUẢ MONG ĐỢI

### Các thuật toán thành công (từ bàn trống):
✅ BFS, DFS, DLS, IDS, UCS  
✅ Best-First Search, A*  
✅ Backtracking, Forward Checking, AC-3  
✅ Beam Search, Genetic Algorithm  
✅ AND-OR Search

### Các thuật toán cần 8 quân hậu ban đầu:
⚠️ Hill Climbing (có thể bị kẹt cực trị cục bộ)  
⚠️ Simulated Annealing (tỷ lệ thành công cao hơn)

---

## 🎓 ĐIỂM MẠNH CỦA BÀI TẬP

### ✨ Tính năng nổi bật:
- 🎨 **Giao diện đồ họa** trực quan với Tkinter
- 📊 **Hệ thống tracking** đầy đủ (time, nodes)
- 💾 **Xuất CSV** để phân tích dữ liệu
- 📜 **Xem lịch sử** với thống kê tổng hợp
- 🎬 **Animation** từng bước giải pháp
- 🎯 **16 thuật toán** AI đa dạng

### 🏆 So với yêu cầu:
- ✅ Đầy đủ 16 thuật toán
- ✅ Giao diện dễ sử dụng
- ✅ Code có comment rõ ràng
- ✅ Kết quả chính xác
- ✅ Tracking hiệu năng chi tiết

---

## 🧪 CÁCH KIỂM TRA BÀI TẬP

### Test cơ bản:
```bash
# 1. Chạy chương trình
python 8Hau.py

# 2. Kiểm tra giao diện
- Thấy 2 bàn cờ
- Thấy các nút thuật toán

# 3. Test đặt quân hậu
- Click vào bàn trái → Thấy quân hậu xuất hiện
- Click lại → Quân hậu biến mất

# 4. Test thuật toán
- Không đặt quân hậu nào hoặc đặt 1 vài quân hậu không xung đột
- Nhấn nút "BFS"
- Thấy quân hậu xuất hiện trên bàn phải
- Popup hiển thị "Thành công"
```

### Test chi tiết:
```bash
# 1. Test từng thuật toán
- Chạy lần lượt 16 thuật toán
- Kiểm tra kết quả

# 2. Test xem lịch sử
- Nhấn "Xem lịch sử"
- Thấy bảng thống kê

# 3. Test xuất CSV  
- Nhấn "Xuất CSV"
- File CSV được tạo ra

# 4. Test Hill Climbing
- Đặt 8 quân hậu (cho phép xung đột)
- Nhấn "Hill Climbing"
- Thuật toán di chuyển quân hậu
```

---

## 📞 LIÊN HỆ HỖ TRỢ

Nếu gặp vấn đề khi chạy code, vui lòng liên hệ:

📧 **Email:** tranquangtoandalat@gmail.com  
📱 **SĐT:** 0389968322  
🔗 **GitHub:** [link github của bạn]

---

## 📄 GIẤY PHÉP

Bài tập cá nhân môn Trí tuệ nhân tạo - Chỉ sử dụng cho mục đích học tập.

---

## 🙏 LỜI CẢM ƠN

Cảm ơn **cô Phan Thị Huyền Trang** đã hướng dẫn và tạo điều kiện để hoàn thành bài tập này!

Cảm ơn các bạn sinh viên đã tham khảo và đóng góp ý kiến! 💪

---
