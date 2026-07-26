"""Generated from Smithy shape ``com.amazonaws.inspector#SubscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.subscription

SubscriptionList: TypeAlias = list["capo_inspector.types.subscription.Subscription"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscriptionList) -> list:
    import capo_inspector.types.subscription

    out: list = []
    for item in value:
        out.append(capo_inspector.types.subscription.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SubscriptionList:
    import capo_inspector.types.subscription

    out: SubscriptionList = []
    for item in data:
        out.append(capo_inspector.types.subscription.deserialize_aws_json_1_1(item))
    return out
