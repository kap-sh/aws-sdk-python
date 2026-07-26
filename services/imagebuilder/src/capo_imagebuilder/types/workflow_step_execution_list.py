"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowStepExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.workflow_step_execution

WorkflowStepExecutionList: TypeAlias = list[
    "capo_imagebuilder.types.workflow_step_execution.WorkflowStepExecution"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepExecutionList) -> list:
    import capo_imagebuilder.types.workflow_step_execution

    out: list = []
    for item in value:
        out.append(capo_imagebuilder.types.workflow_step_execution.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkflowStepExecutionList:
    import capo_imagebuilder.types.workflow_step_execution

    out: WorkflowStepExecutionList = []
    for item in data:
        out.append(
            capo_imagebuilder.types.workflow_step_execution.deserialize_json(item)
        )
    return out
