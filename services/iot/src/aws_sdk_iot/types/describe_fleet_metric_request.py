"""Generated from Smithy shape ``com.amazonaws.iot#DescribeFleetMetricRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.fleet_metric_name


class DescribeFleetMetricRequest(TypedDict):
    metric_name: "aws_sdk_iot.types.fleet_metric_name.FleetMetricName"
    """<p>The name of the fleet metric to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFleetMetricRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeFleetMetricRequest:
    out: DescribeFleetMetricRequest = {}  # type: ignore[typeddict-item]
    return out
