"""Generated from Smithy shape ``com.amazonaws.glue#ListWorkflowsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.workflow_names


class ListWorkflowsResponse(TypedDict, closed=True):
    workflows: NotRequired["aws_sdk_glue.types.workflow_names.WorkflowNames"]
    """<p>List of names of workflows in the account.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if not all workflow names have been returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWorkflowsResponse) -> dict:
    out: dict = {}
    if "workflows" in value:
        import aws_sdk_glue.types.workflow_names

        out["Workflows"] = aws_sdk_glue.types.workflow_names.serialize_aws_json_1_1(
            value["workflows"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWorkflowsResponse:
    out: ListWorkflowsResponse = {}  # type: ignore[typeddict-item]
    if "Workflows" in data:
        import aws_sdk_glue.types.workflow_names

        out["workflows"] = aws_sdk_glue.types.workflow_names.deserialize_aws_json_1_1(
            data["Workflows"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
