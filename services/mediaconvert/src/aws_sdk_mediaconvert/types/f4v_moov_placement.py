"""Generated from Smithy shape ``com.amazonaws.mediaconvert#F4vMoovPlacement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""To place the MOOV atom at the beginning of your output, which is useful for progressive downloading: Leave blank or choose Progressive download. To place the MOOV at the end of your output: Choose Normal."""
F4vMoovPlacement: TypeAlias = Literal[
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


def serialize_json(value: F4vMoovPlacement) -> str:
    return value


def deserialize_json(data: str) -> F4vMoovPlacement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown F4vMoovPlacement value: {data!r}")
    return cast(F4vMoovPlacement, data)
