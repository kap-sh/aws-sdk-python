"""Generated from Smithy shape ``com.amazonaws.resiliencehub#EventSubscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.event_subscription

EventSubscriptionList: TypeAlias = list[
    "capo_resiliencehub.types.event_subscription.EventSubscription"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventSubscriptionList) -> list:
    import capo_resiliencehub.types.event_subscription

    out: list = []
    for item in value:
        out.append(capo_resiliencehub.types.event_subscription.serialize_json(item))
    return out


def deserialize_json(data: list) -> EventSubscriptionList:
    import capo_resiliencehub.types.event_subscription

    out: EventSubscriptionList = []
    for item in data:
        out.append(capo_resiliencehub.types.event_subscription.deserialize_json(item))
    return out
