"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codestar_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.notification_rule_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    arn: (
        "aws_sdk_codestar_notifications.types.notification_rule_arn.NotificationRuleArn"
    )
    """<p>The Amazon Resource Name (ARN) for the notification rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.arn required")
    return out
