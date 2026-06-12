"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListWorkflowExecutionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_build_message
    import aws_sdk_imagebuilder.types.image_build_version_arn
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.pagination_token
    import aws_sdk_imagebuilder.types.workflow_executions_list


class ListWorkflowExecutionsResponse(TypedDict):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    workflow_executions: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_executions_list.WorkflowExecutionsList"
    ]
    """<p>Contains an array of runtime details that represents each time a workflow ran for the requested image build version.</p>"""
    image_build_version_arn: NotRequired[
        "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    ]
    """<p>The resource Amazon Resource Name (ARN) of the image build version for which you requested a list of workflow runtime details.</p>"""
    message: NotRequired[
        "aws_sdk_imagebuilder.types.image_build_message.ImageBuildMessage"
    ]
    """<p>The output message from the list action, if applicable.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowExecutionsResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "workflow_executions" in value:
        import aws_sdk_imagebuilder.types.workflow_executions_list

        out["workflowExecutions"] = (
            aws_sdk_imagebuilder.types.workflow_executions_list.serialize_json(
                value["workflow_executions"]
            )
        )
    if "image_build_version_arn" in value:
        out["imageBuildVersionArn"] = value["image_build_version_arn"]
    if "message" in value:
        out["message"] = value["message"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkflowExecutionsResponse:
    out: ListWorkflowExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "workflowExecutions" in data:
        import aws_sdk_imagebuilder.types.workflow_executions_list

        out["workflow_executions"] = (
            aws_sdk_imagebuilder.types.workflow_executions_list.deserialize_json(
                data["workflowExecutions"]
            )
        )
    if "imageBuildVersionArn" in data:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    if "message" in data:
        out["message"] = data["message"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
