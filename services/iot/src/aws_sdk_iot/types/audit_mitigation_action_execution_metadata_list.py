"""Generated from Smithy shape ``com.amazonaws.iot#AuditMitigationActionExecutionMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_mitigation_action_execution_metadata

AuditMitigationActionExecutionMetadataList: TypeAlias = list[
    "aws_sdk_iot.types.audit_mitigation_action_execution_metadata.AuditMitigationActionExecutionMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditMitigationActionExecutionMetadataList) -> list:
    import aws_sdk_iot.types.audit_mitigation_action_execution_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot.types.audit_mitigation_action_execution_metadata.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AuditMitigationActionExecutionMetadataList:
    import aws_sdk_iot.types.audit_mitigation_action_execution_metadata

    out: AuditMitigationActionExecutionMetadataList = []
    for item in data:
        out.append(
            aws_sdk_iot.types.audit_mitigation_action_execution_metadata.deserialize_json(
                item
            )
        )
    return out
