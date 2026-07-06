"""Generated from Smithy shape ``com.amazonaws.deadline#GetFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id


class GetFleetRequest(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm in the fleet.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID of the fleet to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFleetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFleetRequest:
    out: GetFleetRequest = {}  # type: ignore[typeddict-item]
    return out
