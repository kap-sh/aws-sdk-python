"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowStepExecutionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.workflow_step_metadata

WorkflowStepExecutionsList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.workflow_step_metadata.WorkflowStepMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepExecutionsList) -> list:
    import aws_sdk_imagebuilder.types.workflow_step_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_imagebuilder.types.workflow_step_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WorkflowStepExecutionsList:
    import aws_sdk_imagebuilder.types.workflow_step_metadata

    out: WorkflowStepExecutionsList = []
    for item in data:
        out.append(
            aws_sdk_imagebuilder.types.workflow_step_metadata.deserialize_json(item)
        )
    return out
