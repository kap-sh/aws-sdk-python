"""Generated from Smithy shape ``com.amazonaws.qbusiness#Subscriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.subscription

Subscriptions: TypeAlias = list["capo_qbusiness.types.subscription.Subscription"]


# --- restJson1 ser/de ---
def serialize_json(value: Subscriptions) -> list:
    import capo_qbusiness.types.subscription

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.subscription.serialize_json(item))
    return out


def deserialize_json(data: list) -> Subscriptions:
    import capo_qbusiness.types.subscription

    out: Subscriptions = []
    for item in data:
        out.append(capo_qbusiness.types.subscription.deserialize_json(item))
    return out
