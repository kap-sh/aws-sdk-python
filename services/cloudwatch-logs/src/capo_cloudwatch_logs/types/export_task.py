"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ExportTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.export_destination_bucket
    import capo_cloudwatch_logs.types.export_destination_prefix
    import capo_cloudwatch_logs.types.export_task_execution_info
    import capo_cloudwatch_logs.types.export_task_id
    import capo_cloudwatch_logs.types.export_task_name
    import capo_cloudwatch_logs.types.export_task_status
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.timestamp

ExportTask = TypedDict(
    "ExportTask",
    {
        "task_id": NotRequired[
            "capo_cloudwatch_logs.types.export_task_id.ExportTaskId"
        ],
        "task_name": NotRequired[
            "capo_cloudwatch_logs.types.export_task_name.ExportTaskName"
        ],
        "log_group_name": NotRequired[
            "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
        ],
        "from": NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"],
        "to": NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"],
        "destination": NotRequired[
            "capo_cloudwatch_logs.types.export_destination_bucket.ExportDestinationBucket"
        ],
        "destination_prefix": NotRequired[
            "capo_cloudwatch_logs.types.export_destination_prefix.ExportDestinationPrefix"
        ],
        "status": NotRequired[
            "capo_cloudwatch_logs.types.export_task_status.ExportTaskStatus"
        ],
        "execution_info": NotRequired[
            "capo_cloudwatch_logs.types.export_task_execution_info.ExportTaskExecutionInfo"
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
        import capo_cloudwatch_logs.types.export_task_status

        out["status"] = (
            capo_cloudwatch_logs.types.export_task_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "execution_info" in value:
        import capo_cloudwatch_logs.types.export_task_execution_info

        out["executionInfo"] = (
            capo_cloudwatch_logs.types.export_task_execution_info.serialize_aws_json_1_1(
                value["execution_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportTask:
    out: ExportTask = {}  # type: ignore[typeddict-item]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    if data.get("taskName") is not None:
        out["task_name"] = data["taskName"]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    if data.get("from") is not None:
        out["from"] = data["from"]
    if data.get("to") is not None:
        out["to"] = data["to"]
    if data.get("destination") is not None:
        out["destination"] = data["destination"]
    if data.get("destinationPrefix") is not None:
        out["destination_prefix"] = data["destinationPrefix"]
    if data.get("status") is not None:
        import capo_cloudwatch_logs.types.export_task_status

        out["status"] = (
            capo_cloudwatch_logs.types.export_task_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("executionInfo") is not None:
        import capo_cloudwatch_logs.types.export_task_execution_info

        out["execution_info"] = (
            capo_cloudwatch_logs.types.export_task_execution_info.deserialize_aws_json_1_1(
                data["executionInfo"]
            )
        )
    return out
