"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mpeg2QualityTuningLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding."""
Mpeg2QualityTuningLevel: TypeAlias = Literal[
    "SINGLE_PASS",
    "MULTI_PASS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE_PASS",
        "MULTI_PASS",
    )
)


def serialize_json(value: Mpeg2QualityTuningLevel) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2QualityTuningLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mpeg2QualityTuningLevel value: {data!r}")
    return cast(Mpeg2QualityTuningLevel, data)
