"""Generated from Smithy shape ``com.amazonaws.datasync#StartTaskExecutionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.task_execution_arn


class StartTaskExecutionResponse(TypedDict):
    task_execution_arn: NotRequired[
        "aws_sdk_datasync.types.task_execution_arn.TaskExecutionArn"
    ]
    """<p>The ARN of the running task execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTaskExecutionResponse) -> dict:
    out: dict = {}
    if "task_execution_arn" in value:
        out["TaskExecutionArn"] = value["task_execution_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartTaskExecutionResponse:
    out: StartTaskExecutionResponse = {}  # type: ignore[typeddict-item]
    if "TaskExecutionArn" in data:
        out["task_execution_arn"] = data["TaskExecutionArn"]
    return out
