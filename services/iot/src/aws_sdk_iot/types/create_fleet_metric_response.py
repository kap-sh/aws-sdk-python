"""Generated from Smithy shape ``com.amazonaws.iot#CreateFleetMetricResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.fleet_metric_arn
    import aws_sdk_iot.types.fleet_metric_name


class CreateFleetMetricResponse(TypedDict):
    metric_name: NotRequired["aws_sdk_iot.types.fleet_metric_name.FleetMetricName"]
    """<p>The name of the fleet metric to create.</p>"""
    metric_arn: NotRequired["aws_sdk_iot.types.fleet_metric_arn.FleetMetricArn"]
    """<p>The Amazon Resource Name (ARN) of the new fleet metric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFleetMetricResponse) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["metricName"] = value["metric_name"]
    if "metric_arn" in value:
        out["metricArn"] = value["metric_arn"]
    return out


def deserialize_json(data: dict) -> CreateFleetMetricResponse:
    out: CreateFleetMetricResponse = {}  # type: ignore[typeddict-item]
    if "metricName" in data:
        out["metric_name"] = data["metricName"]
    if "metricArn" in data:
        out["metric_arn"] = data["metricArn"]
    return out
