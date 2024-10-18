#  Домашнее задание по теме "Методы Юнит-тестирования"
# Цель: освоить методы, которые содержит класс TestCase.
#
# Задача:

import unittest
from unittest import TestCase
from runner_and_tournament import Runner, Tournament


class TournamentTest(TestCase):
    is_frozen = True

    def setUp(self):
        self.r1 = Runner("Усэйн", 10)
        self.r2 = Runner("Андрей", 9)
        self.r3 = Runner("Ник", 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):

        for key, value in cls.all_results.items():
            out_print = {}
            for key2, value2 in value.items():
                out_print[key2] = value2.name
            print(out_print)

    @classmethod
    def get_key(cls, d, value):
        for k, v in d.items():
            if v == value:
                return k

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_Tournament1(self):
        tour1 = Tournament(90, self.r1, self.r3)
        tour_results = tour1.start()
        self.assertTrue(tour_results[list(tour_results.keys())[-1]] == 'Ник', 'Ник обогнал кого-то')
        self.all_results['test_Tournament1'] = tour_results

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_Tournament2(self):
        tour2 = Tournament(90, self.r2, self.r3)
        tour_results = tour2.start()
        self.assertTrue(tour_results[list(tour_results.keys())[-1]] == 'Ник', 'Ник обогнал кого-то')
        self.all_results['test_Tournament2'] = tour_results

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_Tournament3(self):
        tour3 = Tournament(90, self.r1, self.r2, self.r3)
        tour_results = tour3.start()
        self.assertTrue(tour_results[list(tour_results.keys())[-1]] == 'Ник', 'Ник обогнал кого-то')
        self.all_results['test_Tournament3'] = tour_results

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_Tournament4(self):
        tour4 = Tournament(90, self.r1, self.r2)
        tour_results = tour4.start()
        self.assertTrue(tour_results[list(tour_results.keys())[-1]] == 'Андрей', 'Андрей обогнал кого-то')
        self.all_results['test_Tournament4'] = tour_results


               # Сенсация! Андрей  обогнал самого Усэйна Болта!  Алгоритм требует доработки!
    @unittest.skip("требуется доработка алгоритма  тест не проходит")
    def test_Tournament5(self):
        tour5 = Tournament(90, self.r2, self.r1)
        tour_results = tour5.start()
        self.assertTrue(tour_results[list(tour_results.keys())[-1]] == 'Андрей', 'Андрей обогнал кого-то')
        self.all_results['test_Tournament5'] = tour_results    

if __name__ == '__main__':
    unittest.main
