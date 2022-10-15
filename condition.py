def compare_to_five(y):
    if y>5:
        return "Greater"
    elif y<0:
        return "Negative"
    elif y<5:
        return "less"
    else:
        return "equal"
print(compare_to_five(10))
print(compare_to_five(1))
print(compare_to_five(5))
print(compare_to_five(-5))