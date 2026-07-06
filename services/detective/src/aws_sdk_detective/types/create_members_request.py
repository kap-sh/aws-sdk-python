"""Generated from Smithy shape ``com.amazonaws.detective#CreateMembersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_detective.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_detective.types.account_list
    import aws_sdk_detective.types.boolean
    import aws_sdk_detective.types.email_message
    import aws_sdk_detective.types.graph_arn


class CreateMembersRequest(TypedDict, closed=True):
    graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph.</p>"""
    message: NotRequired["aws_sdk_detective.types.email_message.EmailMessage"]
    """<p>Customized message text to include in the invitation email message to the invited member accounts.</p>"""
    disable_email_notification: "aws_sdk_detective.types.boolean.Boolean"
    """<p>if set to <code>true</code>, then the invited accounts do not receive email notifications. By default, this is set to <code>false</code>, and the invited accounts receive email notifications.</p> <p>Organization accounts in the organization behavior graph do not receive email notifications.</p>"""
    accounts: "aws_sdk_detective.types.account_list.AccountList"
    """<p>The list of Amazon Web Services accounts to invite or to enable. You can invite or enable up to 50 accounts at a time. For each invited account, the account list contains the account identifier and the Amazon Web Services account root user email address. For organization accounts in the organization behavior graph, the email address is not required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMembersRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    if "message" in value:
        out["Message"] = value["message"]
    out["DisableEmailNotification"] = value.get("disable_email_notification", False)
    import aws_sdk_detective.types.account_list

    out["Accounts"] = aws_sdk_detective.types.account_list.serialize_json(
        value["accounts"]
    )
    return out


def deserialize_json(data: dict) -> CreateMembersRequest:
    out: CreateMembersRequest = {}  # type: ignore[typeddict-item]
    if "GraphArn" in data:
        out["graph_arn"] = data["GraphArn"]
    else:
        raise DeserializationError("CreateMembersRequest.graph_arn required")
    if "Message" in data:
        out["message"] = data["Message"]
    if "DisableEmailNotification" in data:
        out["disable_email_notification"] = data["DisableEmailNotification"]
    else:
        out["disable_email_notification"] = False
    if "Accounts" in data:
        import aws_sdk_detective.types.account_list

        out["accounts"] = aws_sdk_detective.types.account_list.deserialize_json(
            data["Accounts"]
        )
    else:
        raise DeserializationError("CreateMembersRequest.accounts required")
    return out
