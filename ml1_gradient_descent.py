def actual_function(x):
    return (x+3)**2
def gradient_function(x):
    return 2*(x+3)

def gradient_descent(start,iterations,gradient_function,learning_rate):
    points=[start]
    old_value=start
    for i in range(iterations):
        new_value=old_value-learning_rate*gradient_function(old_value)
        points.append(new_value)
        old_value=new_value
    return points

x = gradient_descent(20, 100, gradient_function, 0.1)
final_result = actual_function(x[-1])
print(final_result)
