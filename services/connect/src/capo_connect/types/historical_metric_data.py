"""Generated from Smithy shape ``com.amazonaws.connect#HistoricalMetricData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.historical_metric
    import capo_connect.types.value


class HistoricalMetricData(TypedDict, closed=True):
    metric: NotRequired["capo_connect.types.historical_metric.HistoricalMetric"]
    """<p>Information about the metric.</p>"""
    value: NotRequired["capo_connect.types.value.Value"]
    """<p>The value of the metric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HistoricalMetricData) -> dict:
    out: dict = {}
    if "metric" in value:
        import capo_connect.types.historical_metric

        out["Metric"] = capo_connect.types.historical_metric.serialize_json(
            value["metric"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> HistoricalMetricData:
    out: HistoricalMetricData = {}  # type: ignore[typeddict-item]
    if "Metric" in data:
        import capo_connect.types.historical_metric

        out["metric"] = capo_connect.types.historical_metric.deserialize_json(
            data["Metric"]
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
