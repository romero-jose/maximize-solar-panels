from typing import List, Tuple, Dict
import json
from functools import cache


def calculate_panels(
    panel_width: int, panel_height: int, roof_width: int, roof_height: int
) -> int:
    @cache
    def dp(i: int, j: int) -> int:
        # Base cases:
        if i == 0 or j == 0:
            return 0
        # Exact fit (for either orientation)
        if (
            i % panel_width == 0
            and j % panel_height == 0
            or i % panel_height == 0
            and j % panel_width == 0
        ):
            return (i * j) // (panel_width * panel_height)

        # Inductive case:
        # Try splitting roof vertically at the rightmost edge and horizontally at the bottom edge
        return max(
            # Vertical
            dp(i - panel_width, j) + dp(panel_width, j) if i > panel_width else 0,
            # Vertical, inverted
            dp(i - panel_height, j) + dp(panel_height, j) if i > panel_height else 0,
            # Horizontal
            dp(i, j - panel_height) + dp(i, panel_height) if j > panel_height else 0,
            # Horizontal, inverted
            dp(i, j - panel_width) + dp(i, panel_width) if j > panel_width else 0,
        )

    return dp(roof_width, roof_height)


def run_tests() -> None:
    with open("test_cases.json", "r") as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"],
            }
            for test in data["testCases"]
        ]

    print("Corriendo tests:")
    print("-------------------")

    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]

        print(f"Test {i}:")
        print(
            f"  Panels: {test['panel_w']}x{test['panel_h']}, "
            f"Roof: {test['roof_w']}x{test['roof_h']}"
        )
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")

    run_tests()


if __name__ == "__main__":
    main()
