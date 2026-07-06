"""Generated from Smithy shape ``com.amazonaws.connect#UpdateNotificationContentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.notification_content
    import aws_sdk_connect.types.notification_id


class UpdateNotificationContentRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    notification_id: "aws_sdk_connect.types.notification_id.NotificationId"
    """<p>The unique identifier for the notification to update.</p>"""
    content: "aws_sdk_connect.types.notification_content.NotificationContent"
    """<p>The updated localized content of the notification. A map of locale codes and values. Maximum 500 characters per locale.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNotificationContentRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.notification_content

    out["Content"] = aws_sdk_connect.types.notification_content.serialize_json(
        value["content"]
    )
    return out


def deserialize_json(data: dict) -> UpdateNotificationContentRequest:
    out: UpdateNotificationContentRequest = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        import aws_sdk_connect.types.notification_content

        out["content"] = aws_sdk_connect.types.notification_content.deserialize_json(
            data["Content"]
        )
    else:
        raise DeserializationError("UpdateNotificationContentRequest.content required")
    return out
