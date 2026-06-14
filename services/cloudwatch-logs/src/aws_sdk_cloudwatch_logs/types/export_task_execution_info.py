"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ExportTaskExecutionInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.timestamp


class ExportTaskExecutionInfo(TypedDict):
    creation_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The creation time of the export task, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</p>"""
    completion_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The completion time of the export task, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportTaskExecutionInfo) -> dict:
    out: dict = {}
    if "creation_time" in value:
        out["creationTime"] = value["creation_time"]
    if "completion_time" in value:
        out["completionTime"] = value["completion_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportTaskExecutionInfo:
    out: ExportTaskExecutionInfo = {}  # type: ignore[typeddict-item]
    if "creationTime" in data:
        out["creation_time"] = data["creationTime"]
    if "completionTime" in data:
        out["completion_time"] = data["completionTime"]
    return out
