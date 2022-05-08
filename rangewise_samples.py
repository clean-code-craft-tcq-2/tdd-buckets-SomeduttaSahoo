import math

parameter = {
  '12-bit-0-to-10': {
    'scalingfactor': 10/4094,
    'offset': 0
  },
  '10-bit-neg-15-to-15':{
    'scalingfactor': 30/1022,
    'offset': -15
  }
}

def infers_readings(readings, sensorType, isSequenceOk, convertReadings, sortReadings, detectRange, convertCSVFormat, printOnConsole):
  validReadings = isSequenceOk(readings)
  if validReadings == True:
    readings = convertReadings(readings, sensorType)
    groups = detectRange(readings, differenceReading, getIndexRange, createRange)
    for list in groups:
      formattedString = convertCSVFormat(list)
      printOnConsole(formattedString)
    return formattedString
  return False

def isSequenceOk(readings):
  if len(readings) <= 0:
    return False
  return True

def convertReadings(readings, sensorType):
  if sensorType is None:
    convertedReadings = sortReadings(readings)
  else:
    convertedReadings = convertReadingsToPhysicalValue(readings,sensorType)
    convertedReadings = roundOffToNearestInteger(convertedReadings)
    convertedReadings = convertToAbsoluteReadings(convertedReadings)
    convertedReadings = sortReadings(convertedReadings)
  return convertedReadings


def sortReadings(readings):
  sortedReadings = sorted(readings)
  return sortedReadings

def convertReadingsToPhysicalValue(readings,sensorType):
  convertedReadings = [(reading * parameter[sensorType]['scalingfactor']) + parameter[sensorType]['offset'] for reading in readings]
  return convertedReadings

def roundOffToNearestInteger(readings):
  roundOffReadings = [math.floor(reading) for reading in readings]
  return roundOffReadings

def convertToAbsoluteReadings(readings):
  absoluteReadings = [abs(reading) for reading in readings]
  return absoluteReadings

def detectRange(readings, differenceReading, getIndexRange, createRange):
  diff = differenceReading(readings)
  ind = getIndexRange(diff)
  groups = createRange(ind, readings)
  return groups

def differenceReading(readings):
  diff = [j-i for i, j in zip(readings[:-1], readings[1:])]
  diff.insert(0, 0)
  return diff

def getIndexRange(diff):
  ind = [i for i,v in enumerate(diff) if v >= 2]
  ind.insert(0, 0)
  return ind

def createRange(ind, readings):
  groups = [readings[i:j] for i,j in zip(ind, ind[1:]+[None])]
  return groups

def convertCSVFormat(list):
  return f'{list[0]}-{list[-1]}, {len(list)}'

def printOnConsole(string):
  print(string)
  return True
