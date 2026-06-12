"""Generated from Smithy shape ``com.amazonaws.iot#AuditTaskMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_task_metadata

AuditTaskMetadataList: TypeAlias = list[
    "aws_sdk_iot.types.audit_task_metadata.AuditTaskMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditTaskMetadataList) -> list:
    import aws_sdk_iot.types.audit_task_metadata

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.audit_task_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> AuditTaskMetadataList:
    import aws_sdk_iot.types.audit_task_metadata

    out: AuditTaskMetadataList = []
    for item in data:
        out.append(aws_sdk_iot.types.audit_task_metadata.deserialize_json(item))
    return out
