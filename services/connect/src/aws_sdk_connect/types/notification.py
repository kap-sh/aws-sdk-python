"""Generated from Smithy shape ``com.amazonaws.connect#Notification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.notification_content
    import aws_sdk_connect.types.notification_id
    import aws_sdk_connect.types.notification_priority
    import aws_sdk_connect.types.recipient_list
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.timestamp


class Notification(TypedDict):
    content: NotRequired[
        "aws_sdk_connect.types.notification_content.NotificationContent"
    ]
    """<p>The localized content of the notification. A map where keys are locale codes and values are the notification text in that locale.</p>"""
    id: "aws_sdk_connect.types.notification_id.NotificationId"
    """<p>The unique identifier for the notification.</p>"""
    arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the notification.</p>"""
    priority: NotRequired[
        "aws_sdk_connect.types.notification_priority.NotificationPriority"
    ]
    """<p>The priority level of the notification. Valid values are URGENT, HIGH, and LOW.</p>"""
    recipients: NotRequired["aws_sdk_connect.types.recipient_list.RecipientList"]
    """<p>A list of Amazon Resource Names (ARNs) identifying the recipients of the notification. Maximum of 200 recipients.</p>"""
    last_modified_time: "aws_sdk_connect.types.timestamp.Timestamp"
    """<p>The timestamp when the notification was last modified.</p>"""
    created_at: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the notification was created.</p>"""
    expires_at: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the notification expires and is no longer displayed to users.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The AWS Region where the notification was last modified.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, <code>{ \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Notification) -> dict:
    out: dict = {}
    if "content" in value:
        import aws_sdk_connect.types.notification_content

        out["Content"] = aws_sdk_connect.types.notification_content.serialize_json(
            value["content"]
        )
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    if "priority" in value:
        import aws_sdk_connect.types.notification_priority

        out["Priority"] = aws_sdk_connect.types.notification_priority.serialize_json(
            value["priority"]
        )
    if "recipients" in value:
        import aws_sdk_connect.types.recipient_list

        out["Recipients"] = aws_sdk_connect.types.recipient_list.serialize_json(
            value["recipients"]
        )
    import aws_sdk_connect.types.timestamp

    out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
        value["last_modified_time"]
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
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Notification:
    out: Notification = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        import aws_sdk_connect.types.notification_content

        out["content"] = aws_sdk_connect.types.notification_content.deserialize_json(
            data["Content"]
        )
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("Notification.id required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("Notification.arn required")
    if "Priority" in data:
        import aws_sdk_connect.types.notification_priority

        out["priority"] = aws_sdk_connect.types.notification_priority.deserialize_json(
            data["Priority"]
        )
    if "Recipients" in data:
        import aws_sdk_connect.types.recipient_list

        out["recipients"] = aws_sdk_connect.types.recipient_list.deserialize_json(
            data["Recipients"]
        )
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    else:
        raise DeserializationError("Notification.last_modified_time required")
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
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
