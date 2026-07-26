"""Generated from Smithy shape ``com.amazonaws.connect#MetricFiltersV2List``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.metric_filter_v2

MetricFiltersV2List: TypeAlias = list[
    "capo_connect.types.metric_filter_v2.MetricFilterV2"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricFiltersV2List) -> list:
    import capo_connect.types.metric_filter_v2

    out: list = []
    for item in value:
        out.append(capo_connect.types.metric_filter_v2.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricFiltersV2List:
    import capo_connect.types.metric_filter_v2

    out: MetricFiltersV2List = []
    for item in data:
        out.append(capo_connect.types.metric_filter_v2.deserialize_json(item))
    return out
