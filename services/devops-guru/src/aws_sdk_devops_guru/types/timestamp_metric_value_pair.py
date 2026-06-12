"""Generated from Smithy shape ``com.amazonaws.devopsguru#TimestampMetricValuePair``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.metric_value
    import aws_sdk_devops_guru.types.timestamp


class TimestampMetricValuePair(TypedDict):
    timestamp: NotRequired["aws_sdk_devops_guru.types.timestamp.Timestamp"]
    """<p>A <code>Timestamp</code> that specifies the time the event occurred. </p>"""
    metric_value: NotRequired["aws_sdk_devops_guru.types.metric_value.MetricValue"]
    """<p>Value of the anomalous metric data point at respective Timestamp.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimestampMetricValuePair) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import aws_sdk_devops_guru.types.timestamp

        out["Timestamp"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
            value["timestamp"]
        )
    if "metric_value" in value:
        out["MetricValue"] = value["metric_value"]
    return out


def deserialize_json(data: dict) -> TimestampMetricValuePair:
    out: TimestampMetricValuePair = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["timestamp"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["Timestamp"]
        )
    if "MetricValue" in data:
        out["metric_value"] = data["MetricValue"]
    return out
