"""Generated from Smithy shape ``com.amazonaws.budgets#Notifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_budgets.types.notification

Notifications: TypeAlias = list["capo_budgets.types.notification.Notification"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Notifications) -> list:
    import capo_budgets.types.notification

    out: list = []
    for item in value:
        out.append(capo_budgets.types.notification.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Notifications:
    import capo_budgets.types.notification

    out: Notifications = []
    for item in data:
        out.append(capo_budgets.types.notification.deserialize_aws_json_1_1(item))
    return out
