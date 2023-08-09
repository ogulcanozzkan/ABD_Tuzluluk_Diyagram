## Kütüphane İmport İşlemi
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import base64
from io import BytesIO


## Sag-Chem logosunu içeri akatarma
image_path = "SAG-Chem3.png"
st.image(image_path, width=250, use_column_width=False)


## Başlık ve Excel dosyayısı içeri aktarımı
st.title("ABD Tuzluluk Diyagramı")


## Veri Dosyasını indirme fonksiyonu ve Başlık
st.subheader("1.Veri Dosyasını İndiriniz")
excel_file_path = "Data1.xlsx"

def download_excel():
    with open(excel_file_path, "rb") as f:
        bytes_data = f.read()
        b64_data = base64.b64encode(bytes_data).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64_data}" download="{excel_file_path}">Buraya Tıklayarak Excel Dosyasını İndir</a>'
        st.markdown(href, unsafe_allow_html=True)


# İndirme bağlantısını görüntüle
st.write("Örnek Veri Dosyası, Excel formatında size verilmektedir. Örnek veri dosyasını indiriniz. Verilen sütunları bozmadan, verilerinizi giriniz.")
download_excel()


## Excel dosyasını kullanıcıdan alarak, Data olarak kullanma
st.subheader("2.Excel Dosyanızı Yükleyiniz")
st.write("Verilen örnek excel dosyasına, verilerinizi girdikten sonra yükleyiniz. ")
uploaded_file = st.file_uploader("Excel dosyanızı yükleyin", type=["xlsx", "xls"])
if uploaded_file is not None:
    data = pd.read_excel(uploaded_file, header=0)
    data["Name"] = data["Name"].astype(str)
    data["Sodyum(mg/l)"] = data["Sodyum(mg/l)"].astype(float)
    data["Kalsiyum(mg/L)"] = data["Kalsiyum(mg/L)"].astype(float)
    data["Magnezyum(mg/l)"] = data["Magnezyum(mg/l)"].astype(float)
    data["İletkenlik(µS/cm)"] = data["İletkenlik(µS/cm)"].astype(float)
    data["SAR"] = data["Sodyum(mg/l)"] / (np.sqrt((data["Kalsiyum(mg/L)"] + data["Magnezyum(mg/l)"]) / 2))
    st.success('Başarılı!', icon="✅")
    st.subheader("3.Verilerinizi Kontrol Ediniz")
    st.dataframe(data.head(200))



## Scatter Plot oluşturma
colors = plt.cm.cool(np.linspace(0, 1, len(data)))
labels = data["Name"]
fig, ax = plt.subplots(figsize=(16, 14))
for i in range(len(data)):
    ax.scatter(data.loc[i, 'İletkenlik(µS/cm)'], data.loc[i, 'SAR'],
                marker="o", s=100, c=[colors[i]], edgecolors="black", label=data.loc[i, "Name"])
ax.legend(loc="upper right",bbox_to_anchor=(1.13,1.0))


## Birinci,Solda ki Colorbarı oluşturma
cmap = plt.cm.RdYlGn.reversed()
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=len(data) - 1))
sm.set_array([])
cbar = plt.colorbar(sm, ticks=np.arange(len(data)), location="left",aspect=17)
cbar.set_label("Sodyum Tehlikesi")
cbar.ax.set_yticklabels([])
cbar.ax.set_position(cbar.ax.get_position().translated(+0.0660, 0.225))
cbar.ax.set_position([cbar.ax.get_position().x0,
                      cbar.ax.get_position().y0,
                      cbar.ax.get_position().width * 0.8,
                      cbar.ax.get_position().height * 0.7])
cbar.outline.set_linewidth(1.2)
cbar.outline.set_visible(False)
cbar.ax.tick_params(direction='out', length=0)


## İkinci,Altta ki Colorbarı oluşturma
cmap = plt.cm.RdYlGn.reversed()
sm1 = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=len(data) - 1))
sm1.set_array([])
cbar1 = plt.colorbar(sm, ticks=np.arange(len(data)), location="bottom",aspect=19.5)
cbar1.set_label("           Tuzluluk Tehlikesi")
cbar1.ax.set_xticklabels([])
cbar1.ax.set_position(cbar1.ax.get_position().translated(+0.00000, 0.11))
cbar1.ax.set_position([cbar1.ax.get_position().x0,
                       cbar1.ax.get_position().y0,
                       cbar1.ax.get_position().width * 0.94,
                       cbar1.ax.get_position().height * 0.7])
