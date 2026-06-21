"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ChannelProtocol``."""

from typing import Literal, TypeAlias, cast

ChannelProtocol: TypeAlias = Literal[
    "WSS",
    "HTTPS",
    "WEBRTC",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelProtocol) -> str:
    return value


def deserialize_json(data: str) -> ChannelProtocol:
    return cast(ChannelProtocol, data)
