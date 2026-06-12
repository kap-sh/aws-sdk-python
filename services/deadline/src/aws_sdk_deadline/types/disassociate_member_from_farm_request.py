"""Generated from Smithy shape ``com.amazonaws.deadline#DisassociateMemberFromFarmRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.identity_center_principal_id


class DisassociateMemberFromFarmRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm to disassociate from the member.</p>"""
    principal_id: (
        "aws_sdk_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
    )
    """<p>A member's principal ID to disassociate from a farm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateMemberFromFarmRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateMemberFromFarmRequest:
    out: DisassociateMemberFromFarmRequest = {}  # type: ignore[typeddict-item]
    return out
