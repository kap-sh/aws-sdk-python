"""Generated from Smithy shape ``com.amazonaws.connect#HistoricalMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.historical_metric

HistoricalMetrics: TypeAlias = list[
    "aws_sdk_connect.types.historical_metric.HistoricalMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: HistoricalMetrics) -> list:
    import aws_sdk_connect.types.historical_metric

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.historical_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> HistoricalMetrics:
    import aws_sdk_connect.types.historical_metric

    out: HistoricalMetrics = []
    for item in data:
        out.append(aws_sdk_connect.types.historical_metric.deserialize_json(item))
    return out
