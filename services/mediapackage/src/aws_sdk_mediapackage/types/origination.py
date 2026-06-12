"""Generated from Smithy shape ``com.amazonaws.mediapackage#Origination``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackage.errors import DeserializationError

Origination: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "DENY",
    )
)


def serialize_json(value: Origination) -> str:
    return value


def deserialize_json(data: str) -> Origination:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Origination value: {data!r}")
    return cast(Origination, data)
