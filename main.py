import database as db


def show_menu():
    print("\n=== Task Manager ===")
    print("1. Vazifa qo'shish")
    print("2. Vazifalarni ko'rish")
    print("3. Vazifani bajarilgan deb belgilash")
    print("4. Vazifani o'chirish")
    print("5. Chiqish")


def main():
    db.init_db()
    while True:
        show_menu()
        choice = input("Tanlang: ").strip()

        if choice == "1":
            title = input("Vazifa nomi: ").strip()
            if title:
                db.add_task(title)
                print("Qo'shildi.")
            else:
                print("Nom bo'sh bo'lmasligi kerak.")

        elif choice == "2":
            tasks = db.get_tasks()
            if not tasks:
                print("Vazifalar yo'q.")
            for task_id, title, is_done in tasks:
                mark = "[x]" if is_done else "[ ]"
                print(f"{task_id}. {mark} {title}")

        elif choice == "3":
            task_id = input("Vazifa raqami: ").strip()
            if task_id.isdigit():
                db.mark_done(int(task_id))
                print("Bajarildi deb belgilandi.")
            else:
                print("Raqam kiriting.")

        elif choice == "4":
            task_id = input("Vazifa raqami: ").strip()
            if task_id.isdigit():
                db.delete_task(int(task_id))
                print("O'chirildi.")
            else:
                print("Raqam kiriting.")

        elif choice == "5":
            print("Xayr!")
            break

        else:
            print("Noto'g'ri tanlov.")


if __name__ == "__main__":
    main()