"""Generated from Smithy shape ``com.amazonaws.iot#ScheduledAuditMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.scheduled_audit_metadata

ScheduledAuditMetadataList: TypeAlias = list[
    "capo_iot.types.scheduled_audit_metadata.ScheduledAuditMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledAuditMetadataList) -> list:
    import capo_iot.types.scheduled_audit_metadata

    out: list = []
    for item in value:
        out.append(capo_iot.types.scheduled_audit_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScheduledAuditMetadataList:
    import capo_iot.types.scheduled_audit_metadata

    out: ScheduledAuditMetadataList = []
    for item in data:
        out.append(capo_iot.types.scheduled_audit_metadata.deserialize_json(item))
    return out
