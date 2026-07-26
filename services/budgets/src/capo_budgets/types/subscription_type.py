"""Generated from Smithy shape ``com.amazonaws.budgets#SubscriptionType``."""

from typing import Literal, TypeAlias, cast

"""<p> The subscription type of the subscriber. It can be SMS or EMAIL.</p>"""
SubscriptionType: TypeAlias = Literal[
    "SNS",
    "EMAIL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscriptionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SubscriptionType:
    return cast(SubscriptionType, data)
