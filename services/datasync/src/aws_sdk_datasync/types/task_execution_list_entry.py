"""Generated from Smithy shape ``com.amazonaws.datasync#TaskExecutionListEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.task_execution_arn
    import aws_sdk_datasync.types.task_execution_status
    import aws_sdk_datasync.types.task_mode


class TaskExecutionListEntry(TypedDict):
    task_execution_arn: NotRequired[
        "aws_sdk_datasync.types.task_execution_arn.TaskExecutionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a task execution.</p>"""
    status: NotRequired[
        "aws_sdk_datasync.types.task_execution_status.TaskExecutionStatus"
    ]
    """<p>The status of a task execution. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses\">Task execution statuses</a>.</p>"""
    task_mode: NotRequired["aws_sdk_datasync.types.task_mode.TaskMode"]
    """<p>The task mode that you're using. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html\">Choosing a task mode for your data transfer</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskExecutionListEntry) -> dict:
    out: dict = {}
    if "task_execution_arn" in value:
        out["TaskExecutionArn"] = value["task_execution_arn"]
    if "status" in value:
        import aws_sdk_datasync.types.task_execution_status

        out["Status"] = (
            aws_sdk_datasync.types.task_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "task_mode" in value:
        import aws_sdk_datasync.types.task_mode

        out["TaskMode"] = aws_sdk_datasync.types.task_mode.serialize_aws_json_1_1(
            value["task_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskExecutionListEntry:
    out: TaskExecutionListEntry = {}  # type: ignore[typeddict-item]
    if "TaskExecutionArn" in data:
        out["task_execution_arn"] = data["TaskExecutionArn"]
    if "Status" in data:
        import aws_sdk_datasync.types.task_execution_status

        out["status"] = (
            aws_sdk_datasync.types.task_execution_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "TaskMode" in data:
        import aws_sdk_datasync.types.task_mode

        out["task_mode"] = aws_sdk_datasync.types.task_mode.deserialize_aws_json_1_1(
            data["TaskMode"]
        )
    return out
