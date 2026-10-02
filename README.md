# 人臉辨識考勤系統 👤

本專案為影像處理課程期末專題，使用 **Python 與 OpenCV** 建立簡易的人臉辨識考勤系統。

系統透過 Webcam 即時擷取影像，先使用 **Haar Cascade** 進行人臉偵測，再利用 **LBPH（Local Binary Patterns Histograms）** 進行人臉辨識。當成功辨識使用者後，系統會自動更新出席狀態並記錄辨識時間。

## 🎯 專案功能

- Webcam 即時影像擷取
- Haar Cascade 人臉偵測
- LBPH 人臉辨識
- 多使用者人臉模型訓練
- 即時顯示辨識結果
- 自動更新出席狀態
- 記錄辨識成功的日期與時間
- 未辨識成功的人臉顯示為 `Not Found`
- 程式結束後輸出所有使用者的最終出席狀態

## 🛠 使用技術

- Python
- OpenCV
- NumPy
- Haar Cascade
- LBPH Face Recognizer
- Webcam 即時影像處理

## 🧠 系統流程

```text
人臉影像資料集
        ↓
影像灰階化
        ↓
Haar Cascade 人臉偵測
        ↓
擷取人臉區域
        ↓
指定使用者 ID
        ↓
LBPH 模型訓練
        ↓
產生 face.yml
        ↓
開啟 Webcam
        ↓
即時人臉偵測與辨識
        ↓
更新出席狀態與時間
```

## 📁 專案結構

```text
face-recognition-attendance-system/
├── finalproject.py
├── face.yml
├── haarcascade_frontalface_default.xml
├── 影像期末-人臉辨識系統.pptx
├── 影像處理期末專題-人臉辨識考勤系統.pdf
└── .gitignore
```

### 主要檔案說明

- `finalproject.py`：模型訓練、人臉辨識與考勤功能
- `face.yml`：LBPH 訓練完成後產生的人臉辨識模型
- `haarcascade_frontalface_default.xml`：OpenCV Haar Cascade 人臉偵測模型
- `影像期末-人臉辨識系統.pptx`：專題簡報
- `影像處理期末專題-人臉辨識考勤系統.pdf`：專題報告
- `.gitignore`：排除未公開的人臉影像資料集

## 🔒 資料集與隱私說明

本專案原始訓練資料包含真人臉部影像。

為保護個人隱私，原始人臉照片 **未公開於此 GitHub Repository**。

以下資料夾已透過 `.gitignore` 排除：

```text
face01/
face02/
face03/
```

Repository 中僅保留程式碼、相關模型檔案以及訓練完成後產生的 `face.yml`。

程式中的使用者名稱亦已匿名化為：

```text
Person 1
Person 2
Person 3
```

## 🔄 如何自行重現

若要完整重現本專案，需要自行準備具有合法使用權限的人臉影像資料。

目前程式將三組資料分別對應為：

```text
face01/ → ID 1 → Person 1
face02/ → ID 2 → Person 2
face03/ → ID 3 → Person 3
```

依照原始程式目前的檔案讀取方式，資料集結構如下：

```text
face01/
├── 1.jpg
├── 2.jpg
├── ...
└── 47.jpg

face02/
├── 01.jpg
├── 02.jpg
├── ...
└── 038.jpg

face03/
├── 001.jpg
├── 002.jpg
├── ...
└── 0045.jpg
```

準備好資料集後，程式會依序：

1. 讀取各使用者的人臉影像
2. 將影像轉為灰階
3. 使用 Haar Cascade 偵測人臉
4. 擷取人臉區域
5. 為不同使用者指定 ID
6. 使用 LBPH 訓練人臉辨識模型
7. 將訓練結果儲存為 `face.yml`
8. 開啟 Webcam 進行即時辨識與考勤

## 📦 安裝套件

建議安裝：

```bash
pip install opencv-contrib-python numpy
```

本專案使用：

```python
cv2.face.LBPHFaceRecognizer_create()
```

因此需安裝包含 `cv2.face` 模組的 `opencv-contrib-python`。

## ▶️ 執行方式

執行：

```bash
python finalproject.py
```

程式會先進行模型訓練，接著開啟 Webcam 進行即時人臉辨識。

辨識成功後，系統會：

- 顯示辨識到的使用者
- 將狀態由「未到」更新為「已到」
- 記錄辨識成功的日期與時間

按下：

```text
q
```

即可結束 Webcam。

程式結束後，終端機會輸出所有使用者的最終出席狀態。

## ⚠️ 路徑設定

原始程式目前使用固定路徑，例如：

```text
C:\final\face01\
C:\final\face02\
C:\final\face03\
C:\final\haarcascade_frontalface_default.xml
```

如果專案放在其他位置，需要依照實際資料夾位置修改 `finalproject.py` 中的路徑。

## 💾 關於 face.yml

Repository 中提供已產生的 `face.yml` 模型檔。

不過目前 `finalproject.py` 的流程會在程式啟動時：

```text
讀取原始資料集
→ 重新訓練
→ 儲存 face.yml
→ 再載入 face.yml 進行辨識
```

因此若要直接使用 Repository 中既有的 `face.yml`，需要略過程式前半部的訓練流程，直接載入模型進行 Webcam 辨識。

若要完整重現模型訓練結果，則需自行準備人臉影像資料集。

## 📚 學習收穫

透過本專題，我實際練習並整合了：

- OpenCV 影像處理
- Webcam 即時影像擷取
- Haar Cascade 人臉偵測
- LBPH 人臉辨識
- 人臉資料前處理與模型訓練
- 辨識結果與考勤系統整合
- 日期與時間紀錄
- 個人影像資料的隱私處理
