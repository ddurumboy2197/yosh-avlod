def avlodni_analiz(qoyil_yili):
    yosh = 2024 - qoyil_yili
    avlod = "1" if yosh < 25 else "2" if yosh < 50 else "3"
    return avlod

qoyil_yili = int(input("Foydalanuvchi yoshini kiritib, u qaysi avlodga tegishligini aniqlang: "))
print(avlodni_analiz(qoyil_yili))
```

```python
def avlodni_analiz(qoyil_yili):
    yosh = 2024 - qoyil_yili
    avlod = ["1", "2", "3"][yosh // 25]
    return avlod

qoyil_yili = int(input("Foydalanuvchi yoshini kiritib, u qaysi avlodga tegishligini aniqlang: "))
print(avlodni_analiz(qoyil_yili))
