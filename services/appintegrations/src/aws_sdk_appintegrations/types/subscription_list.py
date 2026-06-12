"""Generated from Smithy shape ``com.amazonaws.appintegrations#SubscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.subscription

SubscriptionList: TypeAlias = list[
    "aws_sdk_appintegrations.types.subscription.Subscription"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionList) -> list:
    import aws_sdk_appintegrations.types.subscription

    out: list = []
    for item in value:
        out.append(aws_sdk_appintegrations.types.subscription.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubscriptionList:
    import aws_sdk_appintegrations.types.subscription

    out: SubscriptionList = []
    for item in data:
        out.append(aws_sdk_appintegrations.types.subscription.deserialize_json(item))
    return out
