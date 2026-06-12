"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MovPaddingControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Unless you need Omneon compatibility: Keep the default value, None. To make this output compatible with Omneon: Choose Omneon. When you do, MediaConvert increases the length of the 'elst' edit list atom. Note that this might cause file rejections when a recipient of the output file doesn't expect this extra padding."""
MovPaddingControl: TypeAlias = Literal[
    "OMNEON",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OMNEON",
        "NONE",
    )
)


def serialize_json(value: MovPaddingControl) -> str:
    return value


def deserialize_json(data: str) -> MovPaddingControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MovPaddingControl value: {data!r}")
    return cast(MovPaddingControl, data)
