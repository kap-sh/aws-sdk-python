"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.billed_size_bytes
    import aws_sdk_dynamodb.types.client_token
    import aws_sdk_dynamodb.types.export_arn
    import aws_sdk_dynamodb.types.export_end_time
    import aws_sdk_dynamodb.types.export_format
    import aws_sdk_dynamodb.types.export_manifest
    import aws_sdk_dynamodb.types.export_start_time
    import aws_sdk_dynamodb.types.export_status
    import aws_sdk_dynamodb.types.export_time
    import aws_sdk_dynamodb.types.export_type
    import aws_sdk_dynamodb.types.failure_code
    import aws_sdk_dynamodb.types.failure_message
    import aws_sdk_dynamodb.types.incremental_export_specification
    import aws_sdk_dynamodb.types.item_count
    import aws_sdk_dynamodb.types.s3_bucket
    import aws_sdk_dynamodb.types.s3_bucket_owner
    import aws_sdk_dynamodb.types.s3_prefix
    import aws_sdk_dynamodb.types.s3_sse_algorithm
    import aws_sdk_dynamodb.types.s3_sse_kms_key_id
    import aws_sdk_dynamodb.types.table_arn
    import aws_sdk_dynamodb.types.table_id


class ExportDescription(TypedDict):
    export_arn: NotRequired["aws_sdk_dynamodb.types.export_arn.ExportArn"]
    """<p>The Amazon Resource Name (ARN) of the table export.</p>"""
    export_status: NotRequired["aws_sdk_dynamodb.types.export_status.ExportStatus"]
    """<p>Export can be in one of the following states: IN_PROGRESS, COMPLETED, or FAILED.</p>"""
    start_time: NotRequired["aws_sdk_dynamodb.types.export_start_time.ExportStartTime"]
    """<p>The time at which the export task began.</p>"""
    end_time: NotRequired["aws_sdk_dynamodb.types.export_end_time.ExportEndTime"]
    """<p>The time at which the export task completed.</p>"""
    export_manifest: NotRequired[
        "aws_sdk_dynamodb.types.export_manifest.ExportManifest"
    ]
    """<p>The name of the manifest file for the export task.</p>"""
    table_arn: NotRequired["aws_sdk_dynamodb.types.table_arn.TableArn"]
    """<p>The Amazon Resource Name (ARN) of the table that was exported.</p>"""
    table_id: NotRequired["aws_sdk_dynamodb.types.table_id.TableId"]
    """<p>Unique ID of the table that was exported.</p>"""
    export_time: NotRequired["aws_sdk_dynamodb.types.export_time.ExportTime"]
    """<p>Point in time from which table data was exported.</p>"""
    client_token: NotRequired["aws_sdk_dynamodb.types.client_token.ClientToken"]
    """<p>The client token that was provided for the export task. A client token makes calls to <code>ExportTableToPointInTimeInput</code> idempotent, meaning that multiple identical calls have the same effect as one single call.</p>"""
    s3_bucket: NotRequired["aws_sdk_dynamodb.types.s3_bucket.S3Bucket"]
    """<p>The name of the Amazon S3 bucket containing the export.</p>"""
    s3_bucket_owner: NotRequired["aws_sdk_dynamodb.types.s3_bucket_owner.S3BucketOwner"]
    """<p>The ID of the Amazon Web Services account that owns the bucket containing the export.</p>"""
    s3_prefix: NotRequired["aws_sdk_dynamodb.types.s3_prefix.S3Prefix"]
    """<p>The Amazon S3 bucket prefix used as the file name and path of the exported snapshot.</p>"""
    s3_sse_algorithm: NotRequired[
        "aws_sdk_dynamodb.types.s3_sse_algorithm.S3SseAlgorithm"
    ]
    """<p>Type of encryption used on the bucket where export data is stored. Valid values for <code>S3SseAlgorithm</code> are:</p> <ul> <li> <p> <code>AES256</code> - server-side encryption with Amazon S3 managed keys</p> </li> <li> <p> <code>KMS</code> - server-side encryption with KMS managed keys</p> </li> </ul>"""
    s3_sse_kms_key_id: NotRequired[
        "aws_sdk_dynamodb.types.s3_sse_kms_key_id.S3SseKmsKeyId"
    ]
    """<p>The ID of the KMS managed key used to encrypt the S3 bucket where export data is stored (if applicable).</p>"""
    failure_code: NotRequired["aws_sdk_dynamodb.types.failure_code.FailureCode"]
    """<p>Status code for the result of the failed export.</p>"""
    failure_message: NotRequired[
        "aws_sdk_dynamodb.types.failure_message.FailureMessage"
    ]
    """<p>Export failure reason description.</p>"""
    export_format: NotRequired["aws_sdk_dynamodb.types.export_format.ExportFormat"]
    """<p>The format of the exported data. Valid values for <code>ExportFormat</code> are <code>DYNAMODB_JSON</code> or <code>ION</code>.</p>"""
    billed_size_bytes: NotRequired[
        "aws_sdk_dynamodb.types.billed_size_bytes.BilledSizeBytes"
    ]
    """<p>The billable size of the table export.</p>"""
    item_count: NotRequired["aws_sdk_dynamodb.types.item_count.ItemCount"]
    """<p>The number of items exported.</p>"""
    export_type: NotRequired["aws_sdk_dynamodb.types.export_type.ExportType"]
    """<p>The type of export that was performed. Valid values are <code>FULL_EXPORT</code> or <code>INCREMENTAL_EXPORT</code>.</p>"""
    incremental_export_specification: NotRequired[
        "aws_sdk_dynamodb.types.incremental_export_specification.IncrementalExportSpecification"
    ]
    """<p>Optional object containing the parameters specific to an incremental export.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportDescription) -> dict:
    out: dict = {}
    if "export_arn" in value:
        out["ExportArn"] = value["export_arn"]
    if "export_status" in value:
        import aws_sdk_dynamodb.types.export_status

        out["ExportStatus"] = (
            aws_sdk_dynamodb.types.export_status.serialize_aws_json_1_0(
                value["export_status"]
            )
        )
    if "start_time" in value:
        import aws_sdk_dynamodb.types.export_start_time

        out["StartTime"] = (
            aws_sdk_dynamodb.types.export_start_time.serialize_aws_json_1_0(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_dynamodb.types.export_end_time

        out["EndTime"] = aws_sdk_dynamodb.types.export_end_time.serialize_aws_json_1_0(
            value["end_time"]
        )
    if "export_manifest" in value:
        out["ExportManifest"] = value["export_manifest"]
    if "table_arn" in value:
        out["TableArn"] = value["table_arn"]
    if "table_id" in value:
        out["TableId"] = value["table_id"]
    if "export_time" in value:
        import aws_sdk_dynamodb.types.export_time

        out["ExportTime"] = aws_sdk_dynamodb.types.export_time.serialize_aws_json_1_0(
            value["export_time"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "s3_bucket" in value:
        out["S3Bucket"] = value["s3_bucket"]
    if "s3_bucket_owner" in value:
        out["S3BucketOwner"] = value["s3_bucket_owner"]
    if "s3_prefix" in value:
        out["S3Prefix"] = value["s3_prefix"]
    if "s3_sse_algorithm" in value:
        import aws_sdk_dynamodb.types.s3_sse_algorithm

        out["S3SseAlgorithm"] = (
            aws_sdk_dynamodb.types.s3_sse_algorithm.serialize_aws_json_1_0(
                value["s3_sse_algorithm"]
            )
        )
    if "s3_sse_kms_key_id" in value:
        out["S3SseKmsKeyId"] = value["s3_sse_kms_key_id"]
    if "failure_code" in value:
        out["FailureCode"] = value["failure_code"]
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "export_format" in value:
        import aws_sdk_dynamodb.types.export_format

        out["ExportFormat"] = (
            aws_sdk_dynamodb.types.export_format.serialize_aws_json_1_0(
                value["export_format"]
            )
        )
    if "billed_size_bytes" in value:
        out["BilledSizeBytes"] = value["billed_size_bytes"]
    if "item_count" in value:
        out["ItemCount"] = value["item_count"]
    if "export_type" in value:
        import aws_sdk_dynamodb.types.export_type

        out["ExportType"] = aws_sdk_dynamodb.types.export_type.serialize_aws_json_1_0(
            value["export_type"]
        )
    if "incremental_export_specification" in value:
        import aws_sdk_dynamodb.types.incremental_export_specification

        out["IncrementalExportSpecification"] = (
            aws_sdk_dynamodb.types.incremental_export_specification.serialize_aws_json_1_0(
                value["incremental_export_specification"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportDescription:
    out: ExportDescription = {}  # type: ignore[typeddict-item]
    if "ExportArn" in data:
        out["export_arn"] = data["ExportArn"]
    if "ExportStatus" in data:
        import aws_sdk_dynamodb.types.export_status

        out["export_status"] = (
            aws_sdk_dynamodb.types.export_status.deserialize_aws_json_1_0(
                data["ExportStatus"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_dynamodb.types.export_start_time

        out["start_time"] = (
            aws_sdk_dynamodb.types.export_start_time.deserialize_aws_json_1_0(
                data["StartTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_dynamodb.types.export_end_time

        out["end_time"] = (
            aws_sdk_dynamodb.types.export_end_time.deserialize_aws_json_1_0(
                data["EndTime"]
            )
        )
    if "ExportManifest" in data:
        out["export_manifest"] = data["ExportManifest"]
    if "TableArn" in data:
        out["table_arn"] = data["TableArn"]
    if "TableId" in data:
        out["table_id"] = data["TableId"]
    if "ExportTime" in data:
        import aws_sdk_dynamodb.types.export_time

        out["export_time"] = (
            aws_sdk_dynamodb.types.export_time.deserialize_aws_json_1_0(
                data["ExportTime"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "S3Bucket" in data:
        out["s3_bucket"] = data["S3Bucket"]
    if "S3BucketOwner" in data:
        out["s3_bucket_owner"] = data["S3BucketOwner"]
    if "S3Prefix" in data:
        out["s3_prefix"] = data["S3Prefix"]
    if "S3SseAlgorithm" in data:
        import aws_sdk_dynamodb.types.s3_sse_algorithm

        out["s3_sse_algorithm"] = (
            aws_sdk_dynamodb.types.s3_sse_algorithm.deserialize_aws_json_1_0(
                data["S3SseAlgorithm"]
            )
        )
    if "S3SseKmsKeyId" in data:
        out["s3_sse_kms_key_id"] = data["S3SseKmsKeyId"]
    if "FailureCode" in data:
        out["failure_code"] = data["FailureCode"]
    if "FailureMessage" in data:
        out["failure_message"] = data["FailureMessage"]
    if "ExportFormat" in data:
        import aws_sdk_dynamodb.types.export_format

        out["export_format"] = (
            aws_sdk_dynamodb.types.export_format.deserialize_aws_json_1_0(
                data["ExportFormat"]
            )
        )
    if "BilledSizeBytes" in data:
        out["billed_size_bytes"] = data["BilledSizeBytes"]
    if "ItemCount" in data:
        out["item_count"] = data["ItemCount"]
    if "ExportType" in data:
        import aws_sdk_dynamodb.types.export_type

        out["export_type"] = (
            aws_sdk_dynamodb.types.export_type.deserialize_aws_json_1_0(
                data["ExportType"]
            )
        )
    if "IncrementalExportSpecification" in data:
        import aws_sdk_dynamodb.types.incremental_export_specification

        out["incremental_export_specification"] = (
            aws_sdk_dynamodb.types.incremental_export_specification.deserialize_aws_json_1_0(
                data["IncrementalExportSpecification"]
            )
        )
    return out
