"""Generated from Smithy shape ``com.amazonaws.mediaconvert#InputSampleRange``."""

from typing import Literal, TypeAlias, cast

"""If the sample range metadata in your input video is accurate, or if you don't know about sample range, keep the default value, Follow, for this setting. When you do, the service automatically detects your input sample range. If your input video has metadata indicating the wrong sample range, specify the accurate sample range here. When you do, MediaConvert ignores any sample range information in the input metadata. Regardless of whether MediaConvert uses the input sample range or the sample range that you specify, MediaConvert uses the sample range for transcoding and also writes it to the output metadata."""
InputSampleRange: TypeAlias = Literal[
    "FOLLOW",
    "FULL_RANGE",
    "LIMITED_RANGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputSampleRange) -> str:
    return value


def deserialize_json(data: str) -> InputSampleRange:
    return cast(InputSampleRange, data)
