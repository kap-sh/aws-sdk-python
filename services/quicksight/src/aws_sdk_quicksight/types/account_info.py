"""Generated from Smithy shape ``com.amazonaws.quicksight#AccountInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_quicksight.types.edition
    import aws_sdk_quicksight.types.string

class AccountInfo(TypedDict):
    account_name: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The account name that you provided for the Amazon Quick Sight subscription in your Amazon Web Services account. You create this name when you sign up for Quick. It's unique over all of Amazon Web Services, and it appears only when users sign in.</p>"""
    edition: NotRequired["aws_sdk_quicksight.types.edition.Edition"]
    """<p>The edition of your Quick Sight account.</p>"""
    notification_email: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The email address that will be used for Quick Sight to send notifications regarding your Amazon Web Services account or Quick Sight subscription.</p>"""
    authentication_type: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The way that your Amazon Quick Sight account is authenticated.</p>"""
    account_subscription_status: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The status of your account subscription.</p>"""
    iam_identity_center_instance_arn: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the IAM Identity Center instance.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AccountInfo) -> dict:
    out: dict = {}
    if "account_name" in value:
        out["AccountName"] = value["account_name"]
    if "edition" in value:
        import aws_sdk_quicksight.types.edition
        out["Edition"] = aws_sdk_quicksight.types.edition.serialize_json(value["edition"])
    if "notification_email" in value:
        out["NotificationEmail"] = value["notification_email"]
    if "authentication_type" in value:
        out["AuthenticationType"] = value["authentication_type"]
    if "account_subscription_status" in value:
        out["AccountSubscriptionStatus"] = value["account_subscription_status"]
    if "iam_identity_center_instance_arn" in value:
        out["IAMIdentityCenterInstanceArn"] = value["iam_identity_center_instance_arn"]
    return out


def deserialize_json(data: dict) -> AccountInfo:
    out: AccountInfo = {}  # type: ignore[typeddict-item]
    if "AccountName" in data:
        out["account_name"] = data["AccountName"]
    if "Edition" in data:
        import aws_sdk_quicksight.types.edition
        out["edition"] = aws_sdk_quicksight.types.edition.deserialize_json(data["Edition"])
    if "NotificationEmail" in data:
        out["notification_email"] = data["NotificationEmail"]
    if "AuthenticationType" in data:
        out["authentication_type"] = data["AuthenticationType"]
    if "AccountSubscriptionStatus" in data:
        out["account_subscription_status"] = data["AccountSubscriptionStatus"]
    if "IAMIdentityCenterInstanceArn" in data:
        out["iam_identity_center_instance_arn"] = data["IAMIdentityCenterInstanceArn"]
    return out