"""Generated from Smithy shape ``com.amazonaws.medialive#InputType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The different types of inputs that AWS Elemental MediaLive supports."""
InputType: TypeAlias = Literal[
    "UDP_PUSH",
    "RTP_PUSH",
    "RTMP_PUSH",
    "RTMP_PULL",
    "URL_PULL",
    "MP4_FILE",
    "MEDIACONNECT",
    "INPUT_DEVICE",
    "AWS_CDI",
    "TS_FILE",
    "SRT_CALLER",
    "MULTICAST",
    "SMPTE_2110_RECEIVER_GROUP",
    "SDI",
    "MEDIACONNECT_ROUTER",
    "SRT_LISTENER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UDP_PUSH",
        "RTP_PUSH",
        "RTMP_PUSH",
        "RTMP_PULL",
        "URL_PULL",
        "MP4_FILE",
        "MEDIACONNECT",
        "INPUT_DEVICE",
        "AWS_CDI",
        "TS_FILE",
        "SRT_CALLER",
        "MULTICAST",
        "SMPTE_2110_RECEIVER_GROUP",
        "SDI",
        "MEDIACONNECT_ROUTER",
        "SRT_LISTENER",
    )
)


def serialize_json(value: InputType) -> str:
    return value


def deserialize_json(data: str) -> InputType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputType value: {data!r}")
    return cast(InputType, data)
