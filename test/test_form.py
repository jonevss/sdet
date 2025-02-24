from pages.form_page import FormPage


def test_form_submission(driver):
    page = FormPage(driver)
    page.open_page()
    page.fill_form("Misha", "123456", "misha@mail.ru")
    page.submit_form()

    alert_text = page.get_alert_text()
    assert alert_text == "Message received!", f"Ожидалось 'Message received!', но получили '{alert_text}'"

