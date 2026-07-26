"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ExportTasks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.export_task

ExportTasks: TypeAlias = list["capo_cloudwatch_logs.types.export_task.ExportTask"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportTasks) -> list:
    import capo_cloudwatch_logs.types.export_task

    out: list = []
    for item in value:
        out.append(capo_cloudwatch_logs.types.export_task.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExportTasks:
    import capo_cloudwatch_logs.types.export_task

    out: ExportTasks = []
    for item in data:
        out.append(
            capo_cloudwatch_logs.types.export_task.deserialize_aws_json_1_1(item)
        )
    return out
