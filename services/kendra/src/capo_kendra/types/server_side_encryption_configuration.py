"""Generated from Smithy shape ``com.amazonaws.kendra#ServerSideEncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.kms_key_id


class ServerSideEncryptionConfiguration(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_kendra.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the KMS key. Amazon Kendra doesn't support asymmetric keys.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServerSideEncryptionConfiguration) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServerSideEncryptionConfiguration:
    out: ServerSideEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
