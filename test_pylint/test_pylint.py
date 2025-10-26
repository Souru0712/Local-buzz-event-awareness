import os

# --- 1. Class Naming Violation (Should trigger invalid-name C0103) ---
# Your rule: class-name-regexp = "[A-Z][a-zA-Z0-9]{1,}$" (PascalCase)
class bad_name:
    """This class is named incorrectly (should be PascalCase)."""
    
    # --- 2. Variable Naming Violation (C0103) ---
    # Your rule: variable-name-regexp = "[a-z_][a-z0-9_]{1,}$" 
    # 'u' is only one character long, violating the {1,} minimum.
    def __init__(self, someArgument):
        # Should trigger 'invalid-name' for the single letter 'u'
        u = 0
        
        # Should trigger 'invalid-name' for 'someArgument' (not snake_case)
        self.someArgument = someArgument

# --- 3. Function/Argument Naming Violation (C0103) ---
# Your rule: function-name-regexp = "[a-z_][a-z0-9_]{1,}$" 
# 'DoWork' is not snake_case.
def DoWork(MyInput):
    """
    Performs some work, violating function and argument naming conventions.
    """
    # --- 4. Unused Variable (W0612) ---
    # Pylint will flag 'local_variable' as it is defined but never used.
    local_variable = 10
    
    if os.name == 'posix':
        print("Running on Linux/macOS")
        
    return MyInput * 2

# --- 5. Constant Naming Violation (C0103) ---
# Your rule: const-name-regexp = "[A-Z_][A-Z0-9_]{1,}$" (UPPER_CASE)
bad_CONST = 1000

# --- 6. Missing Docstring (C0116) ---
# This function is correct by naming standards but lacks a docstring.
def final_function(input_value):
    return input_value + 1

# --- 7. Line Length Violation (C0301) ---
# This line is intentionally very long to exceed the default 100-character limit, 
# triggering 'line-too-long'.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------