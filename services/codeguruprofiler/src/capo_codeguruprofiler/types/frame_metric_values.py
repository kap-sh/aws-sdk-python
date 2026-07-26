"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#FrameMetricValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.frame_metric_value

FrameMetricValues: TypeAlias = list[
    "capo_codeguruprofiler.types.frame_metric_value.FrameMetricValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: FrameMetricValues) -> list:
    return list(value)


def deserialize_json(data: list) -> FrameMetricValues:
    return list(data)
