"""Generated from Smithy shape ``com.amazonaws.kms#EncryptResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.ciphertext_type
    import aws_sdk_kms.types.encryption_algorithm_spec
    import aws_sdk_kms.types.key_id_type


class EncryptResponse(TypedDict):
    ciphertext_blob: NotRequired["aws_sdk_kms.types.ciphertext_type.CiphertextType"]
    """<p>The encrypted plaintext. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p>"""
    key_id: NotRequired["aws_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">key ARN</a>) of the KMS key that was used to encrypt the plaintext.</p>"""
    encryption_algorithm: NotRequired[
        "aws_sdk_kms.types.encryption_algorithm_spec.EncryptionAlgorithmSpec"
    ]
    """<p>The encryption algorithm that was used to encrypt the plaintext.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptResponse) -> dict:
    out: dict = {}
    if "ciphertext_blob" in value:
        import aws_sdk_kms.types.ciphertext_type

        out["CiphertextBlob"] = (
            aws_sdk_kms.types.ciphertext_type.serialize_aws_json_1_1(
                value["ciphertext_blob"]
            )
        )
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "encryption_algorithm" in value:
        import aws_sdk_kms.types.encryption_algorithm_spec

        out["EncryptionAlgorithm"] = (
            aws_sdk_kms.types.encryption_algorithm_spec.serialize_aws_json_1_1(
                value["encryption_algorithm"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptResponse:
    out: EncryptResponse = {}  # type: ignore[typeddict-item]
    if "CiphertextBlob" in data:
        import aws_sdk_kms.types.ciphertext_type

        out["ciphertext_blob"] = (
            aws_sdk_kms.types.ciphertext_type.deserialize_aws_json_1_1(
                data["CiphertextBlob"]
            )
        )
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    if "EncryptionAlgorithm" in data:
        import aws_sdk_kms.types.encryption_algorithm_spec

        out["encryption_algorithm"] = (
            aws_sdk_kms.types.encryption_algorithm_spec.deserialize_aws_json_1_1(
                data["EncryptionAlgorithm"]
            )
        )
    return out
