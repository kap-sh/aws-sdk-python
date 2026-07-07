"""Generated from Smithy shape ``com.amazonaws.networkmonitor#DeleteProbeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmonitor.types.probe_id
    import aws_sdk_networkmonitor.types.resource_name


class DeleteProbeInput(TypedDict, closed=True):
    monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor to delete. </p>"""
    probe_id: "aws_sdk_networkmonitor.types.probe_id.ProbeId"
    """<p>The ID of the probe to delete. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProbeInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProbeInput:
    out: DeleteProbeInput = {}  # type: ignore[typeddict-item]
    return out
