def bmi(weight, height):
    bmi = round(float(weight) / float(height) ** 2, 2)
    return bmi


def imp(pounds, feet, inches):
    def convert_weight(pounds):
        kgs = round(float(pounds * 0.453592), 2)
        return kgs

    new_weight = convert_weight(pounds)

    def convert_height(feet, inches):
        meters = round(float(feet) * 0.3048 + float(inches) * 0.0254, 2)
        return meters

    new_height = convert_height(feet, inches)

    bmi = round(float(new_weight) / float(new_height) ** 2, 2)
    return bmi

