"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowStepExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.workflow_step_execution

WorkflowStepExecutionList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.workflow_step_execution.WorkflowStepExecution"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepExecutionList) -> list:
    import aws_sdk_imagebuilder.types.workflow_step_execution

    out: list = []
    for item in value:
        out.append(
            aws_sdk_imagebuilder.types.workflow_step_execution.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WorkflowStepExecutionList:
    import aws_sdk_imagebuilder.types.workflow_step_execution

    out: WorkflowStepExecutionList = []
    for item in data:
        out.append(
            aws_sdk_imagebuilder.types.workflow_step_execution.deserialize_json(item)
        )
    return out
