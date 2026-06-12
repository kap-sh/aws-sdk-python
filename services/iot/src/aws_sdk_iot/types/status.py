"""Generated from Smithy shape ``com.amazonaws.iot#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

Status: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Cancelled",
    "Cancelling",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Completed",
        "Failed",
        "Cancelled",
        "Cancelling",
    )
)


def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
