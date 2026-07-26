"""Generated from Smithy shape ``com.amazonaws.connect#HistoricalMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.historical_metric

HistoricalMetrics: TypeAlias = list[
    "capo_connect.types.historical_metric.HistoricalMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: HistoricalMetrics) -> list:
    import capo_connect.types.historical_metric

    out: list = []
    for item in value:
        out.append(capo_connect.types.historical_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> HistoricalMetrics:
    import capo_connect.types.historical_metric

    out: HistoricalMetrics = []
    for item in data:
        out.append(capo_connect.types.historical_metric.deserialize_json(item))
    return out
