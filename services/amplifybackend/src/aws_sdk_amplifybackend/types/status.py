"""Generated from Smithy shape ``com.amazonaws.amplifybackend#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifybackend.errors import DeserializationError

Status: TypeAlias = Literal[
    "LATEST",
    "STALE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LATEST",
        "STALE",
    )
)


def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
