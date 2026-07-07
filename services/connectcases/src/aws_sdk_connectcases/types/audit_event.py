"""Generated from Smithy shape ``com.amazonaws.connectcases#AuditEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.audit_event_date_time
    import aws_sdk_connectcases.types.audit_event_field_list
    import aws_sdk_connectcases.types.audit_event_id
    import aws_sdk_connectcases.types.audit_event_performed_by
    import aws_sdk_connectcases.types.audit_event_type
    import aws_sdk_connectcases.types.related_item_type


class AuditEvent(TypedDict, closed=True):
    event_id: "aws_sdk_connectcases.types.audit_event_id.AuditEventId"
    """<p>Unique identifier of a case audit history event.</p>"""
    type: "aws_sdk_connectcases.types.audit_event_type.AuditEventType"
    """<p>The type of audit history event.</p> <p>Valid Values: <code>Case.Created</code> | <code>Case.Updated</code> | <code>RelatedItem.Created</code> | <code>RelatedItem.Updated</code> | <code>RelatedItem.Deleted</code> </p>"""
    related_item_type: NotRequired[
        "aws_sdk_connectcases.types.related_item_type.RelatedItemType"
    ]
    """<p>The Type of the related item.</p>"""
    performed_time: (
        "aws_sdk_connectcases.types.audit_event_date_time.AuditEventDateTime"
    )
    """<p>Time at which an Audit History event took place.</p>"""
    fields: "aws_sdk_connectcases.types.audit_event_field_list.AuditEventFieldList"
    """<p>A list of Case Audit History event fields.</p>"""
    performed_by: NotRequired[
        "aws_sdk_connectcases.types.audit_event_performed_by.AuditEventPerformedBy"
    ]
    """<p>Information of the user which performed the audit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditEvent) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    out["type"] = value["type"]
    if "related_item_type" in value:
        out["relatedItemType"] = value["related_item_type"]
    import aws_sdk_connectcases.types.audit_event_date_time

    out["performedTime"] = (
        aws_sdk_connectcases.types.audit_event_date_time.serialize_json(
            value["performed_time"]
        )
    )
    import aws_sdk_connectcases.types.audit_event_field_list

    out["fields"] = aws_sdk_connectcases.types.audit_event_field_list.serialize_json(
        value["fields"]
    )
    if "performed_by" in value:
        import aws_sdk_connectcases.types.audit_event_performed_by

        out["performedBy"] = (
            aws_sdk_connectcases.types.audit_event_performed_by.serialize_json(
                value["performed_by"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuditEvent:
    out: AuditEvent = {}  # type: ignore[typeddict-item]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    else:
        raise DeserializationError("AuditEvent.event_id required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("AuditEvent.type required")
    if "relatedItemType" in data:
        out["related_item_type"] = data["relatedItemType"]
    if "performedTime" in data:
        import aws_sdk_connectcases.types.audit_event_date_time

        out["performed_time"] = (
            aws_sdk_connectcases.types.audit_event_date_time.deserialize_json(
                data["performedTime"]
            )
        )
    else:
        raise DeserializationError("AuditEvent.performed_time required")
    if "fields" in data:
        import aws_sdk_connectcases.types.audit_event_field_list

        out["fields"] = (
            aws_sdk_connectcases.types.audit_event_field_list.deserialize_json(
                data["fields"]
            )
        )
    else:
        raise DeserializationError("AuditEvent.fields required")
    if "performedBy" in data:
        import aws_sdk_connectcases.types.audit_event_performed_by

        out["performed_by"] = (
            aws_sdk_connectcases.types.audit_event_performed_by.deserialize_json(
                data["performedBy"]
            )
        )
    return out
