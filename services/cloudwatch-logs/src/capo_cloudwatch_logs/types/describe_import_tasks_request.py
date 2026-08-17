"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeImportTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.describe_limit
    import capo_cloudwatch_logs.types.import_id
    import capo_cloudwatch_logs.types.import_status
    import capo_cloudwatch_logs.types.next_token


class DescribeImportTasksRequest(TypedDict, closed=True):
    import_id: NotRequired["capo_cloudwatch_logs.types.import_id.ImportId"]
    """<p>Optional filter to describe a specific import task by its ID.</p>"""
    import_status: NotRequired["capo_cloudwatch_logs.types.import_status.ImportStatus"]
    """<p>Optional filter to list imports by their status. Valid values are IN_PROGRESS, CANCELLED, COMPLETED and FAILED.</p>"""
    import_source_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>Optional filter to list imports from a specific source</p>"""
    limit: NotRequired["capo_cloudwatch_logs.types.describe_limit.DescribeLimit"]
    """<p>The maximum number of import tasks to return in the response. Default: 50</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The pagination token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImportTasksRequest) -> dict:
    out: dict = {}
    if "import_id" in value:
        out["importId"] = value["import_id"]
    if "import_status" in value:
        import capo_cloudwatch_logs.types.import_status

        out["importStatus"] = (
            capo_cloudwatch_logs.types.import_status.serialize_aws_json_1_1(
                value["import_status"]
            )
        )
    if "import_source_arn" in value:
        out["importSourceArn"] = value["import_source_arn"]
    if "limit" in value:
        out["limit"] = value["limit"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImportTasksRequest:
    out: DescribeImportTasksRequest = {}  # type: ignore[typeddict-item]
    if data.get("importId") is not None:
        out["import_id"] = data["importId"]
    if data.get("importStatus") is not None:
        import capo_cloudwatch_logs.types.import_status

        out["import_status"] = (
            capo_cloudwatch_logs.types.import_status.deserialize_aws_json_1_1(
                data["importStatus"]
            )
        )
    if data.get("importSourceArn") is not None:
        out["import_source_arn"] = data["importSourceArn"]
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
