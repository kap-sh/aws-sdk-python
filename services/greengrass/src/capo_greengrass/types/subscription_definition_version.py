"""Generated from Smithy shape ``com.amazonaws.greengrass#SubscriptionDefinitionVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__list_of_subscription


class SubscriptionDefinitionVersion(TypedDict, closed=True):
    subscriptions: NotRequired[
        "capo_greengrass.types.__list_of_subscription.__listOfSubscription"
    ]
    """A list of subscriptions."""


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionDefinitionVersion) -> dict:
    out: dict = {}
    if "subscriptions" in value:
        import capo_greengrass.types.__list_of_subscription

        out["Subscriptions"] = (
            capo_greengrass.types.__list_of_subscription.serialize_json(
                value["subscriptions"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubscriptionDefinitionVersion:
    out: SubscriptionDefinitionVersion = {}  # type: ignore[typeddict-item]
    if "Subscriptions" in data:
        import capo_greengrass.types.__list_of_subscription

        out["subscriptions"] = (
            capo_greengrass.types.__list_of_subscription.deserialize_json(
                data["Subscriptions"]
            )
        )
    return out
