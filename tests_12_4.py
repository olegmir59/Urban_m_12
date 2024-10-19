#  Домашнее задание по теме "Логирование"
# Цель: получить опыт использования простейшего логирования совместно с тестами.
#
# Задача "Логирование бегунов":

import logging
import unittest
from rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filename="runner_tests.log", filemode="w",
                    format='%(asctime)s | %(levelname)s | %(message)s',
                    encoding='utf-8')
class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            walk_1 = Runner("Bob", -5)
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                walk_1.walk()
            self.assertEqual(walk_1.distance, 50)
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")
            logging.warning(f' !!! ValueError: {e}', exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            run_1 = Runner(123)
            logging.info('"test_run" выполнен успешно')
            for i in range(10):
                run_1.run()
            self.assertEqual(run_1.distance, 100)
        except TypeError as ex:
            logging.warning("Неверный тип данных для объекта Runner")
            logging.warning(f' !!! TypeError: {ex}', exc_info=True)



    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        walk_1 = Runner("Bob")
        run_1 = Runner("Peter")
        for i in range(10):
            walk_1.walk()
            run_1.run()
        self.assertNotEqual(run_1.distance, walk_1.distance)


if __name__ == '__main__':
    unittest.main()

