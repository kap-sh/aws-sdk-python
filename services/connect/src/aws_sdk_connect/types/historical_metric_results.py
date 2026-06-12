"""Generated from Smithy shape ``com.amazonaws.connect#HistoricalMetricResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.historical_metric_result

HistoricalMetricResults: TypeAlias = list[
    "aws_sdk_connect.types.historical_metric_result.HistoricalMetricResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: HistoricalMetricResults) -> list:
    import aws_sdk_connect.types.historical_metric_result

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.historical_metric_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> HistoricalMetricResults:
    import aws_sdk_connect.types.historical_metric_result

    out: HistoricalMetricResults = []
    for item in data:
        out.append(
            aws_sdk_connect.types.historical_metric_result.deserialize_json(item)
        )
    return out
