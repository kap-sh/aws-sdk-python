"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdNamespaceIdMappingWorkflowPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_properties

IdNamespaceIdMappingWorkflowPropertiesList: TypeAlias = list[
    "aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_properties.IdNamespaceIdMappingWorkflowProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceIdMappingWorkflowPropertiesList) -> list:
    import aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_properties.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IdNamespaceIdMappingWorkflowPropertiesList:
    import aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_properties

    out: IdNamespaceIdMappingWorkflowPropertiesList = []
    for item in data:
        out.append(
            aws_sdk_entityresolution.types.id_namespace_id_mapping_workflow_properties.deserialize_json(
                item
            )
        )
    return out
