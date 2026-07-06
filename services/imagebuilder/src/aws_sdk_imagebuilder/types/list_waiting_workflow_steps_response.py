"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListWaitingWorkflowStepsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.pagination_token
    import aws_sdk_imagebuilder.types.workflow_step_execution_list


class ListWaitingWorkflowStepsResponse(TypedDict, closed=True):
    steps: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_step_execution_list.WorkflowStepExecutionList"
    ]
    """<p>An array of the workflow steps that are waiting for action in your Amazon Web Services account.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWaitingWorkflowStepsResponse) -> dict:
    out: dict = {}
    if "steps" in value:
        import aws_sdk_imagebuilder.types.workflow_step_execution_list

        out["steps"] = (
            aws_sdk_imagebuilder.types.workflow_step_execution_list.serialize_json(
                value["steps"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWaitingWorkflowStepsResponse:
    out: ListWaitingWorkflowStepsResponse = {}  # type: ignore[typeddict-item]
    if "steps" in data:
        import aws_sdk_imagebuilder.types.workflow_step_execution_list

        out["steps"] = (
            aws_sdk_imagebuilder.types.workflow_step_execution_list.deserialize_json(
                data["steps"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
