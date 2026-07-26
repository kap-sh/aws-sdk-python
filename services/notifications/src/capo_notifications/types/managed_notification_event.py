"""Generated from Smithy shape ``com.amazonaws.notifications#ManagedNotificationEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_notifications.types.aggregation_event_type
    import capo_notifications.types.aggregation_summary
    import capo_notifications.types.event_status
    import capo_notifications.types.message_components
    import capo_notifications.types.notification_event_id
    import capo_notifications.types.notification_type
    import capo_notifications.types.organizational_unit_id
    import capo_notifications.types.schema_version
    import capo_notifications.types.text_parts
    import capo_notifications.types.url


class ManagedNotificationEvent(TypedDict, closed=True):
    schema_version: "capo_notifications.types.schema_version.SchemaVersion"
    """<p>Version of the <code>ManagedNotificationEvent</code> schema.</p>"""
    id: "capo_notifications.types.notification_event_id.NotificationEventId"
    """<p>Unique identifier for a <code>ManagedNotificationEvent</code>.</p>"""
    message_components: "capo_notifications.types.message_components.MessageComponents"
    source_event_detail_url: NotRequired["capo_notifications.types.url.Url"]
    """<p>URL defined by Source Service to be used by notification consumers to get additional information about event.</p>"""
    source_event_detail_url_display_text: NotRequired["str"]
    """<p>Text that needs to be hyperlinked with the sourceEventDetailUrl. For example, the description of the sourceEventDetailUrl.</p>"""
    notification_type: "capo_notifications.types.notification_type.NotificationType"
    """<p>The nature of the event causing this notification.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>ALERT</code> </p> <ul> <li> <p>A notification about an event where something was triggered, initiated, reopened, deployed, or a threshold was breached.</p> </li> </ul> </li> <li> <p> <code>WARNING</code> </p> <ul> <li> <p>A notification about an event where an issue is about to arise. For example, something is approaching a threshold.</p> </li> </ul> </li> <li> <p> <code>ANNOUNCEMENT</code> </p> <ul> <li> <p>A notification about an important event. For example, a step in a workflow or escalation path or that a workflow was updated.</p> </li> </ul> </li> <li> <p> <code>INFORMATIONAL</code> </p> <ul> <li> <p>A notification about informational messages. For example, recommendations, service announcements, or reminders.</p> </li> </ul> </li> </ul> </li> </ul>"""
    event_status: NotRequired["capo_notifications.types.event_status.EventStatus"]
    """<p>The status of an event.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>HEALTHY</code> </p> <ul> <li> <p>All EventRules are <code>ACTIVE</code> and any call can be run.</p> </li> </ul> </li> <li> <p> <code>UNHEALTHY</code> </p> <ul> <li> <p>Some EventRules are <code>ACTIVE</code> and some are <code>INACTIVE</code>. Any call can be run.</p> </li> </ul> </li> </ul> </li> </ul>"""
    aggregation_event_type: NotRequired[
        "capo_notifications.types.aggregation_event_type.AggregationEventType"
    ]
    """<p>The notifications aggregation type.</p>"""
    aggregation_summary: NotRequired[
        "capo_notifications.types.aggregation_summary.AggregationSummary"
    ]
    start_time: NotRequired["datetime.datetime"]
    """<p>The earliest time of events to return from this call.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time of the notification event.</p>"""
    text_parts: "capo_notifications.types.text_parts.TextParts"
    """<p>A list of text values.</p>"""
    organizational_unit_id: NotRequired[
        "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
    ]
    """<p>The Organizational Unit Id that an Amazon Web Services account belongs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedNotificationEvent) -> dict:
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
    if "aggregation_event_type" in value:
        out["aggregationEventType"] = value["aggregation_event_type"]
    if "aggregation_summary" in value:
        import capo_notifications.types.aggregation_summary

        out["aggregationSummary"] = (
            capo_notifications.types.aggregation_summary.serialize_json(
                value["aggregation_summary"]
            )
        )
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
    return out


def deserialize_json(data: dict) -> ManagedNotificationEvent:
    out: ManagedNotificationEvent = {}  # type: ignore[typeddict-item]
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    else:
        raise DeserializationError("ManagedNotificationEvent.schema_version required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ManagedNotificationEvent.id required")
    if "messageComponents" in data:
        import capo_notifications.types.message_components

        out["message_components"] = (
            capo_notifications.types.message_components.deserialize_json(
                data["messageComponents"]
            )
        )
    else:
        raise DeserializationError(
            "ManagedNotificationEvent.message_components required"
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
            "ManagedNotificationEvent.notification_type required"
        )
    if "eventStatus" in data:
        out["event_status"] = data["eventStatus"]
    if "aggregationEventType" in data:
        out["aggregation_event_type"] = data["aggregationEventType"]
    if "aggregationSummary" in data:
        import capo_notifications.types.aggregation_summary

        out["aggregation_summary"] = (
            capo_notifications.types.aggregation_summary.deserialize_json(
                data["aggregationSummary"]
            )
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
        raise DeserializationError("ManagedNotificationEvent.text_parts required")
    if "organizationalUnitId" in data:
        out["organizational_unit_id"] = data["organizationalUnitId"]
    return out
