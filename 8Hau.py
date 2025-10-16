import tkinter as tk
from tkinter import messagebox
import math
import time
import heapq
from collections import deque
import random

CO = 8
O = 60
DEN = "#000000"
TRANG = "#ffffff"
HAU = "♛"
MAU_HAU = "#fe37a1"
MAU_DUONG_DI = "#90EE90"

cua_so = tk.Tk()
cua_so.title("8 Quân Hậu")
cua_so.resizable(False, False)

ban_trai = tk.Canvas(cua_so, width=CO*O, height=CO*O)
ban_trai.grid(row=0, column=0, padx=10, pady=10)

ban_phai = tk.Canvas(cua_so, width=CO*O, height=CO*O)
ban_phai.grid(row=0, column=1, padx=10, pady=10)

frame_nut_1 = tk.Frame(cua_so)
frame_nut_1.grid(row=1, column=0, columnspan=2, pady=5)

frame_nut_2 = tk.Frame(cua_so)
frame_nut_2.grid(row=2, column=0, columnspan=2, pady=5)

nut_bfs = tk.Button(frame_nut_1, text="BFS", width=12)
nut_bfs.pack(side=tk.LEFT, padx=3)

nut_dfs = tk.Button(frame_nut_1, text="DFS", width=12)
nut_dfs.pack(side=tk.LEFT, padx=3)

nut_dls = tk.Button(frame_nut_1, text="DLS", width=12)
nut_dls.pack(side=tk.LEFT, padx=3)

nut_ids = tk.Button(frame_nut_1, text="IDS", width=12)
nut_ids.pack(side=tk.LEFT, padx=3)

nut_ucs = tk.Button(frame_nut_1, text="UCS", width=12)
nut_ucs.pack(side=tk.LEFT, padx=3)

nut_best = tk.Button(frame_nut_1, text="Best-First", width=12)
nut_best.pack(side=tk.LEFT, padx=3)

nut_astar = tk.Button(frame_nut_1, text="A*", width=12)
nut_astar.pack(side=tk.LEFT, padx=3)

nut_hill = tk.Button(frame_nut_2, text="Hill Climbing", width=12)
nut_hill.pack(side=tk.LEFT, padx=3)

nut_sa = tk.Button(frame_nut_2, text="Simulated Annealing", width=12)
nut_sa.pack(side=tk.LEFT, padx=3)

nut_beam = tk.Button(frame_nut_2, text="Beam Search", width=12)
nut_beam.pack(side=tk.LEFT, padx=3)

nut_ga = tk.Button(frame_nut_2, text="Genetic Algorithm", width=12)
nut_ga.pack(side=tk.LEFT, padx=3)

nut_belief = tk.Button(frame_nut_2, text="Belief State", width=12)
nut_belief.pack(side=tk.LEFT, padx=3)

nut_and_or = tk.Button(frame_nut_2, text="AND-OR", width=12)
nut_and_or.pack(side=tk.LEFT, padx=3)

nut_backtrack = tk.Button(frame_nut_2, text="Backtracking", width=12)
nut_backtrack.pack(side=tk.LEFT, padx=3)

nut_forward = tk.Button(frame_nut_2, text="Forward Checking", width=12)
nut_forward.pack(side=tk.LEFT, padx=3)

nut_ac3 = tk.Button(frame_nut_2, text="AC-3", width=12)
nut_ac3.pack(side=tk.LEFT, padx=3)

frame_nut_3 = tk.Frame(cua_so)
frame_nut_3.grid(row=3, column=0, columnspan=2, pady=5)

nut_lich_su = tk.Button(frame_nut_3, text="Xem lịch sử", width=12)
nut_lich_su.pack(side=tk.LEFT, padx=3)

nut_xuat_csv = tk.Button(frame_nut_3, text="Xuất CSV", width=12)
nut_xuat_csv.pack(side=tk.LEFT, padx=3)

hau_dat = set()
hau_ket_qua = set()
duong_di = []
thong_ke = {
    'thoi_gian': 0,
    'so_node': 0,
    'ten_thuat_toan': '',
    'thanh_cong': False
}

lich_su_chay = []  

def ve_ban(ban, danh_sach=None, hau=None, o_duong_di=None):
    ban.delete("all")
    for r in range(CO):
        for c in range(CO):
            x0, y0 = c*O, r*O
            x1, y1 = x0+O, y0+O
            nen = TRANG if (r+c) % 2 == 0 else DEN
            if danh_sach and (r,c) in danh_sach:
                nen = "#f4ae82"
            ban.create_rectangle(x0, y0, x1, y1, fill=nen, outline="black")
    if hau:
        for (r,c) in hau:
            x = c*O + O//2
            y = r*O + O//2
            ban.create_text(x, y, text=HAU, font=("Segoe UI Symbol", int(O*0.6)),fill = MAU_HAU)

def an_chuot(event):
    c = event.x // O
    r = event.y // O
    if (r, c) in hau_dat:  
        hau_dat.remove((r, c))
    else:
        if hop_le(r, c, hau_dat):
            hau_dat.add((r, c))
        else:
            # hỏi người dùng có muốn đặt trùng để dùng cho Hill Climbing không
            dong_y = messagebox.askyesno(
                "Xác nhận",
                "Ô này không hợp lệ để đặt hậu.\nBạn có muốn đặt trùng để giải bằng Hill Climbing không?"
            )
            if dong_y:
                hau_dat.add((r, c))
    cap_nhat()

def hop_le(r, c, hau_set):
    for (rq, cq) in hau_set:
        if rq == r or cq == c:
            return False
        if abs(rq - r) == abs(cq - c):
            return False
    return True

def cap_nhat():
    ve_ban(ban_phai, hau=hau_ket_qua, o_duong_di=set(duong_di))
    khong_an_toan = set()
    for r in range(CO):
        for c in range(CO):
            if (r,c) in hau_dat or not hop_le(r, c, hau_dat):
                khong_an_toan.add((r,c))
    ve_ban(ban_trai, danh_sach=khong_an_toan, hau=hau_dat)

