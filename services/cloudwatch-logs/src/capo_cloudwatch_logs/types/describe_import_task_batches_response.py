"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeImportTaskBatchesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.import_batch_list
    import capo_cloudwatch_logs.types.import_id
    import capo_cloudwatch_logs.types.next_token


class DescribeImportTaskBatchesResponse(TypedDict, closed=True):
    import_source_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the source being imported from.</p>"""
    import_id: NotRequired["capo_cloudwatch_logs.types.import_id.ImportId"]
    """<p>The ID of the import task.</p>"""
    import_batches: NotRequired[
        "capo_cloudwatch_logs.types.import_batch_list.ImportBatchList"
    ]
    """<p>The list of import batches that match the request filters.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of results. Not present if there are no additional results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImportTaskBatchesResponse) -> dict:
    out: dict = {}
    if "import_source_arn" in value:
        out["importSourceArn"] = value["import_source_arn"]
    if "import_id" in value:
        out["importId"] = value["import_id"]
    if "import_batches" in value:
        import capo_cloudwatch_logs.types.import_batch_list

        out["importBatches"] = (
            capo_cloudwatch_logs.types.import_batch_list.serialize_aws_json_1_1(
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
        import capo_cloudwatch_logs.types.import_batch_list

        out["import_batches"] = (
            capo_cloudwatch_logs.types.import_batch_list.deserialize_aws_json_1_1(
                data["importBatches"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
