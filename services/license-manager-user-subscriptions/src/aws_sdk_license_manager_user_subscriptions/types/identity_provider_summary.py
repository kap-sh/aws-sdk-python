"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#IdentityProviderSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_license_manager_user_subscriptions.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.arn
    import aws_sdk_license_manager_user_subscriptions.types.identity_provider
    import aws_sdk_license_manager_user_subscriptions.types.settings

class IdentityProviderSummary(TypedDict):
    identity_provider: "aws_sdk_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
    """<p>The <code>IdentityProvider</code> resource contains information about an identity provider.</p>"""
    settings: "aws_sdk_license_manager_user_subscriptions.types.settings.Settings"
    """<p>The <code>Settings</code> resource contains details about the registered identity provider’s product related configuration settings, such as the subnets to provision VPC endpoints.</p>"""
    product: "str"
    """<p>The name of the user-based subscription product.</p>"""
    status: "str"
    """<p>The status of the identity provider.</p>"""
    identity_provider_arn: NotRequired["aws_sdk_license_manager_user_subscriptions.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the identity provider.</p>"""
    failure_message: NotRequired["str"]
    """<p>The failure message associated with an identity provider.</p>"""
    owner_account_id: NotRequired["str"]
    """<p>The AWS Account ID of the owner of this resource.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: IdentityProviderSummary) -> dict:
    out: dict = {}
    import aws_sdk_license_manager_user_subscriptions.types.identity_provider
    out["IdentityProvider"] = aws_sdk_license_manager_user_subscriptions.types.identity_provider.serialize_json(value["identity_provider"])
    import aws_sdk_license_manager_user_subscriptions.types.settings
    out["Settings"] = aws_sdk_license_manager_user_subscriptions.types.settings.serialize_json(value["settings"])
    out["Product"] = value["product"]
    out["Status"] = value["status"]
    if "identity_provider_arn" in value:
        out["IdentityProviderArn"] = value["identity_provider_arn"]
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    return out


def deserialize_json(data: dict) -> IdentityProviderSummary:
    out: IdentityProviderSummary = {}  # type: ignore[typeddict-item]
    if "IdentityProvider" in data:
        import aws_sdk_license_manager_user_subscriptions.types.identity_provider
        out["identity_provider"] = aws_sdk_license_manager_user_subscriptions.types.identity_provider.deserialize_json(data["IdentityProvider"])
    else:
        raise DeserializationError("IdentityProviderSummary.identity_provider required")
    if "Settings" in data:
        import aws_sdk_license_manager_user_subscriptions.types.settings
        out["settings"] = aws_sdk_license_manager_user_subscriptions.types.settings.deserialize_json(data["Settings"])
    else:
        raise DeserializationError("IdentityProviderSummary.settings required")
    if "Product" in data:
        out["product"] = data["Product"]
    else:
        raise DeserializationError("IdentityProviderSummary.product required")
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("IdentityProviderSummary.status required")
    if "IdentityProviderArn" in data:
        out["identity_provider_arn"] = data["IdentityProviderArn"]
    if "FailureMessage" in data:
        out["failure_message"] = data["FailureMessage"]
    if "OwnerAccountId" in data:
        out["owner_account_id"] = data["OwnerAccountId"]
    return out