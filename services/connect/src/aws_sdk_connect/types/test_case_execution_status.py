"""Generated from Smithy shape ``com.amazonaws.connect#TestCaseExecutionStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a test case execution.</p>"""
TestCaseExecutionStatus: TypeAlias = Literal[
    "INITIATED",
    "PASSED",
    "FAILED",
    "IN_PROGRESS",
    "STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> TestCaseExecutionStatus:
    return cast(TestCaseExecutionStatus, data)
