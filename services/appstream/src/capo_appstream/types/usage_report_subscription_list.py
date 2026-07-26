"""Generated from Smithy shape ``com.amazonaws.appstream#UsageReportSubscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.usage_report_subscription

UsageReportSubscriptionList: TypeAlias = list[
    "capo_appstream.types.usage_report_subscription.UsageReportSubscription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageReportSubscriptionList) -> list:
    import capo_appstream.types.usage_report_subscription

    out: list = []
    for item in value:
        out.append(
            capo_appstream.types.usage_report_subscription.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UsageReportSubscriptionList:
    import capo_appstream.types.usage_report_subscription

    out: UsageReportSubscriptionList = []
    for item in data:
        out.append(
            capo_appstream.types.usage_report_subscription.deserialize_aws_json_1_1(
                item
            )
        )
    return out
