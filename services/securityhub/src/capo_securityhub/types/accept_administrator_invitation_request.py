"""Generated from Smithy shape ``com.amazonaws.securityhub#AcceptAdministratorInvitationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AcceptAdministratorInvitationRequest(TypedDict, closed=True):
    administrator_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The account ID of the Security Hub CSPM administrator account that sent the invitation.</p>"""
    invitation_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the invitation sent from the Security Hub CSPM administrator account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptAdministratorInvitationRequest) -> dict:
    out: dict = {}
    if "administrator_id" in value:
        out["AdministratorId"] = value["administrator_id"]
    if "invitation_id" in value:
        out["InvitationId"] = value["invitation_id"]
    return out


def deserialize_json(data: dict) -> AcceptAdministratorInvitationRequest:
    out: AcceptAdministratorInvitationRequest = {}  # type: ignore[typeddict-item]
    if "AdministratorId" in data:
        out["administrator_id"] = data["AdministratorId"]
    if "InvitationId" in data:
        out["invitation_id"] = data["InvitationId"]
    return out
