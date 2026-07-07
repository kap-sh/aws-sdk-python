"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#SubscribeResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.notification_rule_arn


class SubscribeResult(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_codestar_notifications.types.notification_rule_arn.NotificationRuleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the notification rule for which you have created assocations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribeResult) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> SubscribeResult:
    out: SubscribeResult = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
