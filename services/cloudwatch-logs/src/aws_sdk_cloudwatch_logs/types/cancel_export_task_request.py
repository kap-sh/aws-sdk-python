"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CancelExportTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.export_task_id


class CancelExportTaskRequest(TypedDict, closed=True):
    task_id: "aws_sdk_cloudwatch_logs.types.export_task_id.ExportTaskId"
    """<p>The ID of the export task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelExportTaskRequest) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelExportTaskRequest:
    out: CancelExportTaskRequest = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("CancelExportTaskRequest.task_id required")
    return out
