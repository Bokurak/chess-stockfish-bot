#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Быстрый старт для шахматного бота
"""

from chess_bot import ChessStockfishBot
import time

def quick_demo():
    """Демонстрация работы бота"""
    print("\n" + "="*60)
    print("🚀 ШАХМАТНЫЙ БОТ STOCKFISH - БЫСТРЫЙ СТАРТ")
    print("="*60 + "\n")
    
    print("⏳ Инициализирую бота со Stockfish...")
    bot = ChessStockfishBot(time_limit=2000)
    print("✅ Бот готов!\n")
    
    # Демонстрация 1: Анализ стартовой позиции
    print("📊 ДЕМОНСТРАЦИЯ 1: Анализ стартовой позиции")
    print("-" * 60)
    bot.analyze_position()
    
    print("\n")
    time.sleep(1)
    
    # Демонстрация 2: Лучший ход
    print("📊 ДЕМОНСТРАЦИЯ 2: Лучший ход для белых")
    print("-" * 60)
    best_move = bot.get_best_move(time_ms=2000)
    if best_move:
        print(f"✅ Рекомендуемый ход: {best_move}")
    
    print("\n" + "="*60)
    print("✨ ВСЕ СИСТЕМЫ РАБОТАЮТ!")
    print("="*60)
    print("""
    ✅ Stockfish инициализирован
    ✅ Анализ позиций работает
    ✅ Расчет ходов работает
    
    Теперь можете запустить:
    python chess_bot.py
    """)
    print("="*60 + "\n")


if __name__ == "__main__":
    try:
        quick_demo()
    except KeyboardInterrupt:
        print("\n\n⏹️  Отменено пользователем")
    except Exception as e:
        print(f"\n\n❌ Ошибка: {e}")
        print("\nПопробуйте переустановить зависимости:")
        print("pip install python-chess stockfish selenium")
