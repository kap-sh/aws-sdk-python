"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdateRepositoryEncryptionKeyInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.kms_key_id
    import aws_sdk_codecommit.types.repository_name


class UpdateRepositoryEncryptionKeyInput(TypedDict):
    repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository for which you want to update the KMS encryption key used to encrypt and decrypt the repository.</p>"""
    kms_key_id: "aws_sdk_codecommit.types.kms_key_id.KmsKeyId"
    """<p>The ID of the encryption key. You can view the ID of an encryption key in the KMS console, or use the KMS APIs to programmatically retrieve a key ID. For more information about acceptable values for keyID, see <a href=\"https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html#KMS-Decrypt-request-KeyId\">KeyId</a> in the Decrypt API description in the <i>Key Management Service API Reference</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRepositoryEncryptionKeyInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRepositoryEncryptionKeyInput:
    out: UpdateRepositoryEncryptionKeyInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "UpdateRepositoryEncryptionKeyInput.repository_name required"
        )
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    else:
        raise DeserializationError(
            "UpdateRepositoryEncryptionKeyInput.kms_key_id required"
        )
    return out
