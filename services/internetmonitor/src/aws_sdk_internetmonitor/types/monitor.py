"""Generated from Smithy shape ``com.amazonaws.internetmonitor#Monitor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_internetmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_internetmonitor.types.monitor_arn
    import aws_sdk_internetmonitor.types.monitor_config_state
    import aws_sdk_internetmonitor.types.monitor_processing_status_code
    import aws_sdk_internetmonitor.types.resource_name


class Monitor(TypedDict, closed=True):
    monitor_name: "aws_sdk_internetmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""
    monitor_arn: "aws_sdk_internetmonitor.types.monitor_arn.MonitorArn"
    """<p>The Amazon Resource Name (ARN) of the monitor.</p>"""
    status: "aws_sdk_internetmonitor.types.monitor_config_state.MonitorConfigState"
    """<p>The status of a monitor.</p>"""
    processing_status: NotRequired[
        "aws_sdk_internetmonitor.types.monitor_processing_status_code.MonitorProcessingStatusCode"
    ]
    """<p>The health of data processing for the monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Monitor) -> dict:
    out: dict = {}
    out["MonitorName"] = value["monitor_name"]
    out["MonitorArn"] = value["monitor_arn"]
    out["Status"] = value["status"]
    if "processing_status" in value:
        out["ProcessingStatus"] = value["processing_status"]
    return out


def deserialize_json(data: dict) -> Monitor:
    out: Monitor = {}  # type: ignore[typeddict-item]
    if "MonitorName" in data:
        out["monitor_name"] = data["MonitorName"]
    else:
        raise DeserializationError("Monitor.monitor_name required")
    if "MonitorArn" in data:
        out["monitor_arn"] = data["MonitorArn"]
    else:
        raise DeserializationError("Monitor.monitor_arn required")
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("Monitor.status required")
    if "ProcessingStatus" in data:
        out["processing_status"] = data["ProcessingStatus"]
    return out
