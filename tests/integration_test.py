import cast_upgrade_1_5_9 #@UnusedImport
import unittest

from cast.application.test import run


class Test(unittest.TestCase):
    
    def test1(self):
         
        run('b810_sql_local', 'app2')

    
if __name__ == "__main__":
    unittest.main()
