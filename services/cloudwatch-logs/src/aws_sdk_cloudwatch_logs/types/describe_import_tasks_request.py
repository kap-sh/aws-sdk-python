"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeImportTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.arn
    import aws_sdk_cloudwatch_logs.types.describe_limit
    import aws_sdk_cloudwatch_logs.types.import_id
    import aws_sdk_cloudwatch_logs.types.import_status
    import aws_sdk_cloudwatch_logs.types.next_token


class DescribeImportTasksRequest(TypedDict, closed=True):
    import_id: NotRequired["aws_sdk_cloudwatch_logs.types.import_id.ImportId"]
    """<p>Optional filter to describe a specific import task by its ID.</p>"""
    import_status: NotRequired[
        "aws_sdk_cloudwatch_logs.types.import_status.ImportStatus"
    ]
    """<p>Optional filter to list imports by their status. Valid values are IN_PROGRESS, CANCELLED, COMPLETED and FAILED.</p>"""
    import_source_arn: NotRequired["aws_sdk_cloudwatch_logs.types.arn.Arn"]
    """<p>Optional filter to list imports from a specific source</p>"""
    limit: NotRequired["aws_sdk_cloudwatch_logs.types.describe_limit.DescribeLimit"]
    """<p>The maximum number of import tasks to return in the response. Default: 50</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The pagination token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImportTasksRequest) -> dict:
    out: dict = {}
    if "import_id" in value:
        out["importId"] = value["import_id"]
    if "import_status" in value:
        import aws_sdk_cloudwatch_logs.types.import_status

        out["importStatus"] = (
            aws_sdk_cloudwatch_logs.types.import_status.serialize_aws_json_1_1(
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
    if "importId" in data:
        out["import_id"] = data["importId"]
    if "importStatus" in data:
        import aws_sdk_cloudwatch_logs.types.import_status

        out["import_status"] = (
            aws_sdk_cloudwatch_logs.types.import_status.deserialize_aws_json_1_1(
                data["importStatus"]
            )
        )
    if "importSourceArn" in data:
        out["import_source_arn"] = data["importSourceArn"]
    if "limit" in data:
        out["limit"] = data["limit"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
