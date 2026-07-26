"""Generated from Smithy shape ``com.amazonaws.connect#HistoricalMetricResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.historical_metric_result

HistoricalMetricResults: TypeAlias = list[
    "capo_connect.types.historical_metric_result.HistoricalMetricResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: HistoricalMetricResults) -> list:
    import capo_connect.types.historical_metric_result

    out: list = []
    for item in value:
        out.append(capo_connect.types.historical_metric_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> HistoricalMetricResults:
    import capo_connect.types.historical_metric_result

    out: HistoricalMetricResults = []
    for item in data:
        out.append(capo_connect.types.historical_metric_result.deserialize_json(item))
    return out
