"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "Waiting",
        "InProgress",
        "Completed",
        "Failed",
        "Stopping",
        "Stopped",
    )
)


def serialize_json(value: TestExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> TestExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestExecutionStatus value: {data!r}")
    return cast(TestExecutionStatus, data)
