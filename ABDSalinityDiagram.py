## Kütüphanlerin yüklenmesi
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## Verinin içeri aktarılması
data = pd.read_excel("Data.xlsx",header=0)

## Veri tipini sayısala çevirme
data["Name"]=data["Name"].astype(str)
data["Sodyum(mg/l)"] = data["Sodyum(mg/l)"].astype(float)
data["Kalsiyum(mg/L)"] = data["Kalsiyum(mg/L)"].astype(float)
data["Magnezyum(mg/l)"] = data["Magnezyum(mg/l)"].astype(float)
data["İletkenlik(µS/cm)"] = data["İletkenlik(µS/cm)"].astype(float)

## SAR formülün matematiksel hali
data["SAR"] = data["Sodyum(mg/l)"] / (np.sqrt((data["Kalsiyum(mg/L)"] + data["Magnezyum(mg/l)"]) / 2))

## Scatter Plot oluşturma
colors = plt.cm.cool(np.linspace(0, 1, len(data)))
labels = data["Name"]

plt.figure(figsize=(16, 14))
for i in range(len(data)):
    plt.scatter(data.loc[i, 'İletkenlik(µS/cm)'], data.loc[i, 'SAR'],
                marker="o",s=75, c=[colors[i]],edgecolors="black", label=data.loc[i,"Name"])
plt.legend(loc="upper right")

## Birinci, Solda ki Colorbarı oluşturma
cmap = plt.cm.RdYlGn.reversed()
sm = plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn.reversed(), norm=plt.Normalize(vmin=0, vmax=len(data)-1))
sm.set_array([])
cbar= plt.colorbar(sm, ticks=np.arange(len(data)),location="left")
cbar.set_label("Sodyum Tehlikesi")
cbar.ax.set_yticklabels([])
cbar.ax.set_position(cbar.ax.get_position().translated(+0.0660, 0.225))
cbar.ax.set_position([cbar.ax.get_position().x0,
                      cbar.ax.get_position().y0,
                      cbar.ax.get_position().width * 0.8,
                      cbar.ax.get_position().height * 0.7])
cbar.outline.set_linewidth(1.2)


## İkinci, Altta ki Colorbarı oluşturma
cmap = plt.cm.RdYlGn.reversed()
sm1 = plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn.reversed(), norm=plt.Normalize(vmin=0, vmax=len(data)-1))
sm1.set_array([])
cbar1 = plt.colorbar(sm, ticks=np.arange(len(data)),location="bottom")
cbar1.set_label("Tuzluluk Tehlikesi")
cbar1.ax.set_xticklabels([])
cbar1.ax.set_position(cbar1.ax.get_position().translated(+0.024, 0.08))
cbar1.ax.set_position([cbar1.ax.get_position().x0,
                      cbar1.ax.get_position().y0,
                      cbar1.ax.get_position().width * 0.94,
                      cbar1.ax.get_position().height * 0.7])
cbar1.outline.set_linewidth(1.2)

## Grafik Noktaları
x=[0,250,750,2250,5000]
y=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]

## Eksen başlıkları ve etiketleri
plt.xlabel('İletkenlik [µS/cm]')
plt.ylabel('Sodyum Adsorpsiyon Oranı (SAR)')
plt.title('Wilcox Tuzluluk Diyagramı')

## plt grid mesafeleri
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

## Eksen aralıkları çizdirme
plt.xticks(x)
plt.yticks(y)

## Eksen çizgilerinin rengi
ax = plt.gca()
ax.xaxis.label.set_color('black')
ax.yaxis.label.set_color('black')
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
plt.plot(ş,t,color="gray")
plt.plot(a,c,color="gray")


##plt.plot(a,d,color="black")
plt.plot(a,e,color="gray")
plt.plot(k,f,color="gray")
plt.plot(h,f,color="gray")
plt.plot(ı,f,color="gray")
plt.plot(i,f,color="gray")
plt.plot(j,f,color="gray")
plt.plot(ş,u,color="gray")
plt.plot(ş,ü,color="gray")

plt.fill_between([0,250],[10,9.5], [0], color='#66ff00', alpha=0.05)
plt.text(20, 3, 'C1-S1', fontsize=7, color='black')

