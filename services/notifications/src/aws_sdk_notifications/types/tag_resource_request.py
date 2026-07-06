"""Generated from Smithy shape ``com.amazonaws.notifications#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.notification_configuration_arn
    import aws_sdk_notifications.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The Amazon Resource Name (ARN) to use to tag a resource.</p>"""
    tags: "aws_sdk_notifications.types.tag_map.TagMap"
    """<p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_notifications.types.tag_map

    out["tags"] = aws_sdk_notifications.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_notifications.types.tag_map

        out["tags"] = aws_sdk_notifications.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
