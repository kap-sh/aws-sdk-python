"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#FrameMetricData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.frame_metric_datum

FrameMetricData: TypeAlias = list[
    "capo_codeguruprofiler.types.frame_metric_datum.FrameMetricDatum"
]


# --- restJson1 ser/de ---
def serialize_json(value: FrameMetricData) -> list:
    import capo_codeguruprofiler.types.frame_metric_datum

    out: list = []
    for item in value:
        out.append(capo_codeguruprofiler.types.frame_metric_datum.serialize_json(item))
    return out


def deserialize_json(data: list) -> FrameMetricData:
    import capo_codeguruprofiler.types.frame_metric_datum

    out: FrameMetricData = []
    for item in data:
        out.append(
            capo_codeguruprofiler.types.frame_metric_datum.deserialize_json(item)
        )
    return out
