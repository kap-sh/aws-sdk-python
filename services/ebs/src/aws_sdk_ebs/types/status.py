"""Generated from Smithy shape ``com.amazonaws.ebs#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ebs.errors import DeserializationError

Status: TypeAlias = Literal[
    "completed",
    "pending",
    "error",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "completed",
        "pending",
        "error",
    )
)


def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
