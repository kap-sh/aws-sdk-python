"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#DeleteNotificationRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codestar_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.notification_rule_arn


class DeleteNotificationRuleRequest(TypedDict, closed=True):
    arn: (
        "aws_sdk_codestar_notifications.types.notification_rule_arn.NotificationRuleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the notification rule you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNotificationRuleRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteNotificationRuleRequest:
    out: DeleteNotificationRuleRequest = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DeleteNotificationRuleRequest.arn required")
    return out
