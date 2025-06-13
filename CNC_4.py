# Program Title: Simple List & Dictionary Operations (Beginner Version)

def merge_lists(list1, list2):
    return list1 + list2

def filter_even_numbers(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return even

def square_numbers(numbers):
    squared = []
    for num in numbers:
        squared.append(num ** 2)
    return squared

def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = value
    return merged

def filter_dict_by_value(d, threshold=2):
    result = {}
    for key, value in d.items():
        if value > threshold:
            result[key] = value
    return result

def double_dict_values(d):
    result = {}
    for key, value in d.items():
        result[key] = value * 2
    return result

def main():
    print("\n=== List & Dictionary Operations ===")
    print("1. Merge Lists")
    print("2. Filter Even Numbers from List")
    print("3. Square Numbers in List")
    print("4. Merge Dictionaries")
    print("5. Filter Dictionary by Value (>2)")
    print("6. Double Dictionary Values")
    print("7. Exit")

    while True:
        choice = input("\nEnter your choice (1-7): ")

        if choice == '1':
            list1 = list(map(int, input("Enter first list (space-separated): ").split()))
            list2 = list(map(int, input("Enter second list (space-separated): ").split()))
            print("Merged List:", merge_lists(list1, list2))

        elif choice == '2':
            numbers = list(map(int, input("Enter numbers (space-separated): ").split()))
            print("Even Numbers:", filter_even_numbers(numbers))

        elif choice == '3':
            numbers = list(map(int, input("Enter numbers (space-separated): ").split()))
            print("Squared Numbers:", square_numbers(numbers))

        elif choice == '4':
            dict1 = eval(input("Enter first dictionary (e.g., {'a':1, 'b':2}): "))
            dict2 = eval(input("Enter second dictionary (e.g., {'c':3, 'd':4}): "))
            print("Merged Dictionary:", merge_dicts(dict1, dict2))

        elif choice == '5':
            d = eval(input("Enter dictionary (e.g., {'a':1, 'b':3}): "))
            print("Filtered Dictionary:", filter_dict_by_value(d))

        elif choice == '6':
            d = eval(input("Enter dictionary (e.g., {'x':2, 'y':3}): "))
            print("Doubled Values Dictionary:", double_dict_values(d))

        elif choice == '7':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
