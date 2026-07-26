"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketServerSideEncryptionRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_s3_bucket_server_side_encryption_by_default


class AwsS3BucketServerSideEncryptionRule(TypedDict, closed=True):
    apply_server_side_encryption_by_default: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_server_side_encryption_by_default.AwsS3BucketServerSideEncryptionByDefault"
    ]
    """<p>Specifies the default server-side encryption to apply to new objects in the bucket. If a <code>PUT</code> object request doesn't specify any server-side encryption, this default encryption is applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketServerSideEncryptionRule) -> dict:
    out: dict = {}
    if "apply_server_side_encryption_by_default" in value:
        import capo_securityhub.types.aws_s3_bucket_server_side_encryption_by_default

        out["ApplyServerSideEncryptionByDefault"] = (
            capo_securityhub.types.aws_s3_bucket_server_side_encryption_by_default.serialize_json(
                value["apply_server_side_encryption_by_default"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsS3BucketServerSideEncryptionRule:
    out: AwsS3BucketServerSideEncryptionRule = {}  # type: ignore[typeddict-item]
    if "ApplyServerSideEncryptionByDefault" in data:
        import capo_securityhub.types.aws_s3_bucket_server_side_encryption_by_default

        out["apply_server_side_encryption_by_default"] = (
            capo_securityhub.types.aws_s3_bucket_server_side_encryption_by_default.deserialize_json(
                data["ApplyServerSideEncryptionByDefault"]
            )
        )
    return out
