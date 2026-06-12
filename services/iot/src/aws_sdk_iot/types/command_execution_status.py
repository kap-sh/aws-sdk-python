"""Generated from Smithy shape ``com.amazonaws.iot#CommandExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

CommandExecutionStatus: TypeAlias = Literal[
    "CREATED",
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
    "REJECTED",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
        "REJECTED",
        "TIMED_OUT",
    )
)


def serialize_json(value: CommandExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> CommandExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CommandExecutionStatus value: {data!r}")
    return cast(CommandExecutionStatus, data)
