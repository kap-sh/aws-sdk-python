"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#NotificationRuleSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.notification_rule_arn
    import aws_sdk_codestar_notifications.types.notification_rule_id


class NotificationRuleSummary(TypedDict):
    id: NotRequired[
        "aws_sdk_codestar_notifications.types.notification_rule_id.NotificationRuleId"
    ]
    """<p>The unique ID of the notification rule.</p>"""
    arn: NotRequired[
        "aws_sdk_codestar_notifications.types.notification_rule_arn.NotificationRuleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the notification rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationRuleSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> NotificationRuleSummary:
    out: NotificationRuleSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
