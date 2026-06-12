"""Generated from Smithy shape ``com.amazonaws.iot#AuditMitigationActionsTaskMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_mitigation_actions_task_metadata

AuditMitigationActionsTaskMetadataList: TypeAlias = list[
    "aws_sdk_iot.types.audit_mitigation_actions_task_metadata.AuditMitigationActionsTaskMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditMitigationActionsTaskMetadataList) -> list:
    import aws_sdk_iot.types.audit_mitigation_actions_task_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot.types.audit_mitigation_actions_task_metadata.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AuditMitigationActionsTaskMetadataList:
    import aws_sdk_iot.types.audit_mitigation_actions_task_metadata

    out: AuditMitigationActionsTaskMetadataList = []
    for item in data:
        out.append(
            aws_sdk_iot.types.audit_mitigation_actions_task_metadata.deserialize_json(
                item
            )
        )
    return out
