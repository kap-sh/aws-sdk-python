"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdateRepositoryEncryptionKeyOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.kms_key_id
    import aws_sdk_codecommit.types.repository_id


class UpdateRepositoryEncryptionKeyOutput(TypedDict):
    repository_id: NotRequired["aws_sdk_codecommit.types.repository_id.RepositoryId"]
    """<p>The ID of the repository.</p>"""
    kms_key_id: NotRequired["aws_sdk_codecommit.types.kms_key_id.KmsKeyId"]
    """<p>The ID of the encryption key.</p>"""
    original_kms_key_id: NotRequired["aws_sdk_codecommit.types.kms_key_id.KmsKeyId"]
    """<p>The ID of the encryption key formerly used to encrypt and decrypt the repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRepositoryEncryptionKeyOutput) -> dict:
    out: dict = {}
    if "repository_id" in value:
        out["repositoryId"] = value["repository_id"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "original_kms_key_id" in value:
        out["originalKmsKeyId"] = value["original_kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRepositoryEncryptionKeyOutput:
    out: UpdateRepositoryEncryptionKeyOutput = {}  # type: ignore[typeddict-item]
    if "repositoryId" in data:
        out["repository_id"] = data["repositoryId"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "originalKmsKeyId" in data:
        out["original_kms_key_id"] = data["originalKmsKeyId"]
    return out
