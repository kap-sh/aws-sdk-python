"""Generated from Smithy shape ``com.amazonaws.connect#MetricResultsV2``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.metric_result_v2

MetricResultsV2: TypeAlias = list["capo_connect.types.metric_result_v2.MetricResultV2"]


# --- restJson1 ser/de ---
def serialize_json(value: MetricResultsV2) -> list:
    import capo_connect.types.metric_result_v2

    out: list = []
    for item in value:
        out.append(capo_connect.types.metric_result_v2.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricResultsV2:
    import capo_connect.types.metric_result_v2

    out: MetricResultsV2 = []
    for item in data:
        out.append(capo_connect.types.metric_result_v2.deserialize_json(item))
    return out
