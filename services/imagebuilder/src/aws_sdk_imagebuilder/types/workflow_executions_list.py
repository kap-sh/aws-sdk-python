"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowExecutionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.workflow_execution_metadata

WorkflowExecutionsList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.workflow_execution_metadata.WorkflowExecutionMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowExecutionsList) -> list:
    import aws_sdk_imagebuilder.types.workflow_execution_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_imagebuilder.types.workflow_execution_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WorkflowExecutionsList:
    import aws_sdk_imagebuilder.types.workflow_execution_metadata

    out: WorkflowExecutionsList = []
    for item in data:
        out.append(
            aws_sdk_imagebuilder.types.workflow_execution_metadata.deserialize_json(
                item
            )
        )
    return out
