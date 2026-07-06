"""Generated from Smithy shape ``com.amazonaws.deadline#DisassociateMemberFromFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.identity_center_principal_id


class DisassociateMemberFromFleetRequest(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the fleet to disassociate a member from.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID of the fleet to from which to disassociate a member.</p>"""
    principal_id: (
        "aws_sdk_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
    )
    """<p>A member's principal ID to disassociate from a fleet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateMemberFromFleetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateMemberFromFleetRequest:
    out: DisassociateMemberFromFleetRequest = {}  # type: ignore[typeddict-item]
    return out
