import cv2

# Завантажуємо класифікатор для виявлення облич
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Завантажуємо зображення
img = cv2.imread('Baranovskiy.jpg')

# Перетворюємо зображення в градації сірого (потрібно для виявлення облич)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Використовуємо метод detectMultiScale для виявлення облич на зображенні
# Параметри методу: зображення, масштаб-фактор, мінімальна кількість сусідів
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# Проходимося по кожному виявленому обличчю і малюємо навколо нього прямокутник
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Відображаємо зображення з виділеними обличчями
cv2.imshow("Result", img)

# Очікуємо, доки користувач натисне будь-яку клавішу
cv2.waitKey(0)

