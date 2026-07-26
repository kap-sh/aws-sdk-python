"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateSubscriptionDefinitionVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__list_of_subscription
    import capo_greengrass.types.__string


class CreateSubscriptionDefinitionVersionRequest(TypedDict, closed=True):
    amzn_client_token: NotRequired["capo_greengrass.types.__string.__string"]
    """A client token used to correlate requests and responses."""
    subscription_definition_id: "capo_greengrass.types.__string.__string"
    """The ID of the subscription definition."""
    subscriptions: NotRequired[
        "capo_greengrass.types.__list_of_subscription.__listOfSubscription"
    ]
    """A list of subscriptions."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSubscriptionDefinitionVersionRequest) -> dict:
    out: dict = {}
    if "subscriptions" in value:
        import capo_greengrass.types.__list_of_subscription

        out["Subscriptions"] = (
            capo_greengrass.types.__list_of_subscription.serialize_json(
                value["subscriptions"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSubscriptionDefinitionVersionRequest:
    out: CreateSubscriptionDefinitionVersionRequest = {}  # type: ignore[typeddict-item]
    if "Subscriptions" in data:
        import capo_greengrass.types.__list_of_subscription

        out["subscriptions"] = (
            capo_greengrass.types.__list_of_subscription.deserialize_json(
                data["Subscriptions"]
            )
        )
    return out
