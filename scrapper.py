import requests
import json
import os

def image_search(supercategory, category, offset=0, idx=1, downloaded_timestamps=set()):
    max_items = 10000
    url = f"https://arquivo.pt/imagesearch?q={category}&maxItems=200&offset={offset}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
    except requests.exceptions.RequestException as e:
        print("Error occurred while searching:", e)
        return
    
    if response.status_code == 200:
        print("\n-> " + supercategory + " -> " + category)
        print("#########################")
        print("### Search successful ###")
        print("#########################")
        data = response.json()
        if "responseItems" in data:
            response_items = data["responseItems"]
            for item in response_items:
                img_link = item.get("imgLinkToArchive")
                page_timestamp = item.get("imgTstamp")
                if img_link and page_timestamp:
                    if page_timestamp in downloaded_timestamps:
                        print(f"Skipping image with timestamp {page_timestamp} (already downloaded).")
                        continue
                    download_image(img_link, supercategory, category, page_timestamp, f"{idx}.png")
                    downloaded_timestamps.add(page_timestamp)
                    if idx >= max_items:
                        print("\nReached maximum index (" + str(max_items) + ").")
                        return  # Exit the function to stop further processing
                    idx += 1
                
        else:
            print("No search results found.")
        
        # Check if there are more pages available
        if "nextPage" in data and idx <= max_items:  # Only continue if idx is less than max_items
            next_offset = offset + 200
            image_search(supercategory, category, next_offset, idx, downloaded_timestamps)
    else:
        print(f"Error occurred while searching. Status code: {response.status_code}")

def download_image(url, supercategory, category, page_timestamp, filename):
    folder_path = os.path.join(supercategory, category)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    filepath = os.path.join(folder_path, f"{supercategory}_{category}_{page_timestamp}_{filename}")
    try:
        with open(filepath, 'wb') as f:
            response = requests.get(url)
            response.raise_for_status()
            f.write(response.content)
            print(f"Downloaded {filepath}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {filepath}: {e}")
    except IOError as e:
        print(f"Error occurred while writing {filepath}: {e}")

def main():
    try:
        category_dict = {
            "veículos": ["carro", "mota", "motociclo", "barco", "camião", "autocarro"],
            "pessoas": ["homem", "mulher", "criança", "bebé"],
            "animais": ["cão", "gato", "pássaro", "peixe", "vaca", "ovelha"],
            "mobílias": ["cama", "armário", "mesa", "cadeira", "sofá"],
            "eletrónica": ["telemóvel", "televisão", "TV", "máquina de lavar", "frigorífico", "forno"],
            "comida": ["fruta", "verdura", "carne ", "peixe", "sobremesa"],
            "natureza": ["árvore", "flor", "planta", "relva", "arbusto"],
            "ferragens": ["martelo", "serra", "chave de fendas", "chave de caixa", "parafuso"],
            "edifícios": ["casa", "castelo", "hotel", "apartamento"]
        }
        
        for supercategory, categories in category_dict.items():
            for category in categories:
                image_search(supercategory, category)
    except KeyboardInterrupt:
        print("\n\nProcess interrupted by the user.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
