"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetMonitorInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.resource_name


class GetMonitorInput(TypedDict):
    monitor_name: "aws_sdk_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMonitorInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMonitorInput:
    out: GetMonitorInput = {}  # type: ignore[typeddict-item]
    return out
