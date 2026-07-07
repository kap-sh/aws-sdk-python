"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetWorkflowsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.workflow_names
    import aws_sdk_glue.types.workflows


class BatchGetWorkflowsResponse(TypedDict, closed=True):
    workflows: NotRequired["aws_sdk_glue.types.workflows.Workflows"]
    """<p>A list of workflow resource metadata.</p>"""
    missing_workflows: NotRequired["aws_sdk_glue.types.workflow_names.WorkflowNames"]
    """<p>A list of names of workflows not found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetWorkflowsResponse) -> dict:
    out: dict = {}
    if "workflows" in value:
        import aws_sdk_glue.types.workflows

        out["Workflows"] = aws_sdk_glue.types.workflows.serialize_aws_json_1_1(
            value["workflows"]
        )
    if "missing_workflows" in value:
        import aws_sdk_glue.types.workflow_names

        out["MissingWorkflows"] = (
            aws_sdk_glue.types.workflow_names.serialize_aws_json_1_1(
                value["missing_workflows"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetWorkflowsResponse:
    out: BatchGetWorkflowsResponse = {}  # type: ignore[typeddict-item]
    if "Workflows" in data:
        import aws_sdk_glue.types.workflows

        out["workflows"] = aws_sdk_glue.types.workflows.deserialize_aws_json_1_1(
            data["Workflows"]
        )
    if "MissingWorkflows" in data:
        import aws_sdk_glue.types.workflow_names

        out["missing_workflows"] = (
            aws_sdk_glue.types.workflow_names.deserialize_aws_json_1_1(
                data["MissingWorkflows"]
            )
        )
    return out
