#Tests
import unittest
from cont_mem_algos import best_fit

class TestBasicBestFit(unittest.TestCase):

    def test_pass_empty_map(self): 
        work_memory = []
        req = 0
        index = 0
        search = best_fit(work_memory, req, index)
        self.assertEqual(search, None)

    def test_req_highest(self):
        work_memory = [(0x00A00000, 0x000C0000)]
        req = 0x000D0000
        index = 0
        search = best_fit(work_memory, req, index)
        self.assertEqual(search, None)

    def test_req_highest_list(self):       
        work_memory =  [(0x00A00000, 0x000C0000), (0x00B00000, 0x000C0000), (0x00C00000, 0x000C0000)]
        req = 0x000D0000
        index = 0
        search = best_fit(work_memory, req, index)
        self.assertEqual(search, None)

    # FALLA
    def test_req_choose_last_index(self):
        work_memory = [(0x00A00000, 0x000C0000), (0x00B00000, 0x000C0000), (0x00C00000, 0x000D0000)]
        req = 0x000D0000
        index = 0
        search = best_fit(work_memory, req, index)
        self.assertEqual(search[3], 0)

    def test_req_choose_last_len(self):
        work_memory = [(0x00A00000, 0x000C0000), (0x00B00000, 0x000C0000), (0x00C00000, 0x000D0000)]
        req = 0x000D0000
        index = 0
        len_work_memory = len(work_memory)
        search = best_fit(work_memory, req, index)
        self.assertEqual(len(search[0]), len_work_memory - 1)

    def test_req_choose_middle_index(self):
        work_memory = [(0x00A00000, 0x000C0000), (0x000B0000, 0x000D0000), (0x00C00000, 0x000C0000)]
        req = 0x000D0000
        index = len(work_memory) - 1
        search = best_fit(work_memory, req, index)
        self.assertEqual(search[3], 1)

    def test_req_choose_middle_len(self):
        work_memory = [(0x00A00000, 0x000C0000), (0x000B0000, 0x000D0000), (0x00C00000, 0x000C0000)]
        req = 0x000D0000 
        index = len(work_memory) - 1
        len_work_memory = len(work_memory)
        search = best_fit(work_memory, req, index)
        self.assertEqual(len(search[0]), len_work_memory - 1)

    def test_req_choose_last_index_keep(self):
        work_memory = [(0x00A00000, 0x000C0000), (0x00B00000, 0x000C0000), (0x00C00000, 0x000E0000)]
        req = 0x000D0000
        index = 0
        search = best_fit(work_memory, req, index)
        self.assertEqual(search[3], 2)

    def test_req_choose_last_len_keep(self):
        work_memory = [(0x00A00000, 0x000C0000), (0x00B00000, 0x000C0000), (0x00C00000, 0x000E0000)]
        req = 0x000D0000
        index = 0
        len_work_memory = len(work_memory)
        search = best_fit(work_memory, req, index)
        self.assertEqual(len(search[0]), len_work_memory)

    def test_req_choose_best_fit_len(self):
        work_memory = [(0x00A00000, 0x000D0A0), (0x00B00000, 0x000D000A), (0x00C00000, 0x000D0000)]
        req = 0x000D0000
        index = 0
        len_work_memory = len(work_memory)
        search = best_fit(work_memory, req, index)
        self.assertEqual(len(search[0]), len_work_memory - 1)

    # FALLA
    def test_req_choose_best_fit_index(self):
        work_memory = [(0x00A00000, 0x000D0A0), (0x00B00000, 0x000D000A), (0x00C00000, 0x000D0000)]
        req = 0x000D0000
        index = 0
        search = best_fit(work_memory, req, index)
        self.assertEqual(search[3], 0)
        
if __name__ == '__main__':
    unittest.main()

