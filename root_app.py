import streamlit as st

def digit_root(num):
    """Calculate the digit root of a number."""
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num

def find_combinations(target_sum, num_digits, exclude_numbers, exclude_combinations):
    """Find all numbers with specific digit root and restrictions."""
    start = 10 ** (num_digits - 1)
    end = 10 ** num_digits
    result = []

    for num in range(start, end):
        num_str = str(num)
        
        # Exclude numbers with specific digits
        if any(str(exclude) in num_str for exclude in exclude_numbers):
            continue
        
        # Exclude specific combinations
        if any(combo in num_str for combo in exclude_combinations):
            continue
        
        # Check if the digit root matches the target sum
        if digit_root(num) == target_sum:
            result.append(num)
    return result

# Streamlit App
st.title("Digit Root Combination Finder")

# Inputs
st.sidebar.header("Inputs")
target_sum = st.sidebar.number_input("Enter the target digit root sum:", min_value=1, max_value=9, value=5)
num_digits = st.sidebar.number_input("Enter the number of digits:", min_value=1, max_value=10, value=4)
exclude_numbers = st.sidebar.text_input("Exclude specific digits (comma-separated):", value="").split(",")
exclude_combinations = st.sidebar.text_input("Exclude specific combinations (comma-separated):", value="").split(",")

# Clean inputs
exclude_numbers = [num.strip() for num in exclude_numbers if num.strip().isdigit()]
exclude_combinations = [combo.strip() for combo in exclude_combinations if combo.strip().isdigit()]

# Generate combinations
if st.sidebar.button("Find Combinations"):
    st.header("Results")
    combinations = find_combinations(target_sum, num_digits, exclude_numbers, exclude_combinations)
    st.write(f"Numbers with {num_digits} digits whose digit root equals {target_sum} (excluding specified digits and combinations):")
    st.write(combinations)
    st.success(f"Found {len(combinations)} valid numbers.")
