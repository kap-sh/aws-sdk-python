"""Generated from Smithy shape ``com.amazonaws.appintegrations#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appintegrations.errors import DeserializationError

ExecutionStatus: TypeAlias = Literal[
    "COMPLETED",
    "IN_PROGRESS",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETED",
        "IN_PROGRESS",
        "FAILED",
    )
)


def serialize_json(value: ExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionStatus value: {data!r}")
    return cast(ExecutionStatus, data)
