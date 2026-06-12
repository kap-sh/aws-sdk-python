"""Generated from Smithy shape ``com.amazonaws.securityhub#Member``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.account_id
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.timestamp


class Member(TypedDict):
    account_id: NotRequired["aws_sdk_securityhub.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID of the member account.</p>"""
    email: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The email address of the member account.</p>"""
    master_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>This is replaced by <code>AdministratorID</code>.</p> <p>The Amazon Web Services account ID of the Security Hub CSPM administrator account associated with this member account.</p>"""
    administrator_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Web Services account ID of the Security Hub CSPM administrator account associated with this member account.</p>"""
    member_status: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of the relationship between the member account and its administrator account. </p> <p>The status can have one of the following values:</p> <ul> <li> <p> <code>Created</code> - Indicates that the administrator account added the member account, but has not yet invited the member account.</p> </li> <li> <p> <code>Invited</code> - Indicates that the administrator account invited the member account. The member account has not yet responded to the invitation.</p> </li> <li> <p> <code>Enabled</code> - Indicates that the member account is currently active. For manually invited member accounts, indicates that the member account accepted the invitation.</p> </li> <li> <p> <code>Removed</code> - Indicates that the administrator account disassociated the member account.</p> </li> <li> <p> <code>Resigned</code> - Indicates that the member account disassociated themselves from the administrator account.</p> </li> <li> <p> <code>Deleted</code> - Indicates that the administrator account deleted the member account.</p> </li> <li> <p> <code>AccountSuspended</code> - Indicates that an organization account was suspended from Amazon Web Services at the same time that the administrator account tried to enable the organization account as a member account.</p> </li> </ul>"""
    invited_at: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    """<p>A timestamp for the date and time when the invitation was sent to the member account.</p>"""
    updated_at: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    """<p>The timestamp for the date and time when the member account was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Member) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "email" in value:
        out["Email"] = value["email"]
    if "master_id" in value:
        out["MasterId"] = value["master_id"]
    if "administrator_id" in value:
        out["AdministratorId"] = value["administrator_id"]
    if "member_status" in value:
        out["MemberStatus"] = value["member_status"]
    if "invited_at" in value:
        import aws_sdk_securityhub.types.timestamp

        out["InvitedAt"] = aws_sdk_securityhub.types.timestamp.serialize_json(
            value["invited_at"]
        )
    if "updated_at" in value:
        import aws_sdk_securityhub.types.timestamp

        out["UpdatedAt"] = aws_sdk_securityhub.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> Member:
    out: Member = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "Email" in data:
        out["email"] = data["Email"]
    if "MasterId" in data:
        out["master_id"] = data["MasterId"]
    if "AdministratorId" in data:
        out["administrator_id"] = data["AdministratorId"]
    if "MemberStatus" in data:
        out["member_status"] = data["MemberStatus"]
    if "InvitedAt" in data:
        import aws_sdk_securityhub.types.timestamp

        out["invited_at"] = aws_sdk_securityhub.types.timestamp.deserialize_json(
            data["InvitedAt"]
        )
    if "UpdatedAt" in data:
        import aws_sdk_securityhub.types.timestamp

        out["updated_at"] = aws_sdk_securityhub.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    return out
