"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TamsGapHandling``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify how MediaConvert handles gaps between media segments in your TAMS source. Gaps can occur in live streams due to network issues or other interruptions. Choose from the following options: * Skip gaps - Default. Skip over gaps and join segments together. This creates a continuous output with no blank frames, but may cause timeline discontinuities. * Fill with black - Insert black frames to fill gaps between segments. This maintains timeline continuity but adds black frames where content is missing. * Hold last frame - Repeat the last frame before a gap until the next segment begins. This maintains visual continuity during gaps."""
TamsGapHandling: TypeAlias = Literal[
    "SKIP_GAPS",
    "FILL_WITH_BLACK",
    "HOLD_LAST_FRAME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SKIP_GAPS",
        "FILL_WITH_BLACK",
        "HOLD_LAST_FRAME",
    )
)


def serialize_json(value: TamsGapHandling) -> str:
    return value


def deserialize_json(data: str) -> TamsGapHandling:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TamsGapHandling value: {data!r}")
    return cast(TamsGapHandling, data)
