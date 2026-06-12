"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoCodec``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Type of video codec"""
VideoCodec: TypeAlias = Literal[
    "AV1",
    "AVC_INTRA",
    "FRAME_CAPTURE",
    "GIF",
    "H_264",
    "H_265",
    "MPEG2",
    "PASSTHROUGH",
    "PRORES",
    "UNCOMPRESSED",
    "VC3",
    "VP8",
    "VP9",
    "XAVC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AV1",
        "AVC_INTRA",
        "FRAME_CAPTURE",
        "GIF",
        "H_264",
        "H_265",
        "MPEG2",
        "PASSTHROUGH",
        "PRORES",
        "UNCOMPRESSED",
        "VC3",
        "VP8",
        "VP9",
        "XAVC",
    )
)


def serialize_json(value: VideoCodec) -> str:
    return value


def deserialize_json(data: str) -> VideoCodec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VideoCodec value: {data!r}")
    return cast(VideoCodec, data)
