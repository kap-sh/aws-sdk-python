"""Generated from Smithy shape ``com.amazonaws.guardduty#Member``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_id
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.email
    import capo_guardduty.types.string


class Member(TypedDict, closed=True):
    account_id: NotRequired["capo_guardduty.types.account_id.AccountId"]
    """<p>The ID of the member account.</p>"""
    detector_id: NotRequired["capo_guardduty.types.detector_id.DetectorId"]
    """<p>The detector ID of the member account.</p>"""
    master_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The administrator account ID.</p>"""
    email: NotRequired["capo_guardduty.types.email.Email"]
    """<p>The email address of the member account.</p>"""
    relationship_status: NotRequired["capo_guardduty.types.string.String"]
    """<p>The status of the relationship between the member and the administrator.</p>"""
    invited_at: NotRequired["capo_guardduty.types.string.String"]
    """<p>The timestamp when the invitation was sent.</p>"""
    updated_at: NotRequired["capo_guardduty.types.string.String"]
    """<p>The last-updated timestamp of the member.</p>"""
    administrator_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The administrator account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Member) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "master_id" in value:
        out["masterId"] = value["master_id"]
    if "email" in value:
        out["email"] = value["email"]
    if "relationship_status" in value:
        out["relationshipStatus"] = value["relationship_status"]
    if "invited_at" in value:
        out["invitedAt"] = value["invited_at"]
    if "updated_at" in value:
        out["updatedAt"] = value["updated_at"]
    if "administrator_id" in value:
        out["administratorId"] = value["administrator_id"]
    return out


def deserialize_json(data: dict) -> Member:
    out: Member = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    if "masterId" in data:
        out["master_id"] = data["masterId"]
    if "email" in data:
        out["email"] = data["email"]
    if "relationshipStatus" in data:
        out["relationship_status"] = data["relationshipStatus"]
    if "invitedAt" in data:
        out["invited_at"] = data["invitedAt"]
    if "updatedAt" in data:
        out["updated_at"] = data["updatedAt"]
    if "administratorId" in data:
        out["administrator_id"] = data["administratorId"]
    return out
