"""Generated from Smithy shape ``com.amazonaws.transfer#ListWorkflowsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.listed_workflows
    import aws_sdk_transfer.types.next_token


class ListWorkflowsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_transfer.types.next_token.NextToken"]
    """<p> <code>ListWorkflows</code> returns the <code>NextToken</code> parameter in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional workflows.</p>"""
    workflows: "aws_sdk_transfer.types.listed_workflows.ListedWorkflows"
    """<p>Returns the <code>Arn</code>, <code>WorkflowId</code>, and <code>Description</code> for each workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWorkflowsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_transfer.types.listed_workflows

    out["Workflows"] = aws_sdk_transfer.types.listed_workflows.serialize_aws_json_1_1(
        value["workflows"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWorkflowsResponse:
    out: ListWorkflowsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Workflows" in data:
        import aws_sdk_transfer.types.listed_workflows

        out["workflows"] = (
            aws_sdk_transfer.types.listed_workflows.deserialize_aws_json_1_1(
                data["Workflows"]
            )
        )
    else:
        raise DeserializationError("ListWorkflowsResponse.workflows required")
    return out
