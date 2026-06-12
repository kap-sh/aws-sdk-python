"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ExportTaskStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.export_task_status_code
    import aws_sdk_cloudwatch_logs.types.export_task_status_message


class ExportTaskStatus(TypedDict):
    code: NotRequired[
        "aws_sdk_cloudwatch_logs.types.export_task_status_code.ExportTaskStatusCode"
    ]
    """<p>The status code of the export task.</p>"""
    message: NotRequired[
        "aws_sdk_cloudwatch_logs.types.export_task_status_message.ExportTaskStatusMessage"
    ]
    """<p>The status message related to the status code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportTaskStatus) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_cloudwatch_logs.types.export_task_status_code

        out["code"] = (
            aws_sdk_cloudwatch_logs.types.export_task_status_code.serialize_aws_json_1_1(
                value["code"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportTaskStatus:
    out: ExportTaskStatus = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import aws_sdk_cloudwatch_logs.types.export_task_status_code

        out["code"] = (
            aws_sdk_cloudwatch_logs.types.export_task_status_code.deserialize_aws_json_1_1(
                data["code"]
            )
        )
    if "message" in data:
        out["message"] = data["message"]
    return out
