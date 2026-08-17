"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SubscriptionFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.subscription_filter

SubscriptionFilters: TypeAlias = list[
    "capo_cloudwatch_logs.types.subscription_filter.SubscriptionFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscriptionFilters) -> list:
    import capo_cloudwatch_logs.types.subscription_filter

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.subscription_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SubscriptionFilters:
    import capo_cloudwatch_logs.types.subscription_filter

    out: SubscriptionFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.subscription_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
