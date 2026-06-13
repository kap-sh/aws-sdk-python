"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_networkflowmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.monitor_arn
    import aws_sdk_networkflowmonitor.types.monitor_status
    import aws_sdk_networkflowmonitor.types.resource_name


class MonitorSummary(TypedDict):
    monitor_arn: "aws_sdk_networkflowmonitor.types.monitor_arn.MonitorArn"
    """<p>The Amazon Resource Name (ARN) of the monitor.</p>"""
    monitor_name: "aws_sdk_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""
    monitor_status: "aws_sdk_networkflowmonitor.types.monitor_status.MonitorStatus"
    """<p>The status of a monitor. The status can be one of the following</p> <ul> <li> <p> <code>PENDING</code>: The monitor is in the process of being created.</p> </li> <li> <p> <code>ACTIVE</code>: The monitor is active.</p> </li> <li> <p> <code>INACTIVE</code>: The monitor is inactive.</p> </li> <li> <p> <code>ERROR</code>: Monitor creation failed due to an error.</p> </li> <li> <p> <code>DELETING</code>: The monitor is in the process of being deleted.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonitorSummary) -> dict:
    out: dict = {}
    out["monitorArn"] = value["monitor_arn"]
    out["monitorName"] = value["monitor_name"]
    import aws_sdk_networkflowmonitor.types.monitor_status

    out["monitorStatus"] = (
        aws_sdk_networkflowmonitor.types.monitor_status.serialize_json(
            value["monitor_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> MonitorSummary:
    out: MonitorSummary = {}  # type: ignore[typeddict-item]
    if "monitorArn" in data:
        out["monitor_arn"] = data["monitorArn"]
    else:
        raise DeserializationError("MonitorSummary.monitor_arn required")
    if "monitorName" in data:
        out["monitor_name"] = data["monitorName"]
    else:
        raise DeserializationError("MonitorSummary.monitor_name required")
    if "monitorStatus" in data:
        import aws_sdk_networkflowmonitor.types.monitor_status

        out["monitor_status"] = (
            aws_sdk_networkflowmonitor.types.monitor_status.deserialize_json(
                data["monitorStatus"]
            )
        )
    else:
        raise DeserializationError("MonitorSummary.monitor_status required")
    return out
