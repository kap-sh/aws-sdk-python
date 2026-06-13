"""Generated from Smithy shape ``com.amazonaws.datazone#Subscriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.subscription_summary

Subscriptions: TypeAlias = list[
    "aws_sdk_datazone.types.subscription_summary.SubscriptionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: Subscriptions) -> list:
    import aws_sdk_datazone.types.subscription_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.subscription_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> Subscriptions:
    import aws_sdk_datazone.types.subscription_summary

    out: Subscriptions = []
    for item in data:
        out.append(aws_sdk_datazone.types.subscription_summary.deserialize_json(item))
    return out
