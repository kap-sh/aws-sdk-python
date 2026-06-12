"""Generated from Smithy shape ``com.amazonaws.iotwireless#MessageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

"""<p>Sidewalk device message type. Default value is <code>CUSTOM_COMMAND_ID_NOTIFY</code>.</p>"""
MessageType: TypeAlias = Literal[
    "CUSTOM_COMMAND_ID_NOTIFY",
    "CUSTOM_COMMAND_ID_GET",
    "CUSTOM_COMMAND_ID_SET",
    "CUSTOM_COMMAND_ID_RESP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOM_COMMAND_ID_NOTIFY",
        "CUSTOM_COMMAND_ID_GET",
        "CUSTOM_COMMAND_ID_SET",
        "CUSTOM_COMMAND_ID_RESP",
    )
)


def serialize_json(value: MessageType) -> str:
    return value


def deserialize_json(data: str) -> MessageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MessageType value: {data!r}")
    return cast(MessageType, data)
