"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAccountSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.namespace
    import aws_sdk_quicksight.types.string


class UpdateAccountSettingsRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that contains the Quick Sight settings that you want to list.</p>"""
    default_namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The default namespace for this Amazon Web Services account. Currently, the default is <code>default</code>. IAM users that register for the first time with Amazon Quick Sight provide an email address that becomes associated with the default namespace. </p>"""
    notification_email: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The email address that you want Quick Sight to send notifications to regarding your Amazon Web Services account or Quick Sight subscription.</p>"""
    termination_protection_enabled: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>A boolean value that determines whether or not an Quick Sight account can be deleted. A <code>True</code> value doesn't allow the account to be deleted and results in an error message if a user tries to make a <code>DeleteAccountSubscription</code> request. A <code>False</code> value will allow the account to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountSettingsRequest) -> dict:
    out: dict = {}
    out["DefaultNamespace"] = value["default_namespace"]
    if "notification_email" in value:
        out["NotificationEmail"] = value["notification_email"]
    out["TerminationProtectionEnabled"] = value.get(
        "termination_protection_enabled", False
    )
    return out


def deserialize_json(data: dict) -> UpdateAccountSettingsRequest:
    out: UpdateAccountSettingsRequest = {}  # type: ignore[typeddict-item]
    if "DefaultNamespace" in data:
        out["default_namespace"] = data["DefaultNamespace"]
    else:
        raise DeserializationError(
            "UpdateAccountSettingsRequest.default_namespace required"
        )
    if "NotificationEmail" in data:
        out["notification_email"] = data["NotificationEmail"]
    if "TerminationProtectionEnabled" in data:
        out["termination_protection_enabled"] = data["TerminationProtectionEnabled"]
    else:
        out["termination_protection_enabled"] = False
    return out
