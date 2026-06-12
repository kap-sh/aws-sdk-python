"""Generated from Smithy shape ``com.amazonaws.greengrass#SubscriptionDefinitionVersion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__list_of_subscription


class SubscriptionDefinitionVersion(TypedDict):
    subscriptions: NotRequired[
        "aws_sdk_greengrass.types.__list_of_subscription.__listOfSubscription"
    ]
    """A list of subscriptions."""


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionDefinitionVersion) -> dict:
    out: dict = {}
    if "subscriptions" in value:
        import aws_sdk_greengrass.types.__list_of_subscription

        out["Subscriptions"] = (
            aws_sdk_greengrass.types.__list_of_subscription.serialize_json(
                value["subscriptions"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubscriptionDefinitionVersion:
    out: SubscriptionDefinitionVersion = {}  # type: ignore[typeddict-item]
    if "Subscriptions" in data:
        import aws_sdk_greengrass.types.__list_of_subscription

        out["subscriptions"] = (
            aws_sdk_greengrass.types.__list_of_subscription.deserialize_json(
                data["Subscriptions"]
            )
        )
    return out
