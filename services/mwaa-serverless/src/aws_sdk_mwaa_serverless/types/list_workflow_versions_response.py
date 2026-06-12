"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ListWorkflowVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.workflow_version_summaries


class ListWorkflowVersionsResponse(TypedDict):
    workflow_versions: NotRequired[
        "aws_sdk_mwaa_serverless.types.workflow_version_summaries.WorkflowVersionSummaries"
    ]
    """<p>A list of workflow version summaries for the specified workflow.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token you need to use to retrieve the next set of results. This value is null if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListWorkflowVersionsResponse) -> dict:
    out: dict = {}
    if "workflow_versions" in value:
        import aws_sdk_mwaa_serverless.types.workflow_version_summaries

        out["WorkflowVersions"] = (
            aws_sdk_mwaa_serverless.types.workflow_version_summaries.serialize_aws_json_1_0(
                value["workflow_versions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListWorkflowVersionsResponse:
    out: ListWorkflowVersionsResponse = {}  # type: ignore[typeddict-item]
    if "WorkflowVersions" in data:
        import aws_sdk_mwaa_serverless.types.workflow_version_summaries

        out["workflow_versions"] = (
            aws_sdk_mwaa_serverless.types.workflow_version_summaries.deserialize_aws_json_1_0(
                data["WorkflowVersions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
