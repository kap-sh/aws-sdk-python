"""Generated from Smithy shape ``com.amazonaws.budgets#NotificationWithSubscribersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_budgets.types.notification_with_subscribers

NotificationWithSubscribersList: TypeAlias = list[
    "capo_budgets.types.notification_with_subscribers.NotificationWithSubscribers"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationWithSubscribersList) -> list:
    import capo_budgets.types.notification_with_subscribers

    out: list = []
    for item in value:
        out.append(
            capo_budgets.types.notification_with_subscribers.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NotificationWithSubscribersList:
    import capo_budgets.types.notification_with_subscribers

    out: NotificationWithSubscribersList = []
    for item in data:
        out.append(
            capo_budgets.types.notification_with_subscribers.deserialize_aws_json_1_1(
                item
            )
        )
    return out
