"""Generated from Smithy shape ``com.amazonaws.notifications#ManagedNotificationChildEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_notifications.types.aggregation_detail
    import capo_notifications.types.event_status
    import capo_notifications.types.managed_notification_event_arn
    import capo_notifications.types.message_components
    import capo_notifications.types.notification_event_id
    import capo_notifications.types.notification_type
    import capo_notifications.types.organizational_unit_id
    import capo_notifications.types.schema_version
    import capo_notifications.types.text_parts
    import capo_notifications.types.url


class ManagedNotificationChildEvent(TypedDict, closed=True):
    schema_version: "capo_notifications.types.schema_version.SchemaVersion"
    """<p>The schema version of the Managed Notification Child Event.</p>"""
    id: "capo_notifications.types.notification_event_id.NotificationEventId"
    """<p>The unique identifier for a Managed Notification Child Event.</p>"""
    message_components: "capo_notifications.types.message_components.MessageComponents"
    source_event_detail_url: NotRequired["capo_notifications.types.url.Url"]
    """<p>The source event URL.</p>"""
    source_event_detail_url_display_text: NotRequired["str"]
    """<p>The detailed URL for the source event.</p>"""
    notification_type: "capo_notifications.types.notification_type.NotificationType"
    """<p>The type of event causing the notification.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>ALERT</code> </p> <ul> <li> <p>A notification about an event where something was triggered, initiated, reopened, deployed, or a threshold was breached.</p> </li> </ul> </li> <li> <p> <code>WARNING</code> </p> <ul> <li> <p>A notification about an event where an issue is about to arise. For example, something is approaching a threshold.</p> </li> </ul> </li> <li> <p> <code>ANNOUNCEMENT</code> </p> <ul> <li> <p>A notification about an important event. For example, a step in a workflow or escalation path or that a workflow was updated.</p> </li> </ul> </li> <li> <p> <code>INFORMATIONAL</code> </p> <ul> <li> <p>A notification about informational messages. For example, recommendations, service announcements, or reminders.</p> </li> </ul> </li> </ul> </li> </ul>"""
    event_status: NotRequired["capo_notifications.types.event_status.EventStatus"]
    """<p>The assesed nature of the event.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>HEALTHY</code> </p> <ul> <li> <p>All <code>EventRules</code> are <code>ACTIVE</code>.</p> </li> </ul> </li> <li> <p> <code>UNHEALTHY</code> </p> <ul> <li> <p>Some <code>EventRules</code> are <code>ACTIVE</code> and some are <code>INACTIVE</code>.</p> </li> </ul> </li> </ul> </li> </ul>"""
    aggregate_managed_notification_event_arn: "capo_notifications.types.managed_notification_event_arn.ManagedNotificationEventArn"
    """<p>The Amazon Resource Name (ARN) of the ManagedNotificationEvent that is associated with this Managed Notification Child Event.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The notification event start time.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time of the event.</p>"""
    text_parts: "capo_notifications.types.text_parts.TextParts"
    """<p>A list of text values.</p>"""
    organizational_unit_id: NotRequired[
        "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
    ]
    """<p>The Organizational Unit Id that an Amazon Web Services account belongs to.</p>"""
    aggregation_detail: NotRequired[
        "capo_notifications.types.aggregation_detail.AggregationDetail"
    ]
    """<p>Provides detailed information about the dimensions used for event summarization and aggregation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedNotificationChildEvent) -> dict:
    out: dict = {}
    out["schemaVersion"] = value["schema_version"]
    out["id"] = value["id"]
    import capo_notifications.types.message_components

    out["messageComponents"] = (
        capo_notifications.types.message_components.serialize_json(
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
    out["aggregateManagedNotificationEventArn"] = value[
        "aggregate_managed_notification_event_arn"
    ]
    if "start_time" in value:
        import capo_notifications.types._prelude.timestamp

        out["startTime"] = capo_notifications.types._prelude.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_notifications.types._prelude.timestamp

        out["endTime"] = capo_notifications.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    import capo_notifications.types.text_parts

    out["textParts"] = capo_notifications.types.text_parts.serialize_json(
        value["text_parts"]
    )
    if "organizational_unit_id" in value:
        out["organizationalUnitId"] = value["organizational_unit_id"]
    if "aggregation_detail" in value:
        import capo_notifications.types.aggregation_detail

        out["aggregationDetail"] = (
            capo_notifications.types.aggregation_detail.serialize_json(
                value["aggregation_detail"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManagedNotificationChildEvent:
    out: ManagedNotificationChildEvent = {}  # type: ignore[typeddict-item]
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    else:
        raise DeserializationError(
            "ManagedNotificationChildEvent.schema_version required"
        )
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ManagedNotificationChildEvent.id required")
    if "messageComponents" in data:
        import capo_notifications.types.message_components

        out["message_components"] = (
            capo_notifications.types.message_components.deserialize_json(
                data["messageComponents"]
            )
        )
    else:
        raise DeserializationError(
            "ManagedNotificationChildEvent.message_components required"
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
        raise DeserializationError(
            "ManagedNotificationChildEvent.notification_type required"
        )
    if "eventStatus" in data:
        out["event_status"] = data["eventStatus"]
    if "aggregateManagedNotificationEventArn" in data:
        out["aggregate_managed_notification_event_arn"] = data[
            "aggregateManagedNotificationEventArn"
        ]
    else:
        raise DeserializationError(
            "ManagedNotificationChildEvent.aggregate_managed_notification_event_arn required"
        )
    if "startTime" in data:
        import capo_notifications.types._prelude.timestamp

        out["start_time"] = (
            capo_notifications.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import capo_notifications.types._prelude.timestamp

        out["end_time"] = capo_notifications.types._prelude.timestamp.deserialize_json(
            data["endTime"]
        )
    if "textParts" in data:
        import capo_notifications.types.text_parts

        out["text_parts"] = capo_notifications.types.text_parts.deserialize_json(
            data["textParts"]
        )
    else:
        raise DeserializationError("ManagedNotificationChildEvent.text_parts required")
    if "organizationalUnitId" in data:
        out["organizational_unit_id"] = data["organizationalUnitId"]
    if "aggregationDetail" in data:
        import capo_notifications.types.aggregation_detail

        out["aggregation_detail"] = (
            capo_notifications.types.aggregation_detail.deserialize_json(
                data["aggregationDetail"]
            )
        )
    return out
