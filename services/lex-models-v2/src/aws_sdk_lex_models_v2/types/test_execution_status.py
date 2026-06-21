"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestExecutionStatus``."""

from typing import Literal, TypeAlias, cast

TestExecutionStatus: TypeAlias = Literal[
    "Pending",
    "Waiting",
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> TestExecutionStatus:
    return cast(TestExecutionStatus, data)
