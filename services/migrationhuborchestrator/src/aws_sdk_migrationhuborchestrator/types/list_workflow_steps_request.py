"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListWorkflowStepsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.max_results
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_id
    import aws_sdk_migrationhuborchestrator.types.next_token
    import aws_sdk_migrationhuborchestrator.types.step_group_id


class ListWorkflowStepsRequest(TypedDict):
    next_token: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.next_token.NextToken"
    ]
    """<p>The pagination token.</p>"""
    max_results: "aws_sdk_migrationhuborchestrator.types.max_results.MaxResults"
    """<p>The maximum number of results that can be returned.</p>"""
    workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    """<p>The ID of the migration workflow.</p>"""
    step_group_id: "aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId"
    """<p>The ID of the step group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowStepsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWorkflowStepsRequest:
    out: ListWorkflowStepsRequest = {}  # type: ignore[typeddict-item]
    return out
