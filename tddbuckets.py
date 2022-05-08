class driven_range:
    
    def getRangeListInfo(self):
        cumulativeFrequency = 0
        rangeInfoList = []
        listCurrentPosition = 0
        while (cumulativeFrequency != len(self.inputData)):
            rangeOpenerElement = self.inputData[listCurrentPosition]
            rangeCloserPosition = self.getRangeCloserPosition(listCurrentPosition)
            frequency = rangeCloserPosition - listCurrentPosition + 1
            rangeCloserElement = self.inputData[rangeCloserPosition]
            rangeInfoList.append((rangeOpenerElement, rangeCloserElement, frequency))
            listCurrentPosition = rangeCloserPosition + 1
            cumulativeFrequency+=frequency
        return rangeInfoList

    def getRangeCloserPosition(self, listBeginPosition):
        rangeCloserPosition = listBeginPosition
        for i in range(listBeginPosition+1, len(self.inputData)):
            differenceInValues = (self.inputData[i]-self.inputData[rangeCloserPosition])
            if((self.inputData[i]-self.inputData[rangeCloserPosition]) == 1):
                rangeCloserPosition = i
        return rangeCloserPosition

    def generateResult(self):
        rangeInfoList = self.getRangeListInfo()
        rangeResult = {}
        for rangeInfo in rangeInfoList:
            rangeData = f'{rangeInfo[0]}-{rangeInfo[1]}'
            freqData = f'{rangeInfo[2]}'
            rangeResult.update({rangeData: freqData})
            self.printOnConsole(f'{rangeData}, {freqData}')
        return rangeResult

    def printOnConsole(self, rangeResult):
        print(rangeResult)  
    
    def main(self, inputData):
        inputData.sort()
        self.inputData = inputData.copy()
        return self.generateResult()
    
    def convertADCReadingToAmpereSensor(self, digitalValueRange, ADC_Sensor_Type):
        analogValueRange=[]
        maxDigitalValue, scale, offset = self.sensorParameters(ADC_Sensor_Type)
        for digitalValue in digitalValueRange:
            if (0<=digitalValue and digitalValue<=maxDigitalValue):
                analogValue = abs(round((scale*digitalValue/maxDigitalValue)-offset))
                analogValueRange.append(analogValue)
        return analogValueRange
    
    def sensorParameters(self, ADC_Sensor_Type):
    ADC_Sensor_Type_dict={ 
                            '12Bits':{'maxDigitalValue' : 4094, 'scale' : 10 , 'offset' : 0}, 
                          '10Bits':{'maxDigitalValue' : 1023, 'scale' : 30, 'offset' : 15}
                         }
    return ADC_Sensor_Type_dict[ADC_Sensor_Type]['maxDigitalValue'],ADC_Sensor_Type_dict[ADC_Sensor_Type]['scale'],ADC_Sensor_Type_dict[ADC_Sensor_Type]['offset']
