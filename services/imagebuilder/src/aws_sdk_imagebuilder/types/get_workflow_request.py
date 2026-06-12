"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetWorkflowRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.workflow_version_arn_or_build_version_arn


class GetWorkflowRequest(TypedDict):
    workflow_build_version_arn: "aws_sdk_imagebuilder.types.workflow_version_arn_or_build_version_arn.WorkflowVersionArnOrBuildVersionArn"
    """<p>The Amazon Resource Name (ARN) of the workflow resource that you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWorkflowRequest:
    out: GetWorkflowRequest = {}  # type: ignore[typeddict-item]
    return out
