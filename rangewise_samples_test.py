import unittest
import rangewise_samples
import io
import sys

class RangewiseTest(unittest.TestCase):
  def test_infers_readings_as_per_range(self):
    self.assertTrue(rangewise_samples.infers_readings([4,5], None, rangewise_samples.isSequenceOk, rangewise_samples.convertReadings, rangewise_samples.sortReadings, rangewise_samples.detectRange, rangewise_samples.convertCSVFormat, rangewise_samples.printOnConsole) == "4-5, 2")
    self.assertTrue(rangewise_samples.infers_readings([3, 3, 5, 4, 10, 11, 12], None, rangewise_samples.isSequenceOk, rangewise_samples.convertReadings, rangewise_samples.sortReadings, rangewise_samples.detectRange, rangewise_samples.convertCSVFormat, rangewise_samples.printOnConsole) == "10-12, 3")
    self.assertTrue(rangewise_samples.infers_readings([3], None, rangewise_samples.isSequenceOk, rangewise_samples.convertReadings, rangewise_samples.sortReadings, rangewise_samples.detectRange, rangewise_samples.convertCSVFormat, rangewise_samples.printOnConsole) == "3-3, 1")
    self.assertTrue(rangewise_samples.infers_readings([1229, 1229, 2047, 1638, 4094, 3685, 4094], "12-bit-0-to-10", rangewise_samples.isSequenceOk, rangewise_samples.convertReadings, rangewise_samples.sortReadings, rangewise_samples.detectRange, rangewise_samples.convertCSVFormat, rangewise_samples.printOnConsole) == "9-10, 3")
    self.assertTrue(rangewise_samples.infers_readings([613, 410, 682, 375, 852, 886, 103], "10-bit-neg-15-to-15", rangewise_samples.isSequenceOk, rangewise_samples.convertReadings, rangewise_samples.sortReadings, rangewise_samples.detectRange, rangewise_samples.convertCSVFormat, rangewise_samples.printOnConsole) == "10-12, 3")
    self.assertTrue(rangewise_samples.infers_readings([], None, rangewise_samples.isSequenceOk, rangewise_samples.convertReadings, rangewise_samples.sortReadings, rangewise_samples.detectRange, rangewise_samples.convertCSVFormat, rangewise_samples.printOnConsole) == False)
  
  def test_isSequenceOk(self):
    self.assertTrue(rangewise_samples.isSequenceOk([]) == False)

  def test_detectRange(self):
    self.assertTrue(rangewise_samples.detectRange([3, 3, 4, 5, 10, 11, 12], rangewise_samples.differenceReading, rangewise_samples.getIndexRange, rangewise_samples.createRange) == [[3,3,4,5],[10,11,12]])
  
  def test_convertCSVFormat(self):
    self.assertTrue(rangewise_samples.convertCSVFormat([3,3,4,5]) == "3-5, 4")

  def test_printOnConsole(self):
    self.assertTrue(rangewise_samples.printOnConsole('All is fine!') == True)

if __name__ == '__main__': # pragma: no cover
  unittest.main()
