"""Generated from Smithy shape ``com.amazonaws.networkmonitor#GetProbeInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmonitor.types.probe_id
    import aws_sdk_networkmonitor.types.resource_name


class GetProbeInput(TypedDict):
    monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor associated with the probe. Run <code>ListMonitors</code> to get a list of monitor names.</p>"""
    probe_id: "aws_sdk_networkmonitor.types.probe_id.ProbeId"
    """<p>The ID of the probe to get information about. Run <code>GetMonitor</code> action to get a list of probes and probe IDs for the monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProbeInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProbeInput:
    out: GetProbeInput = {}  # type: ignore[typeddict-item]
    return out
