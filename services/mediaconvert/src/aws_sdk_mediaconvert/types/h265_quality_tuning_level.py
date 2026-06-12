"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265QualityTuningLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding."""
H265QualityTuningLevel: TypeAlias = Literal[
    "SINGLE_PASS",
    "SINGLE_PASS_HQ",
    "MULTI_PASS_HQ",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE_PASS",
        "SINGLE_PASS_HQ",
        "MULTI_PASS_HQ",
    )
)


def serialize_json(value: H265QualityTuningLevel) -> str:
    return value


def deserialize_json(data: str) -> H265QualityTuningLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265QualityTuningLevel value: {data!r}")
    return cast(H265QualityTuningLevel, data)
