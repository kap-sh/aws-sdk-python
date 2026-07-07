"""Generated from Smithy shape ``com.amazonaws.mailmanager#S3Action``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.action_failure_policy
    import aws_sdk_mailmanager.types.iam_role_arn
    import aws_sdk_mailmanager.types.kms_key_id
    import aws_sdk_mailmanager.types.s3_bucket
    import aws_sdk_mailmanager.types.s3_prefix


class S3Action(TypedDict, closed=True):
    action_failure_policy: NotRequired[
        "aws_sdk_mailmanager.types.action_failure_policy.ActionFailurePolicy"
    ]
    """<p>A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the specified the bucket has been deleted.</p>"""
    role_arn: "aws_sdk_mailmanager.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM Role to use while writing to S3. This role must have access to the s3:PutObject, kms:Encrypt, and kms:GenerateDataKey APIs for the given bucket.</p>"""
    s3_bucket: "aws_sdk_mailmanager.types.s3_bucket.S3Bucket"
    """<p>The bucket name of the S3 bucket to write to.</p>"""
    s3_prefix: NotRequired["aws_sdk_mailmanager.types.s3_prefix.S3Prefix"]
    """<p>The S3 prefix to use for the write to the s3 bucket.</p>"""
    s3_sse_kms_key_id: NotRequired["aws_sdk_mailmanager.types.kms_key_id.KmsKeyId"]
    """<p>The KMS Key ID to use to encrypt the message in S3.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3Action) -> dict:
    out: dict = {}
    if "action_failure_policy" in value:
        import aws_sdk_mailmanager.types.action_failure_policy

        out["ActionFailurePolicy"] = (
            aws_sdk_mailmanager.types.action_failure_policy.serialize_aws_json_1_0(
                value["action_failure_policy"]
            )
        )
    out["RoleArn"] = value["role_arn"]
    out["S3Bucket"] = value["s3_bucket"]
    if "s3_prefix" in value:
        out["S3Prefix"] = value["s3_prefix"]
    if "s3_sse_kms_key_id" in value:
        out["S3SseKmsKeyId"] = value["s3_sse_kms_key_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3Action:
    out: S3Action = {}  # type: ignore[typeddict-item]
    if "ActionFailurePolicy" in data:
        import aws_sdk_mailmanager.types.action_failure_policy

        out["action_failure_policy"] = (
            aws_sdk_mailmanager.types.action_failure_policy.deserialize_aws_json_1_0(
                data["ActionFailurePolicy"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("S3Action.role_arn required")
    if "S3Bucket" in data:
        out["s3_bucket"] = data["S3Bucket"]
    else:
        raise DeserializationError("S3Action.s3_bucket required")
    if "S3Prefix" in data:
        out["s3_prefix"] = data["S3Prefix"]
    if "S3SseKmsKeyId" in data:
        out["s3_sse_kms_key_id"] = data["S3SseKmsKeyId"]
    return out
