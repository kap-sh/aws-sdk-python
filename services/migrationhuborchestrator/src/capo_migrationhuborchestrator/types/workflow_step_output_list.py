"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#WorkflowStepOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.workflow_step_output

WorkflowStepOutputList: TypeAlias = list[
    "capo_migrationhuborchestrator.types.workflow_step_output.WorkflowStepOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepOutputList) -> list:
    import capo_migrationhuborchestrator.types.workflow_step_output

    out: list = []
    for item in value:
        out.append(
            capo_migrationhuborchestrator.types.workflow_step_output.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WorkflowStepOutputList:
    import capo_migrationhuborchestrator.types.workflow_step_output

    out: WorkflowStepOutputList = []
    for item in data:
        out.append(
            capo_migrationhuborchestrator.types.workflow_step_output.deserialize_json(
                item
            )
        )
    return out
