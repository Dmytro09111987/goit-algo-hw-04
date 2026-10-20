from pathlib import Path


def get_cats_info(path):
 
    cats_base = []

    try:
        file_path = Path(path)

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                cat_id, name, age = line.split(",")
            
                cat_dict = {
                    "id": cat_id.strip(),
                    "name": name.strip(),
                    "age": age.strip(),
                }
                cats_base.append(cat_dict)
            return cats_base

    except FileNotFoundError:
        print(f"Error: File <<Clinic_database_cat.txt>> not found in the system")
        return []

current_dir = Path(__file__).parent
file_path = current_dir / "Clinic_database_cat.txt"

cats_info = get_cats_info(file_path)

for cat in cats_info:
    print(f"id: {cat['id']}, name: {cat['name']}, age: {cat['age']}")
