"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingWorkflowOutputSourceConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.id_mapping_workflow_output_source

IdMappingWorkflowOutputSourceConfig: TypeAlias = list[
    "capo_entityresolution.types.id_mapping_workflow_output_source.IdMappingWorkflowOutputSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingWorkflowOutputSourceConfig) -> list:
    import capo_entityresolution.types.id_mapping_workflow_output_source

    out: list = []
    for item in value:
        out.append(
            capo_entityresolution.types.id_mapping_workflow_output_source.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IdMappingWorkflowOutputSourceConfig:
    import capo_entityresolution.types.id_mapping_workflow_output_source

    out: IdMappingWorkflowOutputSourceConfig = []
    for item in data:
        out.append(
            capo_entityresolution.types.id_mapping_workflow_output_source.deserialize_json(
                item
            )
        )
    return out
