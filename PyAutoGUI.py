import pyautogui
import keyboard
import time
import random

# Налаштування
MIN_DELAY = 0.05  # Мінімальна пауза (50 мс)
MAX_DELAY = 0.25  # Максимальна пауза (250 мс)

print("Наведи мишу на кнопку.")
print("Натисни 'S' для СТАРТУ, 'Q' для ВИХОДУ.")

keyboard.wait("s")
print("Запущено!")

try:
    while True:

        if keyboard.is_pressed("q"):
            print("Зупинено користувачем.")
            break

        # Додай це перед pyautogui.click(), щоб імітувати тремтіння руки
        x, y = pyautogui.position()
        pyautogui.click(x + random.randint(-1, 1), y + random.randint(-1, 1))

        # pyautogui.click()

        # ГЕНЕРУЄМО РАНДОМНУ ПАУЗУ
        # Це робить твій клікер схожим на людський натиск
        wait_time = random.uniform(MIN_DELAY, MAX_DELAY)
        time.sleep(wait_time)

except Exception as e:
    print(f"Помилка: {e}")
