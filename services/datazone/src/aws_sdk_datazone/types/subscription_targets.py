"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.subscription_target_summary

SubscriptionTargets: TypeAlias = list[
    "aws_sdk_datazone.types.subscription_target_summary.SubscriptionTargetSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionTargets) -> list:
    import aws_sdk_datazone.types.subscription_target_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_datazone.types.subscription_target_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SubscriptionTargets:
    import aws_sdk_datazone.types.subscription_target_summary

    out: SubscriptionTargets = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.subscription_target_summary.deserialize_json(item)
        )
    return out
