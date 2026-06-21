"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ChannelType``."""

from typing import Literal, TypeAlias, cast

ChannelType: TypeAlias = Literal[
    "Facebook",
    "Slack",
    "Twilio-Sms",
    "Kik",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelType) -> str:
    return value


def deserialize_json(data: str) -> ChannelType:
    return cast(ChannelType, data)
