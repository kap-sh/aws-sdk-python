"""Generated from Smithy shape ``com.amazonaws.mediatailor#Tier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

Tier: TypeAlias = Literal[
    "BASIC",
    "STANDARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASIC",
        "STANDARD",
    )
)


def serialize_json(value: Tier) -> str:
    return value


def deserialize_json(data: str) -> Tier:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Tier value: {data!r}")
    return cast(Tier, data)
