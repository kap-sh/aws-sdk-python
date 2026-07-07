"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#GetWorkflowStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_id
    import aws_sdk_migrationhuborchestrator.types.step_group_id
    import aws_sdk_migrationhuborchestrator.types.step_id


class GetWorkflowStepRequest(TypedDict, closed=True):
    workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    """<p>The ID of the migration workflow.</p>"""
    step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId"
    """<p>The ID of the step group.</p>"""
    id: "aws_sdk_migrationhuborchestrator.types.step_id.StepId"
    """<p>The ID of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowStepRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWorkflowStepRequest:
    out: GetWorkflowStepRequest = {}  # type: ignore[typeddict-item]
    return out
