"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeExportTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.describe_limit
    import aws_sdk_cloudwatch_logs.types.export_task_id
    import aws_sdk_cloudwatch_logs.types.export_task_status_code
    import aws_sdk_cloudwatch_logs.types.next_token


class DescribeExportTasksRequest(TypedDict, closed=True):
    task_id: NotRequired["aws_sdk_cloudwatch_logs.types.export_task_id.ExportTaskId"]
    """<p>The ID of the export task. Specifying a task ID filters the results to one or zero export tasks.</p>"""
    status_code: NotRequired[
        "aws_sdk_cloudwatch_logs.types.export_task_status_code.ExportTaskStatusCode"
    ]
    """<p>The status code of the export task. Specifying a status code filters the results to zero or more export tasks.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    limit: NotRequired["aws_sdk_cloudwatch_logs.types.describe_limit.DescribeLimit"]
    """<p>The maximum number of items returned. If you don't specify a value, the default is up to 50 items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExportTasksRequest) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "status_code" in value:
        import aws_sdk_cloudwatch_logs.types.export_task_status_code

        out["statusCode"] = (
            aws_sdk_cloudwatch_logs.types.export_task_status_code.serialize_aws_json_1_1(
                value["status_code"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "limit" in value:
        out["limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExportTasksRequest:
    out: DescribeExportTasksRequest = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "statusCode" in data:
        import aws_sdk_cloudwatch_logs.types.export_task_status_code

        out["status_code"] = (
            aws_sdk_cloudwatch_logs.types.export_task_status_code.deserialize_aws_json_1_1(
                data["statusCode"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "limit" in data:
        out["limit"] = data["limit"]
    return out
