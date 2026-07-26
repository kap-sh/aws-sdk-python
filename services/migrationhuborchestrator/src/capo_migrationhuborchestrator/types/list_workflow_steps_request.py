"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListWorkflowStepsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.max_results
    import capo_migrationhuborchestrator.types.migration_workflow_id
    import capo_migrationhuborchestrator.types.next_token
    import capo_migrationhuborchestrator.types.step_group_id


class ListWorkflowStepsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_migrationhuborchestrator.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    max_results: "capo_migrationhuborchestrator.types.max_results.MaxResults"
    """<p>The maximum number of results that can be returned.</p>"""
    workflow_id: (
        "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    )
    """<p>The ID of the migration workflow.</p>"""
    step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId"
    """<p>The ID of the step group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowStepsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWorkflowStepsRequest:
    out: ListWorkflowStepsRequest = {}  # type: ignore[typeddict-item]
    return out
