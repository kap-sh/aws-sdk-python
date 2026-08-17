"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ExportTaskStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.export_task_status_code
    import capo_cloudwatch_logs.types.export_task_status_message


class ExportTaskStatus(TypedDict, closed=True):
    code: NotRequired[
        "capo_cloudwatch_logs.types.export_task_status_code.ExportTaskStatusCode"
    ]
    """<p>The status code of the export task.</p>"""
    message: NotRequired[
        "capo_cloudwatch_logs.types.export_task_status_message.ExportTaskStatusMessage"
    ]
    """<p>The status message related to the status code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportTaskStatus) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_cloudwatch_logs.types.export_task_status_code

        out["code"] = (
            capo_cloudwatch_logs.types.export_task_status_code.serialize_aws_json_1_1(
                value["code"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportTaskStatus:
    out: ExportTaskStatus = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        import capo_cloudwatch_logs.types.export_task_status_code

        out["code"] = (
            capo_cloudwatch_logs.types.export_task_status_code.deserialize_aws_json_1_1(
                data["code"]
            )
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