def chay_voi_thong_ke(func, ten_thuat_toan):
    """
    Wrapper để đo thời gian và đếm nodes cho các thuật toán
    """
    global thong_ke, lich_su_chay
    
    thong_ke = {
        'thoi_gian': 0,
        'so_node': 0,
        'ten_thuat_toan': ten_thuat_toan,
        'thanh_cong': False,
        'trang_thai_ban_dau': len(hau_dat),
        'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    thoi_gian_bat_dau = time.time()
    
    # Chạy thuật toán
    func()
    
    thoi_gian_ket_thuc = time.time()
    thong_ke['thoi_gian'] = thoi_gian_ket_thuc - thoi_gian_bat_dau
    
    # Lưu vào lịch sử
    lich_su_chay.append(thong_ke.copy())
    
    # Hiển thị kết quả
    hien_thi_thong_ke()

def hien_thi_thong_ke():
    """
    Hiển thị thống kê sau khi chạy thuật toán
    """
    msg = f"=== THỐNG KÊ ===\n"
    msg += f"Thuật toán: {thong_ke['ten_thuat_toan']}\n"
    msg += f"Thời gian: {thong_ke['thoi_gian']:.4f} giây\n"
    msg += f"Số nodes explored: {thong_ke['so_node']}\n"
    msg += f"Kết quả: {'Thành công' if thong_ke['thanh_cong'] else 'Thất bại'}"
    
    print(msg)  # In ra console

def hien_thi_duong_di(trang_thai):
    global duong_di
    duong_di = list(trang_thai)
    
    for i in range(len(duong_di) + 1):
        hau_ket_qua.clear()
        hau_ket_qua.update(duong_di[:i])
        cap_nhat()
        cua_so.update()
        time.sleep(0.25)

def dls_recursive(trang_thai_hien_tai, so_hau, gioi_han, da_tham):
    if so_hau == CO:
        return trang_thai_hien_tai, so_hau, 'found'
    
    if so_hau >= gioi_han:
        return trang_thai_hien_tai, so_hau, 'cutoff'
    
    trang_thai_tot_nhat = trang_thai_hien_tai
    so_hau_tot_nhat = so_hau
    gap_cutoff = False
    
    for r in range(CO):
        for c in range(CO):
            if (r, c) not in trang_thai_hien_tai and hop_le(r, c, trang_thai_hien_tai):
                trang_thai_moi = tuple(sorted(trang_thai_hien_tai + ((r, c),)))
                
                if trang_thai_moi not in da_tham:
                    da_tham.add(trang_thai_moi)
                    
                    ket_qua_trang_thai_moi, so_hau_moi, ket_qua = dls_recursive(
                        trang_thai_moi, so_hau + 1, gioi_han, da_tham
                    )
                    
                    if ket_qua == 'found':
                        return ket_qua_trang_thai_moi, so_hau_moi, 'found'
                    elif ket_qua == 'cutoff':
                        gap_cutoff = True
                    
                    if so_hau_moi > so_hau_tot_nhat:
                        so_hau_tot_nhat = so_hau_moi
                        trang_thai_tot_nhat = ket_qua_trang_thai_moi
    
    if gap_cutoff:
        return trang_thai_tot_nhat, so_hau_tot_nhat, 'cutoff'
    else:
        return trang_thai_tot_nhat, so_hau_tot_nhat, 'not_found'

def dls_recursive(trang_thai_hien_tai, so_hau, gioi_han, da_tham):
    global thong_ke
    thong_ke['so_node'] += 1  
    
    if so_hau == CO:
        return trang_thai_hien_tai, so_hau, 'found'
    
    if so_hau >= gioi_han:
        return trang_thai_hien_tai, so_hau, 'cutoff'
    trang_thai_tot_nhat = trang_thai_hien_tai
    so_hau_tot_nhat = so_hau
    gap_cutoff = False
    
    for r in range(CO):
        for c in range(CO):
            if (r, c) not in trang_thai_hien_tai and hop_le(r, c, trang_thai_hien_tai):
                trang_thai_moi = tuple(sorted(trang_thai_hien_tai + ((r, c),)))
                
                if trang_thai_moi not in da_tham:
                    da_tham.add(trang_thai_moi)
                    
                    ket_qua_trang_thai_moi, so_hau_moi, ket_qua = dls_recursive(
                        trang_thai_moi, so_hau + 1, gioi_han, da_tham
                    )
                    
                    if ket_qua == 'found':
                        return ket_qua_trang_thai_moi, so_hau_moi, 'found'
                    elif ket_qua == 'cutoff':
                        gap_cutoff = True
                    
                    if so_hau_moi > so_hau_tot_nhat:
                        so_hau_tot_nhat = so_hau_moi
                        trang_thai_tot_nhat = ket_qua_trang_thai_moi
    
    if gap_cutoff:
        return trang_thai_tot_nhat, so_hau_tot_nhat, 'cutoff'
    else:
        return trang_thai_tot_nhat, so_hau_tot_nhat, 'not_found'

def dls_tim_trang_thai_dich():
    global thong_ke
    trang_thai_ban_dau = tuple(sorted(hau_dat))
    so_hau_ban_dau = len(trang_thai_ban_dau)
    
    if so_hau_ban_dau == CO:
        messagebox.showinfo("Thông báo", "Bàn cờ đã có đủ 8 quân hậu!")
        hau_ket_qua.clear()
        hau_ket_qua.update(trang_thai_ban_dau)
        cap_nhat()
        thong_ke['thanh_cong'] = True   
        return
    
    GIOI_HAN_DO_SAU = 8
    
    da_tham = set()
    da_tham.add(trang_thai_ban_dau)
    
    vo_hieu_hoa_nut()
    thong_ke['so_node'] = 0   
    
    trang_thai_tot_nhat, so_hau_tot_nhat, ket_qua = dls_recursive(
        trang_thai_ban_dau, so_hau_ban_dau, GIOI_HAN_DO_SAU, da_tham
    )
    
    hau_ket_qua.clear()
    hau_ket_qua.update(trang_thai_tot_nhat)
    
    if ket_qua == 'found':
        thong_ke['thanh_cong'] = True   
        hien_thi_duong_di(trang_thai_tot_nhat)
    
    cap_nhat()
    kich_hoat_nut()
    
    if ket_qua == 'found':
        messagebox.showinfo("Thành công", "Đã tìm thấy giải pháp với 8 quân hậu!")
    else:
        messagebox.showinfo("Thông báo", 
                           f"Không thể đặt đủ 8 quân hậu từ trạng thái ban đầu!\n"
                           f"Số quân hậu ban đầu: {so_hau_ban_dau}\n"
                           f"Số quân hậu tối đa có thể đặt: {so_hau_tot_nhat}")

def ids_tim_trang_thai_dich():
    global thong_ke
    trang_thai_ban_dau = tuple(sorted(hau_dat))
    so_hau_ban_dau = len(trang_thai_ban_dau)
    
    if so_hau_ban_dau == CO:
        messagebox.showinfo("Thông báo", "Bàn cờ đã có đủ 8 quân hậu!")
        hau_ket_qua.clear()
        hau_ket_qua.update(trang_thai_ban_dau)
        cap_nhat()
        thong_ke['thanh_cong'] = True   
        return
    
    vo_hieu_hoa_nut()
    thong_ke['so_node'] = 0   

    for do_sau_toi_da in range(1, CO + 1):
        da_tham = set()
        da_tham.add(trang_thai_ban_dau)
        
        trang_thai_tot_nhat, so_hau_tot_nhat, ket_qua = dls_recursive(
            trang_thai_ban_dau, so_hau_ban_dau, do_sau_toi_da, da_tham
        )
        
        hau_ket_qua.clear()
        hau_ket_qua.update(trang_thai_tot_nhat)
        cap_nhat()
        cua_so.update()
        time.sleep(0.1)
        
        if ket_qua == 'found':
            thong_ke['thanh_cong'] = True   
            hien_thi_duong_di(trang_thai_tot_nhat)
            kich_hoat_nut()
            messagebox.showinfo("Thành công", 
                               f"Đã tìm thấy giải pháp với 8 quân hậu!\n"
                               f"Độ sâu tối đa: {do_sau_toi_da}")
            return
        elif ket_qua == 'not_found':
            break
    
    hau_ket_qua.clear()
    hau_ket_qua.update(trang_thai_tot_nhat)
    cap_nhat()
    kich_hoat_nut()
    
    messagebox.showinfo("Thông báo", 
                       f"Không thể đặt đủ 8 quân hậu từ trạng thái ban đầu!\n"
                       f"Số quân hậu ban đầu: {so_hau_ban_dau}\n"
                       f"Số quân hậu tối đa có thể đặt: {so_hau_tot_nhat}")

def dfs_tim_trang_thai_dich():
    global thong_ke
    trang_thai_ban_dau = tuple(sorted(hau_dat))
    so_hau_ban_dau = len(trang_thai_ban_dau)
    
    if so_hau_ban_dau == CO:
        messagebox.showinfo("Thông báo", "Bàn cờ đã có đủ 8 quân hậu!")
        hau_ket_qua.clear()
        hau_ket_qua.update(trang_thai_ban_dau)
        cap_nhat()
        thong_ke['thanh_cong'] = True   
        return
    
    stack = [(trang_thai_ban_dau, so_hau_ban_dau, [trang_thai_ban_dau])]
    da_tham = set()
    da_tham.add(trang_thai_ban_dau)
    
    trang_thai_tot_nhat = trang_thai_ban_dau
    so_hau_tot_nhat = so_hau_ban_dau
    duong_di_tot_nhat = [trang_thai_ban_dau]
    
    vo_hieu_hoa_nut()
    thong_ke['so_node'] = 0   
    
    while stack:
        trang_thai_hien_tai, so_hau, duong_di_hien_tai = stack.pop()
        thong_ke['so_node'] += 1   
        
        if so_hau == CO:
            hau_ket_qua.clear()
            hau_ket_qua.update(trang_thai_hien_tai)
            hien_thi_duong_di(trang_thai_hien_tai)
            kich_hoat_nut()
            thong_ke['thanh_cong'] = True   
            messagebox.showinfo("Thành công", "Đã tìm thấy giải pháp với 8 quân hậu!")
            return
        
        if so_hau > so_hau_tot_nhat:
            so_hau_tot_nhat = so_hau
            trang_thai_tot_nhat = trang_thai_hien_tai
            duong_di_tot_nhat = duong_di_hien_tai
        
        for r in range(CO):
            for c in range(CO):
                if (r, c) not in trang_thai_hien_tai and hop_le(r, c, trang_thai_hien_tai):
                    trang_thai_moi = tuple(sorted(trang_thai_hien_tai + ((r, c),)))
                    
                    if trang_thai_moi not in da_tham: 
                        da_tham.add(trang_thai_moi)
                        duong_di_moi = duong_di_hien_tai + [trang_thai_moi]
                        stack.append((trang_thai_moi, so_hau + 1, duong_di_moi))
    
    hau_ket_qua.clear()
    hau_ket_qua.update(trang_thai_tot_nhat)
    hien_thi_duong_di(trang_thai_tot_nhat)
    kich_hoat_nut()
    
    if so_hau_tot_nhat == CO:
        thong_ke['thanh_cong'] = True   
        messagebox.showinfo("Thành công", "Đã tìm thấy giải pháp với 8 quân hậu!")
    else:
        messagebox.showinfo("Thông báo", 
                           f"Không thể đặt đủ 8 quân hậu từ trạng thái ban đầu!\n"
                           f"Số quân hậu ban đầu: {so_hau_ban_dau}\n"
                           f"Số quân hậu tối đa có thể đặt: {so_hau_tot_nhat}")

def bfs_tim_trang_thai_dich():
    global thong_ke
    trang_thai_ban_dau = tuple(sorted(hau_dat))
    so_hau_ban_dau = len(trang_thai_ban_dau)
    
    if so_hau_ban_dau == CO:
        messagebox.showinfo("Thông báo", "Bàn cờ đã có đủ 8 quân hậu!")
        hau_ket_qua.clear()
        hau_ket_qua.update(trang_thai_ban_dau)
        cap_nhat()
        thong_ke['thanh_cong'] = True
        return
    
    queue = deque([(trang_thai_ban_dau, so_hau_ban_dau, [trang_thai_ban_dau])])
    da_tham = set()
    da_tham.add(trang_thai_ban_dau)
    
    trang_thai_tot_nhat = trang_thai_ban_dau
    so_hau_tot_nhat = so_hau_ban_dau
    duong_di_tot_nhat = [trang_thai_ban_dau]
    
    vo_hieu_hoa_nut()
    thong_ke['so_node'] = 0  # Reset
    
    while queue:
        trang_thai_hien_tai, so_hau, duong_di_hien_tai = queue.popleft()
        thong_ke['so_node'] += 1  # ĐẾM NODE
        
        if so_hau == CO:
            hau_ket_qua.clear()
            hau_ket_qua.update(trang_thai_hien_tai)
            hien_thi_duong_di(trang_thai_hien_tai)
            kich_hoat_nut()
            thong_ke['thanh_cong'] = True  # ĐÁNH DẤU THÀNH CÔNG
            messagebox.showinfo("Thành công", "Đã tìm thấy giải pháp với 8 quân hậu!")
            return
        
        if so_hau > so_hau_tot_nhat:
            so_hau_tot_nhat = so_hau
            trang_thai_tot_nhat = trang_thai_hien_tai
            duong_di_tot_nhat = duong_di_hien_tai
        
        for r in range(CO):
            for c in range(CO):
                if (r, c) not in trang_thai_hien_tai and hop_le(r, c, trang_thai_hien_tai):
                    trang_thai_moi = tuple(sorted(trang_thai_hien_tai + ((r, c),)))
                    
                    if trang_thai_moi not in da_tham:
                        da_tham.add(trang_thai_moi)
                        duong_di_moi = duong_di_hien_tai + [trang_thai_moi]
                        queue.append((trang_thai_moi, so_hau + 1, duong_di_moi))
    
    hau_ket_qua.clear()
    hau_ket_qua.update(trang_thai_tot_nhat)
    hien_thi_duong_di(trang_thai_tot_nhat)
    kich_hoat_nut()
    
    if so_hau_tot_nhat == CO:
        thong_ke['thanh_cong'] = True
        messagebox.showinfo("Thành công", "Đã tìm thấy giải pháp với 8 quân hậu!")
    else:
        messagebox.showinfo("Thông báo", 
                           f"Không thể đặt đủ 8 quân hậu từ trạng thái ban đầu!\n"
                           f"Số quân hậu ban đầu: {so_hau_ban_dau}\n"
                           f"Số quân hậu tối đa có thể đặt: {so_hau_tot_nhat}")

def tinh_khoang_cach(r1, c1, r2, c2):
    return math.sqrt((r1 - r2)**2 + (c1 - c2)**2)

def tinh_chi_phi(trang_thai, r_moi, c_moi):
    if not trang_thai:
        return 1
    
    khoang_cach_min = float('inf')
    for (r, c) in trang_thai:
        khoang_cach = tinh_khoang_cach(r, c, r_moi, c_moi)
        if khoang_cach < khoang_cach_min:
            khoang_cach_min = khoang_cach
    return 1 / (khoang_cach_min + 1)

def ucs_tim_trang_thai_dich():
    global thong_ke
    trang_thai_ban_dau = tuple(sorted(hau_dat))
    so_hau_ban_dau = len(trang_thai_ban_dau)
    
    if so_hau_ban_dau == CO:
        messagebox.showinfo("Thông báo", "Bàn cờ đã có đủ 8 quân hậu!")
        hau_ket_qua.clear()
        hau_ket_qua.update(trang_thai_ban_dau)
        cap_nhat()
        thong_ke['thanh_cong'] = True   
        return
    
    chi_phi_ban_dau = 0
    for i in range(so_hau_ban_dau):
        for j in range(i + 1, so_hau_ban_dau):
            r1, c1 = trang_thai_ban_dau[i]
            r2, c2 = trang_thai_ban_dau[j]
            chi_phi_ban_dau += tinh_khoang_cach(r1, c1, r2, c2)
    
    pq = [(chi_phi_ban_dau, so_hau_ban_dau, trang_thai_ban_dau, [trang_thai_ban_dau])]
    da_tham = set()
    da_tham.add(trang_thai_ban_dau)
    
    trang_thai_tot_nhat = trang_thai_ban_dau
    so_hau_tot_nhat = so_hau_ban_dau
    duong_di_tot_nhat = [trang_thai_ban_dau]
    chi_phi_tot_nhat = chi_phi_ban_dau
    
    vo_hieu_hoa_nut()
    thong_ke['so_node'] = 0   
    
    while pq:
        tong_chi_phi, so_hau, trang_thai_hien_tai, duong_di_hien_tai = heapq.heappop(pq)
        thong_ke['so_node'] += 1   
        
        if so_hau == CO:
            hau_ket_qua.clear()
            hau_ket_qua.update(trang_thai_hien_tai)
            hien_thi_duong_di(trang_thai_hien_tai)
            kich_hoat_nut()
            thong_ke['thanh_cong'] = True   
            messagebox.showinfo("Thành công", f"Đã tìm thấy giải pháp với 8 quân hậu!\nTổng chi phí: {tong_chi_phi:.2f}")
            return
        
        if so_hau > so_hau_tot_nhat:
            so_hau_tot_nhat = so_hau
            trang_thai_tot_nhat = trang_thai_hien_tai
            duong_di_tot_nhat = duong_di_hien_tai
            chi_phi_tot_nhat = tong_chi_phi
        
        for r in range(CO):
            for c in range(CO):
                if (r, c) not in trang_thai_hien_tai and hop_le(r, c, trang_thai_hien_tai):
                    trang_thai_moi = tuple(sorted(trang_thai_hien_tai + ((r, c),)))
                    
                    if trang_thai_moi not in da_tham:
                        chi_phi_moi = tinh_chi_phi(trang_thai_hien_tai, r, c)
                        tong_chi_phi_moi = tong_chi_phi + chi_phi_moi
                        
                        da_tham.add(trang_thai_moi)
                        duong_di_moi = duong_di_hien_tai + [trang_thai_moi]
                        heapq.heappush(pq, (tong_chi_phi_moi, so_hau + 1, trang_thai_moi, duong_di_moi))
    
    hau_ket_qua.clear()
    hau_ket_qua.update(trang_thai_tot_nhat)
    hien_thi_duong_di(trang_thai_tot_nhat)
    kich_hoat_nut()
    
    if so_hau_tot_nhat == CO:
        thong_ke['thanh_cong'] = True   
        messagebox.showinfo("Thành công", f"Đã tìm thấy giải pháp với 8 quân hậu!\nTổng chi phí: {chi_phi_tot_nhat:.2f}")
    else:
        messagebox.showinfo("Thông báo", 
                           f"Không thể đặt đủ 8 quân hậu từ trạng thái ban đầu!\n"
                           f"Số quân hậu ban đầu: {so_hau_ban_dau}\n"
                           f"Số quân hậu tối đa có thể đặt: {so_hau_tot_nhat}\n"
                           f"Tổng chi phí: {chi_phi_tot_nhat:.2f}")
def dem_xung_dot(trang_thai):
    dem = 0
    for i in range(len(trang_thai)):
        for j in range(i + 1, len(trang_thai)):
            r1, c1 = trang_thai[i]
            r2, c2 = trang_thai[j]
            if r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                dem += 1
    return dem

def best_first_tim_trang_thai_dich():
    global thong_ke
    trang_thai_ban_dau = tuple(sorted(hau_dat))
    so_hau_ban_dau = len(trang_thai_ban_dau)

    if so_hau_ban_dau == CO:
        messagebox.showinfo("Thông báo", "Bàn cờ đã có đủ 8 quân hậu!")
        hau_ket_qua.clear()
        hau_ket_qua.update(trang_thai_ban_dau)
        cap_nhat()
        thong_ke['thanh_cong'] = True   
        return

    pq = [(dem_xung_dot(trang_thai_ban_dau), so_hau_ban_dau, trang_thai_ban_dau, [trang_thai_ban_dau])]
    da_tham = set()
    da_tham.add(trang_thai_ban_dau)

    trang_thai_tot_nhat = trang_thai_ban_dau
    so_hau_tot_nhat = so_hau_ban_dau
    duong_di_tot_nhat = [trang_thai_ban_dau]

    vo_hieu_hoa_nut()
    thong_ke['so_node'] = 0   

    while pq:
        h, so_hau, trang_thai_hien_tai, duong_di_hien_tai = heapq.heappop(pq)
        thong_ke['so_node'] += 1   

        if so_hau == CO and h == 0:
            hau_ket_qua.clear()
            hau_ket_qua.update(trang_thai_hien_tai)
            hien_thi_duong_di(trang_thai_hien_tai)
            kich_hoat_nut()
            thong_ke['thanh_cong'] = True   
            messagebox.showinfo("Thành công", "Đã tìm thấy giải pháp với 8 quân hậu (BestFS)!")
            return

        if so_hau > so_hau_tot_nhat:
            so_hau_tot_nhat = so_hau
            trang_thai_tot_nhat = trang_thai_hien_tai
            duong_di_tot_nhat = duong_di_hien_tai

        for r in range(CO):
            for c in range(CO):
                if (r, c) not in trang_thai_hien_tai and hop_le(r, c, trang_thai_hien_tai):
                    trang_thai_moi = tuple(sorted(trang_thai_hien_tai + ((r, c),)))
                    if trang_thai_moi not in da_tham:
                        da_tham.add(trang_thai_moi)
                        h_moi = dem_xung_dot(trang_thai_moi)
                        duong_di_moi = duong_di_hien_tai + [trang_thai_moi]
                        heapq.heappush(pq, (h_moi, so_hau + 1, trang_thai_moi, duong_di_moi))

    hau_ket_qua.clear()
    hau_ket_qua.update(trang_thai_tot_nhat)
    hien_thi_duong_di(trang_thai_tot_nhat)
    kich_hoat_nut()

    if so_hau_tot_nhat == CO:
        thong_ke['thanh_cong'] = True   
        messagebox.showinfo("Thành công", "Đã tìm thấy giải pháp với 8 quân hậu (BestFS)!")
    else:
        messagebox.showinfo("Thông báo", 
                           f"Không thể đặt đủ 8 quân hậu từ trạng thái ban đầu!\n"
                           f"Số quân hậu ban đầu: {so_hau_ban_dau}\n"
                           f"Số quân hậu tối đa có thể đặt: {so_hau_tot_nhat}")

def a_star_tim_trang_thai_dich():
    global thong_ke
    trang_thai_ban_dau = tuple(sorted(hau_dat))
    so_hau_ban_dau = len(trang_thai_ban_dau)

    if so_hau_ban_dau == CO:
        messagebox.showinfo("Thông báo", "Bàn cờ đã có đủ 8 quân hậu!")
        hau_ket_qua.clear()
        hau_ket_qua.update(trang_thai_ban_dau)
        cap_nhat()
        thong_ke['thanh_cong'] = True   
        return

    g_ban_dau = so_hau_ban_dau
    h_ban_dau = dem_xung_dot(trang_thai_ban_dau)
    f_ban_dau = g_ban_dau + h_ban_dau

    pq = [(f_ban_dau, g_ban_dau, trang_thai_ban_dau, [trang_thai_ban_dau])]
    da_tham = set()
    da_tham.add(trang_thai_ban_dau)

    trang_thai_tot_nhat = trang_thai_ban_dau
    so_hau_tot_nhat = so_hau_ban_dau
    duong_di_tot_nhat = [trang_thai_ban_dau]

    vo_hieu_hoa_nut()
    thong_ke['so_node'] = 0   

    while pq:
        f, g, trang_thai_hien_tai, duong_di_hien_tai = heapq.heappop(pq)
        thong_ke['so_node'] += 1   
        h = dem_xung_dot(trang_thai_hien_tai)

        if g == CO and h == 0:
            hau_ket_qua.clear()
            hau_ket_qua.update(trang_thai_hien_tai)
            hien_thi_duong_di(trang_thai_hien_tai)
            kich_hoat_nut()
            thong_ke['thanh_cong'] = True   
            messagebox.showinfo("Thành công", "Đã tìm thấy giải pháp với 8 quân hậu (A*)!")
            return

        if g > so_hau_tot_nhat:
            so_hau_tot_nhat = g
            trang_thai_tot_nhat = trang_thai_hien_tai
            duong_di_tot_nhat = duong_di_hien_tai

        for r in range(CO):
            for c in range(CO):
                if (r, c) not in trang_thai_hien_tai and hop_le(r, c, trang_thai_hien_tai):
                    trang_thai_moi = tuple(sorted(trang_thai_hien_tai + ((r, c),)))
                    if trang_thai_moi not in da_tham:
                        da_tham.add(trang_thai_moi)
                        g_moi = g + 1
                        h_moi = dem_xung_dot(trang_thai_moi)
                        f_moi = g_moi + h_moi
                        duong_di_moi = duong_di_hien_tai + [trang_thai_moi]
                        heapq.heappush(pq, (f_moi, g_moi, trang_thai_moi, duong_di_moi))

    hau_ket_qua.clear()
    hau_ket_qua.update(trang_thai_tot_nhat)
    hien_thi_duong_di(trang_thai_tot_nhat)
    kich_hoat_nut()

    if so_hau_tot_nhat == CO:
        thong_ke['thanh_cong'] = True   
        messagebox.showinfo("Thành công", "Đã tìm thấy giải pháp với 8 quân hậu (A*)!")
    else:
        messagebox.showinfo("Thông báo",
                           f"Không thể đặt đủ 8 quân hậu từ trạng thái ban đầu!\n"
                           f"Số quân hậu ban đầu: {so_hau_ban_dau}\n"
                           f"Số quân hậu tối đa có thể đặt: {so_hau_tot_nhat}")

def dem_xung_dot_hill(trang_thai):
    """
    Đếm số lượng xung đột (cặp hậu tấn công nhau)
    Giá trị càng thấp càng tốt (0 là tốt nhất)
    """
    dem = 0
    for i in range(len(trang_thai)):
        for j in range(i + 1, len(trang_thai)):
            r1, c1 = trang_thai[i]
            r2, c2 = trang_thai[j]
            # Xung đột nếu cùng hàng, cùng cột, hoặc cùng đường chéo
            if r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                dem += 1
    return dem

def tim_lang_gieng_tot_nhat(trang_thai):
    trang_thai_tot = trang_thai
    xung_dot_tot = dem_xung_dot(trang_thai)
    cai_thien = False

    for i in range(len(trang_thai)):
        r, c = trang_thai[i]
        for r_moi in range(CO):
            if r_moi != r:
                trang_thai_moi = list(trang_thai)
                trang_thai_moi[i] = (r_moi, c)
                trang_thai_moi = tuple(sorted(trang_thai_moi))
                xung_dot_moi = dem_xung_dot(trang_thai_moi)
                if xung_dot_moi < xung_dot_tot:
                    xung_dot_tot = xung_dot_moi
                    trang_thai_tot = trang_thai_moi
                    cai_thien = True
    return trang_thai_tot, xung_dot_tot, cai_thien


def hill_climbing_tim_trang_thai_dich():
    global thong_ke
    trang_thai_ban_dau = tuple(sorted(hau_dat))

    if len(trang_thai_ban_dau) != CO:
        messagebox.showinfo("Thông báo", "Hill Climbing cần đủ 8 quân hậu ban đầu!")
        return

    vo_hieu_hoa_nut()
    thong_ke['so_node'] = 0   

    hien_tai = trang_thai_ban_dau
    xung_dot = dem_xung_dot(hien_tai)
    duong_di = [hien_tai]

    while True:
        thong_ke['so_node'] += 1   
        lang_gieng, xung_dot_moi, cai_thien = tim_lang_gieng_tot_nhat(hien_tai)
        if not cai_thien:
            break
        hien_tai = lang_gieng
        xung_dot = xung_dot_moi
        duong_di.append(hien_tai)

    hau_ket_qua.clear()
    hau_ket_qua.update(hien_tai)
    hien_thi_duong_di(hien_tai)
    kich_hoat_nut()

    if xung_dot == 0:
        thong_ke['thanh_cong'] = True   
        messagebox.showinfo("Thành công", "Đã tìm thấy nghiệm với Hill Climbing!")
    else:
        messagebox.showinfo("Thông báo", f"Hill Climbing dừng ở cực trị cục bộ.\nSố xung đột: {xung_dot}")

def simulated_annealing_tim_trang_thai_dich():
    global thong_ke
    trang_thai_ban_dau = tuple(sorted(hau_dat))
    if len(trang_thai_ban_dau) != CO:
        messagebox.showinfo("Thông báo", "Simulated Annealing cần đủ 8 quân hậu ban đầu!")
        return

    vo_hieu_hoa_nut()
    thong_ke['so_node'] = 0   

    T = 1.0
    T_min = 1e-4
    alpha = 0.995
    max_steps = 5000

    current = list(trang_thai_ban_dau)
    current_conflicts = dem_xung_dot(tuple(current))
    best = list(current)
    best_conflicts = current_conflicts

    steps = 0
    while T > T_min and steps < max_steps and best_conflicts > 0:
        thong_ke['so_node'] += 1   
        
        i = random.randrange(len(current))
        r_old, c = current[i]
        r_new = random.randrange(CO)
        while r_new == r_old:
            r_new = random.randrange(CO)

        neighbor = current.copy()
        neighbor[i] = (r_new, c)
        neighbor_tuple = tuple(sorted(neighbor))
        neighbor_conflicts = dem_xung_dot(neighbor_tuple)

        delta = neighbor_conflicts - current_conflicts

        if delta <= 0:
            current = list(neighbor_tuple)
            current_conflicts = neighbor_conflicts
            if current_conflicts < best_conflicts:
                best = list(current)
                best_conflicts = current_conflicts
        else:
            prob = math.exp(-delta / T)
            if random.random() < prob:
                current = list(neighbor_tuple)
                current_conflicts = neighbor_conflicts

        if steps % 50 == 0:
            hau_ket_qua.clear()
            hau_ket_qua.update(current)
            cap_nhat()
            cua_so.update()

        T *= alpha
        steps += 1

    hau_ket_qua.clear()
    hau_ket_qua.update(best)
    hien_thi_duong_di(best)
    kich_hoat_nut()

    if best_conflicts == 0:
        thong_ke['thanh_cong'] = True   
        messagebox.showinfo("Thành công", f"Đã tìm thấy nghiệm (SA) sau {steps} bước!")
    else:
        messagebox.showinfo("Thông báo", f"SA dừng sau {steps} bước.\nSố xung đột tốt nhất: {best_conflicts}")

def beam_search_tim_trang_thai_dich(k=100):
    global thong_ke

    if len(hau_dat) == 0:
        messagebox.showinfo("Thông báo", "Hãy đặt ít nhất 1 quân hậu ban đầu!")
        return

    vo_hieu_hoa_nut()
    thong_ke['so_node'] = 0   

    trang_thai_ban_dau = tuple(sorted(hau_dat))
    frontier = [trang_thai_ban_dau]

    found = None
    steps = 0

    while frontier and not found:
        successors = []
        for state in frontier:
            thong_ke['so_node'] += 1   
            
            if len(state) == CO:
                if dem_xung_dot(state) == 0:
                    found = state
                    break
                else:
                    continue

            next_col = len(state)
            for r in range(CO):
                new_state = state + ((r, next_col),)
                successors.append(new_state)

        if found:
            break

        successors.sort(key=lambda s: dem_xung_dot(s))
        frontier = successors[:k]

        steps += 1
        if steps % 10 == 0:
            if frontier:
                hau_ket_qua.clear()
                hau_ket_qua.update(frontier[0])
                cap_nhat()
                cua_so.update()

    hau_ket_qua.clear()
    if found:
        thong_ke['thanh_cong'] = True   
        hau_ket_qua.update(found)
        hien_thi_duong_di(found)
        messagebox.showinfo("Thành công", f"Beam Search tìm thấy nghiệm!")
    else:
        if frontier:
            hau_ket_qua.update(frontier[0])
            hien_thi_duong_di(frontier[0])
        messagebox.showinfo("Thông báo", "Beam Search không tìm được nghiệm.")

    kich_hoat_nut()

def genetic_algorithm_tim_trang_thai_dich(pop_size=100, max_gen=1000, p_crossover=0.8, p_mutation=0.2):
    global thong_ke
    vo_hieu_hoa_nut()
    thong_ke['so_node'] = 0   
    
    def tao_ca_the():
        return [random.randint(0, CO - 1) for _ in range(CO)]

    def fitness(ind):
        non_attacking = 28 - dem_xung_dot(tuple((ind[c], c) for c in range(CO)))
        return non_attacking

    def crossover(p1, p2):
        if random.random() < p_crossover:
            cut = random.randint(1, CO - 2)
            return p1[:cut] + p2[cut:], p2[:cut] + p1[cut:]
        else:
            return p1[:], p2[:]

    def mutate(ind):
        if random.random() < p_mutation:
            c = random.randrange(CO)
            ind[c] = random.randrange(CO)
        return ind

    population = [tao_ca_the() for _ in range(pop_size)]
    best = max(population, key=fitness)

    for gen in range(max_gen):
        thong_ke['so_node'] += pop_size  
        if fitness(best) == 28:
            break

        parents = random.choices(population, weights=[fitness(ind) for ind in population], k=pop_size)

        offspring = []
        for i in range(0, pop_size, 2):
            p1, p2 = parents[i], parents[i + 1]
            c1, c2 = crossover(p1, p2)
            offspring.append(mutate(c1))
            offspring.append(mutate(c2))

        population = offspring
        best = max(population, key=fitness)

        if gen % 20 == 0:
            hau_ket_qua.clear()
            hau_ket_qua.update((best[c], c) for c in range(CO))
            cap_nhat()
            cua_so.update()

    hau_ket_qua.clear()
    hau_ket_qua.update((best[c], c) for c in range(CO))
    hien_thi_duong_di(tuple((best[c], c) for c in range(CO)))
    kich_hoat_nut()

    if fitness(best) == 28:
        thong_ke['thanh_cong'] = True   
        messagebox.showinfo("Thành công", f"GA tìm thấy nghiệm sau {gen} thế hệ!")
    else:
        messagebox.showinfo("Thông báo", f"GA dừng ở thế hệ {gen}, fitness tốt nhất = {fitness(best)}")

def belief_state_search():
    global thong_ke
    trang_thai_ban_dau = tuple(sorted(hau_dat, key=lambda x: x[1]))
    so_hau_ban_dau = len(trang_thai_ban_dau)

    if so_hau_ban_dau == CO:
        messagebox.showinfo("Thông báo", "Bàn cờ đã có đủ 8 quân hậu!")
        hau_ket_qua.clear()
        hau_ket_qua.update(trang_thai_ban_dau)
        cap_nhat()
        thong_ke['thanh_cong'] = True   
        return

    vo_hieu_hoa_nut()
    thong_ke['so_node'] = 0   
    log = []
    belief = {trang_thai_ban_dau: [trang_thai_ban_dau]}

    def canonical(state):
        return tuple(sorted(state, key=lambda x: x[1]))

    log.append(f"Khởi tạo belief state với {len(belief)} trạng thái:")
    for s, p in belief.items():
        log.append(f"  - {s}")

    steps_to_do = CO - so_hau_ban_dau

    for step_idx in range(steps_to_do):
        belief_moi = {}
        for state, path in belief.items():
            thong_ke['so_node'] += 1   
            
            used_cols = set(c for (_, c) in state)
            remaining_cols = [c for c in range(CO) if c not in used_cols]
            if not remaining_cols:
                continue
            next_col = remaining_cols[0]

            for r in range(CO):
                c = next_col
                if (r, c) not in state and hop_le(r, c, state):
                    new_state_raw = state + ((r, c),)
                    new_state = canonical(new_state_raw)
                    if new_state not in belief_moi:
                        belief_moi[new_state] = path + [new_state]

        log.append(f"\nBước {so_hau_ban_dau + step_idx + 1}: thêm 1 hậu -> còn {len(belief_moi)} trạng thái hợp lệ")
        for s, p in belief_moi.items():
            log.append(f"  - {s}")

        if belief_moi:
            rep_state = next(iter(belief_moi))
            hau_ket_qua.clear()
            hau_ket_qua.update(rep_state)
            cap_nhat()
            cua_so.update()
            time.sleep(0.15)

        belief = belief_moi

        if not belief:
            break

    kich_hoat_nut()

    if not belief:
        log.append("\n❌ Không tìm thấy trạng thái hợp lệ!")
        result_message = "Không tìm thấy trạng thái hợp lệ!"
    elif len(belief) == 1:
        thong_ke['thanh_cong'] = True   
        ket_qua = next(iter(belief))
        duong_di = belief[ket_qua]

        hau_ket_qua.clear()
        hau_ket_qua.update(ket_qua)
        hien_thi_duong_di(ket_qua)

        log.append("\n✓ Thành công! Tìm được duy nhất 1 trạng thái cuối cùng:")
        log.append(f"  {ket_qua}")
        log.append("\nĐường đi chi tiết (mỗi bước đặt thêm 1 hậu):")
        for i, st in enumerate(duong_di):
            log.append(f"  Bước {i}: {st}")
        result_message = "Đã tìm thấy nghiệm duy nhất."
    else:
        log.append(f"\n⚠ Kết thúc với {len(belief)} trạng thái hợp lệ (không duy nhất).")
        result_message = f"Kết thúc với {len(belief)} trạng thái hợp lệ (không duy nhất)."

    cua_so_log = tk.Toplevel(cua_so)
    cua_so_log.title("Quá trình Belief State Search")
    cua_so_log.geometry("800x600")

    text_log = tk.Text(cua_so_log, wrap="word")
    text_log.pack(expand=True, fill="both")
    
    def luu_log():
        try:
            with open("belief_log.txt", "w", encoding="utf-8") as f:
                for dong in log:
                    f.write(dong + "\n")
            messagebox.showinfo("Lưu thành công", "Đã lưu log vào belief_log.txt")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi lưu file: {e}")

    btn_luu = tk.Button(cua_so_log, text="Lưu log ra belief_log.txt", command=luu_log)
    btn_luu.pack(pady=4)

    for dong in log:
        text_log.insert(tk.END, dong + "\n")
    text_log.config(state="disabled")
    text_log.see("end")

    messagebox.showinfo("Kết thúc Belief Search", result_message)

def and_or_search():
    global thong_ke
    vo_hieu_hoa_nut()
    thong_ke['so_node'] = 0   
    log = []

    def and_or(trang_thai, hang):
        thong_ke['so_node'] += 1   
        
        if hang >= CO:
            return [trang_thai]

        giai_phap = []
        log.append(f"OR node: Đang đặt hậu ở hàng {hang}")

        for cot in range(CO):
            if hop_le(hang, cot, trang_thai):
                log.append(f"  Thử đặt hậu tại ({hang},{cot})")

                trang_thai_moi = trang_thai + ((hang, cot),)
                ket_qua = and_or(trang_thai_moi, hang + 1)
                if ket_qua:
                    giai_phap.extend(ket_qua)
            else:
                log.append(f"  ({hang},{cot}) không hợp lệ")

        return giai_phap

    tat_ca_loi_giai = and_or((), 0)

    hau_ket_qua.clear()
    if tat_ca_loi_giai:
        thong_ke['thanh_cong'] = True   
        hau_ket_qua.update(tat_ca_loi_giai[0])
        cap_nhat()
        log.append(f"\n✓ Tìm thấy {len(tat_ca_loi_giai)} lời giải hợp lệ.")
    else:
        log.append("\n Không tìm thấy lời giải.")

    kich_hoat_nut()
    
    cua_so_log = tk.Toplevel(cua_so)
    cua_so_log.title("Quá trình AND-OR Search")
    cua_so_log.geometry("700x500")

    text_log = tk.Text(cua_so_log, wrap="word")
    text_log.pack(expand=True, fill="both")

    for dong in log:
        text_log.insert(tk.END, dong + "\n")

    if tat_ca_loi_giai:
        text_log.insert(tk.END, "\n--- TẤT CẢ LỜI GIẢI ---\n")
        for i, giai in enumerate(tat_ca_loi_giai, 1):
            text_log.insert(tk.END, f"Lời giải {i}: {giai}\n")

    text_log.config(state="disabled")
    text_log.see("end")

def backtracking_search():
    global thong_ke
    vo_hieu_hoa_nut()
    thong_ke['so_node'] = 0   
    
    def backtrack(trang_thai, hang):
        thong_ke['so_node'] += 1   
        
        if hang >= CO:
            return trang_thai
        
        for cot in range(CO):
            if hop_le(hang, cot, trang_thai):
                trang_thai_moi = trang_thai + ((hang, cot),)
                
                hau_ket_qua.clear()
                hau_ket_qua.update(trang_thai_moi)
                cap_nhat()
                cua_so.update()
                time.sleep(0.1)
                
                ket_qua = backtrack(trang_thai_moi, hang + 1)
                if ket_qua:
                    return ket_qua
        
        return None
    
    trang_thai_ban_dau = tuple(sorted(hau_dat))
    hang_bat_dau = len(trang_thai_ban_dau)
    
    if hang_bat_dau >= CO:
        messagebox.showinfo("Thông báo", "Đã có đủ 8 quân hậu!")
        thong_ke['thanh_cong'] = True   
        kich_hoat_nut()
        return
    
    ket_qua = backtrack(trang_thai_ban_dau, hang_bat_dau)
    
    if ket_qua:
        thong_ke['thanh_cong'] = True   
        hau_ket_qua.clear()
        hau_ket_qua.update(ket_qua)
        hien_thi_duong_di(ket_qua)
        messagebox.showinfo("Thành công", "Backtracking tìm thấy nghiệm!")
    else:
        messagebox.showinfo("Thất bại", "Không tìm thấy nghiệm!")
    
    kich_hoat_nut()


def forward_checking_search():
    global thong_ke
    vo_hieu_hoa_nut()
    thong_ke['so_node'] = 0   
    
    def tinh_mien(trang_thai, hang):
        mien = []
        for cot in range(CO):
            if hop_le(hang, cot, trang_thai):
                mien.append(cot)
        return mien
    
    def forward_check(trang_thai, hang, mien_cac_hang):
        thong_ke['so_node'] += 1   
        
        if hang >= CO:
            return trang_thai
        
        if hang not in mien_cac_hang or not mien_cac_hang[hang]:
            return None
        
        for cot in mien_cac_hang[hang]:
            trang_thai_moi = trang_thai + ((hang, cot),)
            
            hau_ket_qua.clear()
            hau_ket_qua.update(trang_thai_moi)
            cap_nhat()
            cua_so.update()
            time.sleep(0.1)
            
            mien_moi = {}
            hop_le_flag = True
            
            for h in range(hang + 1, CO):
                mien_moi[h] = tinh_mien(trang_thai_moi, h)
                if not mien_moi[h]:
                    hop_le_flag = False
                    break
            
            if hop_le_flag:
                ket_qua = forward_check(trang_thai_moi, hang + 1, mien_moi)
                if ket_qua:
                    return ket_qua
        
        return None
    
    trang_thai_ban_dau = tuple(sorted(hau_dat))
    hang_bat_dau = len(trang_thai_ban_dau)
    
    if hang_bat_dau >= CO:
        messagebox.showinfo("Thông báo", "Đã có đủ 8 quân hậu!")
        thong_ke['thanh_cong'] = True   
        kich_hoat_nut()
        return
    
    mien_ban_dau = {}
    for h in range(hang_bat_dau, CO):
        mien_ban_dau[h] = tinh_mien(trang_thai_ban_dau, h)
    
    ket_qua = forward_check(trang_thai_ban_dau, hang_bat_dau, mien_ban_dau)
    
    if ket_qua:
        thong_ke['thanh_cong'] = True   
        hau_ket_qua.clear()
        hau_ket_qua.update(ket_qua)
        hien_thi_duong_di(ket_qua)
        messagebox.showinfo("Thành công", "Forward Checking tìm thấy nghiệm!")
    else:
        messagebox.showinfo("Thất bại", "Không tìm thấy nghiệm!")
    
    kich_hoat_nut()

def ac3_search():
    global thong_ke
    vo_hieu_hoa_nut()
    thong_ke['so_node'] = 0   
    
    mien = {hang: set(range(CO)) for hang in range(CO)}
    
    trang_thai_ban_dau = tuple(sorted(hau_dat))
    for (r, c) in trang_thai_ban_dau:
        if r in mien:
            mien[r] = {c}
    
    def loai_bo_khong_nhat_quan(hang1, hang2):
        thong_ke['so_node'] += 1   
        
        loai_bo = False
        mien_moi = set()
        
        for c1 in mien[hang1]:
            ton_tai_gia_tri_nhat_quan = False
            
            for c2 in mien[hang2]:
                if c1 != c2 and abs(hang1 - hang2) != abs(c1 - c2):
                    ton_tai_gia_tri_nhat_quan = True
                    break
            
            if ton_tai_gia_tri_nhat_quan:
                mien_moi.add(c1)
            else:
                loai_bo = True
        
        mien[hang1] = mien_moi
        return loai_bo
    
    hang_doi = deque()
    for h1 in range(CO):
        for h2 in range(CO):
            if h1 != h2:
                hang_doi.append((h1, h2))
    
    while hang_doi:
        (h1, h2) = hang_doi.popleft()
        
        if loai_bo_khong_nhat_quan(h1, h2):
            if not mien[h1]:
                messagebox.showinfo("Thất bại", "AC-3: Không tồn tại nghiệm!")
                kich_hoat_nut()
                return
            
            for h3 in range(CO):
                if h3 != h1 and h3 != h2:
                    hang_doi.append((h3, h1))
    
    def backtrack_voi_mien(trang_thai, hang):
        if hang >= CO:
            return trang_thai
        
        for cot in mien[hang]:
            if hop_le(hang, cot, trang_thai):
                trang_thai_moi = trang_thai + ((hang, cot),)
                
                hau_ket_qua.clear()
                hau_ket_qua.update(trang_thai_moi)
                cap_nhat()
                cua_so.update()
                time.sleep(0.1)
                
                ket_qua = backtrack_voi_mien(trang_thai_moi, hang + 1)
                if ket_qua:
                    return ket_qua
        
        return None
    
    hang_bat_dau = len(trang_thai_ban_dau)
    ket_qua = backtrack_voi_mien(trang_thai_ban_dau, hang_bat_dau)
    
    if ket_qua:
        thong_ke['thanh_cong'] = True   
        hau_ket_qua.clear()
        hau_ket_qua.update(ket_qua)
        hien_thi_duong_di(ket_qua)
        messagebox.showinfo("Thành công", "AC-3 tìm thấy nghiệm!")
    else:
        messagebox.showinfo("Thất bại", "AC-3: Không tìm thấy nghiệm!")
    
    kich_hoat_nut()

def xem_lich_su():
    if not lich_su_chay:
        messagebox.showinfo("Thông báo", "Chưa có lịch sử chạy!")
        return
    
    cua_so_lich_su = tk.Toplevel(cua_so)
    cua_so_lich_su.title("Lịch sử chạy thuật toán")
    cua_so_lich_su.geometry("900x600")
    
    # Tạo text widget với scrollbar
    frame = tk.Frame(cua_so_lich_su)
    frame.pack(fill="both", expand=True)
    
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")
    
    text_widget = tk.Text(frame, wrap="none", yscrollcommand=scrollbar.set)
    text_widget.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=text_widget.yview)
    
    # Header
    header = f"{'STT':<5} {'Thời gian':<20} {'Thuật toán':<25} {'Nodes':<10} {'Time(s)':<12} {'Kết quả':<10}\n"
    header += "=" * 100 + "\n"
    text_widget.insert("end", header)
    
    # Data
    for i, record in enumerate(lich_su_chay, 1):
        dong = f"{i:<5} {record['timestamp']:<20} {record['ten_thuat_toan']:<25} "
        dong += f"{record['so_node']:<10} {record['thoi_gian']:<12.4f} "
        dong += f"{'✓' if record['thanh_cong'] else '✗':<10}\n"
        text_widget.insert("end", dong)
    
    # Thống kê tổng hợp
    text_widget.insert("end", "\n" + "=" * 100 + "\n")
    text_widget.insert("end", "THỐNG KÊ TỔNG HỢP\n")
    text_widget.insert("end", "=" * 100 + "\n")
    
    # Group by thuật toán
    thong_ke_theo_thuat_toan = {}
    for record in lich_su_chay:
        ten = record['ten_thuat_toan']
        if ten not in thong_ke_theo_thuat_toan:
            thong_ke_theo_thuat_toan[ten] = {
                'so_lan': 0,
                'tong_thoi_gian': 0,
                'tong_nodes': 0,
                'thanh_cong': 0
            }
        thong_ke_theo_thuat_toan[ten]['so_lan'] += 1
        thong_ke_theo_thuat_toan[ten]['tong_thoi_gian'] += record['thoi_gian']
        thong_ke_theo_thuat_toan[ten]['tong_nodes'] += record['so_node']
        if record['thanh_cong']:
            thong_ke_theo_thuat_toan[ten]['thanh_cong'] += 1
    
    for ten, stat in thong_ke_theo_thuat_toan.items():
        text_widget.insert("end", f"\n{ten}:\n")
        text_widget.insert("end", f"  - Số lần chạy: {stat['so_lan']}\n")
        text_widget.insert("end", f"  - Thành công: {stat['thanh_cong']}/{stat['so_lan']}\n")
        text_widget.insert("end", f"  - Thời gian TB: {stat['tong_thoi_gian']/stat['so_lan']:.4f}s\n")
        text_widget.insert("end", f"  - Nodes TB: {stat['tong_nodes']//stat['so_lan']}\n")
    
    text_widget.config(state="disabled")

