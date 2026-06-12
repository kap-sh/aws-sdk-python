"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsProgramDateTime``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files. The value is calculated as follows: either the program date and time are initialized using the input timecode source, or the time is initialized using the input timecode source and the date is initialized using the timestamp_offset."""
HlsProgramDateTime: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUDE",
        "EXCLUDE",
    )
)


def serialize_json(value: HlsProgramDateTime) -> str:
    return value


def deserialize_json(data: str) -> HlsProgramDateTime:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsProgramDateTime value: {data!r}")
    return cast(HlsProgramDateTime, data)
