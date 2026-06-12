"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#StandardMessages``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_identity.errors import DeserializationError

StandardMessages: TypeAlias = Literal[
    "AUTO",
    "ALL",
    "MENTIONS",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "ALL",
        "MENTIONS",
        "NONE",
    )
)


def serialize_json(value: StandardMessages) -> str:
    return value


def deserialize_json(data: str) -> StandardMessages:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StandardMessages value: {data!r}")
    return cast(StandardMessages, data)
