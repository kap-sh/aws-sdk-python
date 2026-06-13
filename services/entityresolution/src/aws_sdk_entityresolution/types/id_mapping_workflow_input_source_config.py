"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingWorkflowInputSourceConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.id_mapping_workflow_input_source

IdMappingWorkflowInputSourceConfig: TypeAlias = list[
    "aws_sdk_entityresolution.types.id_mapping_workflow_input_source.IdMappingWorkflowInputSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingWorkflowInputSourceConfig) -> list:
    import aws_sdk_entityresolution.types.id_mapping_workflow_input_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_entityresolution.types.id_mapping_workflow_input_source.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IdMappingWorkflowInputSourceConfig:
    import aws_sdk_entityresolution.types.id_mapping_workflow_input_source

    out: IdMappingWorkflowInputSourceConfig = []
    for item in data:
        out.append(
            aws_sdk_entityresolution.types.id_mapping_workflow_input_source.deserialize_json(
                item
            )
        )
    return out
