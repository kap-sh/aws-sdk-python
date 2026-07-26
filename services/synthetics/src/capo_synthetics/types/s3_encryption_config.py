"""Generated from Smithy shape ``com.amazonaws.synthetics#S3EncryptionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.encryption_mode
    import capo_synthetics.types.kms_key_arn


class S3EncryptionConfig(TypedDict, closed=True):
    encryption_mode: NotRequired["capo_synthetics.types.encryption_mode.EncryptionMode"]
    """<p> The encryption method to use for artifacts created by this canary. Specify <code>SSE_S3</code> to use server-side encryption (SSE) with an Amazon S3-managed key. Specify <code>SSE-KMS</code> to use server-side encryption with a customer-managed KMS key.</p> <p>If you omit this parameter, an Amazon Web Services-managed KMS key is used. </p>"""
    kms_key_arn: NotRequired["capo_synthetics.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the customer-managed KMS key to use, if you specify <code>SSE-KMS</code> for <code>EncryptionMode</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3EncryptionConfig) -> dict:
    out: dict = {}
    if "encryption_mode" in value:
        import capo_synthetics.types.encryption_mode

        out["EncryptionMode"] = capo_synthetics.types.encryption_mode.serialize_json(
            value["encryption_mode"]
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> S3EncryptionConfig:
    out: S3EncryptionConfig = {}  # type: ignore[typeddict-item]
    if "EncryptionMode" in data:
        import capo_synthetics.types.encryption_mode

        out["encryption_mode"] = capo_synthetics.types.encryption_mode.deserialize_json(
            data["EncryptionMode"]
        )
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
