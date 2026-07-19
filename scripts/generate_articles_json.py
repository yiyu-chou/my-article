import os
import re
import json
from datetime import datetime

# ==========================================
# 參數配置
# ==========================================
# 依據使用者需求：文章都存放在 list 資料夾
TARGET_DIR = "list" 
# 輸出的 JSON 索引檔案放置在 api 資料夾中
OUTPUT_FILE = "api/articles.json"

# 要排除的 Markdown 檔案名稱（不列入文章索引）
EXCLUDE_FILES = ["README.md", "LICENSE.md"]

def parse_yaml_front_matter(file_path):
    """
    解析 Markdown 頂端的 YAML Front Matter
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"無法讀取檔案 {file_path}: {e}")
        return None

    # 使用正規表達式匹配最上方的 --- ... ---
    match = re.match(r"^---\r?\n([\s\S]*?)\r?\n---\r?\n", content)
    if not match:
        return None

    yaml_block = match.group(1)
    metadata = {}
    
    # 逐行解析 YAML 鍵值對
    for line in yaml_block.split("\n"):
        line = line.strip()
        if not line or ":" not in line:
            continue
        
        key, *val_parts = line.split(":")
        key = key.strip()
        val = ":".join(val_parts).strip()
        
        # 清除前後包裹的引號
        val = val.strip("'\"")
        
        # 特殊處理 tags 陣列 (例如: [ESP32, 物聯網])
        if key == "tags":
            val = val.replace("[", "").replace("]", "")
            metadata[key] = [t.strip("'\" ") for t in val.split(",") if t.strip()]
        else:
            metadata[key] = val

    return metadata

def main():
    print(f"開始掃描 {TARGET_DIR} 資料夾下的 Markdown 檔案...")
    articles_list = []
    
    # 設定掃描路徑為 ./list
    scan_path = os.path.join(".", TARGET_DIR)
    
    if not os.path.exists(scan_path):
        print(f"⚠️ 找不到指定的來源資料夾：{scan_path}，請確認資料夾是否建立。")
        return

    # 遍歷目錄下的所有檔案
    for root, dirs, files in os.walk(scan_path):
        for file in files:
            if file.endswith(".md") and file not in EXCLUDE_FILES:
                file_path = os.path.join(root, file)
                # 正規化路徑，方便前端網頁讀取
                normalized_path = file_path.replace("\\", "/").lstrip("./")
                
                print(f"  正在解析: {normalized_path}")
                metadata = parse_yaml_front_matter(file_path)
                
                if metadata:
                    # 自動補上該文章的檔案路徑，供前端讀取
                    metadata["filepath"] = normalized_path
                    # 如果 yaml 裡沒有 title_main，則用檔名作為備用 title
                    if "title_main" not in metadata and "title" in metadata:
                        metadata["title_main"] = metadata["title"]
                    elif "title_main" not in metadata:
                        metadata["title_main"] = os.path.splitext(file)[0]
                    
                    articles_list.append(metadata)
                else:
                    print(f"   ⚠️ 檔案 {normalized_path} 缺少 YAML Front Matter，已跳過。")

    # 依據日期 (date) 欄位由新到舊排序
    def get_sort_date(item):
        date_str = item.get("date", "1970.01.01")
        date_str = date_str.replace(".", "-")
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            try:
                return datetime.strptime(date_str, "%Y-%m")
            except ValueError:
                return datetime.min

    articles_list.sort(key=get_sort_date, reverse=True)

    # 【防錯機制】確保輸出目標的 api 資料夾存在，若不存在則自動創建
    output_dir = os.path.dirname(OUTPUT_FILE)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        print(f"已自動建立目標輸出資料夾：{output_dir}")

    # 寫入目標 JSON 檔案
    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(articles_list, f, ensure_ascii=False, indent=2)
        print(f"成功生成索引檔：{OUTPUT_FILE} (共 {len(articles_list)} 篇文章)")
    except Exception as e:
        print(f"寫入 JSON 發生錯誤: {e}")

if __name__ == "__main__":
    main()