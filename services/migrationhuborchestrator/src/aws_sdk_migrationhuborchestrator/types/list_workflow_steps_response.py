"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListWorkflowStepsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_migrationhuborchestrator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.next_token
    import aws_sdk_migrationhuborchestrator.types.workflow_steps_summary_list


class ListWorkflowStepsResponse(TypedDict):
    next_token: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.next_token.NextToken"
    ]
    """<p>The pagination token.</p>"""
    workflow_steps_summary: "aws_sdk_migrationhuborchestrator.types.workflow_steps_summary_list.WorkflowStepsSummaryList"
    """<p>The summary of steps in a migration workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowStepsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_migrationhuborchestrator.types.workflow_steps_summary_list

    out["workflowStepsSummary"] = (
        aws_sdk_migrationhuborchestrator.types.workflow_steps_summary_list.serialize_json(
            value["workflow_steps_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListWorkflowStepsResponse:
    out: ListWorkflowStepsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "workflowStepsSummary" in data:
        import aws_sdk_migrationhuborchestrator.types.workflow_steps_summary_list

        out["workflow_steps_summary"] = (
            aws_sdk_migrationhuborchestrator.types.workflow_steps_summary_list.deserialize_json(
                data["workflowStepsSummary"]
            )
        )
    else:
        raise DeserializationError(
            "ListWorkflowStepsResponse.workflow_steps_summary required"
        )
    return out
