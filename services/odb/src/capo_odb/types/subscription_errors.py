"""Generated from Smithy shape ``com.amazonaws.odb#SubscriptionErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.subscription_error

SubscriptionErrors: TypeAlias = list[
    "capo_odb.types.subscription_error.SubscriptionError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SubscriptionErrors) -> list:
    import capo_odb.types.subscription_error

    out: list = []
    for item in value:
        out.append(capo_odb.types.subscription_error.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> SubscriptionErrors:
    import capo_odb.types.subscription_error

    out: SubscriptionErrors = []
    for item in data:
        out.append(capo_odb.types.subscription_error.deserialize_aws_json_1_0(item))
    return out
