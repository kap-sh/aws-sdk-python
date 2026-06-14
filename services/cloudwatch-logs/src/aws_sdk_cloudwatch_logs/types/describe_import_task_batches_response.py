"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeImportTaskBatchesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.arn
    import aws_sdk_cloudwatch_logs.types.import_batch_list
    import aws_sdk_cloudwatch_logs.types.import_id
    import aws_sdk_cloudwatch_logs.types.next_token


class DescribeImportTaskBatchesResponse(TypedDict):
    import_source_arn: NotRequired["aws_sdk_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the source being imported from.</p>"""
    import_id: NotRequired["aws_sdk_cloudwatch_logs.types.import_id.ImportId"]
    """<p>The ID of the import task.</p>"""
    import_batches: NotRequired[
        "aws_sdk_cloudwatch_logs.types.import_batch_list.ImportBatchList"
    ]
    """<p>The list of import batches that match the request filters.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of results. Not present if there are no additional results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImportTaskBatchesResponse) -> dict:
    out: dict = {}
    if "import_source_arn" in value:
        out["importSourceArn"] = value["import_source_arn"]
    if "import_id" in value:
        out["importId"] = value["import_id"]
    if "import_batches" in value:
        import aws_sdk_cloudwatch_logs.types.import_batch_list

        out["importBatches"] = (
            aws_sdk_cloudwatch_logs.types.import_batch_list.serialize_aws_json_1_1(
                value["import_batches"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImportTaskBatchesResponse:
    out: DescribeImportTaskBatchesResponse = {}  # type: ignore[typeddict-item]
    if "importSourceArn" in data:
        out["import_source_arn"] = data["importSourceArn"]
    if "importId" in data:
        out["import_id"] = data["importId"]
    if "importBatches" in data:
        import aws_sdk_cloudwatch_logs.types.import_batch_list

        out["import_batches"] = (
            aws_sdk_cloudwatch_logs.types.import_batch_list.deserialize_aws_json_1_1(
                data["importBatches"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
