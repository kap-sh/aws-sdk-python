"""Generated from Smithy shape ``com.amazonaws.mediaconvert#XavcHdProfileQualityTuningLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding."""
XavcHdProfileQualityTuningLevel: TypeAlias = Literal[
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


def serialize_json(value: XavcHdProfileQualityTuningLevel) -> str:
    return value


def deserialize_json(data: str) -> XavcHdProfileQualityTuningLevel:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown XavcHdProfileQualityTuningLevel value: {data!r}"
        )
    return cast(XavcHdProfileQualityTuningLevel, data)
