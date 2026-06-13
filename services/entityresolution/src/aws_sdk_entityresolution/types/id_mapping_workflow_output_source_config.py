"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingWorkflowOutputSourceConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.id_mapping_workflow_output_source

IdMappingWorkflowOutputSourceConfig: TypeAlias = list[
    "aws_sdk_entityresolution.types.id_mapping_workflow_output_source.IdMappingWorkflowOutputSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingWorkflowOutputSourceConfig) -> list:
    import aws_sdk_entityresolution.types.id_mapping_workflow_output_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_entityresolution.types.id_mapping_workflow_output_source.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IdMappingWorkflowOutputSourceConfig:
    import aws_sdk_entityresolution.types.id_mapping_workflow_output_source

    out: IdMappingWorkflowOutputSourceConfig = []
    for item in data:
        out.append(
            aws_sdk_entityresolution.types.id_mapping_workflow_output_source.deserialize_json(
                item
            )
        )
    return out
