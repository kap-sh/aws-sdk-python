"""Generated from Smithy shape ``com.amazonaws.connectcases#AuditEventField``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.audit_event_field_id
    import aws_sdk_connectcases.types.audit_event_field_value_union


class AuditEventField(TypedDict):
    event_field_id: "aws_sdk_connectcases.types.audit_event_field_id.AuditEventFieldId"
    """<p>Unique identifier of field in an Audit History entry.</p>"""
    old_value: NotRequired[
        "aws_sdk_connectcases.types.audit_event_field_value_union.AuditEventFieldValueUnion"
    ]
    """<p>Union of potential field value types.</p>"""
    new_value: "aws_sdk_connectcases.types.audit_event_field_value_union.AuditEventFieldValueUnion"
    """<p>Union of potential field value types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditEventField) -> dict:
    out: dict = {}
    out["eventFieldId"] = value["event_field_id"]
    if "old_value" in value:
        import aws_sdk_connectcases.types.audit_event_field_value_union

        out["oldValue"] = (
            aws_sdk_connectcases.types.audit_event_field_value_union.serialize_json(
                value["old_value"]
            )
        )
    import aws_sdk_connectcases.types.audit_event_field_value_union

    out["newValue"] = (
        aws_sdk_connectcases.types.audit_event_field_value_union.serialize_json(
            value["new_value"]
        )
    )
    return out


def deserialize_json(data: dict) -> AuditEventField:
    out: AuditEventField = {}  # type: ignore[typeddict-item]
    if "eventFieldId" in data:
        out["event_field_id"] = data["eventFieldId"]
    else:
        raise DeserializationError("AuditEventField.event_field_id required")
    if "oldValue" in data:
        import aws_sdk_connectcases.types.audit_event_field_value_union

        out["old_value"] = (
            aws_sdk_connectcases.types.audit_event_field_value_union.deserialize_json(
                data["oldValue"]
            )
        )
    if "newValue" in data:
        import aws_sdk_connectcases.types.audit_event_field_value_union

        out["new_value"] = (
            aws_sdk_connectcases.types.audit_event_field_value_union.deserialize_json(
                data["newValue"]
            )
        )
    else:
        raise DeserializationError("AuditEventField.new_value required")
    return out
