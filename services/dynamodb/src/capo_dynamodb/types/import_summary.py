"""Generated from Smithy shape ``com.amazonaws.dynamodb#ImportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.cloud_watch_log_group_arn
    import capo_dynamodb.types.import_arn
    import capo_dynamodb.types.import_end_time
    import capo_dynamodb.types.import_start_time
    import capo_dynamodb.types.import_status
    import capo_dynamodb.types.input_format
    import capo_dynamodb.types.s3_bucket_source
    import capo_dynamodb.types.table_arn


class ImportSummary(TypedDict, closed=True):
    import_arn: NotRequired["capo_dynamodb.types.import_arn.ImportArn"]
    """<p> The Amazon Resource Number (ARN) corresponding to the import request. </p>"""
    import_status: NotRequired["capo_dynamodb.types.import_status.ImportStatus"]
    """<p> The status of the import operation. </p>"""
    table_arn: NotRequired["capo_dynamodb.types.table_arn.TableArn"]
    """<p> The Amazon Resource Number (ARN) of the table being imported into. </p>"""
    s3_bucket_source: NotRequired["capo_dynamodb.types.s3_bucket_source.S3BucketSource"]
    """<p> The path and S3 bucket of the source file that is being imported. This includes the S3Bucket (required), S3KeyPrefix (optional) and S3BucketOwner (optional if the bucket is owned by the requester). </p>"""
    cloud_watch_log_group_arn: NotRequired[
        "capo_dynamodb.types.cloud_watch_log_group_arn.CloudWatchLogGroupArn"
    ]
    """<p> The Amazon Resource Number (ARN) of the Cloudwatch Log Group associated with this import task. </p>"""
    input_format: NotRequired["capo_dynamodb.types.input_format.InputFormat"]
    """<p> The format of the source data. Valid values are <code>CSV</code>, <code>DYNAMODB_JSON</code> or <code>ION</code>.</p>"""
    start_time: NotRequired["capo_dynamodb.types.import_start_time.ImportStartTime"]
    """<p> The time at which this import task began. </p>"""
    end_time: NotRequired["capo_dynamodb.types.import_end_time.ImportEndTime"]
    """<p> The time at which this import task ended. (Does this include the successful complete creation of the table it was imported to?) </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportSummary) -> dict:
    out: dict = {}
    if "import_arn" in value:
        out["ImportArn"] = value["import_arn"]
    if "import_status" in value:
        import capo_dynamodb.types.import_status

        out["ImportStatus"] = capo_dynamodb.types.import_status.serialize_aws_json_1_0(
            value["import_status"]
        )
    if "table_arn" in value:
        out["TableArn"] = value["table_arn"]
    if "s3_bucket_source" in value:
        import capo_dynamodb.types.s3_bucket_source

        out["S3BucketSource"] = (
            capo_dynamodb.types.s3_bucket_source.serialize_aws_json_1_0(
                value["s3_bucket_source"]
            )
        )
    if "cloud_watch_log_group_arn" in value:
        out["CloudWatchLogGroupArn"] = value["cloud_watch_log_group_arn"]
    if "input_format" in value:
        import capo_dynamodb.types.input_format

        out["InputFormat"] = capo_dynamodb.types.input_format.serialize_aws_json_1_0(
            value["input_format"]
        )
    if "start_time" in value:
        import capo_dynamodb.types.import_start_time

        out["StartTime"] = capo_dynamodb.types.import_start_time.serialize_aws_json_1_0(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_dynamodb.types.import_end_time

        out["EndTime"] = capo_dynamodb.types.import_end_time.serialize_aws_json_1_0(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportSummary:
    out: ImportSummary = {}  # type: ignore[typeddict-item]
    if "ImportArn" in data:
        out["import_arn"] = data["ImportArn"]
    if "ImportStatus" in data:
        import capo_dynamodb.types.import_status

        out["import_status"] = (
            capo_dynamodb.types.import_status.deserialize_aws_json_1_0(
                data["ImportStatus"]
            )
        )
    if "TableArn" in data:
        out["table_arn"] = data["TableArn"]
    if "S3BucketSource" in data:
        import capo_dynamodb.types.s3_bucket_source

        out["s3_bucket_source"] = (
            capo_dynamodb.types.s3_bucket_source.deserialize_aws_json_1_0(
                data["S3BucketSource"]
            )
        )
    if "CloudWatchLogGroupArn" in data:
        out["cloud_watch_log_group_arn"] = data["CloudWatchLogGroupArn"]
    if "InputFormat" in data:
        import capo_dynamodb.types.input_format

        out["input_format"] = capo_dynamodb.types.input_format.deserialize_aws_json_1_0(
            data["InputFormat"]
        )
    if "StartTime" in data:
        import capo_dynamodb.types.import_start_time

        out["start_time"] = (
            capo_dynamodb.types.import_start_time.deserialize_aws_json_1_0(
                data["StartTime"]
            )
        )
    if "EndTime" in data:
        import capo_dynamodb.types.import_end_time

        out["end_time"] = capo_dynamodb.types.import_end_time.deserialize_aws_json_1_0(
            data["EndTime"]
        )
    return out
