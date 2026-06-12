"""Generated from Smithy shape ``com.amazonaws.chime#License``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime.errors import DeserializationError

License: TypeAlias = Literal[
    "Basic",
    "Plus",
    "Pro",
    "ProTrial",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Basic",
        "Plus",
        "Pro",
        "ProTrial",
    )
)


def serialize_json(value: License) -> str:
    return value


def deserialize_json(data: str) -> License:
    if data not in _VALUES:
        raise DeserializationError(f"unknown License value: {data!r}")
    return cast(License, data)
