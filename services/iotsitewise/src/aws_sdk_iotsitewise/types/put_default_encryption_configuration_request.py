"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PutDefaultEncryptionConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.encryption_type
    import aws_sdk_iotsitewise.types.kms_key_id


class PutDefaultEncryptionConfigurationRequest(TypedDict):
    encryption_type: "aws_sdk_iotsitewise.types.encryption_type.EncryptionType"
    """<p>The type of encryption used for the encryption configuration.</p>"""
    kms_key_id: NotRequired["aws_sdk_iotsitewise.types.kms_key_id.KmsKeyId"]
    """<p>The Key ID of the customer managed key used for KMS encryption. This is required if you use <code>KMS_BASED_ENCRYPTION</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDefaultEncryptionConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.encryption_type

    out["encryptionType"] = aws_sdk_iotsitewise.types.encryption_type.serialize_json(
        value["encryption_type"]
    )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> PutDefaultEncryptionConfigurationRequest:
    out: PutDefaultEncryptionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "encryptionType" in data:
        import aws_sdk_iotsitewise.types.encryption_type

        out["encryption_type"] = (
            aws_sdk_iotsitewise.types.encryption_type.deserialize_json(
                data["encryptionType"]
            )
        )
    else:
        raise DeserializationError(
            "PutDefaultEncryptionConfigurationRequest.encryption_type required"
        )
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
