# 📱 ПОЛНАЯ ИНСТРУКЦИЯ УСТАНОВКИ НА ANDROID

## ШАГ 1: УСТАНОВКА TERMUX

1. Откройте **F-Droid** (https://f-droid.org/)
2. Поищите **"Termux"**
3. Нажмите **"Установить"**
4. Откройте **Termux** (должно появиться чёрное окно)

## ШАГ 2: УСТАНОВКА В TERMUX

Копируйте **по одной команде** и нажимайте **Enter**:

```bash
pkg update && pkg upgrade -y
```

```bash
pkg install python stockfish git -y
```

```bash
git clone https://github.com/Bokurak/chess-stockfish-bot.git
```

```bash
cd chess-stockfish-bot
```

```bash
pip install -r requirements.txt
```

## ШАГ 3: ТЕСТИРОВАНИЕ

```bash
python quick_start.py
```

Если видите зелёные галочки ✅ - всё работает!

## ШАГ 4: ЗАПУСК БОТА

```bash
python chess_bot.py
```

Выберите опцию **2** (Лучший ход для белых).

Если видите ход (например: **e2e4**) - **БОТ РАБОТАЕТ!** 🎉

## КОМАНДЫ

```bash
# Запуск основного бота
python chess_bot.py

# Быстрая демонстрация
python quick_start.py

# Переход в папку проекта
cd chess-stockfish-bot

# Список файлов
ls -la
```

## ⚠️ ЕСЛИ ЧТО-ТО НЕ РАБОТАЕТ

**Ошибка: "Модуль не найден"**
```bash
pip install python-chess stockfish
```

**Ошибка: "Stockfish не найден"**
```bash
pkg install stockfish -y
```

**Проверить установку:**
```bash
stockfish --version
```

**Проверить Python:**
```bash
python --version
```

## 🎯 ГОТОВО!

Теперь бот полностью готов к работе! 🚀
