"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Vp8QualityTuningLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, multi-pass encoding."""
Vp8QualityTuningLevel: TypeAlias = Literal[
    "MULTI_PASS",
    "MULTI_PASS_HQ",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MULTI_PASS",
        "MULTI_PASS_HQ",
    )
)


def serialize_json(value: Vp8QualityTuningLevel) -> str:
    return value


def deserialize_json(data: str) -> Vp8QualityTuningLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Vp8QualityTuningLevel value: {data!r}")
    return cast(Vp8QualityTuningLevel, data)