cbar1.outline.set_linewidth(1.2)
cbar1.outline.set_visible(False)
cbar1.ax.tick_params(direction='out', length=0)


## Grafik Noktalarını belirleme
x = [0, 250, 750, 2250, 5000]
y = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]


## Grafik başlıkları
plt.xlabel('İletkenlik [µS/cm]')
plt.ylabel('Sodyum Adsorpsiyon Oranı (SAR)')
plt.title('ABD Tuzluluk Diyagramı')


## Eksen aralıkları çizdirme
ax.set_xticks(x)
ax.set_yticks(y)


## Eksen çizgilerinin rengi
ax.xaxis.label.set_color('black')
ax.yaxis.label.set_color('black')
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
ax.plot([0, 5000], [10, 2], color="gray")
ax.plot(x, [0] * len(x), color="gray")
ax.plot([0, 5000], [30, 30], color="gray")
ax.plot([0, 5000], [18, 6.5], color="gray")
ax.plot([0, 5000], [26, 11], color="gray")


## Çizgi Noktaları
a=[0,100,250,750,2250,5000]
b=[10,10,10,10,10,10]
c=[0,0,0,0,0,0]
d=[20,20,20,20,20,20]
e=[30,30,30,30,30,30]
f=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
g=[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
h=[250,250,250,250,250,250,250,250,250,250,250,250,250,250,250,250]
ı=[750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750]
i=[2250,2250,2250,2250,2250,2250,2250,2250,2250,2250,2250,2250,2250,2250,2250,2250]
j=[5000,5000,5000,5000,5000,5000,5000,5000,5000,5000,5000,5000,5000,5000,5000,5000]
k=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
t=[10,2]
ş=[0,5000]
u=[18,6.5]
ü=[26,11]


## Plot çizgilerinin yapılması
plt.plot(a,e,color="gray")
plt.plot(k,f,color="gray")
plt.plot(h,f,color="gray")
plt.plot(ı,f,color="gray")
plt.plot(i,f,color="gray")
plt.plot(j,f,color="gray")
plt.plot(ş,u,color="gray")
plt.plot(ş,ü,color="gray")


## Grafiğin bölgelere ayrılması
ax.fill_between([0, 250], [10, 9.5], [0], color='#66ff00', alpha=0.05)
ax.text(20, 3, 'C1-S1', fontsize=7, color='black')

ax.fill_between([250, 750], [9.5, 8.80], 0, color="green", alpha=0.05)
ax.text(400, 3, 'C2-S1', fontsize=7, color='black')

ax.fill_between([750, 2250], [8.80, 6.50], 0, color='#888404', alpha=0.05)
ax.text(1300, 3, 'C3-S1', fontsize=7, color='black')

ax.fill_between([2250, 5000], [6.50, 2], 0, color="#ffdf00", alpha=0.05)
ax.text(2700, 3, 'C4-S1', fontsize=7, color='black')

ax.fill_between([0, 250], [18, 17.50], [10, 9.68], color="green", alpha=0.05)
ax.text(20, 12, 'C1-S2', fontsize=7, color='black')

ax.fill_between([250, 750], [17.50, 16.30], [9.68, 8.93], color='yellow', alpha=0.05)
ax.text(400, 12, 'C2-S2', fontsize=7, color='black')

ax.fill_between([750, 2250], [16.30, 12.90], [8.93, 6.45], color="#e49b0f", alpha=0.05)
ax.text(1300, 10, 'C3-S2', fontsize=7, color='black')

ax.fill_between([2250, 5000], [12.90, 6.5], [6.5, 2], color="#FF7F00", alpha=0.05)
ax.text(2700, 9, 'C4-S2', fontsize=7, color='black')

ax.fill_between([0, 250], [26, 25.34], [18, 17.50], color='#888404', alpha=0.05)
ax.text(20, 20, 'C1-S3', fontsize=7, color='black')

ax.fill_between([250, 750], [25.34, 23.81], [17.50, 16.30], color="#e49b0f", alpha=0.05)
ax.text(400, 20, 'C2-S3', fontsize=7, color='black')

ax.fill_between([750, 2250], [23.81, 19.34], [16.30, 12.92], color="#FF7F00", alpha=0.05)
ax.text(1300, 18, 'C3-S3', fontsize=7, color='black')

ax.fill_between([2250, 5000], [19.34, 11.04], [12.92, 6.5], color="#f34723", alpha=0.05)
ax.text(2700, 15, 'C4-S3', fontsize=7, color='black')

ax.fill_between([0, 250], [30, 30], [26, 25.34], color="#ffdf00", alpha=0.05)
ax.text(20, 27, 'C1-S4', fontsize=7, color='black')

ax.fill_between([250, 750], [30, 30], [25.34, 23.81], color="#FF7F00", alpha=0.05)
ax.text(400, 27, 'C2-S4', fontsize=7, color='black')

ax.fill_between([750, 2250], [30, 30], [23.81, 19.34], color="#f34723", alpha=0.05)
ax.text(1300, 27, 'C3-S4', fontsize=7, color='black')

ax.fill_between([2250, 5000], [30, 30], [19.34, 11.04], color="red", alpha=0.05)
ax.text(2700, 27, 'C4-S4', fontsize=7, color='black')


## Grafiğin kenarlarında ki yazılar
ax.text(0.01, 0.2, 'DÜŞÜK', rotation=90, transform=plt.gca().transAxes, va='center', weight='bold', fontsize=8)
ax.text(0.01, 0.48, 'ORTA', rotation=90, transform=plt.gca().transAxes, va='center', weight='bold', fontsize=8)
ax.text(0.01, 0.72, 'YÜKSEK', rotation=90, transform=plt.gca().transAxes, va='center', weight='bold', fontsize=8)
ax.text(0.01, 0.90, 'ÇOK YÜKSEK', rotation=90, transform=plt.gca().transAxes, va='center', weight='bold', fontsize=8)

ax.text(0.07, 0.02, 'DÜŞÜK', transform=plt.gca().transAxes, ha='center', weight='bold', fontsize=8)
ax.text(0.13, 0.02, 'ORTA', transform=plt.gca().transAxes, ha='center', weight='bold', fontsize=8)
ax.text(0.30, 0.02, 'YÜKSEK', transform=plt.gca().transAxes, ha='center', weight='bold', fontsize=8)
ax.text(0.7, 0.02, 'ÇOK YÜKSEK', transform=plt.gca().transAxes, ha='center', weight='bold', fontsize=8)


## Grafiği gösterme ve başlık
st.subheader("4.ABD Tuzluluk Diyagramı")
st.pyplot(fig)

def download_file(fig, file_format):
    output = BytesIO()

    if file_format == 'pdf':
        fig.savefig(output, format='pdf')
        file_extension = 'pdf'
    elif file_format == 'png':
        fig.savefig(output, format='png')
        file_extension = 'png'

    output.seek(0)
    b64 = base64.b64encode(output.read()).decode()
    href = f'<a href="data:image/{file_extension};base64,{b64}" download="grafik.{file_extension}">Grafik İndir ({file_extension.upper()})</a>'
    st.markdown(href, unsafe_allow_html=True)


## Grafiği indirebilme bölümü
st.subheader("5.Grafiğinizi İndiriniz")

png_buffer = BytesIO()
fig.savefig(png_buffer, format='png')
png_buffer.seek(0)  # Arabelleği başa al
st.download_button(
    label="Grafiği İndir(PNG)",
    data=png_buffer,
    file_name="ABD_Tuzluluk_Diyagramı.png",
    mime="image/png"
)


png_buffer = BytesIO()
fig.savefig(png_buffer, format='pdf')
png_buffer.seek(0)  # Arabelleği başa al
st.download_button(
    label="Grafiği İndir(PDF)",
    data=png_buffer,
    file_name="ABD_Tuzluluk_Diyagramı.pdf",
    mime="image/pdf"
)

