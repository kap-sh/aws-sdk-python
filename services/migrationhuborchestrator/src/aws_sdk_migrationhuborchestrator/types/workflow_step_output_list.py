"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#WorkflowStepOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.workflow_step_output

WorkflowStepOutputList: TypeAlias = list[
    "aws_sdk_migrationhuborchestrator.types.workflow_step_output.WorkflowStepOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepOutputList) -> list:
    import aws_sdk_migrationhuborchestrator.types.workflow_step_output

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhuborchestrator.types.workflow_step_output.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WorkflowStepOutputList:
    import aws_sdk_migrationhuborchestrator.types.workflow_step_output

    out: WorkflowStepOutputList = []
    for item in data:
        out.append(
            aws_sdk_migrationhuborchestrator.types.workflow_step_output.deserialize_json(
                item
            )
        )
    return out
