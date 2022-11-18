TEMPERATURE_SCALES = ('fahrenhite','kelvin')

def convert_to_celsius(degrees,source='fahrenhite'):
    '''convert celsius from fahtenhite or kelvin'''
    if source.lower() == 'fahrenhite':
        return (degrees-32)* (5/9)
    elif source.lower() == 'kelvin':
        return degrees - 273.15
    else:
        return f"Don't know how to convert from {source}"