"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#MediaCapabilities``."""

from typing import Literal, TypeAlias, cast

MediaCapabilities: TypeAlias = Literal[
    "SendReceive",
    "Send",
    "Receive",
    "None",
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaCapabilities) -> str:
    return value


def deserialize_json(data: str) -> MediaCapabilities:
    return cast(MediaCapabilities, data)
