"""Generated from Smithy shape ``com.amazonaws.glue#CancelMLTaskRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string


class CancelMLTaskRunRequest(TypedDict, closed=True):
    transform_id: "aws_sdk_glue.types.hash_string.HashString"
    """<p>The unique identifier of the machine learning transform.</p>"""
    task_run_id: "aws_sdk_glue.types.hash_string.HashString"
    """<p>A unique identifier for the task run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelMLTaskRunRequest) -> dict:
    out: dict = {}
    out["TransformId"] = value["transform_id"]
    out["TaskRunId"] = value["task_run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelMLTaskRunRequest:
    out: CancelMLTaskRunRequest = {}  # type: ignore[typeddict-item]
    if "TransformId" in data:
        out["transform_id"] = data["TransformId"]
    else:
        raise DeserializationError("CancelMLTaskRunRequest.transform_id required")
    if "TaskRunId" in data:
        out["task_run_id"] = data["TaskRunId"]
    else:
        raise DeserializationError("CancelMLTaskRunRequest.task_run_id required")
    return out
