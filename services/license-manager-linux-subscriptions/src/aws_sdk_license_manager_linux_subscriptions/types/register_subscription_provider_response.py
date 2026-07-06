"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#RegisterSubscriptionProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager_linux_subscriptions.types.subscription_provider_source
    import aws_sdk_license_manager_linux_subscriptions.types.subscription_provider_status


class RegisterSubscriptionProviderResponse(TypedDict, closed=True):
    subscription_provider_source: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.subscription_provider_source.SubscriptionProviderSource"
    ]
    """<p>The Linux subscription provider that you registered.</p>"""
    subscription_provider_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the Linux subscription provider resource that you registered.</p>"""
    subscription_provider_status: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.subscription_provider_status.SubscriptionProviderStatus"
    ]
    """<p>Indicates the status of the registration action for the Linux subscription provider that you requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterSubscriptionProviderResponse) -> dict:
    out: dict = {}
    if "subscription_provider_source" in value:
        out["SubscriptionProviderSource"] = value["subscription_provider_source"]
    if "subscription_provider_arn" in value:
        out["SubscriptionProviderArn"] = value["subscription_provider_arn"]
    if "subscription_provider_status" in value:
        out["SubscriptionProviderStatus"] = value["subscription_provider_status"]
    return out


def deserialize_json(data: dict) -> RegisterSubscriptionProviderResponse:
    out: RegisterSubscriptionProviderResponse = {}  # type: ignore[typeddict-item]
    if "SubscriptionProviderSource" in data:
        out["subscription_provider_source"] = data["SubscriptionProviderSource"]
    if "SubscriptionProviderArn" in data:
        out["subscription_provider_arn"] = data["SubscriptionProviderArn"]
    if "SubscriptionProviderStatus" in data:
        out["subscription_provider_status"] = data["SubscriptionProviderStatus"]
    return out
