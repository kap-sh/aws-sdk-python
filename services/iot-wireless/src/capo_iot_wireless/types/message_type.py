"""Generated from Smithy shape ``com.amazonaws.iotwireless#MessageType``."""

from typing import Literal, TypeAlias, cast

"""<p>Sidewalk device message type. Default value is <code>CUSTOM_COMMAND_ID_NOTIFY</code>.</p>"""
MessageType: TypeAlias = Literal[
    "CUSTOM_COMMAND_ID_NOTIFY",
    "CUSTOM_COMMAND_ID_GET",
    "CUSTOM_COMMAND_ID_SET",
    "CUSTOM_COMMAND_ID_RESP",
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageType) -> str:
    return value


def deserialize_json(data: str) -> MessageType:
    return cast(MessageType, data)
