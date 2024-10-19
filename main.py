# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import logging
import unittest
from rt_with_exceptions import Runner

#if __name__ == '__main__':



class RunnerTest(unittest.TestCase):
    is_frozen = False

    #@unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        #with open("runner_tests.log", "w") as f:
            logging.basicConfig(level=logging.INFO, filename="runner_tests.log", filemode="a",
                                format='%(asctime)s | %(levelname)s | %(message)s',
                                encoding='utf-8')
        #logging.info(f'Скорость положительная 10001 ')
            try:
                logging.info(f'test_walk: Скорость положительная 02 ')
                Runner("Bob", -5)
                logging.info(f'Скорость положительная 3 ')
                walk_1 = Runner("Bob", -5)
                for i in range(10):
                    walk_1.walk()
                self.assertEqual(walk_1.distance, 50)
            except ValueError as e:
                logging.info(f' RunnerTest:  Скорость не может быть отрицательной{e}')
                print(f"ValueError  RunnerTest {e}")
"""
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        run_1 = Runner("Peter")
        for i in range(10):
            run_1.run()
        self.assertEqual(run_1.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        walk_1 = Runner("Bob")
        run_1 = Runner("Peter")
        for i in range(10):
            walk_1.walk()
            run_1.run()
        self.assertNotEqual(run_1.distance, walk_1.distance)

"""

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    logging.info(f'Скорость положительная Hi 001 ')

print_hi("name******************")
        # Press the green button in the gutter to run the script.




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
