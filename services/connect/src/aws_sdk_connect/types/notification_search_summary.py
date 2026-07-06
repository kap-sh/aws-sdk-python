"""Generated from Smithy shape ``com.amazonaws.connect#NotificationSearchSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.notification_content
    import aws_sdk_connect.types.notification_id
    import aws_sdk_connect.types.notification_priority
    import aws_sdk_connect.types.recipient_list
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.timestamp


class NotificationSearchSummary(TypedDict, closed=True):
    id: NotRequired["aws_sdk_connect.types.notification_id.NotificationId"]
    """<p>The unique identifier for the notification.</p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the notification.</p>"""
    instance_id: NotRequired["aws_sdk_connect.types.instance_id.InstanceId"]
    """<p>The identifier of the Amazon Connect instance.</p>"""
    content: NotRequired[
        "aws_sdk_connect.types.notification_content.NotificationContent"
    ]
    """<p>The localized content of the notification.</p>"""
    priority: NotRequired[
        "aws_sdk_connect.types.notification_priority.NotificationPriority"
    ]
    """<p>The priority level of the notification.</p>"""
    recipients: NotRequired["aws_sdk_connect.types.recipient_list.RecipientList"]
    """<p>A list of recipient Amazon Resource Names (ARNs).</p>"""
    created_at: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the notification was created.</p>"""
    expires_at: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the notification expires.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The AWS Region where the notification was last modified.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the notification was last modified.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>The tags associated with the notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationSearchSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
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
    if "recipients" in value:
        import aws_sdk_connect.types.recipient_list

        out["Recipients"] = aws_sdk_connect.types.recipient_list.serialize_json(
            value["recipients"]
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
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> NotificationSearchSummary:
    out: NotificationSearchSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
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
    if "Recipients" in data:
        import aws_sdk_connect.types.recipient_list

        out["recipients"] = aws_sdk_connect.types.recipient_list.deserialize_json(
            data["Recipients"]
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
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
