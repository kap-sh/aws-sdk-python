"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#RunInstancesMonitoringEnabled``."""

from typing import TypedDict

from typing_extensions import NotRequired


class RunInstancesMonitoringEnabled(TypedDict):
    enabled: NotRequired["bool"]
    """<p>Enables or disables detailed instance monitoring.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RunInstancesMonitoringEnabled) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RunInstancesMonitoringEnabled:
    out: RunInstancesMonitoringEnabled = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
