"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AvcIntraUhdQualityTuningLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Optional. Use Quality tuning level to choose how many transcoding passes MediaConvert does with your video. When you choose Multi-pass, your video quality is better and your output bitrate is more accurate. That is, the actual bitrate of your output is closer to the target bitrate defined in the specification. When you choose Single-pass, your encoding time is faster. The default behavior is Single-pass."""
AvcIntraUhdQualityTuningLevel: TypeAlias = Literal[
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


def serialize_json(value: AvcIntraUhdQualityTuningLevel) -> str:
    return value


def deserialize_json(data: str) -> AvcIntraUhdQualityTuningLevel:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AvcIntraUhdQualityTuningLevel value: {data!r}"
        )
    return cast(AvcIntraUhdQualityTuningLevel, data)
