"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DeinterlaceAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Only applies when you set Deinterlace mode to Deinterlace or Adaptive. Interpolate produces sharper pictures, while blend produces smoother motion. If your source file includes a ticker, such as a scrolling headline at the bottom of the frame: Choose Interpolate ticker or Blend ticker. To apply field doubling: Choose Linear interpolation. Note that Linear interpolation may introduce video artifacts into your output."""
DeinterlaceAlgorithm: TypeAlias = Literal[
    "INTERPOLATE",
    "INTERPOLATE_TICKER",
    "BLEND",
    "BLEND_TICKER",
    "LINEAR_INTERPOLATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERPOLATE",
        "INTERPOLATE_TICKER",
        "BLEND",
        "BLEND_TICKER",
        "LINEAR_INTERPOLATION",
    )
)


def serialize_json(value: DeinterlaceAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> DeinterlaceAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeinterlaceAlgorithm value: {data!r}")
    return cast(DeinterlaceAlgorithm, data)
