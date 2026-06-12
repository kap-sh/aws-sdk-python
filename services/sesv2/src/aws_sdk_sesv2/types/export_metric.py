"""Generated from Smithy shape ``com.amazonaws.sesv2#ExportMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.metric
    import aws_sdk_sesv2.types.metric_aggregation


class ExportMetric(TypedDict):
    name: NotRequired["aws_sdk_sesv2.types.metric.Metric"]
    aggregation: NotRequired["aws_sdk_sesv2.types.metric_aggregation.MetricAggregation"]


# --- restJson1 ser/de ---
def serialize_json(value: ExportMetric) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_sesv2.types.metric

        out["Name"] = aws_sdk_sesv2.types.metric.serialize_json(value["name"])
    if "aggregation" in value:
        import aws_sdk_sesv2.types.metric_aggregation

        out["Aggregation"] = aws_sdk_sesv2.types.metric_aggregation.serialize_json(
            value["aggregation"]
        )
    return out


def deserialize_json(data: dict) -> ExportMetric:
    out: ExportMetric = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_sesv2.types.metric

        out["name"] = aws_sdk_sesv2.types.metric.deserialize_json(data["Name"])
    if "Aggregation" in data:
        import aws_sdk_sesv2.types.metric_aggregation

        out["aggregation"] = aws_sdk_sesv2.types.metric_aggregation.deserialize_json(
            data["Aggregation"]
        )
    return out
