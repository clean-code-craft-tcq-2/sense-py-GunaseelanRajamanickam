import math

class EmailAlert:
  def __init__(self):
    self.emailSent = False

class LEDAlert:
  def __init__(self):
    self.ledGlows = False

class StatsAlerter:
  def __init__(self,maxThreshold,alerts):
    self.maxThreshold = maxThreshold
    self.alerts = alerts

  def checkAndAlert(self,lists):
        calculatedStats = calculateStats(lists)

        if(calculatedStats["max"] > self.maxThreshold):
          self.alerts[0].emailSent = True
          self.alerts[1].ledGlows = True
       

def calculateStats(numbers):
  if not numbers:
    computedStats={"min": math.nan, "max": math.nan, "avg": math.nan}
    return computedStats
  #Initialize empty dictionary
  computedStats = {}

  #Calculate minimum of numbers
  computedStats["min"] = min(numbers)

  #Calculate maximum of numbers
  computedStats["max"] = max(numbers)

  #Calculate average of numbers
  computedStats["avg"] = sum(numbers)/len(numbers)

  return computedStats
