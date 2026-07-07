"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListWorkflowStepGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.max_results
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_id
    import aws_sdk_migrationhuborchestrator.types.next_token


class ListWorkflowStepGroupsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.next_token.NextToken"
    ]
    """<p>The pagination token.</p>"""
    max_results: "aws_sdk_migrationhuborchestrator.types.max_results.MaxResults"
    """<p>The maximum number of results that can be returned.</p>"""
    workflow_id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    """<p>The ID of the migration workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowStepGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWorkflowStepGroupsRequest:
    out: ListWorkflowStepGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
