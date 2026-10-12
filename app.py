import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# #1. Cau hinh trang web
st.set_page_config(
    page_title="Quan ly diem sinh vien",
    page_icon="📚",
    layout="wide"
)

st.title("QUAN LY DIEM SINH VIEN")
st.write("Ung dung quan ly diem hoc tap bang Python va Streamlit")

# #2. Tao DataFrame du lieu sinh vien
data = {
    "Ho_ten": [
        "Nguyen Van An", "Tran Thi Binh", "Le Van Cuong",
        "Pham Thi Dung", "Hoang Van Em", "Vo Thi Giang",
        "Dang Van Hung", "Bui Thi Lan", "Do Van Minh",
        "Nguyen Thi Nga"
    ],
    "Chuyen_can": [9, 8, 7, 10, 6, 9, 8, 7, 5, 10],
    "Giua_ky": [8, 7, 6, 9, 5, 8, 7, 6, 4, 9],
    "Cuoi_ky": [9, 8, 7, 9, 6, 9, 8, 7, 5, 10]
}

df = pd.DataFrame(data)

# #3. Tinh diem tong ket
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
)

# #4. Xep loai sinh vien
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7.0:
        return "Kha"
    elif diem >= 5.0:
        return "Trung binh"
    else:
        return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# #5. Hien thi bang diem
st.header("1. Bang diem sinh vien")
st.dataframe(df, use_container_width=True)

# #6. Thong ke ket qua hoc tap
diem_tb = df["Tong_ket"].mean()
sv_cao_nhat = df.loc[df["Tong_ket"].idxmax()]
sv_thap_nhat = df.loc[df["Tong_ket"].idxmin()]
so_sv_dat = int((df["Tong_ket"] >= 5).sum())

st.header("2. Thong ke ket qua")

cot1, cot2, cot3, cot4 = st.columns(4)

cot1.metric("Diem trung binh", f"{diem_tb:.2f}")
cot2.metric("Diem cao nhat", f"{sv_cao_nhat['Tong_ket']:.2f}")
cot3.metric("Diem thap nhat", f"{sv_thap_nhat['Tong_ket']:.2f}")
cot4.metric("So sinh vien dat", f"{so_sv_dat}/10")

st.write("**Sinh vien co diem cao nhat:**",
         sv_cao_nhat["Ho_ten"])
st.write("**Sinh vien co diem thap nhat:**",
         sv_thap_nhat["Ho_ten"])

# #7. Chon sinh vien xem chi tiet
st.header("3. Tra cuu sinh vien")

ten_sv = st.selectbox(
    "Chon ten sinh vien:",
    df["Ho_ten"]
)

sv = df[df["Ho_ten"] == ten_sv].iloc[0]

st.write("**Ho ten:**", sv["Ho_ten"])
st.write("**Diem chuyen can:**", sv["Chuyen_can"])
st.write("**Diem giua ky:**", sv["Giua_ky"])
st.write("**Diem cuoi ky:**", sv["Cuoi_ky"])
st.write("**Diem tong ket:**", f"{sv['Tong_ket']:.2f}")
st.write("**Xep loai:**", sv["Xep_loai"])

# #8. Ve bieu do cot
st.header("4. Bieu do diem tong ket")

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_title("DIEM TONG KET CUA 10 SINH VIEN")
ax.set_xlabel("Ho ten sinh vien")
ax.set_ylabel("Diem tong ket")
ax.set_ylim(0, 10)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

# #9. Thong tin nguoi thuc hien
st.divider()
st.caption("Nguoi thuc hien: Nguyễn Nhật Tiến")
st.caption("Ma so sinh vien: 05120801317")
