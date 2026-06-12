"""Generated from Smithy shape ``com.amazonaws.networkmonitor#GetMonitorInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmonitor.types.resource_name


class GetMonitorInput(TypedDict):
    monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor that details are returned for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMonitorInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMonitorInput:
    out: GetMonitorInput = {}  # type: ignore[typeddict-item]
    return out
