"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListWorkflowStepExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_build_message
    import aws_sdk_imagebuilder.types.image_build_version_arn
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.pagination_token
    import aws_sdk_imagebuilder.types.workflow_build_version_arn
    import aws_sdk_imagebuilder.types.workflow_execution_id
    import aws_sdk_imagebuilder.types.workflow_step_executions_list


class ListWorkflowStepExecutionsResponse(TypedDict, closed=True):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    steps: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_step_executions_list.WorkflowStepExecutionsList"
    ]
    """<p>Contains an array of runtime details that represents each step in this runtime instance of the workflow.</p>"""
    workflow_build_version_arn: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_build_version_arn.WorkflowBuildVersionArn"
    ]
    """<p>The build version Amazon Resource Name (ARN) for the Image Builder workflow resource that defines the steps for this runtime instance of the workflow.</p>"""
    workflow_execution_id: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_execution_id.WorkflowExecutionId"
    ]
    """<p>The unique identifier that Image Builder assigned to keep track of runtime details when it ran the workflow.</p>"""
    image_build_version_arn: NotRequired[
        "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    ]
    """<p>The image build version resource Amazon Resource Name (ARN) that's associated with the specified runtime instance of the workflow.</p>"""
    message: NotRequired[
        "aws_sdk_imagebuilder.types.image_build_message.ImageBuildMessage"
    ]
    """<p>The output message from the list action, if applicable.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowStepExecutionsResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "steps" in value:
        import aws_sdk_imagebuilder.types.workflow_step_executions_list

        out["steps"] = (
            aws_sdk_imagebuilder.types.workflow_step_executions_list.serialize_json(
                value["steps"]
            )
        )
    if "workflow_build_version_arn" in value:
        out["workflowBuildVersionArn"] = value["workflow_build_version_arn"]
    if "workflow_execution_id" in value:
        out["workflowExecutionId"] = value["workflow_execution_id"]
    if "image_build_version_arn" in value:
        out["imageBuildVersionArn"] = value["image_build_version_arn"]
    if "message" in value:
        out["message"] = value["message"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkflowStepExecutionsResponse:
    out: ListWorkflowStepExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "steps" in data:
        import aws_sdk_imagebuilder.types.workflow_step_executions_list

        out["steps"] = (
            aws_sdk_imagebuilder.types.workflow_step_executions_list.deserialize_json(
                data["steps"]
            )
        )
    if "workflowBuildVersionArn" in data:
        out["workflow_build_version_arn"] = data["workflowBuildVersionArn"]
    if "workflowExecutionId" in data:
        out["workflow_execution_id"] = data["workflowExecutionId"]
    if "imageBuildVersionArn" in data:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    if "message" in data:
        out["message"] = data["message"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
