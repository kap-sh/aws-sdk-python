"""Generated from Smithy shape ``com.amazonaws.datasync#ListTaskExecutionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.next_token
    import aws_sdk_datasync.types.task_execution_list


class ListTaskExecutionsResponse(TypedDict):
    task_executions: NotRequired[
        "aws_sdk_datasync.types.task_execution_list.TaskExecutionList"
    ]
    """<p>A list of the task's executions.</p>"""
    next_token: NotRequired["aws_sdk_datasync.types.next_token.NextToken"]
    """<p>The opaque string that indicates the position to begin the next list of results in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTaskExecutionsResponse) -> dict:
    out: dict = {}
    if "task_executions" in value:
        import aws_sdk_datasync.types.task_execution_list

        out["TaskExecutions"] = (
            aws_sdk_datasync.types.task_execution_list.serialize_aws_json_1_1(
                value["task_executions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTaskExecutionsResponse:
    out: ListTaskExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "TaskExecutions" in data:
        import aws_sdk_datasync.types.task_execution_list

        out["task_executions"] = (
            aws_sdk_datasync.types.task_execution_list.deserialize_aws_json_1_1(
                data["TaskExecutions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
