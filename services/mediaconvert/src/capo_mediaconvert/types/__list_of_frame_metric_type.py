"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfFrameMetricType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.frame_metric_type

__listOfFrameMetricType: TypeAlias = list[
    "capo_mediaconvert.types.frame_metric_type.FrameMetricType"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfFrameMetricType) -> list:
    import capo_mediaconvert.types.frame_metric_type

    out: list = []
    for item in value:
        out.append(capo_mediaconvert.types.frame_metric_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfFrameMetricType:
    import capo_mediaconvert.types.frame_metric_type

    out: __listOfFrameMetricType = []
    for item in data:
        out.append(capo_mediaconvert.types.frame_metric_type.deserialize_json(item))
    return out
