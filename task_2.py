from pymongo import MongoClient
from pymongo import errors
from bson.objectid import ObjectId

# Підключення до бази даних MongoDB Atlas
client = MongoClient("mongodb+srv://goitlearn:<password>@cluster0.miwzpqi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['cats']  # Назва бази даних
collection = db['cats_collection']  # Назва колекції

# Create (створення запису)
def get_by_id(id: ObjectId) -> dict | None:
    try:
        return collection.find_one({"_id": id})
    except errors.PyMongoError as e:
        return f"Помилка при отриманні кота за ID {id}: {e}"

def create_cat():
    try:
        name = input("Введіть імʼя кота для створення: ").strip()
        age = int(input("Введіть вік кота: "))
        features_input = input("Введіть особливості кота, розділені комою: ")
        features = [
            feature.strip() for feature in features_input.split(",") if feature.strip()
        ]

        data = {"name": name, "age": age, "features": features}

        result_one = collection.insert_one(data)
        return get_by_id(result_one.inserted_id)
    except errors.PyMongoError as e:
        return f"Помилка при створенні кота: {e}"

# Read (читання)
def read_all_cats():
    cats = collection.find()
    for cat in cats:
        print(cat)

# Виводимо інформацію про кота за його ім'ям 
def read_cat():
    try:
        name = input("Введіть ім'я кота: ")
        result = None
        result = collection.find_one({"name": name})
        if result:
            print(result)
        else:
            print("Кіт за таким ім'ям не знайдений")
    except PyMongoError as e:
        print(f"Помилка при роботі за базою даних: {e}")
    except ValueError as e:
        print(f"Помилка вводеня даних: {e}")

# Update (оновлення)
def update_cat_age():
    """
    Оновлює вік кота за його ім'ям.
    """
    name = input("Введіть ім'я кота: ")
    new_age = int(input("Введіть новий вік кота: "))
    collection.update_one({"name": name}, {"$set": {"age": new_age}})
    print("Вік кота оновлено.")

def add_features_by_name():
    """
    Додає нову характеристику до списку features кота за ім'ям.
    """
    name = input("Введіть ім'я кота: ")
    new_feature = input("Введіть нову характеристику кота: ")
    collection.update_one({"name": name}, {"$push": {"features": new_feature}})
    return "Нову характеристику додано."

# Delete (видалення)
def delete_cat_by_name():
    """
    Видаляє запис про кота за його ім'ям.
    """
    name = input("Введіть ім'я кота: ")
    result = collection.delete_one({"name": name})
    if result.deleted_count == 1:
        return "Запис про кота видалено."
    else:
        return "Кіт з таким ім'ям не знайдено."

def delete_all():
    """
    Видаляє всі записи з колекції.
    """
    result = collection.delete_many({})
    return f"Всі записи про котів видалено. Кількість видалених записів: {result.deleted_count}"


def exit_program():
    print("Вихід з програми...")
    exit()

def main_menu():
    print("\nВиберіть опцію або 0. Вихід (exit):")
    print("1. Створити запис про кота (create_cat)")
    print("2. Отримати список всіх котів (read_all_cats)")
    print("3. Отримати кота за ім'ям (read_cat)")
    print("4. Оновити вік кота (update_cat_age)")
    print("5. Додати характеристику коту (add_features_by_name)")
    print("6. Видалити кота за імʼям (delete_cat_by_name)")
    print("8. Видалити всіх котів (delete_all)")

    while True:

        choice = input("Ваш вибір: ")

        if choice == "0":
            exit_program()
        elif choice == "1":
            print(create_cat())
        elif choice == "2":
            print(read_all_cats())
        elif choice == "3":
            print(read_cat())
        elif choice == "4":
            print(update_cat_age())
        elif choice == "5":
            print(add_features_by_name())
        elif choice == "6":
            print(delete_cat_by_name())
        elif choice == "8":
            print(delete_all())

print (main_menu())