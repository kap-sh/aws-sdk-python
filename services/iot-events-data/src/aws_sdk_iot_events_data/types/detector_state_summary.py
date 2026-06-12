"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#DetectorStateSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.state_name


class DetectorStateSummary(TypedDict):
    state_name: NotRequired["aws_sdk_iot_events_data.types.state_name.StateName"]
    """<p>The name of the state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectorStateSummary) -> dict:
    out: dict = {}
    if "state_name" in value:
        out["stateName"] = value["state_name"]
    return out


def deserialize_json(data: dict) -> DetectorStateSummary:
    out: DetectorStateSummary = {}  # type: ignore[typeddict-item]
    if "stateName" in data:
        out["state_name"] = data["stateName"]
    return out
