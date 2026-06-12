"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#DeregisterSubscriptionProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_license_manager_linux_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager_linux_subscriptions.types.subscription_provider_arn


class DeregisterSubscriptionProviderRequest(TypedDict):
    subscription_provider_arn: "aws_sdk_license_manager_linux_subscriptions.types.subscription_provider_arn.SubscriptionProviderArn"
    """<p>The Amazon Resource Name (ARN) of the subscription provider resource to deregister.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterSubscriptionProviderRequest) -> dict:
    out: dict = {}
    out["SubscriptionProviderArn"] = value["subscription_provider_arn"]
    return out


def deserialize_json(data: dict) -> DeregisterSubscriptionProviderRequest:
    out: DeregisterSubscriptionProviderRequest = {}  # type: ignore[typeddict-item]
    if "SubscriptionProviderArn" in data:
        out["subscription_provider_arn"] = data["SubscriptionProviderArn"]
    else:
        raise DeserializationError(
            "DeregisterSubscriptionProviderRequest.subscription_provider_arn required"
        )
    return out
