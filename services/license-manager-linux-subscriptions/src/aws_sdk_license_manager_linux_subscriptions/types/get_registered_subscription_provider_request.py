"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#GetRegisteredSubscriptionProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_license_manager_linux_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager_linux_subscriptions.types.subscription_provider_arn


class GetRegisteredSubscriptionProviderRequest(TypedDict):
    subscription_provider_arn: "aws_sdk_license_manager_linux_subscriptions.types.subscription_provider_arn.SubscriptionProviderArn"
    """<p>The Amazon Resource Name (ARN) of the BYOL registration resource to get details for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRegisteredSubscriptionProviderRequest) -> dict:
    out: dict = {}
    out["SubscriptionProviderArn"] = value["subscription_provider_arn"]
    return out


def deserialize_json(data: dict) -> GetRegisteredSubscriptionProviderRequest:
    out: GetRegisteredSubscriptionProviderRequest = {}  # type: ignore[typeddict-item]
    if "SubscriptionProviderArn" in data:
        out["subscription_provider_arn"] = data["SubscriptionProviderArn"]
    else:
        raise DeserializationError(
            "GetRegisteredSubscriptionProviderRequest.subscription_provider_arn required"
        )
    return out
