"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.notification_rule_arn
    import aws_sdk_codestar_notifications.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    arn: (
        "aws_sdk_codestar_notifications.types.notification_rule_arn.NotificationRuleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the notification rule from which to remove the tags.</p>"""
    tag_keys: "aws_sdk_codestar_notifications.types.tag_keys.TagKeys"
    """<p>The key names of the tags to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
