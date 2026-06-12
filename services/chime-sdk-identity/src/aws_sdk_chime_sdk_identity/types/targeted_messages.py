"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#TargetedMessages``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_identity.errors import DeserializationError

TargetedMessages: TypeAlias = Literal[
    "ALL",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "NONE",
    )
)


def serialize_json(value: TargetedMessages) -> str:
    return value


def deserialize_json(data: str) -> TargetedMessages:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetedMessages value: {data!r}")
    return cast(TargetedMessages, data)
