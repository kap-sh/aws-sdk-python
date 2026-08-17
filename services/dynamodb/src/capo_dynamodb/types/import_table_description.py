"""Generated from Smithy shape ``com.amazonaws.dynamodb#ImportTableDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.client_token
    import capo_dynamodb.types.cloud_watch_log_group_arn
    import capo_dynamodb.types.error_count
    import capo_dynamodb.types.failure_code
    import capo_dynamodb.types.failure_message
    import capo_dynamodb.types.import_arn
    import capo_dynamodb.types.import_end_time
    import capo_dynamodb.types.import_start_time
    import capo_dynamodb.types.import_status
    import capo_dynamodb.types.imported_item_count
    import capo_dynamodb.types.input_compression_type
    import capo_dynamodb.types.input_format
    import capo_dynamodb.types.input_format_options
    import capo_dynamodb.types.long_object
    import capo_dynamodb.types.processed_item_count
    import capo_dynamodb.types.s3_bucket_source
    import capo_dynamodb.types.table_arn
    import capo_dynamodb.types.table_creation_parameters
    import capo_dynamodb.types.table_id


class ImportTableDescription(TypedDict, closed=True):
    import_arn: NotRequired["capo_dynamodb.types.import_arn.ImportArn"]
    """<p> The Amazon Resource Number (ARN) corresponding to the import request. </p>"""
    import_status: NotRequired["capo_dynamodb.types.import_status.ImportStatus"]
    """<p> The status of the import. </p>"""
    table_arn: NotRequired["capo_dynamodb.types.table_arn.TableArn"]
    """<p> The Amazon Resource Number (ARN) of the table being imported into. </p>"""
    table_id: NotRequired["capo_dynamodb.types.table_id.TableId"]
    """<p> The table id corresponding to the table created by import table process. </p>"""
    client_token: NotRequired["capo_dynamodb.types.client_token.ClientToken"]
    """<p> The client token that was provided for the import task. Reusing the client token on retry makes a call to <code>ImportTable</code> idempotent. </p>"""
    s3_bucket_source: NotRequired["capo_dynamodb.types.s3_bucket_source.S3BucketSource"]
    """<p> Values for the S3 bucket the source file is imported from. Includes bucket name (required), key prefix (optional) and bucket account owner ID (optional). </p>"""
    error_count: "capo_dynamodb.types.error_count.ErrorCount"
    """<p> The number of errors occurred on importing the source file into the target table. </p>"""
    cloud_watch_log_group_arn: NotRequired[
        "capo_dynamodb.types.cloud_watch_log_group_arn.CloudWatchLogGroupArn"
    ]
    """<p> The Amazon Resource Number (ARN) of the Cloudwatch Log Group associated with the target table. </p>"""
    input_format: NotRequired["capo_dynamodb.types.input_format.InputFormat"]
    """<p> The format of the source data going into the target table. </p>"""
    input_format_options: NotRequired[
        "capo_dynamodb.types.input_format_options.InputFormatOptions"
    ]
    """<p> The format options for the data that was imported into the target table. There is one value, CsvOption. </p>"""
    input_compression_type: NotRequired[
        "capo_dynamodb.types.input_compression_type.InputCompressionType"
    ]
    """<p> The compression options for the data that has been imported into the target table. The values are NONE, GZIP, or ZSTD. </p>"""
    table_creation_parameters: NotRequired[
        "capo_dynamodb.types.table_creation_parameters.TableCreationParameters"
    ]
    """<p> The parameters for the new table that is being imported into. </p>"""
    start_time: NotRequired["capo_dynamodb.types.import_start_time.ImportStartTime"]
    """<p> The time when this import task started. </p>"""
    end_time: NotRequired["capo_dynamodb.types.import_end_time.ImportEndTime"]
    """<p> The time at which the creation of the table associated with this import task completed. </p>"""
    processed_size_bytes: NotRequired["capo_dynamodb.types.long_object.LongObject"]
    """<p> The total size of data processed from the source file, in Bytes. </p>"""
    processed_item_count: "capo_dynamodb.types.processed_item_count.ProcessedItemCount"
    """<p> The total number of items processed from the source file. </p>"""
    imported_item_count: "capo_dynamodb.types.imported_item_count.ImportedItemCount"
    """<p> The number of items successfully imported into the new table. </p>"""
    failure_code: NotRequired["capo_dynamodb.types.failure_code.FailureCode"]
    """<p> The error code corresponding to the failure that the import job ran into during execution. </p>"""
    failure_message: NotRequired["capo_dynamodb.types.failure_message.FailureMessage"]
    """<p> The error message corresponding to the failure that the import job ran into during execution. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportTableDescription) -> dict:
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
    if "table_id" in value:
        out["TableId"] = value["table_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "s3_bucket_source" in value:
        import capo_dynamodb.types.s3_bucket_source

        out["S3BucketSource"] = (
            capo_dynamodb.types.s3_bucket_source.serialize_aws_json_1_0(
                value["s3_bucket_source"]
            )
        )
    out["ErrorCount"] = value.get("error_count", 0)
    if "cloud_watch_log_group_arn" in value:
        out["CloudWatchLogGroupArn"] = value["cloud_watch_log_group_arn"]
    if "input_format" in value:
        import capo_dynamodb.types.input_format

        out["InputFormat"] = capo_dynamodb.types.input_format.serialize_aws_json_1_0(
            value["input_format"]
        )
    if "input_format_options" in value:
        import capo_dynamodb.types.input_format_options

        out["InputFormatOptions"] = (
            capo_dynamodb.types.input_format_options.serialize_aws_json_1_0(
                value["input_format_options"]
            )
        )
    if "input_compression_type" in value:
        import capo_dynamodb.types.input_compression_type

        out["InputCompressionType"] = (
            capo_dynamodb.types.input_compression_type.serialize_aws_json_1_0(
                value["input_compression_type"]
            )
        )
    if "table_creation_parameters" in value:
        import capo_dynamodb.types.table_creation_parameters

        out["TableCreationParameters"] = (
            capo_dynamodb.types.table_creation_parameters.serialize_aws_json_1_0(
                value["table_creation_parameters"]
            )
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
    if "processed_size_bytes" in value:
        out["ProcessedSizeBytes"] = value["processed_size_bytes"]
    out["ProcessedItemCount"] = value.get("processed_item_count", 0)
    out["ImportedItemCount"] = value.get("imported_item_count", 0)
    if "failure_code" in value:
        out["FailureCode"] = value["failure_code"]
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportTableDescription:
    out: ImportTableDescription = {}  # type: ignore[typeddict-item]
    if data.get("ImportArn") is not None:
        out["import_arn"] = data["ImportArn"]
    if data.get("ImportStatus") is not None:
        import capo_dynamodb.types.import_status

        out["import_status"] = (
            capo_dynamodb.types.import_status.deserialize_aws_json_1_0(
                data["ImportStatus"]
            )
        )
    if data.get("TableArn") is not None:
        out["table_arn"] = data["TableArn"]
    if data.get("TableId") is not None:
        out["table_id"] = data["TableId"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("S3BucketSource") is not None:
        import capo_dynamodb.types.s3_bucket_source

        out["s3_bucket_source"] = (
            capo_dynamodb.types.s3_bucket_source.deserialize_aws_json_1_0(
                data["S3BucketSource"]
            )
        )
    if data.get("ErrorCount") is not None:
        out["error_count"] = data["ErrorCount"]
    else:
        out["error_count"] = 0
    if data.get("CloudWatchLogGroupArn") is not None:
        out["cloud_watch_log_group_arn"] = data["CloudWatchLogGroupArn"]
    if data.get("InputFormat") is not None:
        import capo_dynamodb.types.input_format

        out["input_format"] = capo_dynamodb.types.input_format.deserialize_aws_json_1_0(
            data["InputFormat"]
        )
    if data.get("InputFormatOptions") is not None:
        import capo_dynamodb.types.input_format_options

        out["input_format_options"] = (
            capo_dynamodb.types.input_format_options.deserialize_aws_json_1_0(
                data["InputFormatOptions"]
            )
        )
    if data.get("InputCompressionType") is not None:
        import capo_dynamodb.types.input_compression_type

        out["input_compression_type"] = (
            capo_dynamodb.types.input_compression_type.deserialize_aws_json_1_0(
                data["InputCompressionType"]
            )
        )
    if data.get("TableCreationParameters") is not None:
        import capo_dynamodb.types.table_creation_parameters

        out["table_creation_parameters"] = (
            capo_dynamodb.types.table_creation_parameters.deserialize_aws_json_1_0(
                data["TableCreationParameters"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_dynamodb.types.import_start_time

        out["start_time"] = (
            capo_dynamodb.types.import_start_time.deserialize_aws_json_1_0(
                data["StartTime"]
            )
        )
    if data.get("EndTime") is not None:
        import capo_dynamodb.types.import_end_time

        out["end_time"] = capo_dynamodb.types.import_end_time.deserialize_aws_json_1_0(
            data["EndTime"]
        )
    if data.get("ProcessedSizeBytes") is not None:
        out["processed_size_bytes"] = data["ProcessedSizeBytes"]
    if data.get("ProcessedItemCount") is not None:
        out["processed_item_count"] = data["ProcessedItemCount"]
    else:
        out["processed_item_count"] = 0
    if data.get("ImportedItemCount") is not None:
        out["imported_item_count"] = data["ImportedItemCount"]
    else:
        out["imported_item_count"] = 0
    if data.get("FailureCode") is not None:
        out["failure_code"] = data["FailureCode"]
    if data.get("FailureMessage") is not None:
        out["failure_message"] = data["FailureMessage"]
    return out
