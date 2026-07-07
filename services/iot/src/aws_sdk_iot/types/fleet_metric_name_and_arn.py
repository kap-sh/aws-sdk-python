"""Generated from Smithy shape ``com.amazonaws.iot#FleetMetricNameAndArn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.fleet_metric_arn
    import aws_sdk_iot.types.fleet_metric_name


class FleetMetricNameAndArn(TypedDict, closed=True):
    metric_name: NotRequired["aws_sdk_iot.types.fleet_metric_name.FleetMetricName"]
    """<p>The fleet metric name.</p>"""
    metric_arn: NotRequired["aws_sdk_iot.types.fleet_metric_arn.FleetMetricArn"]
    """<p>The fleet metric ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FleetMetricNameAndArn) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["metricName"] = value["metric_name"]
    if "metric_arn" in value:
        out["metricArn"] = value["metric_arn"]
    return out


def deserialize_json(data: dict) -> FleetMetricNameAndArn:
    out: FleetMetricNameAndArn = {}  # type: ignore[typeddict-item]
    if "metricName" in data:
        out["metric_name"] = data["metricName"]
    if "metricArn" in data:
        out["metric_arn"] = data["metricArn"]
    return out
