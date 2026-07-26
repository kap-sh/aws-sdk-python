"""Generated from Smithy shape ``com.amazonaws.connecthealth#SubscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connecthealth.types.subscription_description

SubscriptionList: TypeAlias = list[
    "capo_connecthealth.types.subscription_description.SubscriptionDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionList) -> list:
    import capo_connecthealth.types.subscription_description

    out: list = []
    for item in value:
        out.append(
            capo_connecthealth.types.subscription_description.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SubscriptionList:
    import capo_connecthealth.types.subscription_description

    out: SubscriptionList = []
    for item in data:
        out.append(
            capo_connecthealth.types.subscription_description.deserialize_json(item)
        )
    return out
