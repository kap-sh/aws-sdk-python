"""Generated from Smithy shape ``com.amazonaws.quicksight#AccountSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.edition
    import aws_sdk_quicksight.types.namespace
    import aws_sdk_quicksight.types.string


class AccountSettings(TypedDict):
    account_name: NotRequired["aws_sdk_quicksight.types.string.String"]
    r"""<p>The \"account name\" you provided for the Quick Sight subscription in your Amazon Web Services account. You create this name when you sign up for Quick Sight. It is unique in all of Amazon Web Services and it appears only when users sign in.</p>"""
    edition: NotRequired["aws_sdk_quicksight.types.edition.Edition"]
    """<p>The edition of Quick Sight that you're currently subscribed to: Enterprise edition or Standard edition.</p>"""
    default_namespace: NotRequired["aws_sdk_quicksight.types.namespace.Namespace"]
    """<p>The default Quick Sight namespace for your Amazon Web Services account. </p>"""
    notification_email: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The main notification email for your Quick Sight subscription.</p>"""
    public_sharing_enabled: "aws_sdk_quicksight.types.boolean.Boolean"
    r"""<p>A Boolean value that indicates whether public sharing is turned on for an Quick account. For more information about turning on public sharing, see <a href=\"https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdatePublicSharingSettings.html\">UpdatePublicSharingSettings</a>.</p>"""
    termination_protection_enabled: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>A boolean value that determines whether or not an Quick Sight account can be deleted. A <code>True</code> value doesn't allow the account to be deleted and results in an error message if a user tries to make a <code>DeleteAccountSubsctiption</code> request. A <code>False</code> value will allow the ccount to be deleted. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountSettings) -> dict:
    out: dict = {}
    if "account_name" in value:
        out["AccountName"] = value["account_name"]
    if "edition" in value:
        import aws_sdk_quicksight.types.edition

        out["Edition"] = aws_sdk_quicksight.types.edition.serialize_json(
            value["edition"]
        )
    if "default_namespace" in value:
        out["DefaultNamespace"] = value["default_namespace"]
    if "notification_email" in value:
        out["NotificationEmail"] = value["notification_email"]
    out["PublicSharingEnabled"] = value.get("public_sharing_enabled", False)
    out["TerminationProtectionEnabled"] = value.get(
        "termination_protection_enabled", False
    )
    return out


def deserialize_json(data: dict) -> AccountSettings:
    out: AccountSettings = {}  # type: ignore[typeddict-item]
    if "AccountName" in data:
        out["account_name"] = data["AccountName"]
    if "Edition" in data:
        import aws_sdk_quicksight.types.edition

        out["edition"] = aws_sdk_quicksight.types.edition.deserialize_json(
            data["Edition"]
        )
    if "DefaultNamespace" in data:
        out["default_namespace"] = data["DefaultNamespace"]
    if "NotificationEmail" in data:
        out["notification_email"] = data["NotificationEmail"]
    if "PublicSharingEnabled" in data:
        out["public_sharing_enabled"] = data["PublicSharingEnabled"]
    else:
        out["public_sharing_enabled"] = False
    if "TerminationProtectionEnabled" in data:
        out["termination_protection_enabled"] = data["TerminationProtectionEnabled"]
    else:
        out["termination_protection_enabled"] = False
    return out
