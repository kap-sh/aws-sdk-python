"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateExportTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.export_destination_bucket
    import aws_sdk_cloudwatch_logs.types.export_destination_prefix
    import aws_sdk_cloudwatch_logs.types.export_task_name
    import aws_sdk_cloudwatch_logs.types.log_group_name
    import aws_sdk_cloudwatch_logs.types.log_stream_name
    import aws_sdk_cloudwatch_logs.types.timestamp

CreateExportTaskRequest = TypedDict(
    "CreateExportTaskRequest",
    {
        "task_name": NotRequired[
            "aws_sdk_cloudwatch_logs.types.export_task_name.ExportTaskName"
        ],
        "log_group_name": "aws_sdk_cloudwatch_logs.types.log_group_name.LogGroupName",
        "log_stream_name_prefix": NotRequired[
            "aws_sdk_cloudwatch_logs.types.log_stream_name.LogStreamName"
        ],
        "from": "aws_sdk_cloudwatch_logs.types.timestamp.Timestamp",
        "to": "aws_sdk_cloudwatch_logs.types.timestamp.Timestamp",
        "destination": "aws_sdk_cloudwatch_logs.types.export_destination_bucket.ExportDestinationBucket",
        "destination_prefix": NotRequired[
            "aws_sdk_cloudwatch_logs.types.export_destination_prefix.ExportDestinationPrefix"
        ],
    },
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExportTaskRequest) -> dict:
    out: dict = {}
    if "task_name" in value:
        out["taskName"] = value["task_name"]
    out["logGroupName"] = value["log_group_name"]
    if "log_stream_name_prefix" in value:
        out["logStreamNamePrefix"] = value["log_stream_name_prefix"]
    out["from"] = value["from"]
    out["to"] = value["to"]
    out["destination"] = value["destination"]
    if "destination_prefix" in value:
        out["destinationPrefix"] = value["destination_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExportTaskRequest:
    out: CreateExportTaskRequest = {}  # type: ignore[typeddict-item]
    if "taskName" in data:
        out["task_name"] = data["taskName"]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError("CreateExportTaskRequest.log_group_name required")
    if "logStreamNamePrefix" in data:
        out["log_stream_name_prefix"] = data["logStreamNamePrefix"]
    if "from" in data:
        out["from"] = data["from"]
    else:
        raise DeserializationError("CreateExportTaskRequest.from required")
    if "to" in data:
        out["to"] = data["to"]
    else:
        raise DeserializationError("CreateExportTaskRequest.to required")
    if "destination" in data:
        out["destination"] = data["destination"]
    else:
        raise DeserializationError("CreateExportTaskRequest.destination required")
    if "destinationPrefix" in data:
        out["destination_prefix"] = data["destinationPrefix"]
    return out
