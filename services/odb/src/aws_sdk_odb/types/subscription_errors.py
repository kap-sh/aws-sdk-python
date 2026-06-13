"""Generated from Smithy shape ``com.amazonaws.odb#SubscriptionErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_odb.types.subscription_error

SubscriptionErrors: TypeAlias = list[
    "aws_sdk_odb.types.subscription_error.SubscriptionError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SubscriptionErrors) -> list:
    import aws_sdk_odb.types.subscription_error

    out: list = []
    for item in value:
        out.append(aws_sdk_odb.types.subscription_error.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> SubscriptionErrors:
    import aws_sdk_odb.types.subscription_error

    out: SubscriptionErrors = []
    for item in data:
        out.append(aws_sdk_odb.types.subscription_error.deserialize_aws_json_1_0(item))
    return out
