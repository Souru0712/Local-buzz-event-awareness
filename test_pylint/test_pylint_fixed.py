import os

# --- 1. Class Naming Violation (Should trigger invalid-name C0103) ---
# Your rule: class-name-regexp = "[A-Z][a-zA-Z0-9]{1,}$" (PascalCase)
class Badname:
    """Turned into Pascal""" 
    # --- 2. Variable Naming Violation (C0103) ---
    # Your rule: variable-name-regexp = "[a-z_][a-z0-9_]{1,}$"
    # 'u' is only one character long, violating the {1,} minimum.
    def __init__(self, some_argument):
        # Should trigger 'invalid-name' for the single letter 'u'
        # Should trigger 'invalid-name' for 'someArgument' (not snake_case)
        self.some_argument = some_argument

# --- 3. Function/Argument Naming Violation (C0103) ---
# Your rule: function-name-regexp = "[a-z_][a-z0-9_]{1,}$"
# 'DoWork' is not snake_case.
def do_work(my_input):
    """
    Performs some work. Fixed function name and parameters with snake_case, removing local variable
    """
    # --- 4. Unused Variable (W0612) ---
    # Pylint will flag 'local_variable' as it is defined but never used.
    if os.name == 'posix':
        print("Running on Linux/macOS")
    return my_input * 2

# --- 5. Constant Naming Violation (C0103) ---
# Your rule: const-name-regexp = "[A-Z_][A-Z0-9_]{1,}$" (UPPER_CASE)
GOOD_CONSTANT = 1000

# --- 6. Missing Docstring (C0116) ---
# This function is correct by naming standards but lacks a docstring.
def final_function(input_value):
    """fixed"""
    return input_value + 1

# --- 7. Line Length Violation (C0301) ---
# This line is intentionally very long to exceed the default 100-character limit,
# triggering 'line-too-long'.
