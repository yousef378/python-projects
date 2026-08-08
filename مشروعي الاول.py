print("--- 🎓 برنامج حساب النسبة والتقدير ---")

# بناخد اسم الطالب ومجموعه
student_name = input("ادخل اسمك: ")
score = input("ادخل مجموعك من 100: ")

# بنحول المجموع لـ رقم صحيح
score = int(score)

print("\nنتيجة الطالب:", student_name)

# استخدام الـ If Conditions اللي درستها مع الزيرو
if score >= 85:
    print("التقدير: ممتاز (A) 🌟")
elif score >= 75:
    print("التقدير: جيد جداً (B) 👍")
elif score >= 65:
    print("التقدير: جيد (C) 🙂")
elif score >= 50:
    print("التقدير: مقبول (D) 😐")
else:
    print("التقدير: راسب (F) 💔 .. شد حيلك المرة الجاية!")