"""Generated from Smithy shape ``com.amazonaws.iot#MetricToRetain``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.behavior_metric
    import aws_sdk_iot.types.export_metric
    import aws_sdk_iot.types.metric_dimension


class MetricToRetain(TypedDict, closed=True):
    metric: "aws_sdk_iot.types.behavior_metric.BehaviorMetric"
    """<p>What is measured by the behavior.</p>"""
    metric_dimension: NotRequired["aws_sdk_iot.types.metric_dimension.MetricDimension"]
    """<p>The dimension of a metric. This can't be used with custom metrics.</p>"""
    export_metric: NotRequired["aws_sdk_iot.types.export_metric.ExportMetric"]
    """<p>The value indicates exporting metrics related to the <code>MetricToRetain </code> when it's true.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricToRetain) -> dict:
    out: dict = {}
    out["metric"] = value["metric"]
    if "metric_dimension" in value:
        import aws_sdk_iot.types.metric_dimension

        out["metricDimension"] = aws_sdk_iot.types.metric_dimension.serialize_json(
            value["metric_dimension"]
        )
    if "export_metric" in value:
        out["exportMetric"] = value["export_metric"]
    return out


def deserialize_json(data: dict) -> MetricToRetain:
    out: MetricToRetain = {}  # type: ignore[typeddict-item]
    if "metric" in data:
        out["metric"] = data["metric"]
    else:
        raise DeserializationError("MetricToRetain.metric required")
    if "metricDimension" in data:
        import aws_sdk_iot.types.metric_dimension

        out["metric_dimension"] = aws_sdk_iot.types.metric_dimension.deserialize_json(
            data["metricDimension"]
        )
    if "exportMetric" in data:
        out["export_metric"] = data["exportMetric"]
    return out
