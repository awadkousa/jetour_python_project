# Jetour Python Project

مشروع موقع سيارات Jetour باستخدام Python Flask وSQLite.

## التشغيل

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

ثم افتح المتصفح على:

`http://127.0.0.1:5000`

## الصفحات
- `/` الصفحة الرئيسية
- `/admin` لوحة الإدارة

## ملاحظات
- قاعدة البيانات تُنشأ تلقائياً باسم `cars.db`
- الصور تتم إضافتها من خلال رابط مباشر
