"""Generated from Smithy shape ``com.amazonaws.workmail#GetMailboxDetailsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.mailbox_quota
    import aws_sdk_workmail.types.mailbox_size


class GetMailboxDetailsResponse(TypedDict):
    mailbox_quota: NotRequired["aws_sdk_workmail.types.mailbox_quota.MailboxQuota"]
    """<p>The maximum allowed mailbox size, in MB, for the specified user.</p>"""
    mailbox_size: "aws_sdk_workmail.types.mailbox_size.MailboxSize"
    """<p>The current mailbox size, in MB, for the specified user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMailboxDetailsResponse) -> dict:
    out: dict = {}
    if "mailbox_quota" in value:
        out["MailboxQuota"] = value["mailbox_quota"]
    out["MailboxSize"] = value.get("mailbox_size", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMailboxDetailsResponse:
    out: GetMailboxDetailsResponse = {}  # type: ignore[typeddict-item]
    if "MailboxQuota" in data:
        out["mailbox_quota"] = data["MailboxQuota"]
    if "MailboxSize" in data:
        out["mailbox_size"] = data["MailboxSize"]
    else:
        out["mailbox_size"] = 0
    return out
