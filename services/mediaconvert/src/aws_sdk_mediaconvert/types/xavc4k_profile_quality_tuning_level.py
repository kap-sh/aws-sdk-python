"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Xavc4kProfileQualityTuningLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding."""
Xavc4kProfileQualityTuningLevel: TypeAlias = Literal[
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


def serialize_json(value: Xavc4kProfileQualityTuningLevel) -> str:
    return value


def deserialize_json(data: str) -> Xavc4kProfileQualityTuningLevel:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown Xavc4kProfileQualityTuningLevel value: {data!r}"
        )
    return cast(Xavc4kProfileQualityTuningLevel, data)
