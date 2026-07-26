"""Generated from Smithy shape ``com.amazonaws.internetmonitor#UpdateMonitorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_internetmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_internetmonitor.types.monitor_arn
    import capo_internetmonitor.types.monitor_config_state


class UpdateMonitorOutput(TypedDict, closed=True):
    monitor_arn: "capo_internetmonitor.types.monitor_arn.MonitorArn"
    """<p>The Amazon Resource Name (ARN) of the monitor.</p>"""
    status: "capo_internetmonitor.types.monitor_config_state.MonitorConfigState"
    """<p>The status of a monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMonitorOutput) -> dict:
    out: dict = {}
    out["MonitorArn"] = value["monitor_arn"]
    out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> UpdateMonitorOutput:
    out: UpdateMonitorOutput = {}  # type: ignore[typeddict-item]
    if "MonitorArn" in data:
        out["monitor_arn"] = data["MonitorArn"]
    else:
        raise DeserializationError("UpdateMonitorOutput.monitor_arn required")
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("UpdateMonitorOutput.status required")
    return out
