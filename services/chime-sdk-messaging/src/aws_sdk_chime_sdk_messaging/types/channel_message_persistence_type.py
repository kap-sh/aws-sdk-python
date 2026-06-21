"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMessagePersistenceType``."""

from typing import Literal, TypeAlias, cast

ChannelMessagePersistenceType: TypeAlias = Literal[
    "PERSISTENT",
    "NON_PERSISTENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMessagePersistenceType) -> str:
    return value


def deserialize_json(data: str) -> ChannelMessagePersistenceType:
    return cast(ChannelMessagePersistenceType, data)
