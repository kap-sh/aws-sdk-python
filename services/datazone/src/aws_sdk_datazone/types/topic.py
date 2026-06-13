"""Generated from Smithy shape ``com.amazonaws.datazone#Topic``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.notification_resource
    import aws_sdk_datazone.types.notification_role


class Topic(TypedDict):
    subject: "str"
    """<p>The subject of the resource mentioned in a notification.</p>"""
    resource: "aws_sdk_datazone.types.notification_resource.NotificationResource"
    role: "aws_sdk_datazone.types.notification_role.NotificationRole"
    """<p>The role of the resource mentioned in a notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Topic) -> dict:
    out: dict = {}
    out["subject"] = value["subject"]
    import aws_sdk_datazone.types.notification_resource

    out["resource"] = aws_sdk_datazone.types.notification_resource.serialize_json(
        value["resource"]
    )
    import aws_sdk_datazone.types.notification_role

    out["role"] = aws_sdk_datazone.types.notification_role.serialize_json(value["role"])
    return out


def deserialize_json(data: dict) -> Topic:
    out: Topic = {}  # type: ignore[typeddict-item]
    if "subject" in data:
        out["subject"] = data["subject"]
    else:
        raise DeserializationError("Topic.subject required")
    if "resource" in data:
        import aws_sdk_datazone.types.notification_resource

        out["resource"] = aws_sdk_datazone.types.notification_resource.deserialize_json(
            data["resource"]
        )
    else:
        raise DeserializationError("Topic.resource required")
    if "role" in data:
        import aws_sdk_datazone.types.notification_role

        out["role"] = aws_sdk_datazone.types.notification_role.deserialize_json(
            data["role"]
        )
    else:
        raise DeserializationError("Topic.role required")
    return out
