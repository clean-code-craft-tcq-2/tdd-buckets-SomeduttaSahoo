import unittest
import chargeRangeReadings

class chargeRangeReadingsTest(unittest.TestCase):
  
  def test(self):
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([], chargeRangeReadings.ADC_12Bit) == "")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([0], chargeRangeReadings.ADC_12Bit) == "0-0, 1\n")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([4094], chargeRangeReadings.ADC_12Bit) == "10-10, 1\n")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([4094,4095], chargeRangeReadings.ADC_12Bit) == "10-10, 1\n")#ignore error readings
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([0,4000], chargeRangeReadings.ADC_12Bit) == "0-0, 1\n10-10, 1\n")
    
    
    
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([], chargeRangeReadings.ADC_10Bit) == "")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([0], chargeRangeReadings.ADC_10Bit) == "15-15, 1\n")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([511], chargeRangeReadings.ADC_10Bit) == "0-0, 1\n")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([1022], chargeRangeReadings.ADC_10Bit) == "15-15, 1\n")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([1022,1023], chargeRangeReadings.ADC_10Bit) == "15-15, 1\n")#ignore error readings
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([0,100,150,300,500,70,1500,700,600,2000,1022], chargeRangeReadings.ADC_10Bit) == "0-0, 1\n3-3, 1\n6-6, 2\n11-13, 3\n15-15, 2\n")

    
unittest.main()
