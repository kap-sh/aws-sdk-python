"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportTableToPointInTimeInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.client_token
    import aws_sdk_dynamodb.types.export_format
    import aws_sdk_dynamodb.types.export_time
    import aws_sdk_dynamodb.types.export_type
    import aws_sdk_dynamodb.types.incremental_export_specification
    import aws_sdk_dynamodb.types.s3_bucket
    import aws_sdk_dynamodb.types.s3_bucket_owner
    import aws_sdk_dynamodb.types.s3_prefix
    import aws_sdk_dynamodb.types.s3_sse_algorithm
    import aws_sdk_dynamodb.types.s3_sse_kms_key_id
    import aws_sdk_dynamodb.types.table_arn


class ExportTableToPointInTimeInput(TypedDict):
    table_arn: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>The Amazon Resource Name (ARN) associated with the table to export.</p>"""
    export_time: NotRequired["aws_sdk_dynamodb.types.export_time.ExportTime"]
    """<p>Time in the past from which to export table data, counted in seconds from the start of the Unix epoch. The table export will be a snapshot of the table's state at this point in time.</p>"""
    client_token: NotRequired["aws_sdk_dynamodb.types.client_token.ClientToken"]
    """<p>Providing a <code>ClientToken</code> makes the call to <code>ExportTableToPointInTimeInput</code> idempotent, meaning that multiple identical calls have the same effect as one single call.</p> <p>A client token is valid for 8 hours after the first request that uses it is completed. After 8 hours, any request with the same client token is treated as a new request. Do not resubmit the same request with the same client token for more than 8 hours, or the result might not be idempotent.</p> <p>If you submit a request with the same client token but a change in other parameters within the 8-hour idempotency window, DynamoDB returns an <code>ExportConflictException</code>.</p>"""
    s3_bucket: "aws_sdk_dynamodb.types.s3_bucket.S3Bucket"
    """<p>The name of the Amazon S3 bucket to export the snapshot to.</p>"""
    s3_bucket_owner: NotRequired["aws_sdk_dynamodb.types.s3_bucket_owner.S3BucketOwner"]
    """<p>The ID of the Amazon Web Services account that owns the bucket the export will be stored in.</p> <note> <p>S3BucketOwner is a required parameter when exporting to a S3 bucket in another account.</p> </note>"""
    s3_prefix: NotRequired["aws_sdk_dynamodb.types.s3_prefix.S3Prefix"]
    """<p>The Amazon S3 bucket prefix to use as the file name and path of the exported snapshot.</p>"""
    s3_sse_algorithm: NotRequired[
        "aws_sdk_dynamodb.types.s3_sse_algorithm.S3SseAlgorithm"
    ]
    """<p>Type of encryption used on the bucket where export data will be stored. Valid values for <code>S3SseAlgorithm</code> are:</p> <ul> <li> <p> <code>AES256</code> - server-side encryption with Amazon S3 managed keys</p> </li> <li> <p> <code>KMS</code> - server-side encryption with KMS managed keys</p> </li> </ul>"""
    s3_sse_kms_key_id: NotRequired[
        "aws_sdk_dynamodb.types.s3_sse_kms_key_id.S3SseKmsKeyId"
    ]
    """<p>The ID of the KMS managed key used to encrypt the S3 bucket where export data will be stored (if applicable).</p>"""
    export_format: NotRequired["aws_sdk_dynamodb.types.export_format.ExportFormat"]
    """<p>The format for the exported data. Valid values for <code>ExportFormat</code> are <code>DYNAMODB_JSON</code> or <code>ION</code>.</p>"""
    export_type: NotRequired["aws_sdk_dynamodb.types.export_type.ExportType"]
    """<p>Choice of whether to execute as a full export or incremental export. Valid values are FULL_EXPORT or INCREMENTAL_EXPORT. The default value is FULL_EXPORT. If INCREMENTAL_EXPORT is provided, the IncrementalExportSpecification must also be used.</p>"""
    incremental_export_specification: NotRequired[
        "aws_sdk_dynamodb.types.incremental_export_specification.IncrementalExportSpecification"
    ]
    """<p>Optional object containing the parameters specific to an incremental export.</p>"""
