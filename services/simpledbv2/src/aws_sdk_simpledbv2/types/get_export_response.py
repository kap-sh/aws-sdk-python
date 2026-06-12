"""Generated from Smithy shape ``com.amazonaws.simpledbv2#GetExportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_simpledbv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_simpledbv2.types.aws_account_id
    import aws_sdk_simpledbv2.types.domain_name
    import aws_sdk_simpledbv2.types.export_arn
    import aws_sdk_simpledbv2.types.export_data_cutoff_time
    import aws_sdk_simpledbv2.types.export_manifest_summary
    import aws_sdk_simpledbv2.types.export_status
    import aws_sdk_simpledbv2.types.failure_code
    import aws_sdk_simpledbv2.types.failure_message
    import aws_sdk_simpledbv2.types.idempotency_token
    import aws_sdk_simpledbv2.types.items_count
    import aws_sdk_simpledbv2.types.requested_at
    import aws_sdk_simpledbv2.types.s3_bucket_name
    import aws_sdk_simpledbv2.types.s3_key_prefix
    import aws_sdk_simpledbv2.types.s3_sse_algorithm
    import aws_sdk_simpledbv2.types.s3_sse_kms_key_id


class GetExportResponse(TypedDict):
    export_arn: "aws_sdk_simpledbv2.types.export_arn.ExportArn"
    """Unique ARN identifier of the export."""
    client_token: "aws_sdk_simpledbv2.types.idempotency_token.IdempotencyToken"
    """The client token provided for this export."""
    export_status: "aws_sdk_simpledbv2.types.export_status.ExportStatus"
    """The current state of the export. Current possible values include : PENDING - export request received, IN_PROGRESS - export is being processed, SUCCEEDED - export completed successfully, and FAILED - export encountered an error."""
    domain_name: "aws_sdk_simpledbv2.types.domain_name.DomainName"
    """The name of the domain that was exported."""
    requested_at: "aws_sdk_simpledbv2.types.requested_at.RequestedAt"
    """Timestamp when the export request was received by the service."""
    s3_bucket: "aws_sdk_simpledbv2.types.s3_bucket_name.S3BucketName"
    """The name of the S3 bucket for this export."""
    s3_key_prefix: NotRequired["aws_sdk_simpledbv2.types.s3_key_prefix.S3KeyPrefix"]
    """The S3 key prefix provided in the corresponding StartDomainExport request."""
    s3_sse_algorithm: NotRequired[
        "aws_sdk_simpledbv2.types.s3_sse_algorithm.S3SseAlgorithm"
    ]
    """The S3 SSE encryption algorithm for this export."""
    s3_sse_kms_key_id: NotRequired[
        "aws_sdk_simpledbv2.types.s3_sse_kms_key_id.S3SseKmsKeyId"
    ]
    """The KMS key ID for this export."""
    s3_bucket_owner: NotRequired["aws_sdk_simpledbv2.types.aws_account_id.AwsAccountId"]
    """The S3 bucket owner account ID for this export."""
    failure_code: NotRequired["aws_sdk_simpledbv2.types.failure_code.FailureCode"]
    """Failure code for the result of the failed export."""
    failure_message: NotRequired[
        "aws_sdk_simpledbv2.types.failure_message.FailureMessage"
    ]
    """Export failure reason description."""
    export_manifest: NotRequired[
        "aws_sdk_simpledbv2.types.export_manifest_summary.ExportManifestSummary"
    ]
    """The name of the manifest summary file for the export."""
    items_count: NotRequired["aws_sdk_simpledbv2.types.items_count.ItemsCount"]
    """Total number of exported items."""
    export_data_cutoff_time: NotRequired[
        "aws_sdk_simpledbv2.types.export_data_cutoff_time.ExportDataCutoffTime"
    ]
    """The timestamp indicating the cutoff point for data inclusion in the export. All data inserted or modified before this time will be present in the exported data. Data insertions or modifications after this timestamp may or may not be present in the export."""


# --- restJson1 ser/de ---
def serialize_json(value: GetExportResponse) -> dict:
    out: dict = {}
    out["exportArn"] = value["export_arn"]
    out["clientToken"] = value["client_token"]
    import aws_sdk_simpledbv2.types.export_status

    out["exportStatus"] = aws_sdk_simpledbv2.types.export_status.serialize_json(
        value["export_status"]
    )
    out["domainName"] = value["domain_name"]
    import aws_sdk_simpledbv2.types.requested_at

    out["requestedAt"] = aws_sdk_simpledbv2.types.requested_at.serialize_json(
        value["requested_at"]
    )
    out["s3Bucket"] = value["s3_bucket"]
    if "s3_key_prefix" in value:
        out["s3KeyPrefix"] = value["s3_key_prefix"]
    if "s3_sse_algorithm" in value:
        import aws_sdk_simpledbv2.types.s3_sse_algorithm

        out["s3SseAlgorithm"] = (
            aws_sdk_simpledbv2.types.s3_sse_algorithm.serialize_json(
                value["s3_sse_algorithm"]
            )
        )
    if "s3_sse_kms_key_id" in value:
        out["s3SseKmsKeyId"] = value["s3_sse_kms_key_id"]
    if "s3_bucket_owner" in value:
        out["s3BucketOwner"] = value["s3_bucket_owner"]
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "export_manifest" in value:
        out["exportManifest"] = value["export_manifest"]
    if "items_count" in value:
        out["itemsCount"] = value["items_count"]
    if "export_data_cutoff_time" in value:
        import aws_sdk_simpledbv2.types.export_data_cutoff_time

        out["exportDataCutoffTime"] = (
            aws_sdk_simpledbv2.types.export_data_cutoff_time.serialize_json(
                value["export_data_cutoff_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetExportResponse:
    out: GetExportResponse = {}  # type: ignore[typeddict-item]
    if "exportArn" in data:
        out["export_arn"] = data["exportArn"]
    else:
        raise DeserializationError("GetExportResponse.export_arn required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("GetExportResponse.client_token required")
    if "exportStatus" in data:
        import aws_sdk_simpledbv2.types.export_status

        out["export_status"] = aws_sdk_simpledbv2.types.export_status.deserialize_json(
            data["exportStatus"]
        )
    else:
        raise DeserializationError("GetExportResponse.export_status required")
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError("GetExportResponse.domain_name required")
    if "requestedAt" in data:
        import aws_sdk_simpledbv2.types.requested_at

        out["requested_at"] = aws_sdk_simpledbv2.types.requested_at.deserialize_json(
            data["requestedAt"]
        )
    else:
        raise DeserializationError("GetExportResponse.requested_at required")
    if "s3Bucket" in data:
        out["s3_bucket"] = data["s3Bucket"]
    else:
        raise DeserializationError("GetExportResponse.s3_bucket required")
    if "s3KeyPrefix" in data:
        out["s3_key_prefix"] = data["s3KeyPrefix"]
    if "s3SseAlgorithm" in data:
        import aws_sdk_simpledbv2.types.s3_sse_algorithm

        out["s3_sse_algorithm"] = (
            aws_sdk_simpledbv2.types.s3_sse_algorithm.deserialize_json(
                data["s3SseAlgorithm"]
            )
        )
    if "s3SseKmsKeyId" in data:
        out["s3_sse_kms_key_id"] = data["s3SseKmsKeyId"]
    if "s3BucketOwner" in data:
        out["s3_bucket_owner"] = data["s3BucketOwner"]
    if "failureCode" in data:
        out["failure_code"] = data["failureCode"]
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    if "exportManifest" in data:
        out["export_manifest"] = data["exportManifest"]
    if "itemsCount" in data:
        out["items_count"] = data["itemsCount"]
    if "exportDataCutoffTime" in data:
        import aws_sdk_simpledbv2.types.export_data_cutoff_time

        out["export_data_cutoff_time"] = (
            aws_sdk_simpledbv2.types.export_data_cutoff_time.deserialize_json(
                data["exportDataCutoffTime"]
            )
        )
    return out
