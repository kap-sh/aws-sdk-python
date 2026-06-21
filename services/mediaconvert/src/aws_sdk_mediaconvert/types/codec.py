"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Codec``."""

from typing import Literal, TypeAlias, cast

Codec: TypeAlias = Literal[
    "UNKNOWN",
    "AAC",
    "AC3",
    "EAC3",
    "FLAC",
    "MP2",
    "MP3",
    "OPUS",
    "PCM",
    "VORBIS",
    "AV1",
    "AVC",
    "HEVC",
    "JPEG2000",
    "MJPEG",
    "MPEG1",
    "MP4V",
    "MPEG2",
    "PRORES",
    "QTRLE",
    "THEORA",
    "UNCOMPRESSED",
    "VFW",
    "VP8",
    "VP9",
    "C608",
    "C708",
    "WEBVTT",
]


# --- restJson1 ser/de ---
def serialize_json(value: Codec) -> str:
    return value


def deserialize_json(data: str) -> Codec:
    return cast(Codec, data)
