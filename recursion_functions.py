def get_max_number_from_list(num_list, max_element=None, current=0):
    if max_element is None:
        max_element = num_list[current]
    if num_list[current] > max_element:
        max_element = num_list[current]
    current += 1
    if current < len(num_list):
        max_element = get_max_number_from_list(num_list, max_element, current)
    return max_element


def get_range_list(a, b, abst_list: list):
    if a <= b:
        abst_list.append(a)
        abst_list = get_range_list(a + 1, b, abst_list)
    return abst_list


def fibonacci_number(count, current=2, current_result=1, pre_result=1):
    if count > current:
        current_result = fibonacci_number(count, current + 1, current_result + pre_result, current_result)
    return current_result


def fibonacci(n):
    if n in [1, 2]:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
