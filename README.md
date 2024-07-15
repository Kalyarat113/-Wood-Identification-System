# ระบบจำแนกชนิดไม้จากภาพถ่ายตัดขวาง (Cross-Section Wood Identification System)

คู่มือในการติดตั้งระบบจำแนกชนิดไม้จากภาพถ่ายตัดขวางบนเครื่องคอมพิวเตอร์

## สิ่งที่ต้องเตรียม

ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้งโปรแกรมดังต่อไปนี้ในเครื่องคอมพิวเตอร์ของคุณ:
- [Git](https://git-scm.com/downloads)
- [Visual Studio Code](https://code.visualstudio.com/download)

## ขั้นตอนการติดตั้ง

### 1. การ clone โปรเจคจาก GitHub ลงมาที่เครื่องคอมพิวเตอร์
1.1 เปิด Command Prompt
1.2 พิมพ์คำสั่ง cd <ตำแหน่งที่ต้องการให้โปรเจคอยู่>
1.3 พิมพ์คำสั่ง “git clone https://github.com/Kalyarat113/-Wood-Identification-System.git”

### 2. ทำการเปิดโปรแกรม Visual Studio Code เปิดโฟลเดอร์ของโปรเจค

### 3. เปิด Terminal 
3.1 กดปุ่ม Terminal บริเวณแถบเครื่องมือในโปรแกรม Visual Studio Code
3.2 กดเลือก New Terminal จากแถบเครื่องมือย่อยจะแสดง จะสังเกตเห็นแถบการทำงานของ Terminal อยู่ด้านล่าง
3.3 ทำการกดเครื่องหมายลูกร V ข้างๆเครื่องหมาย + 
3.4 กดเลือก Command Prompt

### 4. สร้าง Virtual Environment
4.1 พิมพ์คำสั่ง “python -m venv <ชื่อของenvที่ต้องการสร้าง>” ใน Command Prompt

### 5. เปิดใช้งาน Virtual Environment
5.1. พิมพ์คำสั่ง “.\<ชื่อของenv>\Scripts\activate” ใน Command Prompt

### 6. ติดตั้งแพ็กเกจจากไฟล์ requirements.txt
6.1. พิมพ์คำสั่ง “pip install -r requirements.txt” ใน Command Prompt ทำการรอจนกว่าการติดตั้ง
เสร็จสิ้น

### 7. รันไฟล์ main.py
7.1. พิมพ์คำสั่ง “python main.py” ใน Command Prompt
7.2. ทำการกด Ctrl พร้อมกับคลิกลิงก์ http://127.0.0.1:5000 ใน Command Prompt หรือ ป้อนลิงก์
http://127.0.0.1:5000 ในเว็บบราวเซอร์ (Web browser)
