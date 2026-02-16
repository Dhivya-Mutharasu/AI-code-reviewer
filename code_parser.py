import ast
import traceback


def analyze_code(code: str) -> None:
    """
    Analyzes Python source code for:
    1. Syntax errors using AST parsing
    2. Runtime errors through execution
    """

    # Syntax Check
    try:
        ast.parse(code)
        print("Syntax Check: PASSED")
    except SyntaxError as e:
        print(f"Syntax Check: FAILED")
        print(f"Line {e.lineno}: {e.msg}")
        return

    # Runtime Check
    try:
        compiled_code = compile(code, "<string>", "exec")
        exec(compiled_code, {})
        print("Runtime Check: PASSED")
    except Exception:
        print("Runtime Check: FAILED")
        print(traceback.format_exc())



code_input = """
def divide(a, b):
    return a / b

print(divide(10, 3))
"""

analyze_code(code_input)


