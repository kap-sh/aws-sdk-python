"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMessagePersistenceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

ChannelMessagePersistenceType: TypeAlias = Literal[
    "PERSISTENT",
    "NON_PERSISTENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PERSISTENT",
        "NON_PERSISTENT",
    )
)


def serialize_json(value: ChannelMessagePersistenceType) -> str:
    return value


def deserialize_json(data: str) -> ChannelMessagePersistenceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ChannelMessagePersistenceType value: {data!r}"
        )
    return cast(ChannelMessagePersistenceType, data)
