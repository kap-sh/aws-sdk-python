"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#AuditEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail_data.types.audit_event

AuditEvents: TypeAlias = list["capo_cloudtrail_data.types.audit_event.AuditEvent"]


# --- restJson1 ser/de ---
def serialize_json(value: AuditEvents) -> list:
    import capo_cloudtrail_data.types.audit_event

    out: list = []
    for item in value:
        out.append(capo_cloudtrail_data.types.audit_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> AuditEvents:
    import capo_cloudtrail_data.types.audit_event

    out: AuditEvents = []
    for item in data:
        out.append(capo_cloudtrail_data.types.audit_event.deserialize_json(item))
    return out
