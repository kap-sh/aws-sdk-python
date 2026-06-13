"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionGrants``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.subscription_grant_summary

SubscriptionGrants: TypeAlias = list[
    "aws_sdk_datazone.types.subscription_grant_summary.SubscriptionGrantSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionGrants) -> list:
    import aws_sdk_datazone.types.subscription_grant_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_datazone.types.subscription_grant_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SubscriptionGrants:
    import aws_sdk_datazone.types.subscription_grant_summary

    out: SubscriptionGrants = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.subscription_grant_summary.deserialize_json(item)
        )
    return out
