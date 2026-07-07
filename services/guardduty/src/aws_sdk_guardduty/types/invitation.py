"""Generated from Smithy shape ``com.amazonaws.guardduty#Invitation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.account_id
    import aws_sdk_guardduty.types.string


class Invitation(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_guardduty.types.account_id.AccountId"]
    """<p>The ID of the account that the invitation was sent from.</p>"""
    invitation_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The ID of the invitation. This value is used to validate the inviter account to the member account.</p>"""
    relationship_status: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The status of the relationship between the inviter and invitee accounts.</p>"""
    invited_at: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The timestamp when the invitation was sent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Invitation) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "invitation_id" in value:
        out["invitationId"] = value["invitation_id"]
    if "relationship_status" in value:
        out["relationshipStatus"] = value["relationship_status"]
    if "invited_at" in value:
        out["invitedAt"] = value["invited_at"]
    return out


def deserialize_json(data: dict) -> Invitation:
    out: Invitation = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "invitationId" in data:
        out["invitation_id"] = data["invitationId"]
    if "relationshipStatus" in data:
        out["relationship_status"] = data["relationshipStatus"]
    if "invitedAt" in data:
        out["invited_at"] = data["invitedAt"]
    return out
