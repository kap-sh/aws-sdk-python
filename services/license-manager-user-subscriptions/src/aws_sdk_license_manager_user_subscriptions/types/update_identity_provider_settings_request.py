"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#UpdateIdentityProviderSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.arn
    import aws_sdk_license_manager_user_subscriptions.types.identity_provider
    import aws_sdk_license_manager_user_subscriptions.types.update_settings


class UpdateIdentityProviderSettingsRequest(TypedDict):
    identity_provider: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
    ]
    product: NotRequired["str"]
    """<p>The name of the user-based subscription product.</p> <p>Valid values: <code>VISUAL_STUDIO_ENTERPRISE</code> | <code>VISUAL_STUDIO_PROFESSIONAL</code> | <code>OFFICE_PROFESSIONAL_PLUS</code> | <code>REMOTE_DESKTOP_SERVICES</code> </p>"""
    identity_provider_arn: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.arn.Arn"
    ]
    """<p>The Amazon Resource Name (ARN) of the identity provider to update.</p>"""
    update_settings: "aws_sdk_license_manager_user_subscriptions.types.update_settings.UpdateSettings"
    """<p>Updates the registered identity provider’s product related configuration settings. You can update any combination of settings in a single operation such as the:</p> <ul> <li> <p>Subnets which you want to add to provision VPC endpoints.</p> </li> <li> <p>Subnets which you want to remove the VPC endpoints from.</p> </li> <li> <p>Security group ID which permits traffic to the VPC endpoints.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIdentityProviderSettingsRequest) -> dict:
    out: dict = {}
    if "identity_provider" in value:
        import aws_sdk_license_manager_user_subscriptions.types.identity_provider

        out["IdentityProvider"] = (
            aws_sdk_license_manager_user_subscriptions.types.identity_provider.serialize_json(
                value["identity_provider"]
            )
        )
    if "product" in value:
        out["Product"] = value["product"]
    if "identity_provider_arn" in value:
        out["IdentityProviderArn"] = value["identity_provider_arn"]
    import aws_sdk_license_manager_user_subscriptions.types.update_settings

    out["UpdateSettings"] = (
        aws_sdk_license_manager_user_subscriptions.types.update_settings.serialize_json(
            value["update_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateIdentityProviderSettingsRequest:
    out: UpdateIdentityProviderSettingsRequest = {}  # type: ignore[typeddict-item]
    if "IdentityProvider" in data:
        import aws_sdk_license_manager_user_subscriptions.types.identity_provider

        out["identity_provider"] = (
            aws_sdk_license_manager_user_subscriptions.types.identity_provider.deserialize_json(
                data["IdentityProvider"]
            )
        )
    if "Product" in data:
        out["product"] = data["Product"]
    if "IdentityProviderArn" in data:
        out["identity_provider_arn"] = data["IdentityProviderArn"]
    if "UpdateSettings" in data:
        import aws_sdk_license_manager_user_subscriptions.types.update_settings

        out["update_settings"] = (
            aws_sdk_license_manager_user_subscriptions.types.update_settings.deserialize_json(
                data["UpdateSettings"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateIdentityProviderSettingsRequest.update_settings required"
        )
    return out
