"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#AuditEventResultEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail_data.types.audit_event_result_entry

AuditEventResultEntries: TypeAlias = list[
    "capo_cloudtrail_data.types.audit_event_result_entry.AuditEventResultEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditEventResultEntries) -> list:
    import capo_cloudtrail_data.types.audit_event_result_entry

    out: list = []
    for item in value:
        out.append(
            capo_cloudtrail_data.types.audit_event_result_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AuditEventResultEntries:
    import capo_cloudtrail_data.types.audit_event_result_entry

    out: AuditEventResultEntries = []
    for item in data:
        out.append(
            capo_cloudtrail_data.types.audit_event_result_entry.deserialize_json(item)
        )
    return out
