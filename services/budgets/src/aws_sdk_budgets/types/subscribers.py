"""Generated from Smithy shape ``com.amazonaws.budgets#Subscribers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_budgets.types.subscriber

Subscribers: TypeAlias = list["aws_sdk_budgets.types.subscriber.Subscriber"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Subscribers) -> list:
    import aws_sdk_budgets.types.subscriber

    out: list = []
    for item in value:
        out.append(aws_sdk_budgets.types.subscriber.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Subscribers:
    import aws_sdk_budgets.types.subscriber

    out: Subscribers = []
    for item in data:
        out.append(aws_sdk_budgets.types.subscriber.deserialize_aws_json_1_1(item))
    return out
