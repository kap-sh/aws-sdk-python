"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeSubscriptionFiltersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.next_token
    import capo_cloudwatch_logs.types.subscription_filters


class DescribeSubscriptionFiltersResponse(TypedDict, closed=True):
    subscription_filters: NotRequired[
        "capo_cloudwatch_logs.types.subscription_filters.SubscriptionFilters"
    ]
    """<p>The subscription filters.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSubscriptionFiltersResponse) -> dict:
    out: dict = {}
    if "subscription_filters" in value:
        import capo_cloudwatch_logs.types.subscription_filters

        out["subscriptionFilters"] = (
            capo_cloudwatch_logs.types.subscription_filters.serialize_aws_json_1_1(
                value["subscription_filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSubscriptionFiltersResponse:
    out: DescribeSubscriptionFiltersResponse = {}  # type: ignore[typeddict-item]
    if "subscriptionFilters" in data:
        import capo_cloudwatch_logs.types.subscription_filters

        out["subscription_filters"] = (
            capo_cloudwatch_logs.types.subscription_filters.deserialize_aws_json_1_1(
                data["subscriptionFilters"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
