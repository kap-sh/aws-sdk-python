"""Generated from Smithy shape ``com.amazonaws.outposts#SubscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.subscription

SubscriptionList: TypeAlias = list["aws_sdk_outposts.types.subscription.Subscription"]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionList) -> list:
    import aws_sdk_outposts.types.subscription

    out: list = []
    for item in value:
        out.append(aws_sdk_outposts.types.subscription.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubscriptionList:
    import aws_sdk_outposts.types.subscription

    out: SubscriptionList = []
    for item in data:
        out.append(aws_sdk_outposts.types.subscription.deserialize_json(item))
    return out
