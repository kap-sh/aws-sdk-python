"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ChannelProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video.errors import DeserializationError

ChannelProtocol: TypeAlias = Literal[
    "WSS",
    "HTTPS",
    "WEBRTC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WSS",
        "HTTPS",
        "WEBRTC",
    )
)


def serialize_json(value: ChannelProtocol) -> str:
    return value


def deserialize_json(data: str) -> ChannelProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelProtocol value: {data!r}")
    return cast(ChannelProtocol, data)
