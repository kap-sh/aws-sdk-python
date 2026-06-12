"""Generated from Smithy shape ``com.amazonaws.macie2#BucketCountByEncryptionType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__long


class BucketCountByEncryptionType(TypedDict):
    kms_managed: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of buckets whose default encryption settings are configured to encrypt new objects with an KMS key, either an Amazon Web Services managed key or a customer managed key. By default, these buckets encrypt new objects automatically using DSSE-KMS or SSE-KMS encryption.</p>"""
    s3_managed: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of buckets whose default encryption settings are configured to encrypt new objects with an Amazon S3 managed key. By default, these buckets encrypt new objects automatically using SSE-S3 encryption.</p>"""
    unencrypted: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of buckets that don't specify default server-side encryption behavior for new objects. Default encryption settings aren't configured for these buckets.</p>"""
    unknown: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of buckets that Amazon Macie doesn't have current encryption metadata for. For example, the buckets' permissions settings or a quota prevented Macie from retrieving the default encryption settings for the buckets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BucketCountByEncryptionType) -> dict:
    out: dict = {}
    if "kms_managed" in value:
        out["kmsManaged"] = value["kms_managed"]
    if "s3_managed" in value:
        out["s3Managed"] = value["s3_managed"]
    if "unencrypted" in value:
        out["unencrypted"] = value["unencrypted"]
    if "unknown" in value:
        out["unknown"] = value["unknown"]
    return out


def deserialize_json(data: dict) -> BucketCountByEncryptionType:
    out: BucketCountByEncryptionType = {}  # type: ignore[typeddict-item]
    if "kmsManaged" in data:
        out["kms_managed"] = data["kmsManaged"]
    if "s3Managed" in data:
        out["s3_managed"] = data["s3Managed"]
    if "unencrypted" in data:
        out["unencrypted"] = data["unencrypted"]
    if "unknown" in data:
        out["unknown"] = data["unknown"]
    return out
