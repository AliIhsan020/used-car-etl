import pandas as pd
import glob
import time
from datetime import datetime
import os

log_file = 'log_file.txt'
target_file = 'processed_data.csv'
source_dir = 'data_source'

def log(message, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] [{level}] - {message}\n")

def extract_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        log(f"CSV read success: {file_path} ({len(data)} rows)")
        return data
    except Exception as e:
        log(f"Error reading CSV {file_path}: {e}", "ERROR")
        return None

def extract_json(file_path):
    try:
        data = pd.read_json(file_path, lines=True)
        log(f"JSON read success: {file_path} ({len(data)} rows)")
        return data
    except Exception as e:
        log(f"Error reading JSON {file_path}: {e}", "ERROR")
        return None

def extract_xml(file_path):
    try:
        data = pd.read_xml(file_path)
        log(f"XML read success: {file_path} ({len(data)} rows)")
        return data
    except Exception as e:
        log(f"Error reading XML {file_path}: {e}", "ERROR")
        return None

def extract():
    all_data_frames = []
    log("Extraction process started.")

    file_types = {
        "*.csv": extract_csv,
        "*.json": extract_json,
        "*.xml": extract_xml
    }

    for pattern, extract_func in file_types.items():
        path_pattern = os.path.join(source_dir, pattern)
        files = glob.glob(path_pattern)
        log(f"Found {len(files)} files for pattern {pattern}")

        for file in files:
            if os.path.basename(file) == target_file:
                continue
            data = extract_func(file)
            if data is not None and not data.empty:
                all_data_frames.append(data)

    if all_data_frames:
        combined_data = pd.concat(all_data_frames, ignore_index=True)
        log(f"Extraction completed. Total rows: {len(combined_data)}")
        return combined_data
    else:
        log("No data found to extract!", "WARNING")
        return pd.DataFrame()

def transform_data(data):
    if data.empty:
        return data
    try:
        log("Transformation started.")
        float_cols = data.select_dtypes(include=['float64', 'float32']).columns
        data[float_cols] = data[float_cols].round(2)
        log(f"Transformation completed. Rounded columns: {list(float_cols)}")
        return data
    except Exception as e:
        log(f"Transformation failed: {e}", "ERROR")
        return None

def load(data):
    try:
        log(f"Loading data into {target_file}")
        data.to_csv(target_file, index=False)
        log("Load phase completed successfully.")
    except Exception as e:
        log(f"Loading failed: {e}", "ERROR")

def etl_pipeline():
    start_time = time.time()
    log("=== ETL JOB INITIALIZED ===")
    extracted_data = extract()
    if not extracted_data.empty:
        transformed_data = transform_data(extracted_data)
        if transformed_data is not None:
            load(transformed_data)
            log("ETL Job Finished Successfully.")
        else:
            log("ETL Job failed during transformation.", "ERROR")
    else:
        log("ETL Job aborted: No data extracted.", "WARNING")
    end_time = time.time()
    duration = round(end_time - start_time, 2)
    log(f"=== Total Execution Time: {duration} seconds ===\n")

if __name__ == "__main__":
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)
    etl_pipeline()