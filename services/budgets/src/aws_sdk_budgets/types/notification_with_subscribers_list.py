"""Generated from Smithy shape ``com.amazonaws.budgets#NotificationWithSubscribersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_budgets.types.notification_with_subscribers

NotificationWithSubscribersList: TypeAlias = list[
    "aws_sdk_budgets.types.notification_with_subscribers.NotificationWithSubscribers"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationWithSubscribersList) -> list:
    import aws_sdk_budgets.types.notification_with_subscribers

    out: list = []
    for item in value:
        out.append(
            aws_sdk_budgets.types.notification_with_subscribers.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NotificationWithSubscribersList:
    import aws_sdk_budgets.types.notification_with_subscribers

    out: NotificationWithSubscribersList = []
    for item in data:
        out.append(
            aws_sdk_budgets.types.notification_with_subscribers.deserialize_aws_json_1_1(
                item
            )
        )
    return out
