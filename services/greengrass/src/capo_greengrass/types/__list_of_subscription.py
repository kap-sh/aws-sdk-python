"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfSubscription``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrass.types.subscription

__listOfSubscription: TypeAlias = list[
    "capo_greengrass.types.subscription.Subscription"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSubscription) -> list:
    import capo_greengrass.types.subscription

    out: list = []
    for item in value:
        out.append(capo_greengrass.types.subscription.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSubscription:
    import capo_greengrass.types.subscription

    out: __listOfSubscription = []
    for item in data:
        out.append(capo_greengrass.types.subscription.deserialize_json(item))
    return out
