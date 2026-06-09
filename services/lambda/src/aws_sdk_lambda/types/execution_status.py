"""Generated from Smithy shape ``com.amazonaws.lambda#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

ExecutionStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "TIMED_OUT",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "TIMED_OUT",
        "STOPPED",
    )
)


def serialize_json(value: ExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionStatus value: {data!r}")
    return cast(ExecutionStatus, data)
