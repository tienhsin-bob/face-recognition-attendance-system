import cv2
import numpy as np
from datetime import datetime

# 載入人臉追蹤模型
detector = cv2.CascadeClassifier(r"C:\\final\\haarcascade_frontalface_default.xml")
recog = cv2.face.LBPHFaceRecognizer_create()      # 啟用訓練人臉模型方法
faces = []   # 儲存人臉位置大小的串列
ids = []     # 記錄該人臉 id 的串列

# 記錄到達狀態
attendance = {
    '1': {"name": "Ling Chi Ni", "status": "未到", "time": None},
    '2': {"name": "Kuo Miao Hsuan", "status": "未到", "time": None},
    '3': {"name": "Tiang Shin", "status": "未到", "time": None},
}

# 資料訓練部分
for i in range(1, 48):
    img = cv2.imread(f"C:\\final\\face01\\{i}.jpg")
    if img is None:
        print(f"/Users/samhsu/Desktop/final/face01/{i}.jpg")
        continue  # 跳過無法讀取的檔案

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 色彩轉換成黑白
    img_np = np.array(gray, 'uint8')              # 轉換成指定編碼的 numpy 陣列
    face = detector.detectMultiScale(gray)        # 擷取人臉區域
    for (x, y, w, h) in face:
        faces.append(img_np[y:y+h, x:x+w])        # 記錄1人臉的位置和大小內像素的數值
        ids.append(1)

for i in range(1, 39):
    img = cv2.imread(f"C:\\final\\face02\\0{i}.jpg")
    if img is None:
        print(f"/Users/samhsu/Desktop/final/face02/0{i}.jpg")
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_np = np.array(gray, 'uint8')
    face = detector.detectMultiScale(gray)
    for (x, y, w, h) in face:
        faces.append(gray[y:y+h, x:x+w])
        ids.append(2)

for i in range(1, 46):
    img = cv2.imread(f"C:\\final\\face03\\00{i}.jpg")
    if img is None:
        print(f"/Users/samhsu/Desktop/final/face03/00{i}.jpg")
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_np = np.array(gray, 'uint8')
    face = detector.detectMultiScale(gray)
    for (x, y, w, h) in face:
        faces.append(gray[y:y+h, x:x+w])
        ids.append(3)

print('training...')
recog.train(faces, np.array(ids))  # 開始訓練
recog.save('face.yml')             # 訓練完成儲存為 face.yml
print('ok!')

# 實時辨識部分
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('face.yml')
face_cascade = cv2.CascadeClassifier(r"C:\\final\\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)  # 開啟攝影機
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break

    img = cv2.resize(img, (540, 300))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        idnum, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        idnum_str = str(idnum)

        # 偵測到人臉並更新狀態
        if confidence < 60 and idnum_str in attendance:
            if attendance[idnum_str]["status"] == "未到":
                attendance[idnum_str]["status"] = "已到"
                attendance[idnum_str]["time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{attendance[idnum_str]['name']} 已到 - 時間: {attendance[idnum_str]['time']}")

            text = attendance[idnum_str]["name"]
        else:
            text = "Not Found"

        cv2.putText(img, text, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Attendance', img)
    if cv2.waitKey(5) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# 結束程式後輸出最終狀態
print("\n最終到達狀態:")
for idnum, info in attendance.items():
    print(f"{info['name']} - {info['status']} - {info['time'] if info['time'] else '無到達時間'}")
