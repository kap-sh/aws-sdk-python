"""Generated from Smithy shape ``com.amazonaws.fsx#CancelDataRepositoryTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.task_id


class CancelDataRepositoryTaskRequest(TypedDict):
    task_id: NotRequired["aws_sdk_fsx.types.task_id.TaskId"]
    """<p>Specifies the data repository task to cancel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelDataRepositoryTaskRequest) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelDataRepositoryTaskRequest:
    out: CancelDataRepositoryTaskRequest = {}  # type: ignore[typeddict-item]
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    return out
