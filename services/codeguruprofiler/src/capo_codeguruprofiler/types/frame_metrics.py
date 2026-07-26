"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#FrameMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.frame_metric

FrameMetrics: TypeAlias = list["capo_codeguruprofiler.types.frame_metric.FrameMetric"]


# --- restJson1 ser/de ---
def serialize_json(value: FrameMetrics) -> list:
    import capo_codeguruprofiler.types.frame_metric

    out: list = []
    for item in value:
        out.append(capo_codeguruprofiler.types.frame_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> FrameMetrics:
    import capo_codeguruprofiler.types.frame_metric

    out: FrameMetrics = []
    for item in data:
        out.append(capo_codeguruprofiler.types.frame_metric.deserialize_json(item))
    return out
