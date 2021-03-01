import logging

logger = logging.getLogger(__name__)


"""Addition of two number
  input parameter : (float) a , (float) b
   return value: sum of both the number"""

def addition(a, b):
    try:
        print(a+b)
        return a + b;
    except NameError:
        logger.error("Error due to non-numeric number passed")
        raise

"""Subtraction of two number
  input parameter : (float) a , (float) b
   return value: Difference of both the number"""

def subtraction(a, b):
    try:
        print(a-b)
        return a - b;
    except NameError:
        logger.error("Error due to non-numeric number passed")
        raise

"""Multiplication of two number
  input parameter : (float) a , (float) b
   return value: Multiplication of both the number"""

def multiplication(a, b):
    try:
        print(a*b)
        return a * b;
    except NameError:
        logger.error("Error due to non-numeric number passed")
        raise

"""Divide one number by other number
  input parameter : (float) a , (float) b
   return value: Divident of both the number"""

def divide(a, b):
    try:
        print(a/b)
        return a / b;
    except NameError:
        logger.error("Error due to non-numeric number passed")
        raise
    except ZeroDivisionError:
        logger.error("Error due to non-numeric number passed")
        raise




