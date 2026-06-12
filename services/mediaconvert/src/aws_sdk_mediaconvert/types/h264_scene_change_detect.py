"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H264SceneChangeDetect``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Enable this setting to insert I-frames at scene changes that the service automatically detects. This improves video quality and is enabled by default. If this output uses QVBR, choose Transition detection for further video quality improvement. For more information about QVBR, see https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr."""
H264SceneChangeDetect: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "TRANSITION_DETECTION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
        "TRANSITION_DETECTION",
    )
)


def serialize_json(value: H264SceneChangeDetect) -> str:
    return value


def deserialize_json(data: str) -> H264SceneChangeDetect:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264SceneChangeDetect value: {data!r}")
    return cast(H264SceneChangeDetect, data)
