"""Generated from Smithy shape ``com.amazonaws.macie2#BucketServerSideEncryption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.type


class BucketServerSideEncryption(TypedDict):
    kms_master_key_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) or unique identifier (key ID) for the KMS key that's used by default to encrypt objects that are added to the bucket. This value is null if the bucket is configured to use an Amazon S3 managed key to encrypt new objects.</p>"""
    type: NotRequired["aws_sdk_macie2.types.type.Type"]
    """<p>The server-side encryption algorithm that's used by default to encrypt objects that are added to the bucket. Possible values are:</p> <ul><li><p>AES256 - New objects use SSE-S3 encryption. They're encrypted with an Amazon S3 managed key.</p></li> <li><p>aws:kms - New objects use SSE-KMS encryption. They're encrypted with an KMS key (kmsMasterKeyId), either an Amazon Web Services managed key or a customer managed key.</p></li> <li><p>aws:kms:dsse - New objects use DSSE-KMS encryption. They're encrypted with an KMS key (kmsMasterKeyId), either an Amazon Web Services managed key or a customer managed key.</p></li> <li><p>NONE - The bucket's default encryption settings don't specify server-side encryption behavior for new objects.</p></li></ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: BucketServerSideEncryption) -> dict:
    out: dict = {}
    if "kms_master_key_id" in value:
        out["kmsMasterKeyId"] = value["kms_master_key_id"]
    if "type" in value:
        import aws_sdk_macie2.types.type

        out["type"] = aws_sdk_macie2.types.type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> BucketServerSideEncryption:
    out: BucketServerSideEncryption = {}  # type: ignore[typeddict-item]
    if "kmsMasterKeyId" in data:
        out["kms_master_key_id"] = data["kmsMasterKeyId"]
    if "type" in data:
        import aws_sdk_macie2.types.type

        out["type"] = aws_sdk_macie2.types.type.deserialize_json(data["type"])
    return out
