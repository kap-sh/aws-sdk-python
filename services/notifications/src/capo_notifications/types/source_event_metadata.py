"""Generated from Smithy shape ``com.amazonaws.notifications#SourceEventMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_notifications.types.account_id
    import capo_notifications.types.region
    import capo_notifications.types.resources
    import capo_notifications.types.source


class SourceEventMetadata(TypedDict, closed=True):
    event_type_version: "str"
    """<p>The version of the type of event.</p>"""
    source_event_id: "str"
    """<p>The source event id.</p>"""
    event_origin_region: NotRequired["capo_notifications.types.region.Region"]
    """<p>The Region the event originated from.</p>"""
    related_account: "capo_notifications.types.account_id.AccountId"
    """<p>The primary Amazon Web Services account of <code>SourceEvent</code>.</p>"""
    source: "capo_notifications.types.source.Source"
    """<p>The Amazon Web Services service the event originates from. For example <code>aws.cloudwatch</code>.</p>"""
    event_occurrence_time: "datetime.datetime"
    """<p>The date and time the source event occurred. This is based on the Source Event.</p>"""
    event_type: "str"
    """<p>The type of event. For example, an Amazon CloudWatch state change.</p>"""
    related_resources: "capo_notifications.types.resources.Resources"
    """<p>A list of resources related to this <code>NotificationEvent</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceEventMetadata) -> dict:
    out: dict = {}
    out["eventTypeVersion"] = value["event_type_version"]
    out["sourceEventId"] = value["source_event_id"]
    if "event_origin_region" in value:
        out["eventOriginRegion"] = value["event_origin_region"]
    out["relatedAccount"] = value["related_account"]
    out["source"] = value["source"]
    import capo_notifications.types._prelude.timestamp

    out["eventOccurrenceTime"] = (
        capo_notifications.types._prelude.timestamp.serialize_json(
            value["event_occurrence_time"]
        )
    )
    out["eventType"] = value["event_type"]
    import capo_notifications.types.resources

    out["relatedResources"] = capo_notifications.types.resources.serialize_json(
        value["related_resources"]
    )
    return out


def deserialize_json(data: dict) -> SourceEventMetadata:
    out: SourceEventMetadata = {}  # type: ignore[typeddict-item]
    if "eventTypeVersion" in data:
        out["event_type_version"] = data["eventTypeVersion"]
    else:
        raise DeserializationError("SourceEventMetadata.event_type_version required")
    if "sourceEventId" in data:
        out["source_event_id"] = data["sourceEventId"]
    else:
        raise DeserializationError("SourceEventMetadata.source_event_id required")
    if "eventOriginRegion" in data:
        out["event_origin_region"] = data["eventOriginRegion"]
    if "relatedAccount" in data:
        out["related_account"] = data["relatedAccount"]
    else:
        raise DeserializationError("SourceEventMetadata.related_account required")
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("SourceEventMetadata.source required")
    if "eventOccurrenceTime" in data:
        import capo_notifications.types._prelude.timestamp

        out["event_occurrence_time"] = (
            capo_notifications.types._prelude.timestamp.deserialize_json(
                data["eventOccurrenceTime"]
            )
        )
    else:
        raise DeserializationError("SourceEventMetadata.event_occurrence_time required")
    if "eventType" in data:
        out["event_type"] = data["eventType"]
    else:
        raise DeserializationError("SourceEventMetadata.event_type required")
    if "relatedResources" in data:
        import capo_notifications.types.resources

        out["related_resources"] = capo_notifications.types.resources.deserialize_json(
            data["relatedResources"]
        )
    else:
        raise DeserializationError("SourceEventMetadata.related_resources required")
    return out
