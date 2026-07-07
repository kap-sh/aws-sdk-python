"""Generated from Smithy shape ``com.amazonaws.internetmonitor#CreateMonitorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_internetmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_internetmonitor.types.monitor_arn
    import aws_sdk_internetmonitor.types.monitor_config_state


class CreateMonitorOutput(TypedDict, closed=True):
    arn: "aws_sdk_internetmonitor.types.monitor_arn.MonitorArn"
    """<p>The Amazon Resource Name (ARN) of the monitor.</p>"""
    status: "aws_sdk_internetmonitor.types.monitor_config_state.MonitorConfigState"
    """<p>The status of a monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMonitorOutput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> CreateMonitorOutput:
    out: CreateMonitorOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("CreateMonitorOutput.arn required")
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("CreateMonitorOutput.status required")
    return out
