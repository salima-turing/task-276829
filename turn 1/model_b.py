import unittest
import random
from typing import List

# Simulated streaming source function
def simulate_streaming_source(num_samples: int) -> List[int]:
    return [random.randint(0, 100) for _ in range(num_samples)]

# Data processing function
def process_streaming_data(streaming_data: List[int]) -> List[int]:
    return [value for value in streaming_data if isinstance(value, int) and value >= 1]

class TestDataQuality(unittest.TestCase):
    def test_consistency_and_integrity(self):
        # Simulate streaming data and process it
        num_samples = 1000
        streaming_data = simulate_streaming_source(num_samples)
        processed_data = process_streaming_data(streaming_data)

        # Perform validation checks
        self.assertEqual(len(processed_data), num_samples, "Expected all data to be processed.")
        for value in processed_data:
            self.assertIsInstance(value, int, "Expected integer values only.")
            self.assertGreaterEqual(value, 1, "Expected minimum value of 1.")

if __name__ == '__main__':
    unittest.main()
