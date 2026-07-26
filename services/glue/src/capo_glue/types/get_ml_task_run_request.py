"""Generated from Smithy shape ``com.amazonaws.glue#GetMLTaskRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.hash_string


class GetMLTaskRunRequest(TypedDict, closed=True):
    transform_id: "capo_glue.types.hash_string.HashString"
    """<p>The unique identifier of the machine learning transform.</p>"""
    task_run_id: "capo_glue.types.hash_string.HashString"
    """<p>The unique identifier of the task run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMLTaskRunRequest) -> dict:
    out: dict = {}
    out["TransformId"] = value["transform_id"]
    out["TaskRunId"] = value["task_run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMLTaskRunRequest:
    out: GetMLTaskRunRequest = {}  # type: ignore[typeddict-item]
    if "TransformId" in data:
        out["transform_id"] = data["TransformId"]
    else:
        raise DeserializationError("GetMLTaskRunRequest.transform_id required")
    if "TaskRunId" in data:
        out["task_run_id"] = data["TaskRunId"]
    else:
        raise DeserializationError("GetMLTaskRunRequest.task_run_id required")
    return out
