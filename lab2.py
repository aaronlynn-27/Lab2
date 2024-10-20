
def main():
    display_main_menu()

    input_values = get_user_input()

    sorted_values = sort_temp(input_values)

    average_temperature = calc_average(sorted_values)
    print(f"The average temperature is: {average_temperature:.2f}")

    min_max_value = find_min_max(sorted_values)
    print(f"The minimum and maximum temperatue: {min_max_value}")

    median_temp = cal_median(sorted_values)
    print(f"The median temperature: {median_temp:.2f}")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    input_number = input()
    number_split = input_number.split(",")
    number = [float(value) for value in number_split]
    return number

def sort_temp(temperatures):
    temperatures.sort()
    return temperatures

def calc_average(temperatures):
    sum_of_temperatures = sum(temperatures)
    count = len(temperatures)
    average_temp = sum_of_temperatures / count
    return average_temp

def find_min_max(temperatures):
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    return [min_temp, max_temp]

def cal_median(temperatures):
    total_number = len(temperatures)
    mid_index = total_number // 2


    if total_number % 2 == 1:
        return temperatures[mid_index]
    else:
        return (temperatures[mid_index - 1] + temperatures[mid_index])/2

if __name__ == "__main__":
    main()