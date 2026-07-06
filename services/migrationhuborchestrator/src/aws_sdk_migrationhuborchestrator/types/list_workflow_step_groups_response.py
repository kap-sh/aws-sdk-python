"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListWorkflowStepGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_migrationhuborchestrator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.next_token
    import aws_sdk_migrationhuborchestrator.types.workflow_step_groups_summary_list


class ListWorkflowStepGroupsResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.next_token.NextToken"
    ]
    """<p>The pagination token.</p>"""
    workflow_step_groups_summary: "aws_sdk_migrationhuborchestrator.types.workflow_step_groups_summary_list.WorkflowStepGroupsSummaryList"
    """<p>The summary of step groups in a migration workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowStepGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_migrationhuborchestrator.types.workflow_step_groups_summary_list

    out["workflowStepGroupsSummary"] = (
        aws_sdk_migrationhuborchestrator.types.workflow_step_groups_summary_list.serialize_json(
            value["workflow_step_groups_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListWorkflowStepGroupsResponse:
    out: ListWorkflowStepGroupsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "workflowStepGroupsSummary" in data:
        import aws_sdk_migrationhuborchestrator.types.workflow_step_groups_summary_list

        out["workflow_step_groups_summary"] = (
            aws_sdk_migrationhuborchestrator.types.workflow_step_groups_summary_list.deserialize_json(
                data["workflowStepGroupsSummary"]
            )
        )
    else:
        raise DeserializationError(
            "ListWorkflowStepGroupsResponse.workflow_step_groups_summary required"
        )
    return out
