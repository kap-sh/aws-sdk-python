"""Generated from Smithy shape ``com.amazonaws.fsx#CancelDataRepositoryTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.data_repository_task_lifecycle
    import aws_sdk_fsx.types.task_id


class CancelDataRepositoryTaskResponse(TypedDict, closed=True):
    lifecycle: NotRequired[
        "aws_sdk_fsx.types.data_repository_task_lifecycle.DataRepositoryTaskLifecycle"
    ]
    """<p>The lifecycle status of the data repository task, as follows:</p> <ul> <li> <p> <code>PENDING</code> - Amazon FSx has not started the task.</p> </li> <li> <p> <code>EXECUTING</code> - Amazon FSx is processing the task.</p> </li> <li> <p> <code>FAILED</code> - Amazon FSx was not able to complete the task. For example, there may be files the task failed to process. The <a>DataRepositoryTaskFailureDetails</a> property provides more information about task failures.</p> </li> <li> <p> <code>SUCCEEDED</code> - FSx completed the task successfully.</p> </li> <li> <p> <code>CANCELED</code> - Amazon FSx canceled the task and it did not complete.</p> </li> <li> <p> <code>CANCELING</code> - FSx is in process of canceling the task.</p> </li> </ul>"""
    task_id: NotRequired["aws_sdk_fsx.types.task_id.TaskId"]
    """<p>The ID of the task being canceled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelDataRepositoryTaskResponse) -> dict:
    out: dict = {}
    if "lifecycle" in value:
        import aws_sdk_fsx.types.data_repository_task_lifecycle

        out["Lifecycle"] = (
            aws_sdk_fsx.types.data_repository_task_lifecycle.serialize_aws_json_1_1(
                value["lifecycle"]
            )
        )
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelDataRepositoryTaskResponse:
    out: CancelDataRepositoryTaskResponse = {}  # type: ignore[typeddict-item]
    if "Lifecycle" in data:
        import aws_sdk_fsx.types.data_repository_task_lifecycle

        out["lifecycle"] = (
            aws_sdk_fsx.types.data_repository_task_lifecycle.deserialize_aws_json_1_1(
                data["Lifecycle"]
            )
        )
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    return out
