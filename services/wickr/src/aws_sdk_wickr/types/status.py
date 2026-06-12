"""Generated from Smithy shape ``com.amazonaws.wickr#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wickr.errors import DeserializationError

Status: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "FORCE_ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
        "FORCE_ENABLED",
    )
)


def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
