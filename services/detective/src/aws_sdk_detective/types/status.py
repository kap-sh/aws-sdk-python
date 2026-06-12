"""Generated from Smithy shape ``com.amazonaws.detective#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_detective.errors import DeserializationError

Status: TypeAlias = Literal[
    "RUNNING",
    "FAILED",
    "SUCCESSFUL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "FAILED",
        "SUCCESSFUL",
    )
)


def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
