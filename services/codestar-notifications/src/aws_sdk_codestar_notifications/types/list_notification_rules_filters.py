"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListNotificationRulesFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.list_notification_rules_filter

ListNotificationRulesFilters: TypeAlias = list[
    "aws_sdk_codestar_notifications.types.list_notification_rules_filter.ListNotificationRulesFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationRulesFilters) -> list:
    import aws_sdk_codestar_notifications.types.list_notification_rules_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codestar_notifications.types.list_notification_rules_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListNotificationRulesFilters:
    import aws_sdk_codestar_notifications.types.list_notification_rules_filter

    out: ListNotificationRulesFilters = []
    for item in data:
        out.append(
            aws_sdk_codestar_notifications.types.list_notification_rules_filter.deserialize_json(
                item
            )
        )
    return out
