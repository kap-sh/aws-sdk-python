"""Generated from Smithy shape ``com.amazonaws.imagebuilder#SendWorkflowStepActionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.image_build_version_arn
    import aws_sdk_imagebuilder.types.workflow_step_execution_id


class SendWorkflowStepActionResponse(TypedDict):
    step_execution_id: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_step_execution_id.WorkflowStepExecutionId"
    ]
    """<p>The workflow step that sent the step action.</p>"""
    image_build_version_arn: NotRequired[
        "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image build version that received the action request.</p>"""
    client_token: NotRequired["aws_sdk_imagebuilder.types.client_token.ClientToken"]
    """<p>The client token that uniquely identifies the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendWorkflowStepActionResponse) -> dict:
    out: dict = {}
    if "step_execution_id" in value:
        out["stepExecutionId"] = value["step_execution_id"]
    if "image_build_version_arn" in value:
        out["imageBuildVersionArn"] = value["image_build_version_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> SendWorkflowStepActionResponse:
    out: SendWorkflowStepActionResponse = {}  # type: ignore[typeddict-item]
    if "stepExecutionId" in data:
        out["step_execution_id"] = data["stepExecutionId"]
    if "imageBuildVersionArn" in data:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
