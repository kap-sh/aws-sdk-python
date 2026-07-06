"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeUsageReportSubscriptionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.string
    import aws_sdk_appstream.types.usage_report_subscription_list


class DescribeUsageReportSubscriptionsResult(TypedDict, closed=True):
    usage_report_subscriptions: NotRequired[
        "aws_sdk_appstream.types.usage_report_subscription_list.UsageReportSubscriptionList"
    ]
    """<p>Information about the usage report subscription.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUsageReportSubscriptionsResult) -> dict:
    out: dict = {}
    if "usage_report_subscriptions" in value:
        import aws_sdk_appstream.types.usage_report_subscription_list

        out["UsageReportSubscriptions"] = (
            aws_sdk_appstream.types.usage_report_subscription_list.serialize_aws_json_1_1(
                value["usage_report_subscriptions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUsageReportSubscriptionsResult:
    out: DescribeUsageReportSubscriptionsResult = {}  # type: ignore[typeddict-item]
    if "UsageReportSubscriptions" in data:
        import aws_sdk_appstream.types.usage_report_subscription_list

        out["usage_report_subscriptions"] = (
            aws_sdk_appstream.types.usage_report_subscription_list.deserialize_aws_json_1_1(
                data["UsageReportSubscriptions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
