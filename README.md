# Python Project-2
Тема проекта: реализация приложения, которое поможет найти оптимальное распределение сотрудников по дням и сменам, с учетом их пожеланий. 
Проект написан на языке программирования Python с использованием PyQt6 (библиотека python для разработки графического интерфейса).

Для пользователей представлен интуитивно-понятный интерфейс программы:
на первой вкладке "Количество" вводятся необходимые входные данные;
![2023-01-12_12-58-01](https://user-images.githubusercontent.com/70623604/212036500-62c9bd39-c9e6-4950-b5ff-82ad9ca66799.png)

у некоторых кнопок есть подсказки;
![image](https://user-images.githubusercontent.com/70623604/212036401-b05180d4-c67a-4a2b-983c-500a556a3a9b.png)

на вкладке "Список" вводятся ФИО сотрудников, их рейтинг и их пожелания на смены;
![image](https://user-images.githubusercontent.com/70623604/212037073-d08dfa9e-400b-40d8-a90b-59caa5201a43.png)

эти данные программа считывает и передает в основную функцию для составления оптимального расписания;
![image](https://user-images.githubusercontent.com/70623604/212037264-f6be0daf-a647-4d03-b1b2-0675884e866c.png)

после нажатия на кнопку "Далее" происходит переход на вкладку "Результат", где в виде таблицы отображен результат, который при необходимости можно сохранить в exel файл
- цветом выделены утвержденные смены
- первый знак +\- означает утвердили смену или нет
- второй знак +\- означает был ли запрос на эту смену
![image](https://user-images.githubusercontent.com/70623604/212039088-f2274dfa-57c2-4889-ac8f-6e099fe0e979.png)

рейтинг сотрудников влияет на распределение смен: чем выше рейтинг, тем больше смен будут соответствовать запросам.
Например, в 2 день в 1 смену не было запросов на смену, но так как там было необходимо 2 сотрудника, программа назначила на эту смену сотрудников с меньшим рейтингом.
![image](https://user-images.githubusercontent.com/70623604/212040235-0b21b72b-a1f0-472c-9d1e-0613c753d3fa.png)

Файлы представленные в репозитории: 
- main.py - соединение всех файлов (назначение функций для элементов интерфейса)
- main_function.py - преобразованный файл assignment_problem.py в одну основную функцию, принимающую данные которые вводит пользователь и возвращающуюсоставленное расписание
- interface.py - интерфейс приложения  

Разделение обязанностей: Байгубекова Регина — реализация интерфейса, Александрова Юля — реализация основной функции.

