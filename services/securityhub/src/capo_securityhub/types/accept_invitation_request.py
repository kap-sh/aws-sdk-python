"""Generated from Smithy shape ``com.amazonaws.securityhub#AcceptInvitationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AcceptInvitationRequest(TypedDict, closed=True):
    master_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The account ID of the Security Hub CSPM administrator account that sent the invitation.</p>"""
    invitation_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the invitation sent from the Security Hub CSPM administrator account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptInvitationRequest) -> dict:
    out: dict = {}
    if "master_id" in value:
        out["MasterId"] = value["master_id"]
    if "invitation_id" in value:
        out["InvitationId"] = value["invitation_id"]
    return out


def deserialize_json(data: dict) -> AcceptInvitationRequest:
    out: AcceptInvitationRequest = {}  # type: ignore[typeddict-item]
    if "MasterId" in data:
        out["master_id"] = data["MasterId"]
    if "InvitationId" in data:
        out["invitation_id"] = data["InvitationId"]
    return out
