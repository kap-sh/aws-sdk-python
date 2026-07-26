"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsSnsTopicSubscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_sns_topic_subscription

AwsSnsTopicSubscriptionList: TypeAlias = list[
    "capo_securityhub.types.aws_sns_topic_subscription.AwsSnsTopicSubscription"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsSnsTopicSubscriptionList) -> list:
    import capo_securityhub.types.aws_sns_topic_subscription

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_sns_topic_subscription.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsSnsTopicSubscriptionList:
    import capo_securityhub.types.aws_sns_topic_subscription

    out: AwsSnsTopicSubscriptionList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_sns_topic_subscription.deserialize_json(item)
        )
    return out
