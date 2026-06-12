"""Generated from Smithy shape ``com.amazonaws.deadline#CompletedStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

CompletedStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "INTERRUPTED",
    "CANCELED",
    "NEVER_ATTEMPTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "FAILED",
        "INTERRUPTED",
        "CANCELED",
        "NEVER_ATTEMPTED",
    )
)


def serialize_json(value: CompletedStatus) -> str:
    return value


def deserialize_json(data: str) -> CompletedStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CompletedStatus value: {data!r}")
    return cast(CompletedStatus, data)
