"""Generated from Smithy shape ``com.amazonaws.kms#ReEncryptResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.backing_key_id_type
    import aws_sdk_kms.types.ciphertext_type
    import aws_sdk_kms.types.encryption_algorithm_spec
    import aws_sdk_kms.types.key_id_type


class ReEncryptResponse(TypedDict):
    ciphertext_blob: NotRequired["aws_sdk_kms.types.ciphertext_type.CiphertextType"]
    """<p>The reencrypted data. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p>"""
    source_key_id: NotRequired["aws_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>Unique identifier of the KMS key used to originally encrypt the data.</p>"""
    key_id: NotRequired["aws_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">key ARN</a>) of the KMS key that was used to reencrypt the data.</p>"""
    source_encryption_algorithm: NotRequired[
        "aws_sdk_kms.types.encryption_algorithm_spec.EncryptionAlgorithmSpec"
    ]
    """<p>The encryption algorithm that was used to decrypt the ciphertext before it was reencrypted.</p>"""
    destination_encryption_algorithm: NotRequired[
        "aws_sdk_kms.types.encryption_algorithm_spec.EncryptionAlgorithmSpec"
    ]
    """<p>The encryption algorithm that was used to reencrypt the data.</p>"""
    source_key_material_id: NotRequired[
        "aws_sdk_kms.types.backing_key_id_type.BackingKeyIdType"
    ]
    """<p>The identifier of the key material used to originally encrypt the data. This field is present only when the original encryption used a symmetric encryption KMS key.</p>"""
    destination_key_material_id: NotRequired[
        "aws_sdk_kms.types.backing_key_id_type.BackingKeyIdType"
    ]
    """<p>The identifier of the key material used to reencrypt the data. This field is present only when data is reencrypted using a symmetric encryption KMS key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReEncryptResponse) -> dict:
    out: dict = {}
    if "ciphertext_blob" in value:
        import aws_sdk_kms.types.ciphertext_type

        out["CiphertextBlob"] = (
            aws_sdk_kms.types.ciphertext_type.serialize_aws_json_1_1(
                value["ciphertext_blob"]
            )
        )
    if "source_key_id" in value:
        out["SourceKeyId"] = value["source_key_id"]
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "source_encryption_algorithm" in value:
        import aws_sdk_kms.types.encryption_algorithm_spec

        out["SourceEncryptionAlgorithm"] = (
            aws_sdk_kms.types.encryption_algorithm_spec.serialize_aws_json_1_1(
                value["source_encryption_algorithm"]
            )
        )
    if "destination_encryption_algorithm" in value:
        import aws_sdk_kms.types.encryption_algorithm_spec

        out["DestinationEncryptionAlgorithm"] = (
            aws_sdk_kms.types.encryption_algorithm_spec.serialize_aws_json_1_1(
                value["destination_encryption_algorithm"]
            )
        )
    if "source_key_material_id" in value:
        out["SourceKeyMaterialId"] = value["source_key_material_id"]
    if "destination_key_material_id" in value:
        out["DestinationKeyMaterialId"] = value["destination_key_material_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReEncryptResponse:
    out: ReEncryptResponse = {}  # type: ignore[typeddict-item]
    if "CiphertextBlob" in data:
        import aws_sdk_kms.types.ciphertext_type

        out["ciphertext_blob"] = (
            aws_sdk_kms.types.ciphertext_type.deserialize_aws_json_1_1(
                data["CiphertextBlob"]
            )
        )
    if "SourceKeyId" in data:
        out["source_key_id"] = data["SourceKeyId"]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    if "SourceEncryptionAlgorithm" in data:
        import aws_sdk_kms.types.encryption_algorithm_spec

        out["source_encryption_algorithm"] = (
            aws_sdk_kms.types.encryption_algorithm_spec.deserialize_aws_json_1_1(
                data["SourceEncryptionAlgorithm"]
            )
        )
    if "DestinationEncryptionAlgorithm" in data:
        import aws_sdk_kms.types.encryption_algorithm_spec

        out["destination_encryption_algorithm"] = (
            aws_sdk_kms.types.encryption_algorithm_spec.deserialize_aws_json_1_1(
                data["DestinationEncryptionAlgorithm"]
            )
        )
    if "SourceKeyMaterialId" in data:
        out["source_key_material_id"] = data["SourceKeyMaterialId"]
    if "DestinationKeyMaterialId" in data:
        out["destination_key_material_id"] = data["DestinationKeyMaterialId"]
    return out
