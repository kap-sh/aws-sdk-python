"""Generated from Smithy shape ``com.amazonaws.connect#MetricFiltersV2List``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.metric_filter_v2

MetricFiltersV2List: TypeAlias = list[
    "aws_sdk_connect.types.metric_filter_v2.MetricFilterV2"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricFiltersV2List) -> list:
    import aws_sdk_connect.types.metric_filter_v2

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.metric_filter_v2.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricFiltersV2List:
    import aws_sdk_connect.types.metric_filter_v2

    out: MetricFiltersV2List = []
    for item in data:
        out.append(aws_sdk_connect.types.metric_filter_v2.deserialize_json(item))
    return out
