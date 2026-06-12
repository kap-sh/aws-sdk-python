"""Generated from Smithy shape ``com.amazonaws.pinpoint#ChannelType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: ChannelType) -> str:
    return value


def deserialize_json(data: str) -> ChannelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelType value: {data!r}")
    return cast(ChannelType, data)
