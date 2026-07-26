"""Generated from Smithy shape ``com.amazonaws.shield#SubscriptionState``."""

from typing import Literal, TypeAlias, cast

SubscriptionState: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscriptionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SubscriptionState:
    return cast(SubscriptionState, data)
