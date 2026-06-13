"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#StartProductSubscriptionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.identity_provider
    import aws_sdk_license_manager_user_subscriptions.types.tags


class StartProductSubscriptionRequest(TypedDict):
    username: "str"
    """<p>The user name from the identity provider of the user.</p>"""
    identity_provider: "aws_sdk_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
    """<p>An object that specifies details for the identity provider.</p>"""
    product: "str"
    """<p>The name of the user-based subscription product.</p> <p>Valid values: <code>VISUAL_STUDIO_ENTERPRISE</code> | <code>VISUAL_STUDIO_PROFESSIONAL</code> | <code>OFFICE_PROFESSIONAL_PLUS</code> | <code>REMOTE_DESKTOP_SERVICES</code> </p>"""
    domain: NotRequired["str"]
    """<p>The domain name of the Active Directory that contains the user for whom to start the product subscription.</p>"""
    tags: NotRequired["aws_sdk_license_manager_user_subscriptions.types.tags.Tags"]
    """<p>The tags that apply to the product subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartProductSubscriptionRequest) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    import aws_sdk_license_manager_user_subscriptions.types.identity_provider

    out["IdentityProvider"] = (
        aws_sdk_license_manager_user_subscriptions.types.identity_provider.serialize_json(
            value["identity_provider"]
        )
    )
    out["Product"] = value["product"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "tags" in value:
        import aws_sdk_license_manager_user_subscriptions.types.tags

        out["Tags"] = (
            aws_sdk_license_manager_user_subscriptions.types.tags.serialize_json(
                value["tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartProductSubscriptionRequest:
    out: StartProductSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("StartProductSubscriptionRequest.username required")
    if "IdentityProvider" in data:
        import aws_sdk_license_manager_user_subscriptions.types.identity_provider

        out["identity_provider"] = (
            aws_sdk_license_manager_user_subscriptions.types.identity_provider.deserialize_json(
                data["IdentityProvider"]
            )
        )
    else:
        raise DeserializationError(
            "StartProductSubscriptionRequest.identity_provider required"
        )
    if "Product" in data:
        out["product"] = data["Product"]
    else:
        raise DeserializationError("StartProductSubscriptionRequest.product required")
    if "Domain" in data:
        out["domain"] = data["Domain"]
    if "Tags" in data:
        import aws_sdk_license_manager_user_subscriptions.types.tags

        out["tags"] = (
            aws_sdk_license_manager_user_subscriptions.types.tags.deserialize_json(
                data["Tags"]
            )
        )
    return out
