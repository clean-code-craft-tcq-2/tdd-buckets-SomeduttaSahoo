ADC_12Bit = {"max_permissible_value" : 4094 , "intercept" : 0 , "max_current_range" : 10}
ADC_10Bit = {"max_permissible_value" : 511 , "intercept" : 511 , "max_current_range" : 15}


def map_adc_values_to_amps(A2Dvalues, ADC_dict):
    result=[]
    for value in A2Dvalues:
        value -= ADC_dict["intercept"]
        if value<=ADC_dict["max_permissible_value"] :
            result.append(abs(round(((value)/ADC_dict["max_permissible_value"])*ADC_dict["max_current_range"])))
    return result


def getSortedListofUniqueItems(listOfItems):
    setofList = set(listOfItems)
    sortedList = list(setofList)
    sortedList.sort()
    return sortedList
    
    
def get_ListOfContinousRanges(charge_readings):
    listOfItems = getSortedListofUniqueItems(charge_readings)
    listOfRange=[]
    if len(listOfItems) == 0:
        return []
    rangeDict = { "min":listOfItems[0],"max":listOfItems[0],"freq":0}
    for item in listOfItems:
        if(item <= (rangeDict["max"]+1)):
            rangeDict["max"] = item  
        else:
            listOfRange.append(rangeDict.copy())
            rangeDict["min"] = item
            rangeDict["max"] = item
    listOfRange.append(rangeDict.copy()) # store the last items
    return listOfRange
    
    
def updateFrequencyOfReading(reading,listOfRange):
    for rangeItem in listOfRange:
        if(reading <= rangeItem["max"]):
            rangeItem["freq"]=rangeItem["freq"]+1
            return listOfRange
    return listOfRange
    
    
def updateFreqOfRange(listOfRange,charge_readings):
    for item in charge_readings:
        listOfRange = updateFrequencyOfReading(item,listOfRange)
    return listOfRange        
    
    
def output_to_console(listOfRange):    
    result = ""
    for item in listOfRange:
        result += (f"{item['min']}-{item['max']}, {item['freq']}\n")
    return result
    

def getFreqOfChargeRanges(InputList, ADC_dict):
    charge_readings = map_adc_values_to_amps(InputList,ADC_dict)
    listOfRange = get_ListOfContinousRanges(charge_readings)
    listOfRange = updateFreqOfRange(listOfRange,charge_readings)
    responseText = output_to_console(listOfRange)
    return responseText
