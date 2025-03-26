### **Excel Processor - Desktop App**

🚀 A cross-platform **Excel processing tool** built with Python! It allows you to:  
✅ Identify & separate **duplicate and unique rows**  
✅ Perform **sorting** (ascending/descending, numeric/alphabetical)  
✅ **Split large Excel files** into smaller chunks  
✅ Works on **Windows & Linux**

---

## **🛠 Installation**

### **Windows (exe)**

1. Download the latest **`app.exe`** from [Releases](https://github.com/your-username/your-repo/releases)
2. Double-click to run!

### **Linux (Debian-based)**

1. Download **`excel-processor.deb`** from [Releases](https://github.com/your-username/your-repo/releases)
2. Install using:
   ```bash
   sudo dpkg -i excel-processor.deb
   ```
3. Run using:
   ```bash
   excel-processor
   ```

---

## **🚀 Features**

🔹 **Duplicate Detection** – Check for duplicates based on selected columns using **AND/OR** logic  
🔹 **Sorting** – Sort numerically or alphabetically (ascending/descending)  
🔹 **Row Splitting** – Divide large files into multiple **smaller** files  
🔹 **Cross-Platform** – Works on both **Windows & Linux**

---

## **🔧 Build from Source**

### **1️⃣ Setup Environment**

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
```

### **2️⃣ Run the App**

```bash
python app.py
```

### **3️⃣ Build Executable**

#### **Windows**

```bash
pyinstaller --onefile --windowed app.py
```

#### **Linux**

```bash
pyinstaller --onefile --windowed app.py
dpkg-deb --build excel-processor
```

---

## **📦 GitHub Actions - Auto Release**

This project uses **GitHub Workflows** to:  
✅ Automatically build **Windows (.exe)** and **Linux (.deb)** binaries  
✅ Upload them to [GitHub Releases](https://github.com/your-username/your-repo/releases)

To trigger a new release:

1. **Create a new tag**
   ```bash
   git tag v1.0
   git push origin v1.0
   ```

---

## **📜 License**

📝 MIT License – Feel free to modify and use!

---
