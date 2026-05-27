"""Generated from Smithy shape ``com.amazonaws.dynamodb#ImportSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.cloud_watch_log_group_arn
    import aws_sdk_dynamodb.types.import_arn
    import aws_sdk_dynamodb.types.import_end_time
    import aws_sdk_dynamodb.types.import_start_time
    import aws_sdk_dynamodb.types.import_status
    import aws_sdk_dynamodb.types.input_format
    import aws_sdk_dynamodb.types.s3_bucket_source
    import aws_sdk_dynamodb.types.table_arn


class ImportSummary(TypedDict):
    import_arn: NotRequired["aws_sdk_dynamodb.types.import_arn.ImportArn"]
    """<p> The Amazon Resource Number (ARN) corresponding to the import request. </p>"""
    import_status: NotRequired["aws_sdk_dynamodb.types.import_status.ImportStatus"]
    """<p> The status of the import operation. </p>"""
    table_arn: NotRequired["aws_sdk_dynamodb.types.table_arn.TableArn"]
    """<p> The Amazon Resource Number (ARN) of the table being imported into. </p>"""
    s3_bucket_source: NotRequired[
        "aws_sdk_dynamodb.types.s3_bucket_source.S3BucketSource"
    ]
    """<p> The path and S3 bucket of the source file that is being imported. This includes the S3Bucket (required), S3KeyPrefix (optional) and S3BucketOwner (optional if the bucket is owned by the requester). </p>"""
    cloud_watch_log_group_arn: NotRequired[
        "aws_sdk_dynamodb.types.cloud_watch_log_group_arn.CloudWatchLogGroupArn"
    ]
    """<p> The Amazon Resource Number (ARN) of the Cloudwatch Log Group associated with this import task. </p>"""
    input_format: NotRequired["aws_sdk_dynamodb.types.input_format.InputFormat"]
    """<p> The format of the source data. Valid values are <code>CSV</code>, <code>DYNAMODB_JSON</code> or <code>ION</code>.</p>"""
    start_time: NotRequired["aws_sdk_dynamodb.types.import_start_time.ImportStartTime"]
    """<p> The time at which this import task began. </p>"""
    end_time: NotRequired["aws_sdk_dynamodb.types.import_end_time.ImportEndTime"]
    """<p> The time at which this import task ended. (Does this include the successful complete creation of the table it was imported to?) </p>"""
