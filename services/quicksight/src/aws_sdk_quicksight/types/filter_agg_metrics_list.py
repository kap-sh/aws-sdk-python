"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterAggMetricsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.filter_agg_metrics

FilterAggMetricsList: TypeAlias = list[
    "aws_sdk_quicksight.types.filter_agg_metrics.FilterAggMetrics"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterAggMetricsList) -> list:
    import aws_sdk_quicksight.types.filter_agg_metrics

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.filter_agg_metrics.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterAggMetricsList:
    import aws_sdk_quicksight.types.filter_agg_metrics

    out: FilterAggMetricsList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.filter_agg_metrics.deserialize_json(item))
    return out
