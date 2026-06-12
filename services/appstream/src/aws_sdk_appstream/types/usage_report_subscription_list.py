"""Generated from Smithy shape ``com.amazonaws.appstream#UsageReportSubscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.usage_report_subscription

UsageReportSubscriptionList: TypeAlias = list[
    "aws_sdk_appstream.types.usage_report_subscription.UsageReportSubscription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageReportSubscriptionList) -> list:
    import aws_sdk_appstream.types.usage_report_subscription

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appstream.types.usage_report_subscription.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UsageReportSubscriptionList:
    import aws_sdk_appstream.types.usage_report_subscription

    out: UsageReportSubscriptionList = []
    for item in data:
        out.append(
            aws_sdk_appstream.types.usage_report_subscription.deserialize_aws_json_1_1(
                item
            )
        )
    return out
