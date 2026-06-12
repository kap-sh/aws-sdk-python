"""Generated from Smithy shape ``com.amazonaws.transfer#ListExecutionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.listed_executions
    import aws_sdk_transfer.types.next_token
    import aws_sdk_transfer.types.workflow_id


class ListExecutionsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_transfer.types.next_token.NextToken"]
    """<p> <code>ListExecutions</code> returns the <code>NextToken</code> parameter in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional executions.</p>"""
    workflow_id: "aws_sdk_transfer.types.workflow_id.WorkflowId"
    """<p>A unique identifier for the workflow.</p>"""
    executions: "aws_sdk_transfer.types.listed_executions.ListedExecutions"
    """<p>Returns the details for each execution, in a <code>ListedExecution</code> array.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListExecutionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["WorkflowId"] = value["workflow_id"]
    import aws_sdk_transfer.types.listed_executions

    out["Executions"] = aws_sdk_transfer.types.listed_executions.serialize_aws_json_1_1(
        value["executions"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListExecutionsResponse:
    out: ListExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "WorkflowId" in data:
        out["workflow_id"] = data["WorkflowId"]
    else:
        raise DeserializationError("ListExecutionsResponse.workflow_id required")
    if "Executions" in data:
        import aws_sdk_transfer.types.listed_executions

        out["executions"] = (
            aws_sdk_transfer.types.listed_executions.deserialize_aws_json_1_1(
                data["Executions"]
            )
        )
    else:
        raise DeserializationError("ListExecutionsResponse.executions required")
    return out