def xuat_csv():
    if not lich_su_chay:
        messagebox.showinfo("Thông báo", "Chưa có dữ liệu để xuất!")
        return
    
    import csv
    
    ten_file = f"ket_qua_8_quan_hau_{time.strftime('%Y%m%d_%H%M%S')}.csv"
    
    try:
        with open(ten_file, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'STT', 'Timestamp', 'Thuật toán', 'Số nodes', 
                'Thời gian (s)', 'Thành công', 'Trạng thái ban đầu'
            ])
            writer.writeheader()
            
            for i, record in enumerate(lich_su_chay, 1):
                writer.writerow({
                    'STT': i,
                    'Timestamp': record['timestamp'],
                    'Thuật toán': record['ten_thuat_toan'],
                    'Số nodes': record['so_node'],
                    'Thời gian (s)': f"{record['thoi_gian']:.4f}",
                    'Thành công': 'Có' if record['thanh_cong'] else 'Không',
                    'Trạng thái ban đầu': record.get('trang_thai_ban_dau', 0)
                })
        
        messagebox.showinfo("Thành công", f"Đã xuất dữ liệu ra file:\n{ten_file}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể xuất file: {e}")

def vo_hieu_hoa_nut():
    nut_dls.config(state=tk.DISABLED)
    nut_dfs.config(state=tk.DISABLED)
    nut_bfs.config(state=tk.DISABLED)
    nut_ucs.config(state=tk.DISABLED)
    nut_ids.config(state=tk.DISABLED)
    nut_best.config(state=tk.DISABLED)
    nut_astar.config(state=tk.DISABLED)
    nut_hill.config(state=tk.DISABLED)
    nut_sa.config(state=tk.DISABLED)
    nut_beam.config(state=tk.DISABLED)
    nut_ga.config(state=tk.DISABLED)
    nut_belief.config(state=tk.DISABLED)
    nut_and_or.config(state=tk.DISABLED)
    nut_backtrack.config(state=tk.DISABLED)
    nut_forward.config(state=tk.DISABLED)
    nut_ac3.config(state=tk.DISABLED)

