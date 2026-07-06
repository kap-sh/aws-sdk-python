"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#RegisterIdentityProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.identity_provider
    import aws_sdk_license_manager_user_subscriptions.types.settings
    import aws_sdk_license_manager_user_subscriptions.types.tags


class RegisterIdentityProviderRequest(TypedDict, closed=True):
    identity_provider: "aws_sdk_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
    """<p>An object that specifies details for the identity provider to register.</p>"""
    product: "str"
    """<p>The name of the user-based subscription product.</p> <p>Valid values: <code>VISUAL_STUDIO_ENTERPRISE</code> | <code>VISUAL_STUDIO_PROFESSIONAL</code> | <code>OFFICE_PROFESSIONAL_PLUS</code> | <code>REMOTE_DESKTOP_SERVICES</code> </p>"""
    settings: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.settings.Settings"
    ]
    """<p>The registered identity provider’s product related configuration settings such as the subnets to provision VPC endpoints.</p>"""
    tags: NotRequired["aws_sdk_license_manager_user_subscriptions.types.tags.Tags"]
    """<p>The tags that apply to the identity provider's registration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterIdentityProviderRequest) -> dict:
    out: dict = {}
    import aws_sdk_license_manager_user_subscriptions.types.identity_provider

    out["IdentityProvider"] = (
        aws_sdk_license_manager_user_subscriptions.types.identity_provider.serialize_json(
            value["identity_provider"]
        )
    )
    out["Product"] = value["product"]
    if "settings" in value:
        import aws_sdk_license_manager_user_subscriptions.types.settings

        out["Settings"] = (
            aws_sdk_license_manager_user_subscriptions.types.settings.serialize_json(
                value["settings"]
            )
        )
    if "tags" in value:
        import aws_sdk_license_manager_user_subscriptions.types.tags

        out["Tags"] = (
            aws_sdk_license_manager_user_subscriptions.types.tags.serialize_json(
                value["tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegisterIdentityProviderRequest:
    out: RegisterIdentityProviderRequest = {}  # type: ignore[typeddict-item]
    if "IdentityProvider" in data:
        import aws_sdk_license_manager_user_subscriptions.types.identity_provider

        out["identity_provider"] = (
            aws_sdk_license_manager_user_subscriptions.types.identity_provider.deserialize_json(
                data["IdentityProvider"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterIdentityProviderRequest.identity_provider required"
        )
    if "Product" in data:
        out["product"] = data["Product"]
    else:
        raise DeserializationError("RegisterIdentityProviderRequest.product required")
    if "Settings" in data:
        import aws_sdk_license_manager_user_subscriptions.types.settings

        out["settings"] = (
            aws_sdk_license_manager_user_subscriptions.types.settings.deserialize_json(
                data["Settings"]
            )
        )
    if "Tags" in data:
        import aws_sdk_license_manager_user_subscriptions.types.tags

        out["tags"] = (
            aws_sdk_license_manager_user_subscriptions.types.tags.deserialize_json(
                data["Tags"]
            )
        )
    return out
