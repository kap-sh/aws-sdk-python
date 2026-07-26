"""Generated from Smithy shape ``com.amazonaws.iot#AuditMitigationActionsTaskMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.audit_mitigation_actions_task_metadata

AuditMitigationActionsTaskMetadataList: TypeAlias = list[
    "capo_iot.types.audit_mitigation_actions_task_metadata.AuditMitigationActionsTaskMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditMitigationActionsTaskMetadataList) -> list:
    import capo_iot.types.audit_mitigation_actions_task_metadata

    out: list = []
    for item in value:
        out.append(
            capo_iot.types.audit_mitigation_actions_task_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AuditMitigationActionsTaskMetadataList:
    import capo_iot.types.audit_mitigation_actions_task_metadata

    out: AuditMitigationActionsTaskMetadataList = []
    for item in data:
        out.append(
            capo_iot.types.audit_mitigation_actions_task_metadata.deserialize_json(item)
        )
    return out
