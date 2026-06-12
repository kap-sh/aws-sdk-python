"""Generated from Smithy shape ``com.amazonaws.mediaconvert#NoiseFilterPostTemporalSharpeningStrength``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Use Post temporal sharpening strength to define the amount of sharpening the transcoder applies to your output. Set Post temporal sharpening strength to Low, Medium, or High to indicate the amount of sharpening."""
NoiseFilterPostTemporalSharpeningStrength: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOW",
        "MEDIUM",
        "HIGH",
    )
)


def serialize_json(value: NoiseFilterPostTemporalSharpeningStrength) -> str:
    return value


def deserialize_json(data: str) -> NoiseFilterPostTemporalSharpeningStrength:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NoiseFilterPostTemporalSharpeningStrength value: {data!r}"
        )
    return cast(NoiseFilterPostTemporalSharpeningStrength, data)
