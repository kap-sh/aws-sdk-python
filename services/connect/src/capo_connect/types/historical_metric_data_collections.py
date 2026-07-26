"""Generated from Smithy shape ``com.amazonaws.connect#HistoricalMetricDataCollections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.historical_metric_data

HistoricalMetricDataCollections: TypeAlias = list[
    "capo_connect.types.historical_metric_data.HistoricalMetricData"
]


# --- restJson1 ser/de ---
def serialize_json(value: HistoricalMetricDataCollections) -> list:
    import capo_connect.types.historical_metric_data

    out: list = []
    for item in value:
        out.append(capo_connect.types.historical_metric_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> HistoricalMetricDataCollections:
    import capo_connect.types.historical_metric_data

    out: HistoricalMetricDataCollections = []
    for item in data:
        out.append(capo_connect.types.historical_metric_data.deserialize_json(item))
    return out
