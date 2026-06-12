"""Generated from Smithy shape ``com.amazonaws.sesv2#BounceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

BounceType: TypeAlias = Literal[
    "UNDETERMINED",
    "TRANSIENT",
    "PERMANENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNDETERMINED",
        "TRANSIENT",
        "PERMANENT",
    )
)


def serialize_json(value: BounceType) -> str:
    return value


def deserialize_json(data: str) -> BounceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BounceType value: {data!r}")
    return cast(BounceType, data)
