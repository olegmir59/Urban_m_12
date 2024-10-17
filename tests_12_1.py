# Домашнее задание по теме "Простые Юнит-Тесты"
# Цель: приобрести навык создания простейших Юнит-тестов
#
# Задача "Проверка на выносливость":

import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walk_1 = runner.Runner("Bob")
        for i in range(10):
            walk_1.walk()
        self.assertEqual(walk_1.distance, 50)

    def test_run(self):
        run_1 = runner.Runner("Peter")
        for i in range(10):
            run_1.run()
        self.assertEqual(run_1.distance, 100)

    def test_challenge(self):
        walk_1 = runner.Runner("Bob")
        run_1 = runner.Runner("Peter")
        for i in range(10):
            walk_1.walk()
            run_1.run()
        self.assertNotEqual(run_1.distance, walk_1.distance)


if __name__ == '__main__':
    unittest.main