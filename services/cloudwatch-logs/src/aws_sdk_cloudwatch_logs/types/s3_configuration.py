"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#S3Configuration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.account_id
    import aws_sdk_cloudwatch_logs.types.kms_key_id
    import aws_sdk_cloudwatch_logs.types.role_arn
    import aws_sdk_cloudwatch_logs.types.s3_uri


class S3Configuration(TypedDict):
    destination_identifier: "aws_sdk_cloudwatch_logs.types.s3_uri.S3Uri"
    """<p>The Amazon S3 URI where query results are delivered. Must be a valid S3 URI format.</p>"""
    role_arn: "aws_sdk_cloudwatch_logs.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that grants permissions to write query results to the specified Amazon S3 destination.</p>"""
    owner_account_id: NotRequired["aws_sdk_cloudwatch_logs.types.account_id.AccountId"]
    """<p>The Amazon Web Services accountId for the bucket owning account.</p>"""
    kms_key_id: NotRequired["aws_sdk_cloudwatch_logs.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Resource Name (ARN) of the KMS encryption key. Must belong to the same Amazon Web Services Region as the destination Amazon S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Configuration) -> dict:
    out: dict = {}
    out["destinationIdentifier"] = value["destination_identifier"]
    out["roleArn"] = value["role_arn"]
    if "owner_account_id" in value:
        out["ownerAccountId"] = value["owner_account_id"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Configuration:
    out: S3Configuration = {}  # type: ignore[typeddict-item]
    if "destinationIdentifier" in data:
        out["destination_identifier"] = data["destinationIdentifier"]
    else:
        raise DeserializationError("S3Configuration.destination_identifier required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("S3Configuration.role_arn required")
    if "ownerAccountId" in data:
        out["owner_account_id"] = data["ownerAccountId"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
