"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mp4MoovPlacement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""To place the MOOV atom at the beginning of your output, which is useful for progressive downloading: Leave blank or choose Progressive download. To place the MOOV at the end of your output: Choose Normal."""
Mp4MoovPlacement: TypeAlias = Literal[
    "PROGRESSIVE_DOWNLOAD",
    "NORMAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROGRESSIVE_DOWNLOAD",
        "NORMAL",
    )
)


def serialize_json(value: Mp4MoovPlacement) -> str:
    return value


def deserialize_json(data: str) -> Mp4MoovPlacement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mp4MoovPlacement value: {data!r}")
    return cast(Mp4MoovPlacement, data)
