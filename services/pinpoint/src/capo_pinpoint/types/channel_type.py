"""Generated from Smithy shape ``com.amazonaws.pinpoint#ChannelType``."""

from typing import Literal, TypeAlias, cast

ChannelType: TypeAlias = Literal[
    "PUSH",
    "GCM",
    "APNS",
    "APNS_SANDBOX",
    "APNS_VOIP",
    "APNS_VOIP_SANDBOX",
    "ADM",
    "SMS",
    "VOICE",
    "EMAIL",
    "BAIDU",
    "CUSTOM",
    "IN_APP",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelType) -> str:
    return value


def deserialize_json(data: str) -> ChannelType:
    return cast(ChannelType, data)
