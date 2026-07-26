"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#SubscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager_linux_subscriptions.types.subscription

SubscriptionList: TypeAlias = list[
    "capo_license_manager_linux_subscriptions.types.subscription.Subscription"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionList) -> list:
    import capo_license_manager_linux_subscriptions.types.subscription

    out: list = []
    for item in value:
        out.append(
            capo_license_manager_linux_subscriptions.types.subscription.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SubscriptionList:
    import capo_license_manager_linux_subscriptions.types.subscription

    out: SubscriptionList = []
    for item in data:
        out.append(
            capo_license_manager_linux_subscriptions.types.subscription.deserialize_json(
                item
            )
        )
    return out
