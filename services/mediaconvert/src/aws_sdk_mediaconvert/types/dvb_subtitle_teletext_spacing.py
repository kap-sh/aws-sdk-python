"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DvbSubtitleTeletextSpacing``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify whether the Text spacing in your captions is set by the captions grid, or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read for closed captions. Within your job settings, all of your DVB-Sub settings must be identical."""
DvbSubtitleTeletextSpacing: TypeAlias = Literal[
    "FIXED_GRID",
    "PROPORTIONAL",
    "AUTO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIXED_GRID",
        "PROPORTIONAL",
        "AUTO",
    )
)


def serialize_json(value: DvbSubtitleTeletextSpacing) -> str:
    return value


def deserialize_json(data: str) -> DvbSubtitleTeletextSpacing:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DvbSubtitleTeletextSpacing value: {data!r}"
        )
    return cast(DvbSubtitleTeletextSpacing, data)
