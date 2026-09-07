#!/usr/bin/env python3
"""Быстрый тест бота"""

from chess_bot import ChessStockfishBot
import time

print("\n" + "="*60)
print("🚀 ТЕСТ ШАХМАТНОГО БОТА")
print("="*60 + "\n")

print("⏳ Инициализирую Stockfish...")
bot = ChessStockfishBot(time_limit=2000)
print("✅ Готово!\n")

print("📊 Анализирую стартовую позицию...")
bot.analyze_position()

print("\n🎯 Получаю лучший ход...")
move = bot.get_best_move(time_ms=2000)

print("\n" + "="*60)
print("✅ ВСЕ СИСТЕМЫ РАБОТАЮТ!")
print("="*60 + "\n")
