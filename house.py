import tkinter as tk
from tkinter import ttk
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# إعداد بيانات تدريب افتراضية مع المواقع (المساحة، عدد الغرف، عدد الحمامات، الصالات، المطابخ، الشوارع المطلّة، مساحة الشوارع، الموقع)
X = np.array([
    [120, 3, 2, 1, 1, 2, 12, 8, "صنعاء"],
    [150, 4, 3, 2, 1, 1, 15, 10, "عدن"],
    [100, 2, 1, 1, 1, 2, 8, 6, "تعز"],
    [200, 5, 4, 2, 1, 3, 20, 15, "صنعاء"],
    [130, 3, 2, 1, 1, 1, 10, 7, "المكلا"],
    # يمكنك إضافة المزيد من البيانات هنا لتحسين التدريب
])

# الأسعار الافتراضية بالريال اليمني
y = np.array([30000000, 50000000, 20000000, 70000000, 35000000])

# استخدام OneHotEncoder لتحويل المواقع الجغرافية إلى تمثيل عددي
encoder = OneHotEncoder(sparse_output=False,handle_unknown='ignore')
locations = X[:, -1].reshape(-1, 1)
encoded_locations = encoder.fit_transform(locations)

# دمج الموقع الجغرافي المشفر مع بقية الخصائص
X_encoded = np.hstack((X[:, :-1].astype(float), encoded_locations))

# تقسيم البيانات إلى تدريب واختبار
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# استخدام RandomForestRegressor كبديل أكثر تعقيدًا للانحدار الخطي
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# تقييم النموذج
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")

# إنشاء واجهة المستخدم الرسومية
root = tk.Tk()
root.title("تنبؤ بسعر المنزل")

# إعداد إطار الإدخال
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0)

# تسميات وإدخالات المستخدم
labels = ["المساحة (متر مربع)", "عدد الغرف", "عدد الحمامات", "عدد الصالات", "عدد المطابخ", "عدد الشوارع", "مساحة الشارع 1", "مساحة الشارع 2", "الموقع"]
entries = []

for i, label in enumerate(labels[:-1]):
    ttk.Label(frame, text=label).grid(row=i, column=0, sticky=tk.W)
    entry = ttk.Entry(frame)
    entry.grid(row=i, column=1)
    entries.append(entry)

# إدخال الموقع الجغرافي باستخدام قائمة منسدلة
ttk.Label(frame, text="الموقع").grid(row=len(labels)-1, column=0, sticky=tk.W)
location_var = tk.StringVar()
location_menu = ttk.OptionMenu(frame, location_var, "صنعاء", "صنعاء", "عدن", "تعز", "المكلا")
location_menu.grid(row=len(labels)-1, column=1)

# دالة لحساب السعر المتوقع
def calculate_price():
    try:
        # الحصول على الإدخالات وتحويلها إلى أرقام
        inputs = [float(entry.get()) for entry in entries]
       
        # الحصول على الموقع واستخدام الترميز الخاص به
        location = location_var.get()
        location_encoded = encoder.transform([[location]])
       
        # دمج الإدخالات مع الموقع المشفر
        inputs = np.hstack((inputs, location_encoded.flatten()))
       
        # التنبؤ بالسعر باستخدام النموذج
        prediction = model.predict([inputs])[0]
        # عرض السعر المتوقع في واجهة المستخدم
        price_label.config(text=f"السعر المتوقع: {prediction:,.0f} ريال يمني")
    except ValueError:
        price_label.config(text="يرجى إدخال قيم صحيحة.")
    except Exception as e:
        price_label.config(text=f"حدث خطأ: {str(e)}")

# زر للتنبؤ بالسعر
predict_button = ttk.Button(frame, text="تنبؤ بالسعر", command=calculate_price)
predict_button.grid(row=len(labels), column=0, columnspan=2)

# منطقة لعرض السعر المتوقع
price_label = ttk.Label(frame, text="السعر المتوقع: ", font=("Arial", 14))
price_label.grid(row=len(labels) + 1, column=0, columnspan=2)

# تشغيل الواجهة الرسومية
root.mainloop()