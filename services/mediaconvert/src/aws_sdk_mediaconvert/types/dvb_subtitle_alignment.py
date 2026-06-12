"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DvbSubtitleAlignment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the alignment of your captions. If no explicit x_position is provided, setting alignment to centered will placethe captions at the bottom center of the output. Similarly, setting a left alignment willalign captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Within your job settings, all of your DVB-Sub settings must be identical."""
DvbSubtitleAlignment: TypeAlias = Literal[
    "CENTERED",
    "LEFT",
    "AUTO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CENTERED",
        "LEFT",
        "AUTO",
    )
)


def serialize_json(value: DvbSubtitleAlignment) -> str:
    return value


def deserialize_json(data: str) -> DvbSubtitleAlignment:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DvbSubtitleAlignment value: {data!r}")
    return cast(DvbSubtitleAlignment, data)
