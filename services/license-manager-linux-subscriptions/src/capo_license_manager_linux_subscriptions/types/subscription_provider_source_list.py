"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#SubscriptionProviderSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager_linux_subscriptions.types.subscription_provider_source

SubscriptionProviderSourceList: TypeAlias = list[
    "capo_license_manager_linux_subscriptions.types.subscription_provider_source.SubscriptionProviderSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionProviderSourceList) -> list:
    return list(value)


def deserialize_json(data: list) -> SubscriptionProviderSourceList:
    return list(data)
