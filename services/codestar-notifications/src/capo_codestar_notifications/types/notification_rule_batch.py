"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#NotificationRuleBatch``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codestar_notifications.types.notification_rule_summary

NotificationRuleBatch: TypeAlias = list[
    "capo_codestar_notifications.types.notification_rule_summary.NotificationRuleSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationRuleBatch) -> list:
    import capo_codestar_notifications.types.notification_rule_summary

    out: list = []
    for item in value:
        out.append(
            capo_codestar_notifications.types.notification_rule_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NotificationRuleBatch:
    import capo_codestar_notifications.types.notification_rule_summary

    out: NotificationRuleBatch = []
    for item in data:
        out.append(
            capo_codestar_notifications.types.notification_rule_summary.deserialize_json(
                item
            )
        )
    return out
