"""Generated from Smithy shape ``com.amazonaws.guardduty#AcceptAdministratorInvitationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.string


class AcceptAdministratorInvitationRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector of the GuardDuty member account.</p>"""
    administrator_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The account ID of the GuardDuty administrator account whose invitation you're accepting.</p>"""
    invitation_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The value that is used to validate the administrator account to the member account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptAdministratorInvitationRequest) -> dict:
    out: dict = {}
    if "administrator_id" in value:
        out["administratorId"] = value["administrator_id"]
    if "invitation_id" in value:
        out["invitationId"] = value["invitation_id"]
    return out


def deserialize_json(data: dict) -> AcceptAdministratorInvitationRequest:
    out: AcceptAdministratorInvitationRequest = {}  # type: ignore[typeddict-item]
    if "administratorId" in data:
        out["administrator_id"] = data["administratorId"]
    if "invitationId" in data:
        out["invitation_id"] = data["invitationId"]
    return out
