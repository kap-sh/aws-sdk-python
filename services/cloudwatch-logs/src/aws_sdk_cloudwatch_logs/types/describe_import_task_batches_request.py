"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeImportTaskBatchesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.describe_limit
    import aws_sdk_cloudwatch_logs.types.import_id
    import aws_sdk_cloudwatch_logs.types.import_status_list
    import aws_sdk_cloudwatch_logs.types.next_token


class DescribeImportTaskBatchesRequest(TypedDict):
    import_id: "aws_sdk_cloudwatch_logs.types.import_id.ImportId"
    """<p>The ID of the import task to get batch information for.</p>"""
    batch_import_status: NotRequired[
        "aws_sdk_cloudwatch_logs.types.import_status_list.ImportStatusList"
    ]
    """<p>Optional filter to list import batches by their status. Accepts multiple status values: IN_PROGRESS, CANCELLED, COMPLETED and FAILED.</p>"""
    limit: NotRequired["aws_sdk_cloudwatch_logs.types.describe_limit.DescribeLimit"]
    """<p>The maximum number of import batches to return in the response. Default: 10</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The pagination token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImportTaskBatchesRequest) -> dict:
    out: dict = {}
    out["importId"] = value["import_id"]
    if "batch_import_status" in value:
        import aws_sdk_cloudwatch_logs.types.import_status_list

        out["batchImportStatus"] = (
            aws_sdk_cloudwatch_logs.types.import_status_list.serialize_aws_json_1_1(
                value["batch_import_status"]
            )
        )
    if "limit" in value:
        out["limit"] = value["limit"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImportTaskBatchesRequest:
    out: DescribeImportTaskBatchesRequest = {}  # type: ignore[typeddict-item]
    if "importId" in data:
        out["import_id"] = data["importId"]
    else:
        raise DeserializationError(
            "DescribeImportTaskBatchesRequest.import_id required"
        )
    if "batchImportStatus" in data:
        import aws_sdk_cloudwatch_logs.types.import_status_list

        out["batch_import_status"] = (
            aws_sdk_cloudwatch_logs.types.import_status_list.deserialize_aws_json_1_1(
                data["batchImportStatus"]
            )
        )
    if "limit" in data:
        out["limit"] = data["limit"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
