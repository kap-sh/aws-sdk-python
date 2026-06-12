"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Vp9QualityTuningLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, multi-pass encoding."""
Vp9QualityTuningLevel: TypeAlias = Literal[
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


def serialize_json(value: Vp9QualityTuningLevel) -> str:
    return value


def deserialize_json(data: str) -> Vp9QualityTuningLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Vp9QualityTuningLevel value: {data!r}")
    return cast(Vp9QualityTuningLevel, data)
