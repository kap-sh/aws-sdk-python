"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeExportTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.export_tasks
    import capo_cloudwatch_logs.types.next_token


class DescribeExportTasksResponse(TypedDict, closed=True):
    export_tasks: NotRequired["capo_cloudwatch_logs.types.export_tasks.ExportTasks"]
    """<p>The export tasks.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExportTasksResponse) -> dict:
    out: dict = {}
    if "export_tasks" in value:
        import capo_cloudwatch_logs.types.export_tasks

        out["exportTasks"] = (
            capo_cloudwatch_logs.types.export_tasks.serialize_aws_json_1_1(
                value["export_tasks"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExportTasksResponse:
    out: DescribeExportTasksResponse = {}  # type: ignore[typeddict-item]
    if data.get("exportTasks") is not None:
        import capo_cloudwatch_logs.types.export_tasks

        out["export_tasks"] = (
            capo_cloudwatch_logs.types.export_tasks.deserialize_aws_json_1_1(
                data["exportTasks"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
