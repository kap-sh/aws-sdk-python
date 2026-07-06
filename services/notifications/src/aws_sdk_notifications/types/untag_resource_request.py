"""Generated from Smithy shape ``com.amazonaws.notifications#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_notifications.types.notification_configuration_arn
    import aws_sdk_notifications.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The Amazon Resource Name (ARN) to use to untag a resource.</p>"""
    tag_keys: "aws_sdk_notifications.types.tag_keys.TagKeys"
    """<p>The tag keys to use to untag a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
