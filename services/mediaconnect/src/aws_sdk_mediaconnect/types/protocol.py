"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Protocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

Protocol: TypeAlias = Literal[
    "zixi-push",
    "rtp-fec",
    "rtp",
    "zixi-pull",
    "rist",
    "st2110-jpegxs",
    "cdi",
    "srt-listener",
    "srt-caller",
    "fujitsu-qos",
    "udp",
    "ndi-speed-hq",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "zixi-push",
        "rtp-fec",
        "rtp",
        "zixi-pull",
        "rist",
        "st2110-jpegxs",
        "cdi",
        "srt-listener",
        "srt-caller",
        "fujitsu-qos",
        "udp",
        "ndi-speed-hq",
    )
)


def serialize_json(value: Protocol) -> str:
    return value


def deserialize_json(data: str) -> Protocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Protocol value: {data!r}")
    return cast(Protocol, data)
