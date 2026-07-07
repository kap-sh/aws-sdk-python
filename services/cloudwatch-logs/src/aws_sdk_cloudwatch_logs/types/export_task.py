"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ExportTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.export_destination_bucket
    import aws_sdk_cloudwatch_logs.types.export_destination_prefix
    import aws_sdk_cloudwatch_logs.types.export_task_execution_info
    import aws_sdk_cloudwatch_logs.types.export_task_id
    import aws_sdk_cloudwatch_logs.types.export_task_name
    import aws_sdk_cloudwatch_logs.types.export_task_status
    import aws_sdk_cloudwatch_logs.types.log_group_name
    import aws_sdk_cloudwatch_logs.types.timestamp

ExportTask = TypedDict(
    "ExportTask",
    {
        "task_id": NotRequired[
            "aws_sdk_cloudwatch_logs.types.export_task_id.ExportTaskId"
        ],
        "task_name": NotRequired[
            "aws_sdk_cloudwatch_logs.types.export_task_name.ExportTaskName"
        ],
        "log_group_name": NotRequired[
            "aws_sdk_cloudwatch_logs.types.log_group_name.LogGroupName"
        ],
        "from": NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"],
        "to": NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"],
        "destination": NotRequired[
            "aws_sdk_cloudwatch_logs.types.export_destination_bucket.ExportDestinationBucket"
        ],
        "destination_prefix": NotRequired[
            "aws_sdk_cloudwatch_logs.types.export_destination_prefix.ExportDestinationPrefix"
        ],
        "status": NotRequired[
            "aws_sdk_cloudwatch_logs.types.export_task_status.ExportTaskStatus"
        ],
        "execution_info": NotRequired[
            "aws_sdk_cloudwatch_logs.types.export_task_execution_info.ExportTaskExecutionInfo"
        ],
    },
    closed=True,
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportTask) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "task_name" in value:
        out["taskName"] = value["task_name"]
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    if "from" in value:
        out["from"] = value["from"]
    if "to" in value:
        out["to"] = value["to"]
    if "destination" in value:
        out["destination"] = value["destination"]
    if "destination_prefix" in value:
        out["destinationPrefix"] = value["destination_prefix"]
    if "status" in value:
        import aws_sdk_cloudwatch_logs.types.export_task_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.export_task_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "execution_info" in value:
        import aws_sdk_cloudwatch_logs.types.export_task_execution_info

        out["executionInfo"] = (
            aws_sdk_cloudwatch_logs.types.export_task_execution_info.serialize_aws_json_1_1(
                value["execution_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportTask:
    out: ExportTask = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "taskName" in data:
        out["task_name"] = data["taskName"]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    if "from" in data:
        out["from"] = data["from"]
    if "to" in data:
        out["to"] = data["to"]
    if "destination" in data:
        out["destination"] = data["destination"]
    if "destinationPrefix" in data:
        out["destination_prefix"] = data["destinationPrefix"]
    if "status" in data:
        import aws_sdk_cloudwatch_logs.types.export_task_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.export_task_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "executionInfo" in data:
        import aws_sdk_cloudwatch_logs.types.export_task_execution_info

        out["execution_info"] = (
            aws_sdk_cloudwatch_logs.types.export_task_execution_info.deserialize_aws_json_1_1(
                data["executionInfo"]
            )
        )
    return out
