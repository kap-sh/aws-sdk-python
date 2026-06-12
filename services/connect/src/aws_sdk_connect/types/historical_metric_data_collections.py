"""Generated from Smithy shape ``com.amazonaws.connect#HistoricalMetricDataCollections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.historical_metric_data

HistoricalMetricDataCollections: TypeAlias = list[
    "aws_sdk_connect.types.historical_metric_data.HistoricalMetricData"
]


# --- restJson1 ser/de ---
def serialize_json(value: HistoricalMetricDataCollections) -> list:
    import aws_sdk_connect.types.historical_metric_data

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.historical_metric_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> HistoricalMetricDataCollections:
    import aws_sdk_connect.types.historical_metric_data

    out: HistoricalMetricDataCollections = []
    for item in data:
        out.append(aws_sdk_connect.types.historical_metric_data.deserialize_json(item))
    return out
