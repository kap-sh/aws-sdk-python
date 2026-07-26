"""Generated from Smithy shape ``com.amazonaws.datasync#DeleteTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.task_arn


class DeleteTaskRequest(TypedDict, closed=True):
    task_arn: "capo_datasync.types.task_arn.TaskArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the task that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTaskRequest) -> dict:
    out: dict = {}
    out["TaskArn"] = value["task_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTaskRequest:
    out: DeleteTaskRequest = {}  # type: ignore[typeddict-item]
    if "TaskArn" in data:
        out["task_arn"] = data["TaskArn"]
    else:
        raise DeserializationError("DeleteTaskRequest.task_arn required")
    return out
