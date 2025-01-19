from gtts import gTTS
from playsound import playsound
import os


def text_to_speech(text, lang='ru'):
    """
    Преобразует текст в аудио и воспроизводит его.

    :param text: Текст для синтеза речи.
    :param lang: Код языка (по умолчанию 'ru' для русского).
    """
    try:
        # Создаём объект gTTS
        tts = gTTS(text=text, lang=lang)

        # Временное имя файла
        filename = "output2.mp3"

        # Сохраняем аудио в файл
        tts.save(filename)
        print("Аудиофайл сохранён как 'output2.mp3'")

        # Воспроизводим аудиофайл
        playsound(filename)

        # Удаляем файл после воспроизведения (опционально)
        os.remove(filename)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    user_text = input("Введите текст для озвучивания: ")
    if user_text.strip() == "":
        print("Пустой текст не может быть озвучен.")
    else:
        text_to_speech(user_text)