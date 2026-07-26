"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketServerSideEncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_s3_bucket_server_side_encryption_rules


class AwsS3BucketServerSideEncryptionConfiguration(TypedDict, closed=True):
    rules: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_server_side_encryption_rules.AwsS3BucketServerSideEncryptionRules"
    ]
    """<p>The encryption rules that are applied to the S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketServerSideEncryptionConfiguration) -> dict:
    out: dict = {}
    if "rules" in value:
        import capo_securityhub.types.aws_s3_bucket_server_side_encryption_rules

        out["Rules"] = (
            capo_securityhub.types.aws_s3_bucket_server_side_encryption_rules.serialize_json(
                value["rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsS3BucketServerSideEncryptionConfiguration:
    out: AwsS3BucketServerSideEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "Rules" in data:
        import capo_securityhub.types.aws_s3_bucket_server_side_encryption_rules

        out["rules"] = (
            capo_securityhub.types.aws_s3_bucket_server_side_encryption_rules.deserialize_json(
                data["Rules"]
            )
        )
    return out
