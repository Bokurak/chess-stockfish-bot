#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Шахматный бот с Stockfish для Chess.com
Автоматически играет с максимальным уровнем сложности
"""

import time
import chess
from stockfish import Stockfish
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ChessStockfishBot:
    def __init__(self, elo=3200, time_limit=2000):
        """
        Инициализация бота
        :param elo: Уровень Stockfish (3200 = максимум)
        :param time_limit: Время на ход в миллисекундах
        """
        self.elo = elo
        self.time_limit = time_limit
        self.board = chess.Board()
        
        # Инициализация Stockfish
        try:
            self.stockfish = Stockfish(
                path="/data/data/com.termux/files/usr/bin/stockfish",
                elo=elo,
                depth=20
            )
            logger.info(f"✅ Stockfish инициализирован (ELO: {elo})")
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации Stockfish: {e}")
            raise

    def get_board_position(self, fen=None):
        """Установить позицию доски"""
        if fen:
            self.board = chess.Board(fen)
        logger.info(f"📍 Позиция: {self.board.fen()}")
        return self.board.fen()

    def get_best_move(self, depth=20, time_ms=None):
        """
        Получить лучший ход от Stockfish
        :param depth: Глубина анализа
        :param time_ms: Время на расчет в мс
        :return: Лучший ход
        """
        if time_ms is None:
            time_ms = self.time_limit

        try:
            self.stockfish.set_fen_position(self.board.fen())
            best_move = self.stockfish.get_best_move_time(time_ms)
            
            if best_move:
                logger.info(f"🎯 Лучший ход: {best_move} (время: {time_ms}ms)")
                
                evaluation = self.stockfish.get_evaluation()
                if evaluation and evaluation.get('value', 0) > 300:
                    logger.info("⭐ БЛЕСТЯЩИЙ ХОД! Evaluation: " + str(evaluation))
                elif evaluation and evaluation.get('value', 0) > 150:
                    logger.info("✨ ЗАМЕЧАТЕЛЬНЫЙ ХОД! Evaluation: " + str(evaluation))
                
                return best_move
            else:
                logger.warning("⚠️ Ход не найден")
                return None
        except Exception as e:
            logger.error(f"❌ Ошибка расчета хода: {e}")
            return None

    def analyze_position(self, fen=None):
        """
        Анализировать текущую позицию
        :param fen: FEN позиция (если None, используется текущая)
        """
        if fen:
            self.stockfish.set_fen_position(fen)
        else:
            self.stockfish.set_fen_position(self.board.fen())
        
        evaluation = self.stockfish.get_evaluation()
        best_moves = self.stockfish.get_top_moves(5)
        
        logger.info(f"\n📊 АНАЛИЗ ПОЗИЦИИ:")
        logger.info(f"Evaluation: {evaluation}")
        logger.info(f"Топ 5 ходов:")
        for i, move in enumerate(best_moves, 1):
            logger.info(f"  {i}. {move}")


def main():
    """Главная функция"""
    print("\n" + "="*60)
    print("♟️  ШАХМАТНЫЙ БОТ STOCKFISH ♟️")
    print("="*60)
    print()
    
    bot = ChessStockfishBot(elo=3200, time_limit=2000)
    
    print("Выберите действие:")
    print("1. Анализировать стартовую позицию")
    print("2. Получить лучший ход для белых")
    print("3. Анализировать позицию (введите FEN)")
    print("4. Выход")
    
    choice = input("\nВаш выбор (1-4): ").strip()
    
    if choice == "1":
        print("\n🔍 Анализирую стартовую позицию...")
        bot.analyze_position()
    
    elif choice == "2":
        print("\n🎯 Рассчитываю лучший ход для белых...")
        move = bot.get_best_move(time_ms=2000)
        if move:
            print(f"\n✅ Рекомендуемый ход: {move}")
    
    elif choice == "3":
        fen = input("\nВведите FEN позицию: ").strip()
        if fen:
            bot.board = chess.Board(fen)
            bot.analyze_position(fen)
        else:
            print("❌ FEN не введен")
    
    elif choice == "4":
        print("\n👋 До встречи!")
    
    else:
        print("❌ Неверный выбор!")


if __name__ == "__main__":
    main()
