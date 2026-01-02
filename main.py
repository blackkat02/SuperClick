from playwright.sync_api import sync_playwright
import time


def run_scenario(target_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print(f"[СТАРТ] Перехід за адресою: {target_url}")
        page.goto(target_url)

        page.wait_for_selector("#btn-count1", timeout=10000)
        print("[УСПІХ] Сторінка завантажена, кнопки знайдені.")

        print("[ДІЯ] Набиваю Число 1...")
        for _ in range(21):
            page.click("#btn-count1")

        print("[ДІЯ] Набиваю Число 2...")
        for _ in range(13):
            page.click("#btn-count2")

        print("[ДІЯ] Розрахунок суми...")
        page.click("#btn-sum")

        result_text = page.inner_text("#val-sum")

        if result_text == "34":
            print(f"--- ТЕСТ ПРОЙДЕНО: Сума {result_text} вірна! ---")
        else:
            print(f"--- ТЕСТ ПРОВАЛЕНО: Очікували 34, отримали {result_text} ---")

        time.sleep(12)
        browser.close()


if __name__ == "__main__":
    run_scenario("https://chess-b.vercel.app/sandbox")
