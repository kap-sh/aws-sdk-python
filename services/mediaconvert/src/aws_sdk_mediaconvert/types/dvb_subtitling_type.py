"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DvbSubtitlingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify whether your DVB subtitles are standard or for hearing impaired. Choose hearing impaired if your subtitles include audio descriptions and dialogue. Choose standard if your subtitles include only dialogue."""
DvbSubtitlingType: TypeAlias = Literal[
    "HEARING_IMPAIRED",
    "STANDARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEARING_IMPAIRED",
        "STANDARD",
    )
)


def serialize_json(value: DvbSubtitlingType) -> str:
    return value


def deserialize_json(data: str) -> DvbSubtitlingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DvbSubtitlingType value: {data!r}")
    return cast(DvbSubtitlingType, data)
