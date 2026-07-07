"""Generated from Smithy shape ``com.amazonaws.connect#CurrentMetricData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.current_metric
    import aws_sdk_connect.types.value


class CurrentMetricData(TypedDict, closed=True):
    metric: NotRequired["aws_sdk_connect.types.current_metric.CurrentMetric"]
    """<p>Information about the metric.</p>"""
    value: NotRequired["aws_sdk_connect.types.value.Value"]
    """<p>The value of the metric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CurrentMetricData) -> dict:
    out: dict = {}
    if "metric" in value:
        import aws_sdk_connect.types.current_metric

        out["Metric"] = aws_sdk_connect.types.current_metric.serialize_json(
            value["metric"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> CurrentMetricData:
    out: CurrentMetricData = {}  # type: ignore[typeddict-item]
    if "Metric" in data:
        import aws_sdk_connect.types.current_metric

        out["metric"] = aws_sdk_connect.types.current_metric.deserialize_json(
            data["Metric"]
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
