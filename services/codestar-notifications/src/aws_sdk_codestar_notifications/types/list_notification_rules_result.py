"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListNotificationRulesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.next_token
    import aws_sdk_codestar_notifications.types.notification_rule_batch


class ListNotificationRulesResult(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_codestar_notifications.types.next_token.NextToken"]
    """<p>An enumeration token that can be used in a request to return the next batch of the results.</p>"""
    notification_rules: NotRequired[
        "aws_sdk_codestar_notifications.types.notification_rule_batch.NotificationRuleBatch"
    ]
    """<p>The list of notification rules for the Amazon Web Services account, by Amazon Resource Name (ARN) and ID. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationRulesResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "notification_rules" in value:
        import aws_sdk_codestar_notifications.types.notification_rule_batch

        out["NotificationRules"] = (
            aws_sdk_codestar_notifications.types.notification_rule_batch.serialize_json(
                value["notification_rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListNotificationRulesResult:
    out: ListNotificationRulesResult = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "NotificationRules" in data:
        import aws_sdk_codestar_notifications.types.notification_rule_batch

        out["notification_rules"] = (
            aws_sdk_codestar_notifications.types.notification_rule_batch.deserialize_json(
                data["NotificationRules"]
            )
        )
    return out
