"""Generated from Smithy shape ``com.amazonaws.dynamodb#ImportTableDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.client_token
    import aws_sdk_dynamodb.types.cloud_watch_log_group_arn
    import aws_sdk_dynamodb.types.error_count
    import aws_sdk_dynamodb.types.failure_code
    import aws_sdk_dynamodb.types.failure_message
    import aws_sdk_dynamodb.types.import_arn
    import aws_sdk_dynamodb.types.import_end_time
    import aws_sdk_dynamodb.types.import_start_time
    import aws_sdk_dynamodb.types.import_status
    import aws_sdk_dynamodb.types.imported_item_count
    import aws_sdk_dynamodb.types.input_compression_type
    import aws_sdk_dynamodb.types.input_format
    import aws_sdk_dynamodb.types.input_format_options
    import aws_sdk_dynamodb.types.long_object
    import aws_sdk_dynamodb.types.processed_item_count
    import aws_sdk_dynamodb.types.s3_bucket_source
    import aws_sdk_dynamodb.types.table_arn
    import aws_sdk_dynamodb.types.table_creation_parameters
    import aws_sdk_dynamodb.types.table_id


class ImportTableDescription(TypedDict):
    import_arn: NotRequired["aws_sdk_dynamodb.types.import_arn.ImportArn"]
    """<p> The Amazon Resource Number (ARN) corresponding to the import request. </p>"""
    import_status: NotRequired["aws_sdk_dynamodb.types.import_status.ImportStatus"]
    """<p> The status of the import. </p>"""
    table_arn: NotRequired["aws_sdk_dynamodb.types.table_arn.TableArn"]
    """<p> The Amazon Resource Number (ARN) of the table being imported into. </p>"""
    table_id: NotRequired["aws_sdk_dynamodb.types.table_id.TableId"]
    """<p> The table id corresponding to the table created by import table process. </p>"""
    client_token: NotRequired["aws_sdk_dynamodb.types.client_token.ClientToken"]
    """<p> The client token that was provided for the import task. Reusing the client token on retry makes a call to <code>ImportTable</code> idempotent. </p>"""
    s3_bucket_source: NotRequired[
        "aws_sdk_dynamodb.types.s3_bucket_source.S3BucketSource"
    ]
    """<p> Values for the S3 bucket the source file is imported from. Includes bucket name (required), key prefix (optional) and bucket account owner ID (optional). </p>"""
    error_count: "aws_sdk_dynamodb.types.error_count.ErrorCount"
    """<p> The number of errors occurred on importing the source file into the target table. </p>"""
    cloud_watch_log_group_arn: NotRequired[
        "aws_sdk_dynamodb.types.cloud_watch_log_group_arn.CloudWatchLogGroupArn"
    ]
    """<p> The Amazon Resource Number (ARN) of the Cloudwatch Log Group associated with the target table. </p>"""
    input_format: NotRequired["aws_sdk_dynamodb.types.input_format.InputFormat"]
    """<p> The format of the source data going into the target table. </p>"""
    input_format_options: NotRequired[
        "aws_sdk_dynamodb.types.input_format_options.InputFormatOptions"
    ]
    """<p> The format options for the data that was imported into the target table. There is one value, CsvOption. </p>"""
    input_compression_type: NotRequired[
        "aws_sdk_dynamodb.types.input_compression_type.InputCompressionType"
    ]
    """<p> The compression options for the data that has been imported into the target table. The values are NONE, GZIP, or ZSTD. </p>"""
    table_creation_parameters: NotRequired[
        "aws_sdk_dynamodb.types.table_creation_parameters.TableCreationParameters"
    ]
    """<p> The parameters for the new table that is being imported into. </p>"""
    start_time: NotRequired["aws_sdk_dynamodb.types.import_start_time.ImportStartTime"]
    """<p> The time when this import task started. </p>"""
    end_time: NotRequired["aws_sdk_dynamodb.types.import_end_time.ImportEndTime"]
    """<p> The time at which the creation of the table associated with this import task completed. </p>"""
    processed_size_bytes: NotRequired["aws_sdk_dynamodb.types.long_object.LongObject"]
    """<p> The total size of data processed from the source file, in Bytes. </p>"""
    processed_item_count: (
        "aws_sdk_dynamodb.types.processed_item_count.ProcessedItemCount"
    )
    """<p> The total number of items processed from the source file. </p>"""
    imported_item_count: "aws_sdk_dynamodb.types.imported_item_count.ImportedItemCount"
    """<p> The number of items successfully imported into the new table. </p>"""
    failure_code: NotRequired["aws_sdk_dynamodb.types.failure_code.FailureCode"]
    """<p> The error code corresponding to the failure that the import job ran into during execution. </p>"""
    failure_message: NotRequired[
        "aws_sdk_dynamodb.types.failure_message.FailureMessage"
    ]
    """<p> The error message corresponding to the failure that the import job ran into during execution. </p>"""
