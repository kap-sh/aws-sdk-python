"""Generated from Smithy shape ``com.amazonaws.appflow#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

ExecutionStatus: TypeAlias = Literal[
    "InProgress",
    "Successful",
    "Error",
    "CancelStarted",
    "Canceled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Successful",
        "Error",
        "CancelStarted",
        "Canceled",
    )
)


def serialize_json(value: ExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionStatus value: {data!r}")
    return cast(ExecutionStatus, data)
