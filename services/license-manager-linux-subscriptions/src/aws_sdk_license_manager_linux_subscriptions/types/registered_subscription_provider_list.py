"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#RegisteredSubscriptionProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager_linux_subscriptions.types.registered_subscription_provider

RegisteredSubscriptionProviderList: TypeAlias = list[
    "aws_sdk_license_manager_linux_subscriptions.types.registered_subscription_provider.RegisteredSubscriptionProvider"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredSubscriptionProviderList) -> list:
    import aws_sdk_license_manager_linux_subscriptions.types.registered_subscription_provider

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager_linux_subscriptions.types.registered_subscription_provider.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RegisteredSubscriptionProviderList:
    import aws_sdk_license_manager_linux_subscriptions.types.registered_subscription_provider

    out: RegisteredSubscriptionProviderList = []
    for item in data:
        out.append(
            aws_sdk_license_manager_linux_subscriptions.types.registered_subscription_provider.deserialize_json(
                item
            )
        )
    return out
