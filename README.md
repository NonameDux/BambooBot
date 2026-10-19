# 🎋 Bamboo Growth Telegram Bot

*(🇷🇺 Русская версия ниже / Russian version below)*

A fun, interactive Telegram bot created to grow your virtual bamboo, compete with friends, and claim random bonuses! 

**Why was this created?**  
The main idea was to build a clean, fun game bot exclusively for friends. We got tired of using third-party bots that are heavily overloaded with annoying ads and spam. This bot is 100% ad-free and community-focused.

## 🛠 Tech Stack
- **Language:** Python 3.x
- **Framework:** [aiogram 3.x](https://docs.aiogram.dev/) (Asynchronous framework for Telegram Bot API)
- **Database:** Custom database module (using `database.py` and `settings.py`)
- **Async:** `asyncio`

## 🚧 Status: Work In Progress (WIP)
This project is currently under active development. 
**Planned features:**
- Multi-chat support (currently, it is optimized for a single chat).
- Moving configuration variables to `.env` files.
- Expanded achievements and boss fights (e.g., feeding the Panda).

## ⚙️ Installation & Setup
At this stage of development, some variables need to be entered manually into the code.

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bamboo-bot.git
   cd bamboo-bot
   ```
2. Install dependencies:
   ```bash
   pip install aiogram
   ```
3. **Manual Configuration:**
   Open `bot.py` (or `bot_2.py`) and manually insert your credentials:
   - Paste your Bot Token (from [@BotFather](https://t.me/BotFather)) into the `TOKEN` variable:
     ```python
     TOKEN = "YOUR_BOT_TOKEN_HERE"
     ```
   - Update the `CHAT_ID` variable in the `wait_for_sync_end` function with your target group's ID:
     ```python
     CHAT_ID = -100XXXXXXXXXX
     ```
4. Run the bot:
   ```bash
   python bot.py
   ```

---

# 🎋 Телеграм-бот "Вырасти бамбук"

Веселый интерактивный Telegram-бот для выращивания виртуального бамбука, соревнований с друзьями и сбора случайных бонусов!

**Идея создания**  
Основная цель проекта — сделать чистого и веселого игрового бота исключительно для друзей. Чужие боты сильно надоели обилием навязчивой рекламы, спама и платных подписок. Этот бот на 100% свободен от рекламы.

## 🛠 Стек технологий
- **Язык:** Python 3.x
- **Фреймворк:** [aiogram 3.x](https://docs.aiogram.dev/) (Асинхронная библиотека для Telegram API)
- **База данных:** Кастомный модуль БД (`database.py` и `settings.py`)
- **Асинхронность:** `asyncio`

## 🚧 Статус: В разработке
Проект находится на стадии активной доработки. 
**В планах:**
- Мультичатовость (сейчас бот настроен на работу преимущественно в одном чате).
- Вынос настроек и токенов в `.env` файлы.
- Расширение списка достижений и добавление мировых боссов (например, "накорми Панду").

## ⚙️ Установка и запуск
На данном этапе разработки для запуска требуется ручное вмешательство в код.

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/bamboo-bot.git
   cd bamboo-bot
   ```
2. Установите зависимости:
   ```bash
   pip install aiogram
   ```
3. **Ручная настройка кода:**
   Откройте файл `bot.py` (или `bot_2.py`) и вручную впишите свои данные:
   - Вставьте токен вашего бота (полученный у [@BotFather](https://t.me/BotFather)) в переменную `TOKEN`:
     ```python
     TOKEN = "ВАШ_ТОКЕН_ЗДЕСЬ"
     ```
   - Укажите ID вашего чата в переменной `CHAT_ID` внутри функции `wait_for_sync_end`:
     ```python
     CHAT_ID = -100XXXXXXXXXX
     ```
4. Запустите бота:
   ```bash
   python bot.py
   ```
