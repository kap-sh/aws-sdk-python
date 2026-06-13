"""Generated from Smithy shape ``com.amazonaws.notifications#NotificationEventSchema``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_notifications.types.aggregation_event_type
    import aws_sdk_notifications.types.aggregation_summary
    import aws_sdk_notifications.types.event_status
    import aws_sdk_notifications.types.media
    import aws_sdk_notifications.types.message_components
    import aws_sdk_notifications.types.notification_event_arn
    import aws_sdk_notifications.types.notification_event_id
    import aws_sdk_notifications.types.notification_type
    import aws_sdk_notifications.types.organizational_unit_id
    import aws_sdk_notifications.types.schema_version
    import aws_sdk_notifications.types.source_event_metadata
    import aws_sdk_notifications.types.text_parts
    import aws_sdk_notifications.types.url


class NotificationEventSchema(TypedDict):
    schema_version: "aws_sdk_notifications.types.schema_version.SchemaVersion"
    """<p>The schema version of the Notification Event.</p>"""
    id: "aws_sdk_notifications.types.notification_event_id.NotificationEventId"
    """<p>The unique identifier for a <code>NotificationEvent</code>.</p>"""
    source_event_metadata: (
        "aws_sdk_notifications.types.source_event_metadata.SourceEventMetadata"
    )
    """<p>The source event metadata.</p>"""
    message_components: (
        "aws_sdk_notifications.types.message_components.MessageComponents"
    )
    source_event_detail_url: NotRequired["aws_sdk_notifications.types.url.Url"]
    """<p>The source event URL.</p>"""
    source_event_detail_url_display_text: NotRequired["str"]
    """<p>The detailed URL for the source event.</p>"""
    notification_type: "aws_sdk_notifications.types.notification_type.NotificationType"
    """<p>The type of event causing the notification.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>ALERT</code> </p> <ul> <li> <p>A notification about an event where something was triggered, initiated, reopened, deployed, or a threshold was breached.</p> </li> </ul> </li> <li> <p> <code>WARNING</code> </p> <ul> <li> <p>A notification about an event where an issue is about to arise. For example, something is approaching a threshold.</p> </li> </ul> </li> <li> <p> <code>ANNOUNCEMENT</code> </p> <ul> <li> <p>A notification about an important event. For example, a step in a workflow or escalation path or that a workflow was updated.</p> </li> </ul> </li> <li> <p> <code>INFORMATIONAL</code> </p> <ul> <li> <p>A notification about informational messages. For example, recommendations, service announcements, or reminders.</p> </li> </ul> </li> </ul> </li> </ul>"""
    event_status: NotRequired["aws_sdk_notifications.types.event_status.EventStatus"]
    """<p>The assessed nature of the event.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>HEALTHY</code> </p> <ul> <li> <p>All <code>EventRules</code> are <code>ACTIVE</code> and any call can be run.</p> </li> </ul> </li> <li> <p> <code>UNHEALTHY</code> </p> <ul> <li> <p>Some <code>EventRules</code> are <code>ACTIVE</code> and some are <code>INACTIVE</code>. Any call can be run.</p> </li> </ul> </li> </ul> </li> </ul>"""
    aggregation_event_type: NotRequired[
        "aws_sdk_notifications.types.aggregation_event_type.AggregationEventType"
    ]
    """<p>The aggregation type of the <code>NotificationConfiguration</code>.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>AGGREGATE</code> </p> <ul> <li> <p>The notification event is an aggregate notification. Aggregate notifications summarize grouped events over a specified time period.</p> </li> </ul> </li> <li> <p> <code>CHILD</code> </p> <ul> <li> <p>Some <code>EventRules</code> are <code>ACTIVE</code> and some are <code>INACTIVE</code>. Any call can be run.</p> </li> </ul> </li> <li> <p> <code>NONE</code> </p> <ul> <li> <p>The notification isn't aggregated.</p> </li> </ul> </li> </ul> </li> </ul>"""
    aggregate_notification_event_arn: NotRequired[
        "aws_sdk_notifications.types.notification_event_arn.NotificationEventArn"
    ]
    """<p>If the value of <code>aggregationEventType</code> is not <code>NONE</code>, this is the Amazon Resource Event (ARN) of the parent aggregate notification.</p> <p>This is omitted if notification isn't aggregated.</p>"""
    aggregation_summary: NotRequired[
        "aws_sdk_notifications.types.aggregation_summary.AggregationSummary"
    ]
    """<p>Provides additional information about how multiple notifications are grouped.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The notification event start time.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time of the event.</p>"""
    text_parts: "aws_sdk_notifications.types.text_parts.TextParts"
    """<p>A list of text values.</p>"""
    media: "aws_sdk_notifications.types.media.Media"
    """<p>A list of media elements.</p>"""
    organizational_unit_id: NotRequired[
        "aws_sdk_notifications.types.organizational_unit_id.OrganizationalUnitId"
    ]
    """<p>The unique identifier of the organizational unit associated with the notification event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationEventSchema) -> dict:
    out: dict = {}
    out["schemaVersion"] = value["schema_version"]
    out["id"] = value["id"]
    import aws_sdk_notifications.types.source_event_metadata

    out["sourceEventMetadata"] = (
        aws_sdk_notifications.types.source_event_metadata.serialize_json(
            value["source_event_metadata"]
        )
    )
    import aws_sdk_notifications.types.message_components

    out["messageComponents"] = (
        aws_sdk_notifications.types.message_components.serialize_json(
            value["message_components"]
        )
    )
    if "source_event_detail_url" in value:
        out["sourceEventDetailUrl"] = value["source_event_detail_url"]
    if "source_event_detail_url_display_text" in value:
        out["sourceEventDetailUrlDisplayText"] = value[
            "source_event_detail_url_display_text"
        ]
    out["notificationType"] = value["notification_type"]
    if "event_status" in value:
        out["eventStatus"] = value["event_status"]
    if "aggregation_event_type" in value:
        out["aggregationEventType"] = value["aggregation_event_type"]
    if "aggregate_notification_event_arn" in value:
        out["aggregateNotificationEventArn"] = value["aggregate_notification_event_arn"]
    if "aggregation_summary" in value:
        import aws_sdk_notifications.types.aggregation_summary

        out["aggregationSummary"] = (
            aws_sdk_notifications.types.aggregation_summary.serialize_json(
                value["aggregation_summary"]
            )
        )
    if "start_time" in value:
        import aws_sdk_notifications.types._prelude.timestamp

        out["startTime"] = (
            aws_sdk_notifications.types._prelude.timestamp.serialize_json(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_notifications.types._prelude.timestamp

        out["endTime"] = aws_sdk_notifications.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    import aws_sdk_notifications.types.text_parts

    out["textParts"] = aws_sdk_notifications.types.text_parts.serialize_json(
        value["text_parts"]
    )
    import aws_sdk_notifications.types.media

    out["media"] = aws_sdk_notifications.types.media.serialize_json(value["media"])
    if "organizational_unit_id" in value:
        out["organizationalUnitId"] = value["organizational_unit_id"]
    return out


def deserialize_json(data: dict) -> NotificationEventSchema:
    out: NotificationEventSchema = {}  # type: ignore[typeddict-item]
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    else:
        raise DeserializationError("NotificationEventSchema.schema_version required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("NotificationEventSchema.id required")
    if "sourceEventMetadata" in data:
        import aws_sdk_notifications.types.source_event_metadata

        out["source_event_metadata"] = (
            aws_sdk_notifications.types.source_event_metadata.deserialize_json(
                data["sourceEventMetadata"]
            )
        )
    else:
        raise DeserializationError(
            "NotificationEventSchema.source_event_metadata required"
        )
    if "messageComponents" in data:
        import aws_sdk_notifications.types.message_components

        out["message_components"] = (
            aws_sdk_notifications.types.message_components.deserialize_json(
                data["messageComponents"]
            )
        )
    else:
        raise DeserializationError(
            "NotificationEventSchema.message_components required"
        )
    if "sourceEventDetailUrl" in data:
        out["source_event_detail_url"] = data["sourceEventDetailUrl"]
    if "sourceEventDetailUrlDisplayText" in data:
        out["source_event_detail_url_display_text"] = data[
            "sourceEventDetailUrlDisplayText"
        ]
    if "notificationType" in data:
        out["notification_type"] = data["notificationType"]
    else:
        raise DeserializationError("NotificationEventSchema.notification_type required")
    if "eventStatus" in data:
        out["event_status"] = data["eventStatus"]
    if "aggregationEventType" in data:
        out["aggregation_event_type"] = data["aggregationEventType"]
    if "aggregateNotificationEventArn" in data:
        out["aggregate_notification_event_arn"] = data["aggregateNotificationEventArn"]
    if "aggregationSummary" in data:
        import aws_sdk_notifications.types.aggregation_summary

        out["aggregation_summary"] = (
            aws_sdk_notifications.types.aggregation_summary.deserialize_json(
                data["aggregationSummary"]
            )
        )
    if "startTime" in data:
        import aws_sdk_notifications.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_notifications.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import aws_sdk_notifications.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_notifications.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    if "textParts" in data:
        import aws_sdk_notifications.types.text_parts

        out["text_parts"] = aws_sdk_notifications.types.text_parts.deserialize_json(
            data["textParts"]
        )
    else:
        raise DeserializationError("NotificationEventSchema.text_parts required")
    if "media" in data:
        import aws_sdk_notifications.types.media

        out["media"] = aws_sdk_notifications.types.media.deserialize_json(data["media"])
    else:
        raise DeserializationError("NotificationEventSchema.media required")
    if "organizationalUnitId" in data:
        out["organizational_unit_id"] = data["organizationalUnitId"]
    return out
