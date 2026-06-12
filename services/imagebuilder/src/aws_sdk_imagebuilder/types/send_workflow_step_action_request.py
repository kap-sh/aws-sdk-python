"""Generated from Smithy shape ``com.amazonaws.imagebuilder#SendWorkflowStepActionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.image_build_version_arn
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.workflow_step_action_type
    import aws_sdk_imagebuilder.types.workflow_step_execution_id


class SendWorkflowStepActionRequest(TypedDict):
    step_execution_id: (
        "aws_sdk_imagebuilder.types.workflow_step_execution_id.WorkflowStepExecutionId"
    )
    """<p>Uniquely identifies the workflow step that sent the step action.</p>"""
    image_build_version_arn: (
        "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the image build version to send action for.</p>"""
    action: (
        "aws_sdk_imagebuilder.types.workflow_step_action_type.WorkflowStepActionType"
    )
    """<p>The action for the image creation process to take while a workflow <code>WaitForAction</code> step waits for an asynchronous action to complete.</p>"""
    reason: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The reason why this action is sent.</p>"""
    client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken"
    """<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendWorkflowStepActionRequest) -> dict:
    out: dict = {}
    out["stepExecutionId"] = value["step_execution_id"]
    out["imageBuildVersionArn"] = value["image_build_version_arn"]
    import aws_sdk_imagebuilder.types.workflow_step_action_type

    out["action"] = aws_sdk_imagebuilder.types.workflow_step_action_type.serialize_json(
        value["action"]
    )
    if "reason" in value:
        out["reason"] = value["reason"]
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> SendWorkflowStepActionRequest:
    out: SendWorkflowStepActionRequest = {}  # type: ignore[typeddict-item]
    if "stepExecutionId" in data:
        out["step_execution_id"] = data["stepExecutionId"]
    else:
        raise DeserializationError(
            "SendWorkflowStepActionRequest.step_execution_id required"
        )
    if "imageBuildVersionArn" in data:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    else:
        raise DeserializationError(
            "SendWorkflowStepActionRequest.image_build_version_arn required"
        )
    if "action" in data:
        import aws_sdk_imagebuilder.types.workflow_step_action_type

        out["action"] = (
            aws_sdk_imagebuilder.types.workflow_step_action_type.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("SendWorkflowStepActionRequest.action required")
    if "reason" in data:
        out["reason"] = data["reason"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "SendWorkflowStepActionRequest.client_token required"
        )
    return out
