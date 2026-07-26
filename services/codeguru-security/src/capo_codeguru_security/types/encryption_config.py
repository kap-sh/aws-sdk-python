"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#EncryptionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_security.types.kms_key_arn


class EncryptionConfig(TypedDict, closed=True):
    kms_key_arn: NotRequired["capo_codeguru_security.types.kms_key_arn.KmsKeyArn"]
    """<p>The KMS key ARN that is used for encryption. If an AWS-managed key is used for encryption, returns empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfig) -> dict:
    out: dict = {}
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> EncryptionConfig:
    out: EncryptionConfig = {}  # type: ignore[typeddict-item]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
