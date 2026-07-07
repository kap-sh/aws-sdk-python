"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#SimulationClock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.clock_status
    import aws_sdk_simspaceweaver.types.clock_target_status


class SimulationClock(TypedDict, closed=True):
    status: NotRequired["aws_sdk_simspaceweaver.types.clock_status.ClockStatus"]
    """<p>The current status of the simulation clock.</p>"""
    target_status: NotRequired[
        "aws_sdk_simspaceweaver.types.clock_target_status.ClockTargetStatus"
    ]
    """<p>The desired status of the simulation clock.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SimulationClock) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    if "target_status" in value:
        out["TargetStatus"] = value["target_status"]
    return out


def deserialize_json(data: dict) -> SimulationClock:
    out: SimulationClock = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    if "TargetStatus" in data:
        out["target_status"] = data["TargetStatus"]
    return out
