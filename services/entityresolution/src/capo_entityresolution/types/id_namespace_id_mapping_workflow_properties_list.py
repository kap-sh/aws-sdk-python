"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdNamespaceIdMappingWorkflowPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.id_namespace_id_mapping_workflow_properties

IdNamespaceIdMappingWorkflowPropertiesList: TypeAlias = list[
    "capo_entityresolution.types.id_namespace_id_mapping_workflow_properties.IdNamespaceIdMappingWorkflowProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceIdMappingWorkflowPropertiesList) -> list:
    import capo_entityresolution.types.id_namespace_id_mapping_workflow_properties

    out: list = []
    for item in value:
        out.append(
            capo_entityresolution.types.id_namespace_id_mapping_workflow_properties.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IdNamespaceIdMappingWorkflowPropertiesList:
    import capo_entityresolution.types.id_namespace_id_mapping_workflow_properties

    out: IdNamespaceIdMappingWorkflowPropertiesList = []
    for item in data:
        out.append(
            capo_entityresolution.types.id_namespace_id_mapping_workflow_properties.deserialize_json(
                item
            )
        )
    return out
