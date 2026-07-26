"""Generated from Smithy shape ``com.amazonaws.inspector#EventSubscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.event_subscription

EventSubscriptionList: TypeAlias = list[
    "capo_inspector.types.event_subscription.EventSubscription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventSubscriptionList) -> list:
    import capo_inspector.types.event_subscription

    out: list = []
    for item in value:
        out.append(capo_inspector.types.event_subscription.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EventSubscriptionList:
    import capo_inspector.types.event_subscription

    out: EventSubscriptionList = []
    for item in data:
        out.append(
            capo_inspector.types.event_subscription.deserialize_aws_json_1_1(item)
        )
    return out
