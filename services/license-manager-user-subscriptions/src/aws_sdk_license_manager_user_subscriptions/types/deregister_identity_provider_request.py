"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#DeregisterIdentityProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.arn
    import aws_sdk_license_manager_user_subscriptions.types.identity_provider

class DeregisterIdentityProviderRequest(TypedDict):
    identity_provider: NotRequired["aws_sdk_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"]
    """<p>An object that specifies details for the Active Directory identity provider.</p>"""
    product: NotRequired["str"]
    """<p>The name of the user-based subscription product.</p> <p>Valid values: <code>VISUAL_STUDIO_ENTERPRISE</code> | <code>VISUAL_STUDIO_PROFESSIONAL</code> | <code>OFFICE_PROFESSIONAL_PLUS</code> | <code>REMOTE_DESKTOP_SERVICES</code> </p>"""
    identity_provider_arn: NotRequired["aws_sdk_license_manager_user_subscriptions.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that identifies the identity provider to deregister.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeregisterIdentityProviderRequest) -> dict:
    out: dict = {}
    if "identity_provider" in value:
        import aws_sdk_license_manager_user_subscriptions.types.identity_provider
        out["IdentityProvider"] = aws_sdk_license_manager_user_subscriptions.types.identity_provider.serialize_json(value["identity_provider"])
    if "product" in value:
        out["Product"] = value["product"]
    if "identity_provider_arn" in value:
        out["IdentityProviderArn"] = value["identity_provider_arn"]
    return out


def deserialize_json(data: dict) -> DeregisterIdentityProviderRequest:
    out: DeregisterIdentityProviderRequest = {}  # type: ignore[typeddict-item]
    if "IdentityProvider" in data:
        import aws_sdk_license_manager_user_subscriptions.types.identity_provider
        out["identity_provider"] = aws_sdk_license_manager_user_subscriptions.types.identity_provider.deserialize_json(data["IdentityProvider"])
    if "Product" in data:
        out["product"] = data["Product"]
    if "IdentityProviderArn" in data:
        out["identity_provider_arn"] = data["IdentityProviderArn"]
    return out