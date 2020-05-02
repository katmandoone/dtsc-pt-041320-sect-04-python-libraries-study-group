"""An example library for converting temperatures."""


def convert_f_to_c(temperature_f):
    """Convert Fahrenheit to Celsius."""
    temperature_c = (temperature_f - 32) * (5/9)
    return temperature_c




def convert_c_to_f(c):
    """Convert Celsius to Fahrenheit."""
    return c * (9/5) + 32


## CREATE THE ADDITIONAL FUNCTIONS BELOW


# convert_c_to_k
def convert_c_to_k(c):
    return c + 273.15


# convert_f_to_k
def convert_f_to_k(f):
    return convert_c_to_k(convert_f_to_c(f))


# convert_k_to_c
def convert_k_to_c(k):
    return k - 273.15


# convert_k_to_f
def convert_k_to_f(k):
    return convert_c_to_f(convert_k_to_c(k))


## LEVEL UP

# convert_f_to_all
def convert_f_to_all(f):
    print(f'C: {round(convert_f_to_c(f),2)} \nK: {round(convert_f_to_k(f),2)}')
    return None