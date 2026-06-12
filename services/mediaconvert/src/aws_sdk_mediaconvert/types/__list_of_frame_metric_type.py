"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfFrameMetricType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.frame_metric_type

__listOfFrameMetricType: TypeAlias = list[
    "aws_sdk_mediaconvert.types.frame_metric_type.FrameMetricType"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfFrameMetricType) -> list:
    import aws_sdk_mediaconvert.types.frame_metric_type

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.frame_metric_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfFrameMetricType:
    import aws_sdk_mediaconvert.types.frame_metric_type

    out: __listOfFrameMetricType = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.frame_metric_type.deserialize_json(item))
    return out
