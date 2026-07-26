"""Generated from Smithy shape ``com.amazonaws.workdocs#SubscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.subscription

SubscriptionList: TypeAlias = list["capo_workdocs.types.subscription.Subscription"]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionList) -> list:
    import capo_workdocs.types.subscription

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.subscription.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubscriptionList:
    import capo_workdocs.types.subscription

    out: SubscriptionList = []
    for item in data:
        out.append(capo_workdocs.types.subscription.deserialize_json(item))
    return out
