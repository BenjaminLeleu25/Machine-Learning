from scipy.special import expit


def linear_combination(x: any, a: any, b: any) -> any:
    """
    Return the linear combination for a given x

    Args:
        x (any): A value to evaluate
        a (any): The slope
        b (any): The intercept
    
    Returns:
        any: The result of the linear combination
    """
    return x * a + b


def sigmoid(x: any) -> any:
    """
    Compute the sigmoid function for a given x using the following equation:

    **f(x) = 1 / (1 + exp(-x))**

    Args:
        x (any): An x to evaluate
    
    Returns:
        any: The result of the sigmoid function
    """
    return expit(x)