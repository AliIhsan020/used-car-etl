# 🚗 Used Car Prices — ETL Pipeline

A lightweight ETL (Extract, Transform, Load) pipeline that consolidates used car price data from multiple file formats (CSV, JSON, XML) into a single clean dataset.

---

## 📁 Project Structure

```
used-car-etl/
├── etl_code.py            # Main ETL pipeline script
├── processed_data.csv     # Output: cleaned & combined data
├── log_file.txt           # Runtime logs
└── data_source/           # Input data files
    ├── used_car_prices1.csv
    ├── used_car_prices2.csv
    ├── used_car_prices3.csv
    ├── used_car_prices1.json
    ├── used_car_prices2.json
    ├── used_car_prices3.json
    ├── used_car_prices1.xml
    ├── used_car_prices2.xml
    └── used_car_prices3.xml
```

---

## ⚙️ How It Works

The pipeline runs in three stages:

### 1. Extract
- Scans the `data_source/` directory for `.csv`, `.json`, and `.xml` files
- Reads each file using `pandas` and appends to a combined DataFrame
- Logs the number of rows extracted from each file

### 2. Transform
- Rounds all float columns to 2 decimal places
- Currently transforms the `price` column

### 3. Load
- Writes the final DataFrame to `processed_data.csv`

---

## 📊 Dataset Columns

| Column              | Type    | Description                      |
|---------------------|---------|----------------------------------|
| `car_model`         | string  | Name of the car model            |
| `year_of_manufacture` | int   | Year the car was manufactured    |
| `price`             | float   | Price in local currency units    |
| `fuel`              | string  | Fuel type (Petrol, Diesel, CNG)  |

---

## 🚀 Getting Started

### Requirements

- Python 3.7+
- pandas

### Installation

```bash
pip install pandas
```

### Run the Pipeline

```bash
python etl_code.py
```

The script will:
1. Create the `data_source/` folder if it doesn't exist
2. Process all supported files inside it
3. Save output to `processed_data.csv`
4. Append logs to `log_file.txt`

---

## 📋 Sample Log Output

```
[2026-04-22 16:14:21] [INFO] - === ETL JOB INITIALIZED ===
[2026-04-22 16:14:21] [INFO] - Found 3 files for pattern *.csv
[2026-04-22 16:14:21] [INFO] - CSV read success: data_source\used_car_prices1.csv (10 rows)
...
[2026-04-22 16:14:21] [INFO] - Extraction completed. Total rows: 90
[2026-04-22 16:14:21] [INFO] - Transformation completed. Rounded columns: ['price']
[2026-04-22 16:14:21] [INFO] - Load phase completed successfully.
[2026-04-22 16:14:21] [INFO] - === Total Execution Time: 0.03 seconds ===
```

---

## 🔧 Extending the Pipeline

You can easily extend the pipeline by:

- **Adding new file types**: Implement a new `extract_*` function and add the pattern to the `file_types` dict in `extract()`
- **Adding transformations**: Edit the `transform_data()` function to include cleaning, filtering, or enrichment steps
- **Changing the output**: Modify `load()` to write to a database, API, or different file format

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🇹🇷 Türkçe Özet

Bu proje, ikinci el araç fiyat verilerini birden fazla dosya formatından (CSV, JSON, XML) okuyup tek bir temiz veri setine dönüştüren hafif bir ETL pipeline'ıdır.

**Nasıl Çalışır?**
- **Extract (Çıkarma):** `data_source/` klasöründeki tüm desteklenen dosyalar okunur ve birleştirilir.
- **Transform (Dönüştürme):** Sayısal sütunlar 2 ondalık basamağa yuvarlanır.
- **Load (Yükleme):** İşlenmiş veri `processed_data.csv` dosyasına kaydedilir.

**Veri Seti:** Her biri 10 satırdan oluşan 9 kaynak dosyadan toplam 90 satır araç verisi işlenmektedir. Veriler; araç modeli, üretim yılı, fiyat ve yakıt türü bilgilerini içermektedir.

**Gereksinimler:** Python 3.7+ ve pandas kütüphanesi yeterlidir. Çalıştırmak için `python etl_code.py` komutu kullanılır.
