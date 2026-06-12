"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#Capability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

Capability: TypeAlias = Literal[
    "Voice",
    "SMS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Voice",
        "SMS",
    )
)


def serialize_json(value: Capability) -> str:
    return value


def deserialize_json(data: str) -> Capability:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Capability value: {data!r}")
    return cast(Capability, data)
