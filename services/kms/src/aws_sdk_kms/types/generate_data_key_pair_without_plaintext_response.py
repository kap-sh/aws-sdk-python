"""Generated from Smithy shape ``com.amazonaws.kms#GenerateDataKeyPairWithoutPlaintextResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.backing_key_id_type
    import aws_sdk_kms.types.ciphertext_type
    import aws_sdk_kms.types.data_key_pair_spec
    import aws_sdk_kms.types.key_id_type
    import aws_sdk_kms.types.public_key_type


class GenerateDataKeyPairWithoutPlaintextResponse(TypedDict):
    private_key_ciphertext_blob: NotRequired[
        "aws_sdk_kms.types.ciphertext_type.CiphertextType"
    ]
    """<p>The encrypted copy of the private key. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p>"""
    public_key: NotRequired["aws_sdk_kms.types.public_key_type.PublicKeyType"]
    """<p>The public key (in plaintext). When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p>"""
    key_id: NotRequired["aws_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">key ARN</a>) of the KMS key that encrypted the private key.</p>"""
    key_pair_spec: NotRequired["aws_sdk_kms.types.data_key_pair_spec.DataKeyPairSpec"]
    """<p>The type of data key pair that was generated.</p>"""
    key_material_id: NotRequired[
        "aws_sdk_kms.types.backing_key_id_type.BackingKeyIdType"
    ]
    """<p>The identifier of the key material used to encrypt the private key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerateDataKeyPairWithoutPlaintextResponse) -> dict:
    out: dict = {}
    if "private_key_ciphertext_blob" in value:
        import aws_sdk_kms.types.ciphertext_type

        out["PrivateKeyCiphertextBlob"] = (
            aws_sdk_kms.types.ciphertext_type.serialize_aws_json_1_1(
                value["private_key_ciphertext_blob"]
            )
        )
    if "public_key" in value:
        import aws_sdk_kms.types.public_key_type

        out["PublicKey"] = aws_sdk_kms.types.public_key_type.serialize_aws_json_1_1(
            value["public_key"]
        )
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "key_pair_spec" in value:
        import aws_sdk_kms.types.data_key_pair_spec

        out["KeyPairSpec"] = (
            aws_sdk_kms.types.data_key_pair_spec.serialize_aws_json_1_1(
                value["key_pair_spec"]
            )
        )
    if "key_material_id" in value:
        out["KeyMaterialId"] = value["key_material_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GenerateDataKeyPairWithoutPlaintextResponse:
    out: GenerateDataKeyPairWithoutPlaintextResponse = {}  # type: ignore[typeddict-item]
    if "PrivateKeyCiphertextBlob" in data:
        import aws_sdk_kms.types.ciphertext_type

        out["private_key_ciphertext_blob"] = (
            aws_sdk_kms.types.ciphertext_type.deserialize_aws_json_1_1(
                data["PrivateKeyCiphertextBlob"]
            )
        )
    if "PublicKey" in data:
        import aws_sdk_kms.types.public_key_type

        out["public_key"] = aws_sdk_kms.types.public_key_type.deserialize_aws_json_1_1(
            data["PublicKey"]
        )
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    if "KeyPairSpec" in data:
        import aws_sdk_kms.types.data_key_pair_spec

        out["key_pair_spec"] = (
            aws_sdk_kms.types.data_key_pair_spec.deserialize_aws_json_1_1(
                data["KeyPairSpec"]
            )
        )
    if "KeyMaterialId" in data:
        out["key_material_id"] = data["KeyMaterialId"]
    return out
