"""Generated from Smithy shape ``com.amazonaws.costexplorer#UpdateAnomalyMonitorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string


class UpdateAnomalyMonitorRequest(TypedDict, closed=True):
    monitor_arn: "aws_sdk_cost_explorer.types.generic_string.GenericString"
    """<p>Cost anomaly monitor Amazon Resource Names (ARNs). </p>"""
    monitor_name: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The new name for the cost anomaly monitor. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAnomalyMonitorRequest) -> dict:
    out: dict = {}
    out["MonitorArn"] = value["monitor_arn"]
    if "monitor_name" in value:
        out["MonitorName"] = value["monitor_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAnomalyMonitorRequest:
    out: UpdateAnomalyMonitorRequest = {}  # type: ignore[typeddict-item]
    if "MonitorArn" in data:
        out["monitor_arn"] = data["MonitorArn"]
    else:
        raise DeserializationError("UpdateAnomalyMonitorRequest.monitor_arn required")
    if "MonitorName" in data:
        out["monitor_name"] = data["MonitorName"]
    return out
