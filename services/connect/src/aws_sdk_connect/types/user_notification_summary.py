"""Generated from Smithy shape ``com.amazonaws.connect#UserNotificationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_id
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.notification_content
    import aws_sdk_connect.types.notification_id
    import aws_sdk_connect.types.notification_priority
    import aws_sdk_connect.types.notification_source
    import aws_sdk_connect.types.notification_status
    import aws_sdk_connect.types.timestamp


class UserNotificationSummary(TypedDict):
    notification_id: NotRequired["aws_sdk_connect.types.notification_id.NotificationId"]
    """<p>The unique identifier for the notification.</p>"""
    notification_status: NotRequired[
        "aws_sdk_connect.types.notification_status.NotificationStatus"
    ]
    """<p>The status of the notification for this user. Valid values are READ, UNREAD, and HIDDEN.</p>"""
    instance_id: NotRequired["aws_sdk_connect.types.instance_id.InstanceId"]
    """<p>The identifier of the Amazon Connect instance.</p>"""
    recipient_id: NotRequired["aws_sdk_connect.types.agent_id.AgentId"]
    """<p>The identifier of the recipient user.</p>"""
    content: NotRequired[
        "aws_sdk_connect.types.notification_content.NotificationContent"
    ]
    """<p>The localized content of the notification.</p>"""
    priority: NotRequired[
        "aws_sdk_connect.types.notification_priority.NotificationPriority"
    ]
    """<p>The priority level of the notification.</p>"""
    source: NotRequired["aws_sdk_connect.types.notification_source.NotificationSource"]
    """<p>The source that created the notification. Valid values are CUSTOMER, RULES, and SYSTEM.</p>"""
    created_at: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the notification was created.</p>"""
    expires_at: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the notification expires.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserNotificationSummary) -> dict:
    out: dict = {}
    if "notification_id" in value:
        out["NotificationId"] = value["notification_id"]
    if "notification_status" in value:
        import aws_sdk_connect.types.notification_status

        out["NotificationStatus"] = (
            aws_sdk_connect.types.notification_status.serialize_json(
                value["notification_status"]
            )
        )
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "recipient_id" in value:
        out["RecipientId"] = value["recipient_id"]
    if "content" in value:
        import aws_sdk_connect.types.notification_content

        out["Content"] = aws_sdk_connect.types.notification_content.serialize_json(
            value["content"]
        )
    if "priority" in value:
        import aws_sdk_connect.types.notification_priority

        out["Priority"] = aws_sdk_connect.types.notification_priority.serialize_json(
            value["priority"]
        )
    if "source" in value:
        import aws_sdk_connect.types.notification_source

        out["Source"] = aws_sdk_connect.types.notification_source.serialize_json(
            value["source"]
        )
    if "created_at" in value:
        import aws_sdk_connect.types.timestamp

        out["CreatedAt"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "expires_at" in value:
        import aws_sdk_connect.types.timestamp

        out["ExpiresAt"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["expires_at"]
        )
    return out


def deserialize_json(data: dict) -> UserNotificationSummary:
    out: UserNotificationSummary = {}  # type: ignore[typeddict-item]
    if "NotificationId" in data:
        out["notification_id"] = data["NotificationId"]
    if "NotificationStatus" in data:
        import aws_sdk_connect.types.notification_status

        out["notification_status"] = (
            aws_sdk_connect.types.notification_status.deserialize_json(
                data["NotificationStatus"]
            )
        )
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "RecipientId" in data:
        out["recipient_id"] = data["RecipientId"]
    if "Content" in data:
        import aws_sdk_connect.types.notification_content

        out["content"] = aws_sdk_connect.types.notification_content.deserialize_json(
            data["Content"]
        )
    if "Priority" in data:
        import aws_sdk_connect.types.notification_priority

        out["priority"] = aws_sdk_connect.types.notification_priority.deserialize_json(
            data["Priority"]
        )
    if "Source" in data:
        import aws_sdk_connect.types.notification_source

        out["source"] = aws_sdk_connect.types.notification_source.deserialize_json(
            data["Source"]
        )
    if "CreatedAt" in data:
        import aws_sdk_connect.types.timestamp

        out["created_at"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "ExpiresAt" in data:
        import aws_sdk_connect.types.timestamp

        out["expires_at"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["ExpiresAt"]
        )
    return out
