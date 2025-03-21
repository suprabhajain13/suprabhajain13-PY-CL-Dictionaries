from lab import *


def main():
    # Create dictionary from user input
    keys = input("Enter keys separated by spaces: ").split(',')
    values = input("Enter values separated by spaces: ").split(',')
    user_dict = create_dict_from_lists(keys, values)
    print()
    print("Dictionary created from user inputs:", user_dict)



    # Get items in dictionary
    print()
    print("Items in default dictionary:", get_items(user_dict))

    # Get keys in dictionary
    print()
    print("Keys in default dictionary:", get_keys(user_dict))

    # Get values in dictionary
    print()
    print("Values in default dictionary:", get_values(user_dict))

    # Get value for a key
    print()
    key = input("Enter a key to get its value: ")
    value = get_value(user_dict, key)
    print("Value for key '{}' in default dictionary: {}".format(key, value))

    # Remove a key from dictionary
    print()
    key_to_remove = input("Enter a key to remove from default dictionary: ")
    removed_value = remove_key(user_dict, key_to_remove)    
    print("Dictionary after removing key '{}': {}".format(key_to_remove, user_dict))


    # Copy dictionary
    copied_dict = copy_dict(user_dict)
    print()
    print("Copied dictionary:", copied_dict)

    # Clear dictionary
    clear_dict(user_dict)
    print()
    print("Dictionary after clearing:", user_dict)


if __name__ == "__main__":
    main()
