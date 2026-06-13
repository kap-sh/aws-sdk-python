"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ProductUserSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.arn
    import aws_sdk_license_manager_user_subscriptions.types.identity_provider


class ProductUserSummary(TypedDict):
    username: "str"
    """<p>The user name from the identity provider for this product user.</p>"""
    product: "str"
    """<p>The name of the user-based subscription product.</p>"""
    identity_provider: "aws_sdk_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
    """<p>An object that specifies details for the identity provider.</p>"""
    status: "str"
    """<p>The status of a product for this user.</p>"""
    product_user_arn: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.arn.Arn"
    ]
    """<p>The Amazon Resource Name (ARN) for this product user.</p>"""
    status_message: NotRequired["str"]
    """<p>The status message for a product for this user.</p>"""
    domain: NotRequired["str"]
    """<p>The domain name of the Active Directory that contains the user information for the product subscription.</p>"""
    subscription_start_date: NotRequired["str"]
    """<p>The start date of a subscription.</p>"""
    subscription_end_date: NotRequired["str"]
    """<p>The end date of a subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProductUserSummary) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    out["Product"] = value["product"]
    import aws_sdk_license_manager_user_subscriptions.types.identity_provider

    out["IdentityProvider"] = (
        aws_sdk_license_manager_user_subscriptions.types.identity_provider.serialize_json(
            value["identity_provider"]
        )
    )
    out["Status"] = value["status"]
    if "product_user_arn" in value:
        out["ProductUserArn"] = value["product_user_arn"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "subscription_start_date" in value:
        out["SubscriptionStartDate"] = value["subscription_start_date"]
    if "subscription_end_date" in value:
        out["SubscriptionEndDate"] = value["subscription_end_date"]
    return out


def deserialize_json(data: dict) -> ProductUserSummary:
    out: ProductUserSummary = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("ProductUserSummary.username required")
    if "Product" in data:
        out["product"] = data["Product"]
    else:
        raise DeserializationError("ProductUserSummary.product required")
    if "IdentityProvider" in data:
        import aws_sdk_license_manager_user_subscriptions.types.identity_provider

        out["identity_provider"] = (
            aws_sdk_license_manager_user_subscriptions.types.identity_provider.deserialize_json(
                data["IdentityProvider"]
            )
        )
    else:
        raise DeserializationError("ProductUserSummary.identity_provider required")
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("ProductUserSummary.status required")
    if "ProductUserArn" in data:
        out["product_user_arn"] = data["ProductUserArn"]
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    if "SubscriptionStartDate" in data:
        out["subscription_start_date"] = data["SubscriptionStartDate"]
    if "SubscriptionEndDate" in data:
        out["subscription_end_date"] = data["SubscriptionEndDate"]
    return out
