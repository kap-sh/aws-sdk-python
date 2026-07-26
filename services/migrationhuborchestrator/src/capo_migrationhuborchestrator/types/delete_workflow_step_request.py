"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#DeleteWorkflowStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.migration_workflow_id
    import capo_migrationhuborchestrator.types.step_group_id
    import capo_migrationhuborchestrator.types.step_id


class DeleteWorkflowStepRequest(TypedDict, closed=True):
    id: "capo_migrationhuborchestrator.types.step_id.StepId"
    """<p>The ID of the step you want to delete.</p>"""
    step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId"
    """<p>The ID of the step group that contains the step you want to delete.</p>"""
    workflow_id: (
        "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    )
    """<p>The ID of the migration workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkflowStepRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkflowStepRequest:
    out: DeleteWorkflowStepRequest = {}  # type: ignore[typeddict-item]
    return out
