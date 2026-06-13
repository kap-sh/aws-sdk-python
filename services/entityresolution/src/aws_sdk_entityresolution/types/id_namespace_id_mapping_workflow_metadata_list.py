"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdNamespaceIdMappingWorkflowMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_metadata

IdNamespaceIdMappingWorkflowMetadataList: TypeAlias = list[
    "aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_metadata.IdNamespaceIdMappingWorkflowMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceIdMappingWorkflowMetadataList) -> list:
    import aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_metadata.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IdNamespaceIdMappingWorkflowMetadataList:
    import aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_metadata

    out: IdNamespaceIdMappingWorkflowMetadataList = []
    for item in data:
        out.append(
            aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_metadata.deserialize_json(
                item
            )
        )
    return out
