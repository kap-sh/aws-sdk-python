"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketServerSideEncryptionByDefault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsS3BucketServerSideEncryptionByDefault(TypedDict):
    sse_algorithm: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Server-side encryption algorithm to use for the default encryption. Valid values are <code>aws: kms</code> or <code>AES256</code>.</p>"""
    kms_master_key_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>KMS key ID to use for the default encryption.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketServerSideEncryptionByDefault) -> dict:
    out: dict = {}
    if "sse_algorithm" in value:
        out["SSEAlgorithm"] = value["sse_algorithm"]
    if "kms_master_key_id" in value:
        out["KMSMasterKeyID"] = value["kms_master_key_id"]
    return out


def deserialize_json(data: dict) -> AwsS3BucketServerSideEncryptionByDefault:
    out: AwsS3BucketServerSideEncryptionByDefault = {}  # type: ignore[typeddict-item]
    if "SSEAlgorithm" in data:
        out["sse_algorithm"] = data["SSEAlgorithm"]
    if "KMSMasterKeyID" in data:
        out["kms_master_key_id"] = data["KMSMasterKeyID"]
    return out
