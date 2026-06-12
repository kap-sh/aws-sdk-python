"""Generated from Smithy shape ``com.amazonaws.workmail#UpdateMailboxQuotaRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.entity_identifier
    import aws_sdk_workmail.types.mailbox_quota
    import aws_sdk_workmail.types.organization_id


class UpdateMailboxQuotaRequest(TypedDict):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization that contains the user for whom to update the mailbox quota.</p>"""
    user_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifer for the user for whom to update the mailbox quota.</p> <p>The identifier can be the <i>UserId</i>, <i>Username</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>User ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: user@domain.tld</p> </li> <li> <p>User name: user</p> </li> </ul>"""
    mailbox_quota: "aws_sdk_workmail.types.mailbox_quota.MailboxQuota"
    """<p>The updated mailbox quota, in MB, for the specified user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMailboxQuotaRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["UserId"] = value["user_id"]
    out["MailboxQuota"] = value["mailbox_quota"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMailboxQuotaRequest:
    out: UpdateMailboxQuotaRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("UpdateMailboxQuotaRequest.organization_id required")
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("UpdateMailboxQuotaRequest.user_id required")
    if "MailboxQuota" in data:
        out["mailbox_quota"] = data["MailboxQuota"]
    else:
        raise DeserializationError("UpdateMailboxQuotaRequest.mailbox_quota required")
    return out
