"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Codec``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: Codec) -> str:
    return value


def deserialize_json(data: str) -> Codec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Codec value: {data!r}")
    return cast(Codec, data)
