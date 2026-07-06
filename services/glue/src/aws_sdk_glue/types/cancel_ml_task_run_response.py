"""Generated from Smithy shape ``com.amazonaws.glue#CancelMLTaskRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.task_status_type


class CancelMLTaskRunResponse(TypedDict, closed=True):
    transform_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The unique identifier of the machine learning transform.</p>"""
    task_run_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The unique identifier for the task run.</p>"""
    status: NotRequired["aws_sdk_glue.types.task_status_type.TaskStatusType"]
    """<p>The status for this run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelMLTaskRunResponse) -> dict:
    out: dict = {}
    if "transform_id" in value:
        out["TransformId"] = value["transform_id"]
    if "task_run_id" in value:
        out["TaskRunId"] = value["task_run_id"]
    if "status" in value:
        import aws_sdk_glue.types.task_status_type

        out["Status"] = aws_sdk_glue.types.task_status_type.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelMLTaskRunResponse:
    out: CancelMLTaskRunResponse = {}  # type: ignore[typeddict-item]
    if "TransformId" in data:
        out["transform_id"] = data["TransformId"]
    if "TaskRunId" in data:
        out["task_run_id"] = data["TaskRunId"]
    if "Status" in data:
        import aws_sdk_glue.types.task_status_type

        out["status"] = aws_sdk_glue.types.task_status_type.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
