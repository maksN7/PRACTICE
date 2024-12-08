import sqlite3

# Підключення до бази даних (створюється, якщо її немає)
conn = sqlite3.connect('goals.db')
cursor = conn.cursor()


def show_goals():
    """Показує всі цілі з їх статусом."""
    cursor.execute("SELECT id, goal, status FROM goals")
    goals = cursor.fetchall()
    if goals:
        print("\nВаші цілі:")
        for goal in goals:
            print(f"{goal[0]}. {goal[1]} - {goal[2]}")
    else:
        print("\nУ вас немає встановлених цілей.")


def add_goal():
    """Додає нову ціль."""
    goal = input("Введіть нову ціль: ")
    cursor.execute("INSERT INTO goals (goal) VALUES (?)", (goal,))
    conn.commit()
    print("Ціль додано!")


def mark_goal_as_completed():
    """Позначає ціль як виконану."""
    goal_id = input("Введіть ID цілі, яку хочете відзначити як виконану: ")
    cursor.execute("UPDATE goals SET status = 'completed' WHERE id = ?", (goal_id,))
    conn.commit()
    print("Ціль відзначено як виконану!")


def delete_goal():
    """Видаляє ціль."""
    goal_id = input("Введіть ID цілі, яку хочете видалити: ")
    cursor.execute("DELETE FROM goals WHERE id = ?", (goal_id,))
    conn.commit()
    print("Ціль видалено!")


def main():
    while True:
        print("\nМеню:")
        print("1. Показати всі цілі")
        print("2. Додати нову ціль")
        print("3. Позначити ціль як виконану")
        print("4. Видалити ціль")
        print("5. Вихід")

        choice = input("Оберіть дію (1-5): ")

        if choice == '1':
            show_goals()
        elif choice == '2':
            add_goal()
        elif choice == '3':
            mark_goal_as_completed()
        elif choice == '4':
            delete_goal()
        elif choice == '5':
            print("До побачення!")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
    conn.close()