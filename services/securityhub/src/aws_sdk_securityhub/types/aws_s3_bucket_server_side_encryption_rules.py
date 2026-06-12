"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketServerSideEncryptionRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_s3_bucket_server_side_encryption_rule

AwsS3BucketServerSideEncryptionRules: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_s3_bucket_server_side_encryption_rule.AwsS3BucketServerSideEncryptionRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketServerSideEncryptionRules) -> list:
    import aws_sdk_securityhub.types.aws_s3_bucket_server_side_encryption_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_s3_bucket_server_side_encryption_rule.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsS3BucketServerSideEncryptionRules:
    import aws_sdk_securityhub.types.aws_s3_bucket_server_side_encryption_rule

    out: AwsS3BucketServerSideEncryptionRules = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_s3_bucket_server_side_encryption_rule.deserialize_json(
                item
            )
        )
    return out
