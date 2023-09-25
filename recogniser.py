import speech_recognition as sr
import json

def google_recog(audio_file: str, dir_save_to: str): 
    """
    Распознавание русской речи с помощью модели Google. 
    
    Аргументы:
        `audio_file` (str) - путь к файлу в строковом формате (формат файла должен состоять из 3 букв). \n
        `dir_save_to` (str) - папка в которую нужно сохранить результат распознавание.
        
    Функция ничего не возвращает, только выводит результат на экран 
    и сохраняет его в формате `.txt` в указанную папку.
    """
    
    recog = sr.Recognizer() # инициализация распознавателя

    # записываем аудио на распознаватель
    with sr.AudioFile(audio_file) as audio:
        rec = recog.record(audio)

    # распознаем аудио с помощью гугла, указываем русский язык
    result = recog.recognize_google(audio_data=rec, language='ru-RU') 

    print(result)
    
    # сравниваем и сохраняем результат
    filename = audio_file.split('/')[-1][:-4] # выделяем имя файла 
    result_path = f'{dir_save_to}/{filename}_google_text.txt' # путь к файлу
    
    with open(result_path, 'w') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)