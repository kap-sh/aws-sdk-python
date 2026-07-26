"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ListWorkflowsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mwaa_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.workflow_summaries


class ListWorkflowsResponse(TypedDict, closed=True):
    workflows: "capo_mwaa_serverless.types.workflow_summaries.WorkflowSummaries"
    """<p>A list of workflow summaries for all workflows in your account.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token you need to use to retrieve the next set of results. This value is null if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListWorkflowsResponse) -> dict:
    out: dict = {}
    import capo_mwaa_serverless.types.workflow_summaries

    out["Workflows"] = (
        capo_mwaa_serverless.types.workflow_summaries.serialize_aws_json_1_0(
            value["workflows"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListWorkflowsResponse:
    out: ListWorkflowsResponse = {}  # type: ignore[typeddict-item]
    if "Workflows" in data:
        import capo_mwaa_serverless.types.workflow_summaries

        out["workflows"] = (
            capo_mwaa_serverless.types.workflow_summaries.deserialize_aws_json_1_0(
                data["Workflows"]
            )
        )
    else:
        raise DeserializationError("ListWorkflowsResponse.workflows required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
