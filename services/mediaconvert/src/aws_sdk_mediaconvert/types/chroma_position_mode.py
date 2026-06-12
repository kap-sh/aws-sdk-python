"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ChromaPositionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the chroma sample positioning metadata for your H.264 or H.265 output. To have MediaConvert automatically determine chroma positioning: We recommend that you keep the default value, Auto. To specify center positioning: Choose Force center. To specify top left positioning: Choose Force top left."""
ChromaPositionMode: TypeAlias = Literal[
    "AUTO",
    "FORCE_CENTER",
    "FORCE_TOP_LEFT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "FORCE_CENTER",
        "FORCE_TOP_LEFT",
    )
)


def serialize_json(value: ChromaPositionMode) -> str:
    return value


def deserialize_json(data: str) -> ChromaPositionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChromaPositionMode value: {data!r}")
    return cast(ChromaPositionMode, data)
