# Домашнее задание по теме "Систематизация и пропуск тестов".
# Цель: понять на практике как объединять тесты при помощи TestSuite. Научиться пропускать тесты при помощи встроенных в unittest декораторов.
#
# Задача "Заморозка кейсов":
import unittest
import tests_12_2

tourTS = unittest.TestSuite()
tourTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner()
