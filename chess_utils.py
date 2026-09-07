#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Утилиты для работы с шахматным ботом
Включает вспомогательные функции и инструменты
"""

import chess
import chess.pgn
import chess.engine
from datetime import datetime
import json
from pathlib import Path


class GameAnalyzer:
    """Анализатор сыгранных партий"""
    
    def __init__(self, pgn_file=None):
        """Инициализация анализатора"""
        self.pgn_file = pgn_file
        self.games = []
    
    def load_game(self, pgn_path):
        """Загрузить игру из PGN файла"""
        try:
            with open(pgn_path, 'r', encoding='utf-8') as f:
                game = chess.pgn.read_game(f)
            if game:
                self.games.append(game)
                return True
            return False
        except Exception as e:
            print(f"❌ Ошибка загрузки: {e}")
            return False
    
    def analyze_game(self, game=None):
        """Анализировать партию"""
        if game is None and self.games:
            game = self.games[0]
        
        if not game:
            print("❌ Нет игры для анализа")
            return
        
        print("\n" + "="*60)
        print("📊 АНАЛИЗ ПАРТИИ")
        print("="*60)
        
        # Базовая информация
        headers = game.headers
        print(f"\n📋 Информация:")
        print(f"   Белые: {headers.get('White', 'Unknown')}")
        print(f"   Черные: {headers.get('Black', 'Unknown')}")
        print(f"   Результат: {headers.get('Result', 'Unknown')}")
        print(f"   Дата: {headers.get('Date', 'Unknown')}")
        print(f"   Событие: {headers.get('Event', 'Unknown')}")
        
        # Количество ходов
        move_count = 0
        for move in game.mainline_moves():
            move_count += 1
        
        print(f"   Ходов: {move_count}")
        print(f"   Ходов белых: {(move_count + 1) // 2}")
        print(f"   Ходов черных: {move_count // 2}")
        
        print("\n" + "="*60 + "\n")


class MoveValidator:
    """Валидатор шахматных ходов"""
    
    @staticmethod
    def is_valid_uci(move_uci, fen=None):
        """Проверить валидность UCI хода"""
        try:
            board = chess.Board(fen) if fen else chess.Board()
            move = chess.Move.from_uci(move_uci)
            return move in board.legal_moves
        except:
            return False
    
    @staticmethod
    def is_valid_san(move_san, fen=None):
        """Проверить валидность алгебраической нотации"""
        try:
            board = chess.Board(fen) if fen else chess.Board()
            move = board.parse_san(move_san)
            return move in board.legal_moves
        except:
            return False


class PositionEvaluator:
    """Оценка позиций"""
    
    @staticmethod
    def evaluate_position(fen, stockfish_obj):
        """Оценить позицию"""
        try:
            stockfish_obj.set_fen_position(fen)
            evaluation = stockfish_obj.get_evaluation()
            return evaluation
        except Exception as e:
            print(f"❌ Ошибка оценки: {e}")
            return None
    
    @staticmethod
    def is_brilliant_move(evaluation, threshold=300):
        """Является ли ход блестящим"""
        if evaluation and evaluation.get('value', 0) > threshold:
            return True
        return False
    
    @staticmethod
    def is_wonderful_move(evaluation, threshold_min=150, threshold_max=300):
        """Является ли ход замечательным"""
        if evaluation:
            value = evaluation.get('value', 0)
            if threshold_min < value <= threshold_max:
                return True
        return False


class GameRecorder:
    """Запись игр в различные форматы"""
    
    @staticmethod
    def save_as_pgn(game, filename):
        """Сохранить игру в PGN"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(str(game))
            print(f"✅ Игра сохранена в {filename}")
            return True
        except Exception as e:
            print(f"❌ Ошибка сохранения: {e}")
            return False
    
    @staticmethod
    def save_as_json(game_data, filename):
        """Сохранить данные в JSON"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(game_data, f, indent=2, ensure_ascii=False)
            print(f"✅ Данные сохранены в {filename}")
            return True
        except Exception as e:
            print(f"❌ Ошибка сохранения: {e}")
            return False


class OpeningBook:
    """Работа с дебютной библиотекой"""
    
    def __init__(self):
        self.book_path = Path("openings.json")
        self.openings = self._load_openings()
    
    def _load_openings(self):
        """Загрузить дебютную библиотеку"""
        if self.book_path.exists():
            try:
                with open(self.book_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def get_opening_name(self, fen):
        """Получить название дебюта по FEN"""
        # Упрощенная версия - в реальной версии нужна полная БД дебютов
        if fen in self.openings:
            return self.openings[fen]
        return None
    
    def is_in_opening(self, board):
        """Находимся ли мы в фазе дебюта"""
        return len(list(board.move_stack)) < 16  # Примерно до 8 ходов каждого


class StatisticsTracker:
    """Отслеживание статистики"""
    
    def __init__(self, stats_file="stats.json"):
        self.stats_file = stats_file
        self.stats = self._load_stats()
    
    def _load_stats(self):
        """Загрузить статистику"""
        if Path(self.stats_file).exists():
            try:
                with open(self.stats_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return self._default_stats()
        return self._default_stats()
    
    def _default_stats(self):
        """Статистика по умолчанию"""
        return {
            "total_games": 0,
            "wins": 0,
            "losses": 0,
            "draws": 0,
            "total_moves": 0,
            "brilliant_moves": 0,
            "wonderful_moves": 0,
            "average_elo": 3200,
            "games_by_time_control": {}
        }
    
    def update_game_result(self, result, moves_count, brilliant=0, wonderful=0):
        """Обновить результат игры"""
        self.stats["total_games"] += 1
        self.stats["total_moves"] += moves_count
        self.stats["brilliant_moves"] += brilliant
        self.stats["wonderful_moves"] += wonderful
        
        if result == "1-0":
            self.stats["wins"] += 1
        elif result == "0-1":
            self.stats["losses"] += 1
        else:
            self.stats["draws"] += 1
        
        self.save()
    
    def save(self):
        """Сохранить статистику"""
        try:
            with open(self.stats_file, 'w', encoding='utf-8') as f:
                json.dump(self.stats, f, indent=2)
            print("✅ Статистика обновлена")
        except Exception as e:
            print(f"❌ Ошибка сохранения: {e}")
    
    def get_stats(self):
        """Получить статистику"""
        return self.stats
    
    def get_win_rate(self):
        """Процент побед"""
        total = self.stats["total_games"]
        if total == 0:
            return 0
        return (self.stats["wins"] / total) * 100


def print_board(board):
    """Красиво вывести доску"""
    print("\n")
    print(board)
    print("\nFEN:", board.fen())
    print("Ходов сделано:", len(list(board.move_stack)))
    print()


# Пример использования
if __name__ == "__main__":
    print("🛠️ Утилиты для шахматного бота\n")
    
    # Валидатор
    print("1️⃣ Валидация ходов:")
    print(f"   e2e4 валидный? {MoveValidator.is_valid_uci('e2e4')}")
    print(f"   z9z9 валидный? {MoveValidator.is_valid_uci('z9z9')}")
    
    # Трекер статистики
    print("\n2️⃣ Статистика:")
    tracker = StatisticsTracker()
    print(f"   Всего игр: {tracker.stats['total_games']}")
    print(f"   Побед: {tracker.stats['wins']}")
    print(f"   Процент побед: {tracker.get_win_rate():.1f}%")
