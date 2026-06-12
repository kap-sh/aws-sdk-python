"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ChannelType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

ChannelType: TypeAlias = Literal[
    "Facebook",
    "Slack",
    "Twilio-Sms",
    "Kik",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Facebook",
        "Slack",
        "Twilio-Sms",
        "Kik",
    )
)


def serialize_json(value: ChannelType) -> str:
    return value


def deserialize_json(data: str) -> ChannelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelType value: {data!r}")
    return cast(ChannelType, data)