def kich_hoat_nut():
    nut_dls.config(state=tk.NORMAL)
    nut_dfs.config(state=tk.NORMAL)
    nut_bfs.config(state=tk.NORMAL)
    nut_ucs.config(state=tk.NORMAL)
    nut_ids.config(state=tk.NORMAL)
    nut_best.config(state=tk.NORMAL)   
    nut_astar.config(state=tk.NORMAL)
    nut_hill.config(state=tk.NORMAL)
    nut_sa.config(state=tk.NORMAL)
    nut_beam.config(state=tk.NORMAL)
    nut_ga.config(state=tk.NORMAL)
    nut_belief.config(state=tk.NORMAL)
    nut_and_or.config(state=tk.NORMAL)
    nut_backtrack.config(state=tk.NORMAL)
    nut_forward.config(state=tk.NORMAL)
    nut_ac3.config(state=tk.NORMAL)

nut_bfs.config(command=lambda: chay_voi_thong_ke(bfs_tim_trang_thai_dich, "BFS"))
nut_dfs.config(command=lambda: chay_voi_thong_ke(dfs_tim_trang_thai_dich, "DFS"))
nut_dls.config(command=lambda: chay_voi_thong_ke(dls_tim_trang_thai_dich, "DLS"))
nut_ids.config(command=lambda: chay_voi_thong_ke(ids_tim_trang_thai_dich, "IDS"))
nut_ucs.config(command=lambda: chay_voi_thong_ke(ucs_tim_trang_thai_dich, "UCS"))
nut_best.config(command=lambda: chay_voi_thong_ke(best_first_tim_trang_thai_dich, "Best-First"))
nut_astar.config(command=lambda: chay_voi_thong_ke(a_star_tim_trang_thai_dich, "A*"))
nut_hill.config(command=lambda: chay_voi_thong_ke(hill_climbing_tim_trang_thai_dich, "Hill Climbing"))
nut_sa.config(command=lambda: chay_voi_thong_ke(simulated_annealing_tim_trang_thai_dich, "Simulated Annealing"))
nut_beam.config(command=lambda: chay_voi_thong_ke(lambda: beam_search_tim_trang_thai_dich(k=100), "Beam Search"))
nut_ga.config(command=lambda: chay_voi_thong_ke(genetic_algorithm_tim_trang_thai_dich, "Genetic Algorithm"))
nut_belief.config(command=lambda: chay_voi_thong_ke(belief_state_search, "Belief State"))
nut_and_or.config(command=lambda: chay_voi_thong_ke(and_or_search, "AND-OR"))
nut_backtrack.config(command=lambda: chay_voi_thong_ke(backtracking_search, "Backtracking"))
nut_forward.config(command=lambda: chay_voi_thong_ke(forward_checking_search, "Forward Checking"))
nut_ac3.config(command=lambda: chay_voi_thong_ke(ac3_search, "AC-3"))
nut_lich_su.config(command=xem_lich_su)
nut_xuat_csv.config(command=xuat_csv)
ban_trai.bind("<Button-1>", an_chuot)
ve_ban(ban_trai)
ve_ban(ban_phai)

cua_so.mainloop()