#!/bin/bash
# Скрипт для установки бота на Android через Termux

echo "================================"
echo "🤖 УСТАНОВКА CHESS-STOCKFISH БОТ"
echo "================================"
echo ""

# Обновляем систему
echo "📦 Обновляю пакеты..."
pkg update -y
pkg upgrade -y

# Устанавливаем Python
echo "🐍 Устанавливаю Python..."
pkg install python -y

# Устанавливаем Stockfish
echo "♟️ Устанавливаю Stockfish..."
pkg install stockfish -y

# Устанавливаем необходимые зависимости
echo "📚 Устанавливаю Python зависимости..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "================================"
echo "✅ УСТАНОВКА ЗАВЕРШЕНА!"
echo "================================"
echo ""
echo "📝 Команды для запуска:"
echo "  cd chess-stockfish-bot"
echo "  python chess_bot.py"
echo ""
