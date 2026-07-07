"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#DeleteWorkflowStepGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_id
    import aws_sdk_migrationhuborchestrator.types.step_group_id


class DeleteWorkflowStepGroupRequest(TypedDict, closed=True):
    workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    """<p>The ID of the migration workflow.</p>"""
    id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId"
    """<p>The ID of the step group you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkflowStepGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkflowStepGroupRequest:
    out: DeleteWorkflowStepGroupRequest = {}  # type: ignore[typeddict-item]
    return out
