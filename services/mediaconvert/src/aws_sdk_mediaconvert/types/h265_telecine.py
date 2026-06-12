"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265Telecine``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""This field applies only if the Streams > Advanced > Framerate field is set to 29.970. This field works with the Streams > Advanced > Preprocessors > Deinterlacer field and the Streams > Advanced > Interlaced Mode field to identify the scan type for the output: Progressive, Interlaced, Hard Telecine or Soft Telecine. - Hard: produces 29.97i output from 23.976 input. - Soft: produces 23.976; the player converts this output to 29.97i."""
H265Telecine: TypeAlias = Literal[
    "NONE",
    "SOFT",
    "HARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "SOFT",
        "HARD",
    )
)


def serialize_json(value: H265Telecine) -> str:
    return value


def deserialize_json(data: str) -> H265Telecine:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265Telecine value: {data!r}")
    return cast(H265Telecine, data)
