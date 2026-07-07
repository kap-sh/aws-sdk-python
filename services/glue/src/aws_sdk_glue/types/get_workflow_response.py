"""Generated from Smithy shape ``com.amazonaws.glue#GetWorkflowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.workflow


class GetWorkflowResponse(TypedDict, closed=True):
    workflow: NotRequired["aws_sdk_glue.types.workflow.Workflow"]
    """<p>The resource metadata for the workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWorkflowResponse) -> dict:
    out: dict = {}
    if "workflow" in value:
        import aws_sdk_glue.types.workflow

        out["Workflow"] = aws_sdk_glue.types.workflow.serialize_aws_json_1_1(
            value["workflow"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWorkflowResponse:
    out: GetWorkflowResponse = {}  # type: ignore[typeddict-item]
    if "Workflow" in data:
        import aws_sdk_glue.types.workflow

        out["workflow"] = aws_sdk_glue.types.workflow.deserialize_aws_json_1_1(
            data["Workflow"]
        )
    return out
