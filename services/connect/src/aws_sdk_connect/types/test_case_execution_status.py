"""Generated from Smithy shape ``com.amazonaws.connect#TestCaseExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

"""<p>The status of a test case execution.</p>"""
TestCaseExecutionStatus: TypeAlias = Literal[
    "INITIATED",
    "PASSED",
    "FAILED",
    "IN_PROGRESS",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIATED",
        "PASSED",
        "FAILED",
        "IN_PROGRESS",
        "STOPPED",
    )
)


def serialize_json(value: TestCaseExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> TestCaseExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestCaseExecutionStatus value: {data!r}")
    return cast(TestCaseExecutionStatus, data)