plt.fill_between([250,750], [9.5,8.80], 0, color="green", alpha=0.05)
plt.text(400, 3, 'C2-S1', fontsize=7, color='black')

plt.fill_between([750,2250], [8.80,6.50], 0, color='#888404', alpha=0.05)
plt.text(1300, 3, 'C3-S1', fontsize=7, color='black')

plt.fill_between([2250,5000], [6.50,2], 0, color="#ffdf00", alpha=0.05)
plt.text(2700, 3, 'C4-S1', fontsize=7, color='black')


plt.fill_between([0,250], [18,17.50],[10,9.68], color="green", alpha=0.05)
plt.text(20, 12, 'C1-S2', fontsize=7, color='black')

plt.fill_between([250,750], [17.50,16.30],[9.68,8.93], color='yellow', alpha=0.05)
plt.text(400, 12, 'C2-S2', fontsize=7, color='black')

plt.fill_between([750,2250], [16.30,12.90],[8.93,6.45], color="#e49b0f",alpha=0.05)
plt.text(1300, 10, 'C3-S2', fontsize=7, color='black')

plt.fill_between([2250,5000], [12.90,6.5],[6.5,2], color="#FF7F00",alpha=0.05)
plt.text(2700, 9, 'C4-S2', fontsize=7, color='black')


plt.fill_between([0,250], [26,25.34],[18,17.50], color='#888404',alpha=0.05)
plt.text(20, 20, 'C1-S3', fontsize=7, color='black')

plt.fill_between([250,750], [25.34,23.81],[17.50,16.30], color="#e49b0f",alpha=0.05)
plt.text(400, 20, 'C2-S3', fontsize=7, color='black')

plt.fill_between([750,2250], [23.81,19.34],[16.30,12.92], color="#FF7F00",alpha=0.05)
plt.text(1300, 18, 'C3-S3', fontsize=7, color='black')

plt.fill_between([2250,5000], [19.34,11.04],[12.92,6.5], color="#f34723",alpha=0.05)
plt.text(2700, 15, 'C4-S3', fontsize=7, color='black')


plt.fill_between([0,250], [30,30],[26,25.34], color="#ffdf00",alpha=0.05)
plt.text(20, 27, 'C1-S4', fontsize=7, color='black')

plt.fill_between([250,750], [30,30],[25.34,23.81], color="#FF7F00",alpha=0.05)
plt.text(400, 27, 'C2-S4', fontsize=7, color='black')

plt.fill_between([750,2250], [30,30],[23.81,19.34], color="#f34723",alpha=0.05)
plt.text(1300, 27, 'C3-S4', fontsize=7, color='black')

plt.fill_between([2250,5000], [30,30],[19.34,11.04], color="red",alpha=0.05)
plt.text(2700, 27, 'C4-S4', fontsize=7, color='black')


plt.text(0.01, 0.2, 'DÜŞÜK', rotation=90, transform=plt.gca().transAxes, va='center',weight='bold',fontsize=8)
plt.text(0.01, 0.48, 'ORTA', rotation=90, transform=plt.gca().transAxes, va='center',weight='bold',fontsize=8)
plt.text(0.01, 0.72, 'YÜKSEK', rotation=90, transform=plt.gca().transAxes, va='center',weight='bold',fontsize=8)
plt.text(0.01, 0.92, 'ÇOK YÜKSEK', rotation=90, transform=plt.gca().transAxes, va='center',weight='bold',fontsize=8)

plt.text(0.07, 0.02, 'DÜŞÜK', transform=plt.gca().transAxes, ha='center',weight='bold',fontsize=8)
plt.text(0.13, 0.02, 'ORTA', transform=plt.gca().transAxes, ha='center',weight='bold',fontsize=8)
plt.text(0.30, 0.02, 'YÜKSEK', transform=plt.gca().transAxes, ha='center',weight='bold',fontsize=8)
plt.text(0.7, 0.02, 'ÇOK YÜKSEK', transform=plt.gca().transAxes, ha='center',weight='bold',fontsize=8)

plt.show(block=True)
plt.pause(5)
