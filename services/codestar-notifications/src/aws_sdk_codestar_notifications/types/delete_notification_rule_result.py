"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#DeleteNotificationRuleResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.notification_rule_arn


class DeleteNotificationRuleResult(TypedDict):
    arn: NotRequired[
        "aws_sdk_codestar_notifications.types.notification_rule_arn.NotificationRuleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the deleted notification rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNotificationRuleResult) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteNotificationRuleResult:
    out: DeleteNotificationRuleResult = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
