"""Generated from Smithy shape ``com.amazonaws.datazone#NotificationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.action_link
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.message
    import aws_sdk_datazone.types.metadata_map
    import aws_sdk_datazone.types.notification_type
    import aws_sdk_datazone.types.task_id
    import aws_sdk_datazone.types.task_status
    import aws_sdk_datazone.types.title
    import aws_sdk_datazone.types.topic


class NotificationOutput(TypedDict, closed=True):
    identifier: "aws_sdk_datazone.types.task_id.TaskId"
    """<p>The identifier of the notification.</p>"""
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of a Amazon DataZone domain in which the notification exists.</p>"""
    type: "aws_sdk_datazone.types.notification_type.NotificationType"
    """<p>The type of the notification.</p>"""
    topic: "aws_sdk_datazone.types.topic.Topic"
    """<p>The topic of the notification.</p>"""
    title: "aws_sdk_datazone.types.title.Title"
    """<p>The title of the notification.</p>"""
    message: "aws_sdk_datazone.types.message.Message"
    """<p>The message included in the notification.</p>"""
    status: NotRequired["aws_sdk_datazone.types.task_status.TaskStatus"]
    """<p>The status included in the notification.</p>"""
    action_link: "aws_sdk_datazone.types.action_link.ActionLink"
    """<p>The action link included in the notification.</p>"""
    creation_timestamp: "datetime.datetime"
    """<p>The timestamp of when a notification was created.</p>"""
    last_updated_timestamp: "datetime.datetime"
    """<p>The timestamp of when the notification was last updated.</p>"""
    metadata: NotRequired["aws_sdk_datazone.types.metadata_map.MetadataMap"]
    """<p>The metadata included in the notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationOutput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    out["domainIdentifier"] = value["domain_identifier"]
    import aws_sdk_datazone.types.notification_type

    out["type"] = aws_sdk_datazone.types.notification_type.serialize_json(value["type"])
    import aws_sdk_datazone.types.topic

    out["topic"] = aws_sdk_datazone.types.topic.serialize_json(value["topic"])
    out["title"] = value["title"]
    out["message"] = value["message"]
    if "status" in value:
        import aws_sdk_datazone.types.task_status

        out["status"] = aws_sdk_datazone.types.task_status.serialize_json(
            value["status"]
        )
    out["actionLink"] = value["action_link"]
    import aws_sdk_datazone.types._prelude.timestamp

    out["creationTimestamp"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
        value["creation_timestamp"]
    )
    import aws_sdk_datazone.types._prelude.timestamp

    out["lastUpdatedTimestamp"] = (
        aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["last_updated_timestamp"]
        )
    )
    if "metadata" in value:
        import aws_sdk_datazone.types.metadata_map

        out["metadata"] = aws_sdk_datazone.types.metadata_map.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> NotificationOutput:
    out: NotificationOutput = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("NotificationOutput.identifier required")
    if "domainIdentifier" in data:
        out["domain_identifier"] = data["domainIdentifier"]
    else:
        raise DeserializationError("NotificationOutput.domain_identifier required")
    if "type" in data:
        import aws_sdk_datazone.types.notification_type

        out["type"] = aws_sdk_datazone.types.notification_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("NotificationOutput.type required")
    if "topic" in data:
        import aws_sdk_datazone.types.topic

        out["topic"] = aws_sdk_datazone.types.topic.deserialize_json(data["topic"])
    else:
        raise DeserializationError("NotificationOutput.topic required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("NotificationOutput.title required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("NotificationOutput.message required")
    if "status" in data:
        import aws_sdk_datazone.types.task_status

        out["status"] = aws_sdk_datazone.types.task_status.deserialize_json(
            data["status"]
        )
    if "actionLink" in data:
        out["action_link"] = data["actionLink"]
    else:
        raise DeserializationError("NotificationOutput.action_link required")
    if "creationTimestamp" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["creation_timestamp"] = (
            aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
                data["creationTimestamp"]
            )
        )
    else:
        raise DeserializationError("NotificationOutput.creation_timestamp required")
    if "lastUpdatedTimestamp" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedTimestamp"]
            )
        )
    else:
        raise DeserializationError("NotificationOutput.last_updated_timestamp required")
    if "metadata" in data:
        import aws_sdk_datazone.types.metadata_map

        out["metadata"] = aws_sdk_datazone.types.metadata_map.deserialize_json(
            data["metadata"]
        )
    return out
