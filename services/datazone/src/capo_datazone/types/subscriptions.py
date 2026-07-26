"""Generated from Smithy shape ``com.amazonaws.datazone#Subscriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.subscription_summary

Subscriptions: TypeAlias = list[
    "capo_datazone.types.subscription_summary.SubscriptionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: Subscriptions) -> list:
    import capo_datazone.types.subscription_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.subscription_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> Subscriptions:
    import capo_datazone.types.subscription_summary

    out: Subscriptions = []
    for item in data:
        out.append(capo_datazone.types.subscription_summary.deserialize_json(item))
    return out
