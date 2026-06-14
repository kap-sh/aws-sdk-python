"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateExportTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.export_task_id


class CreateExportTaskResponse(TypedDict):
    task_id: NotRequired["aws_sdk_cloudwatch_logs.types.export_task_id.ExportTaskId"]
    """<p>The ID of the export task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExportTaskResponse) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExportTaskResponse:
    out: CreateExportTaskResponse = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    return out
