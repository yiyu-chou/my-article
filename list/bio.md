---
title_main: 基於智慧邊緣計算的
title_gradient: 低延遲環境感測整合系統開發
description: 探討如何整合 ESP32 單晶片、多感測器反饋迴路，並透過極簡自建 API 實現邊緣數據初篩與雲端零延遲同步。
category: 自主學習 / 工程專案
tags: [物聯網, 邊緣計算, ESP32, 卡爾曼濾波]
date: 2026-07-18
author: 周奕宇 YiYu Chou
---

# 台灣特有種介紹

台灣因地形多變、海拔落差大，加上長期與亞洲大陸隔離，孕育出許多世界上僅分布於台灣的特有種。這些物種具有高度的生態價值，也是研究演化、生態及保育的重要對象。

---

## 1. 台灣黑熊（Ursus thibetanus formosanus）

![台灣黑熊](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Formosan_Black_Bear.JPG/250px-Formosan_Black_Bear.JPG)

**圖片來源：** wikimedia

### 簡介
台灣黑熊是台灣唯一原生熊類，也是台灣最具代表性的保育動物之一。胸前具有明顯的白色 V 字形斑紋，因此又被稱為「月熊」。

### 棲息環境
- 海拔約 1,000～3,500 公尺山區森林
- 玉山國家公園
- 雪霸國家公園
- 中央山脈森林

### 保育現況
目前屬於瀕危野生動物，主要受到棲地破壞與非法獵捕影響。

---

## 2. 帝雉（Syrmaticus mikado）

![帝雉](https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Female_Mikado_Pheasant.jpg/330px-Female_Mikado_Pheasant.jpg)

**圖片來源：** wikimedia

### 簡介
帝雉為台灣特有鳥類，也是台灣國寶級野鳥。雄鳥羽色呈深藍黑色，尾羽修長，非常美麗，因此有「迷霧中的王者」之稱。

### 棲息環境
- 中高海拔森林
- 海拔約 1,800～3,500 公尺

### 保育現況
目前已列入珍貴稀有保育類野生動物。

---

## 3. 藍腹鷴（Lophura swinhoii）

![藍腹鷴](https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Female_Mikado_Pheasant.jpg/330px-Female_Mikado_Pheasant.jpg)

**圖片來源：** https://commons.wikimedia.org/wiki/Category:Lophura_swinhoii

### 簡介
藍腹鷴是台灣特有雉科鳥類，雄鳥擁有亮麗的藍色羽毛與鮮紅色腳，被譽為「台灣最美麗的野鳥」。

### 棲息環境
- 中低海拔森林
- 闊葉林

### 保育現況
目前受到棲地破壞及人為干擾威脅。

---

## 4. 櫻花鉤吻鮭（Oncorhynchus masou formosanus）

![櫻花鉤吻鮭](https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Female_Mikado_Pheasant.jpg/330px-Female_Mikado_Pheasant.jpg)

**圖片來源：** wikimedia

### 簡介
櫻花鉤吻鮭是冰河時期遺留下來的珍貴魚類，也是全球分布最南端的鮭魚，被稱為「國寶魚」。

### 棲息環境
- 雪霸國家公園七家灣溪
- 高山冷水溪流

### 保育現況
受到氣候變遷、水質污染及溪流工程影響，目前為高度保育物種。

---

## 5. 台灣獼猴（Macaca cyclopis）

![台灣獼猴](https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Female_Mikado_Pheasant.jpg/330px-Female_Mikado_Pheasant.jpg)

**圖片來源：** https://commons.wikimedia.org/wiki/Category:Macaca_cyclopis

### 簡介
台灣獼猴是台灣唯一原生靈長類動物，具有高度社會性，生活於森林之中，以水果、嫩葉及昆蟲為食。

### 棲息環境
- 全台中低海拔森林
- 山區自然保護區

### 保育現況
雖然族群較穩定，但仍受到棲地縮減及人猴衝突影響。

---

# 小結

台灣特有種是經過數百萬年演化所形成的重要自然資產，不僅具有生態價值，也展現出台灣豐富的自然特色。透過建立國家公園、保護區、野生動物保育法及全民環境教育，可以共同守護這些珍貴的生命資源，讓生物多樣性得以永續保存，並為下一代留下完整而健康的自然環境。