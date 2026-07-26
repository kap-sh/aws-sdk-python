"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#MessagingDataType``."""

from typing import Literal, TypeAlias, cast

MessagingDataType: TypeAlias = Literal[
    "Channel",
    "ChannelMessage",
]


# --- restJson1 ser/de ---
def serialize_json(value: MessagingDataType) -> str:
    return value


def deserialize_json(data: str) -> MessagingDataType:
    return cast(MessagingDataType, data)
