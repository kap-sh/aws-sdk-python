"""Generated from Smithy shape ``com.amazonaws.securityhub#Invitation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.account_id
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.timestamp


class Invitation(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_securityhub.types.account_id.AccountId"]
    """<p>The account ID of the Security Hub CSPM administrator account that the invitation was sent from.</p>"""
    invitation_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the invitation sent to the member account.</p>"""
    invited_at: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    """<p>The timestamp of when the invitation was sent.</p>"""
    member_status: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The current status of the association between the member and administrator accounts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Invitation) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "invitation_id" in value:
        out["InvitationId"] = value["invitation_id"]
    if "invited_at" in value:
        import aws_sdk_securityhub.types.timestamp

        out["InvitedAt"] = aws_sdk_securityhub.types.timestamp.serialize_json(
            value["invited_at"]
        )
    if "member_status" in value:
        out["MemberStatus"] = value["member_status"]
    return out


def deserialize_json(data: dict) -> Invitation:
    out: Invitation = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "InvitationId" in data:
        out["invitation_id"] = data["InvitationId"]
    if "InvitedAt" in data:
        import aws_sdk_securityhub.types.timestamp

        out["invited_at"] = aws_sdk_securityhub.types.timestamp.deserialize_json(
            data["InvitedAt"]
        )
    if "MemberStatus" in data:
        out["member_status"] = data["MemberStatus"]
    return out
