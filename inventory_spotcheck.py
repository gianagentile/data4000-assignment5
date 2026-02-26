from random import seed
import requests


#Part A - Inventory Entry 
#Step 1: Student key 
def get_seed():
    while True:
        try:
            student_key = input("Student key:").strip()
            if not student_key:
                raise ValueError("Student key cannot be empty.")
            seed = sum(ord(char) for char in student_key)
            return seed
        except ValueError as e:
            print("Error:", e)

#Step 2: SKU Entry Loop 
def get_sku():
    while True:
        sku = input("SKU:").strip()
        if sku == "DONE":
            return "DONE"
        if sku == "":
            print("Error: SKU cannot be blank.")
        else:
            return sku
        
#Step 3: On Hand Quanity 
def get_on_hand():
    while True:
        try:
            qty = int(input("On hand:").strip())
            if qty <0:
                raise ValueError
            return qty
        except ValueError:
            print("Error: Quantity must be an integer greater than or equal to 0.")

# Steps 6-9 Api Spot check
def perform_api_spotcheck(seed):
    term = "weezer" if seed % 2 == 0 else "drake"
    url = "https://itunes.apple.com/search"
    params = {"entity": "song", "limit": 5, "term": term}
    song_count = "N/A"
    status = "FAILED"
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        if "results" not in data: 
            status = "INVALID_RESPONSE"
        else:
            song_count = sum(1 for item in data["results"] if item.get("kind") == "song")
            status = "OK"
    except requests.exceptions.RequestException:
        status = "FAILED"
    except (ValueError, KeyError):
        status = "INVALID_RESPONSE"
    return term, song_count, status

#Steps 4-5 Main Function
def main():
    seed = get_seed()
    if seed % 3 == 0:
        threshold = 15
    elif seed % 3 == 1:
        threshold = 12
    else:
        threshold = 9
    total_skus = 0
    reorder_count = 0
    while True:
        sku = get_sku()
        if sku == "DONE":
            break
        on_hand = get_on_hand()
        total_skus += 1
        if on_hand < threshold:
            reorder_count += 1
    term, song_count, api_status = perform_api_spotcheck(seed)


#Step 10: Output Format 
    print(f"Seed: {seed}")
    print(f" Threshold: {threshold}")
    print(f"SKUs entered: {total_skus}")
    print(f"Reorder flagged: {reorder_count}")
    print(f"Spotcheck term: {term}")
    print(f"Songs returned: {song_count}")
    print(f"API status: {api_status}")
if __name__ == "__main__":
    main()
    
    