"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#DescribeBatchLoadTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.batch_load_task_id


class DescribeBatchLoadTaskRequest(TypedDict):
    task_id: "aws_sdk_timestream_write.types.batch_load_task_id.BatchLoadTaskId"
    """<p>The ID of the batch load task.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeBatchLoadTaskRequest) -> dict:
    out: dict = {}
    out["TaskId"] = value["task_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeBatchLoadTaskRequest:
    out: DescribeBatchLoadTaskRequest = {}  # type: ignore[typeddict-item]
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    else:
        raise DeserializationError("DescribeBatchLoadTaskRequest.task_id required")
    return out
