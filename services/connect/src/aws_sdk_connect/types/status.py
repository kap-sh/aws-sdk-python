"""Generated from Smithy shape ``com.amazonaws.connect#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

Status: TypeAlias = Literal[
    "COMPLETE",
    "IN_PROGRESS",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETE",
        "IN_PROGRESS",
        "DELETED",
    )
)


def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
