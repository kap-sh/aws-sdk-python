"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeMonitorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.arn


class DescribeMonitorRequest(TypedDict, closed=True):
    monitor_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the monitor resource to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMonitorRequest) -> dict:
    out: dict = {}
    out["MonitorArn"] = value["monitor_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMonitorRequest:
    out: DescribeMonitorRequest = {}  # type: ignore[typeddict-item]
    if "MonitorArn" in data:
        out["monitor_arn"] = data["MonitorArn"]
    else:
        raise DeserializationError("DescribeMonitorRequest.monitor_arn required")
    return out
