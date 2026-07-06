"""Generated from Smithy shape ``com.amazonaws.deadline#AssumeFleetRoleForReadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id


class AssumeFleetRoleForReadRequest(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID for the fleet's farm.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssumeFleetRoleForReadRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssumeFleetRoleForReadRequest:
    out: AssumeFleetRoleForReadRequest = {}  # type: ignore[typeddict-item]
    return out
