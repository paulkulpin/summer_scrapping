# summer_scrapping

ПМИ 2021 (2 курс).

Был написан телеграм-бот, использующий скрапинг-алгоритмы. Он умеет парсить данные с ютуб-каналов, перечень которых хранится в файле YT.json, по запросу пользователя и выдавать видео за последнюю неделю в формате название-канал-ссылка.

Доп функицонал:
возможность добавления новых каналов в перечень
возможность исключения каналов из перечня

Данный проект был выполнен по личной инициативе и нелюбви автора к бесконечным уведомлениям. Суть проста - отключаем уведомления, не тратим время на поиск видео в огромной ленте, по запросу получаем все теоретически интересные видео.

Были изучены следующие статьи:
*на этом моменте я понял, что давно потерял все ссылки, но точно могу сказать, что кусками читал книгу Ryan Mitchell - Web Scraping with Python*

Используемые библиотеки и прочее:
-bs4
-aiogram
-json
-selenium
-также требуется наличие браузера Google Chrome и драйвера для него, который будет актуальным для данной версии хрома. скачивать отсюда: https://sites.google.com/a/chromium.org/chromedriver/downloads

Бот работает только локально и расчитан на одного пользователя. Расширение функицонала до статуса онлайн-сервиса требует финансовой поддержки проекта.
