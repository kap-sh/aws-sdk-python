"""Generated from Smithy shape ``com.amazonaws.osis#EncryptionAtRestOptions``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_osis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_osis.types.kms_key_arn


class EncryptionAtRestOptions(TypedDict):
    kms_key_arn: "aws_sdk_osis.types.kms_key_arn.KmsKeyArn"
    """<p>The ARN of the KMS key used to encrypt buffer data. By default, data is encrypted using an Amazon Web Services owned key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionAtRestOptions) -> dict:
    out: dict = {}
    out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> EncryptionAtRestOptions:
    out: EncryptionAtRestOptions = {}  # type: ignore[typeddict-item]
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    else:
        raise DeserializationError("EncryptionAtRestOptions.kms_key_arn required")
    return out
