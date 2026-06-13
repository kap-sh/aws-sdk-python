"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#DeleteMonitorInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.resource_name


class DeleteMonitorInput(TypedDict):
    monitor_name: "aws_sdk_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMonitorInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMonitorInput:
    out: DeleteMonitorInput = {}  # type: ignore[typeddict-item]
    return out
