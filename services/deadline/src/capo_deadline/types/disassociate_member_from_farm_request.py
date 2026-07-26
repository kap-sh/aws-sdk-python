"""Generated from Smithy shape ``com.amazonaws.deadline#DisassociateMemberFromFarmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.identity_center_principal_id


class DisassociateMemberFromFarmRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm to disassociate from the member.</p>"""
    principal_id: (
        "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
    )
    """<p>A member's principal ID to disassociate from a farm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateMemberFromFarmRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateMemberFromFarmRequest:
    out: DisassociateMemberFromFarmRequest = {}  # type: ignore[typeddict-item]
    return out
