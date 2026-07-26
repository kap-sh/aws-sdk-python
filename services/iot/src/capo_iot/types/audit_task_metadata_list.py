"""Generated from Smithy shape ``com.amazonaws.iot#AuditTaskMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.audit_task_metadata

AuditTaskMetadataList: TypeAlias = list[
    "capo_iot.types.audit_task_metadata.AuditTaskMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditTaskMetadataList) -> list:
    import capo_iot.types.audit_task_metadata

    out: list = []
    for item in value:
        out.append(capo_iot.types.audit_task_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> AuditTaskMetadataList:
    import capo_iot.types.audit_task_metadata

    out: AuditTaskMetadataList = []
    for item in data:
        out.append(capo_iot.types.audit_task_metadata.deserialize_json(item))
    return out
