"""Generated from Smithy shape ``com.amazonaws.forecast#MetricResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.double
    import capo_forecast.types.metric_name


class MetricResult(TypedDict, closed=True):
    metric_name: NotRequired["capo_forecast.types.metric_name.MetricName"]
    """<p>The name of the metric.</p>"""
    metric_value: NotRequired["capo_forecast.types.double.Double"]
    """<p>The value for the metric.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricResult) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "metric_value" in value:
        out["MetricValue"] = value["metric_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricResult:
    out: MetricResult = {}  # type: ignore[typeddict-item]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "MetricValue" in data:
        out["metric_value"] = data["MetricValue"]
    return out
