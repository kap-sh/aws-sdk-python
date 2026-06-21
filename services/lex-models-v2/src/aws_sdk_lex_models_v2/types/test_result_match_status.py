"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestResultMatchStatus``."""

from typing import Literal, TypeAlias, cast

TestResultMatchStatus: TypeAlias = Literal[
    "Matched",
    "Mismatched",
    "ExecutionError",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestResultMatchStatus) -> str:
    return value


def deserialize_json(data: str) -> TestResultMatchStatus:
    return cast(TestResultMatchStatus, data)
