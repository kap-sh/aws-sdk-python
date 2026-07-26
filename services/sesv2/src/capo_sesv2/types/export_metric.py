"""Generated from Smithy shape ``com.amazonaws.sesv2#ExportMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.metric
    import capo_sesv2.types.metric_aggregation


class ExportMetric(TypedDict, closed=True):
    name: NotRequired["capo_sesv2.types.metric.Metric"]
    aggregation: NotRequired["capo_sesv2.types.metric_aggregation.MetricAggregation"]


# --- restJson1 ser/de ---
def serialize_json(value: ExportMetric) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_sesv2.types.metric

        out["Name"] = capo_sesv2.types.metric.serialize_json(value["name"])
    if "aggregation" in value:
        import capo_sesv2.types.metric_aggregation

        out["Aggregation"] = capo_sesv2.types.metric_aggregation.serialize_json(
            value["aggregation"]
        )
    return out


def deserialize_json(data: dict) -> ExportMetric:
    out: ExportMetric = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import capo_sesv2.types.metric

        out["name"] = capo_sesv2.types.metric.deserialize_json(data["Name"])
    if "Aggregation" in data:
        import capo_sesv2.types.metric_aggregation

        out["aggregation"] = capo_sesv2.types.metric_aggregation.deserialize_json(
            data["Aggregation"]
        )
    return out
