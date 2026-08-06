# CustomTkinter Image Viewer

A simple desktop image viewer built with **CustomTkinter** and **Pillow**. Select any image file through a native file dialog and preview it instantly in a clean, dark-themed window.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-teal)

---

## 🇬🇧 English

### Overview
A lightweight image viewer application. Clicking the "Select Image" button opens the operating system's native file picker, and the chosen image is displayed instantly inside the app window.

### Features
- Native file selection dialog (PNG, JPG, JPEG, BMP supported)
- Instant image preview, resized to fit the window
- Simple, modern dark-themed interface
- No hardcoded file paths — works on any machine out of the box

### Requirements
- Python 3.10 or higher
- `customtkinter`
- `Pillow`

### Installation
```bash
pip install customtkinter pillow
```

### Usage
```bash
python image_viewer.py
```

Click **"Select Image"**, choose a file from your system, and it will appear in the preview area above the button.

### How it works
`filedialog.askopenfilename()` opens the operating system's native file browser, filtered to common image formats. The selected file is loaded with `PIL.Image.open()`, converted into a `CTkImage` object sized to fit the display area, and applied to the label widget for instant preview.

---

## 🇩🇪 Deutsch

### Überblick
Eine schlanke Bildbetrachter-Anwendung. Ein Klick auf die Schaltfläche "Select Image" öffnet den nativen Dateiauswahldialog des Betriebssystems, und das ausgewählte Bild wird sofort im Anwendungsfenster angezeigt.

### Funktionen
- Nativer Dateiauswahldialog (PNG, JPG, JPEG, BMP werden unterstützt)
- Sofortige Bildvorschau, an das Fenster angepasst
- Einfache, moderne Benutzeroberfläche im Dunkelmodus
- Keine fest codierten Dateipfade — funktioniert sofort auf jedem Rechner

### Voraussetzungen
- Python 3.10 oder höher
- `customtkinter`
- `Pillow`

### Installation
```bash
pip install customtkinter pillow
```

### Verwendung
```bash
python image_viewer.py
```

Klicke auf **"Select Image"**, wähle eine Datei von deinem System aus, und sie erscheint im Vorschaubereich oberhalb der Schaltfläche.

### Funktionsweise
`filedialog.askopenfilename()` öffnet den nativen Dateibrowser des Betriebssystems, gefiltert nach gängigen Bildformaten. Die ausgewählte Datei wird mit `PIL.Image.open()` geladen, in ein `CTkImage`-Objekt umgewandelt, das an den Anzeigebereich angepasst ist, und auf das Label-Widget angewendet, um eine sofortige Vorschau zu ermöglichen.

---

## 🇹🇷 Türkçe

### Genel Bakış
Sade bir masaüstü resim görüntüleme uygulaması. "Select Image" butonuna tıklamak, işletim sisteminin yerel dosya seçme penceresini açar ve seçilen resim anında uygulama penceresinde görüntülenir.

### Özellikler
- Yerel dosya seçme penceresi (PNG, JPG, JPEG, BMP destekleniyor)
- Pencereye sığacak şekilde anında resim önizlemesi
- Sade, modern karanlık temalı arayüz
- Sabit kodlanmış dosya yolu yok — herhangi bir bilgisayarda doğrudan çalışır

### Gereksinimler
- Python 3.10 veya üzeri
- `customtkinter`
- `Pillow`

### Kurulum
```bash
pip install customtkinter pillow
```

### Kullanım
```bash
python image_viewer.py
```

**"Select Image"** butonuna tıkla, sisteminden bir dosya seç, resim butonun üstündeki önizleme alanında görünecek.

### Nasıl çalışır?
`filedialog.askopenfilename()`, yaygın resim formatlarına göre filtrelenmiş, işletim sisteminin yerel dosya tarayıcısını açar. Seçilen dosya `PIL.Image.open()` ile yüklenir, görüntüleme alanına sığacak boyutta bir `CTkImage` nesnesine dönüştürülür ve anında önizleme için etiket (label) bileşenine uygulanır.
