import unittest
import json
from power_dispatcher import get_power_dispatch


def compute_power_dispatcher(file_path: str):
    with open(file_path, 'r') as f:
        data = json.load(f)

    return data, get_power_dispatch(data)


data1, power_dispatcher_1 = compute_power_dispatcher(
    './example_payloads/payload1.json')
data2, power_dispatcher_2 = compute_power_dispatcher(
    './example_payloads/payload2.json')
data3, power_dispatcher_3 = compute_power_dispatcher(
    './example_payloads/payload3.json')


class TestPowerDispatcher(unittest.TestCase):

    # TEST SUM
    def test_sum_1(self):
        self.assertEqual(data1['load'], sum([x['p']
                         for x in power_dispatcher_1]))

    def test_sum_2(self):
        self.assertEqual(data2['load'], sum([x['p']
                         for x in power_dispatcher_2]))

    def test_sum_3(self):
        self.assertEqual(data3['load'], sum([x['p']
                         for x in power_dispatcher_3]))

    # TEST FORMAT
    def test_format_1(self):
        self.assertEqual(set([plant['name'] for plant in data1['powerplants']]), set(
            [plant['name'] for plant in power_dispatcher_1]))

    def test_format_2(self):
        self.assertEqual(set([plant['name'] for plant in data2['powerplants']]), set(
            [plant['name'] for plant in power_dispatcher_2]))

    def test_format_3(self):
        self.assertEqual(set([plant['name'] for plant in data3['powerplants']]), set(
            [plant['name'] for plant in power_dispatcher_3]))


if __name__ == '__main__':
    unittest.main()
