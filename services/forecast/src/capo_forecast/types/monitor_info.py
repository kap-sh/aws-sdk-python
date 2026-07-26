"""Generated from Smithy shape ``com.amazonaws.forecast#MonitorInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.status


class MonitorInfo(TypedDict, closed=True):
    monitor_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the monitor resource.</p>"""
    status: NotRequired["capo_forecast.types.status.Status"]
    """<p>The status of the monitor. States include:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>ACTIVE_STOPPING</code>, <code>ACTIVE_STOPPED</code> </p> </li> <li> <p> <code>UPDATE_IN_PROGRESS</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitorInfo) -> dict:
    out: dict = {}
    if "monitor_arn" in value:
        out["MonitorArn"] = value["monitor_arn"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitorInfo:
    out: MonitorInfo = {}  # type: ignore[typeddict-item]
    if "MonitorArn" in data:
        out["monitor_arn"] = data["MonitorArn"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
