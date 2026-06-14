"""Generated from Smithy shape ``com.amazonaws.kms#DecryptResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.backing_key_id_type
    import aws_sdk_kms.types.ciphertext_type
    import aws_sdk_kms.types.encryption_algorithm_spec
    import aws_sdk_kms.types.key_id_type
    import aws_sdk_kms.types.plaintext_type


class DecryptResponse(TypedDict):
    key_id: NotRequired["aws_sdk_kms.types.key_id_type.KeyIdType"]
    r"""<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">key ARN</a>) of the KMS key that was used to decrypt the ciphertext.</p>"""
    plaintext: NotRequired["aws_sdk_kms.types.plaintext_type.PlaintextType"]
    """<p>Decrypted plaintext data. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p> <p>If the response includes the <code>CiphertextForRecipient</code> field, the <code>Plaintext</code> field is null or empty.</p>"""
    encryption_algorithm: NotRequired[
        "aws_sdk_kms.types.encryption_algorithm_spec.EncryptionAlgorithmSpec"
    ]
    """<p>The encryption algorithm that was used to decrypt the ciphertext.</p>"""
    ciphertext_for_recipient: NotRequired[
        "aws_sdk_kms.types.ciphertext_type.CiphertextType"
    ]
    r"""<p>The plaintext data encrypted with the public key from the attestation document. This ciphertext can be decrypted only by using a private key from the attested environment. </p> <p>This field is included in the response only when the <code>Recipient</code> parameter in the request includes a valid attestation document from an Amazon Web Services Nitro enclave or NitroTPM. For information about the interaction between KMS and Amazon Web Services Nitro Enclaves or Amazon Web Services NitroTPM, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html\">Cryptographic attestation support in KMS</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    key_material_id: NotRequired[
        "aws_sdk_kms.types.backing_key_id_type.BackingKeyIdType"
    ]
    """<p>The identifier of the key material used to decrypt the ciphertext. This field is present only when the operation uses a symmetric encryption KMS key. This field is omitted if the request includes the <code>Recipient</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DecryptResponse) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "plaintext" in value:
        import aws_sdk_kms.types.plaintext_type

        out["Plaintext"] = aws_sdk_kms.types.plaintext_type.serialize_aws_json_1_1(
            value["plaintext"]
        )
    if "encryption_algorithm" in value:
        import aws_sdk_kms.types.encryption_algorithm_spec

        out["EncryptionAlgorithm"] = (
            aws_sdk_kms.types.encryption_algorithm_spec.serialize_aws_json_1_1(
                value["encryption_algorithm"]
            )
        )
    if "ciphertext_for_recipient" in value:
        import aws_sdk_kms.types.ciphertext_type

        out["CiphertextForRecipient"] = (
            aws_sdk_kms.types.ciphertext_type.serialize_aws_json_1_1(
                value["ciphertext_for_recipient"]
            )
        )
    if "key_material_id" in value:
        out["KeyMaterialId"] = value["key_material_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DecryptResponse:
    out: DecryptResponse = {}  # type: ignore[typeddict-item]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    if "Plaintext" in data:
        import aws_sdk_kms.types.plaintext_type

        out["plaintext"] = aws_sdk_kms.types.plaintext_type.deserialize_aws_json_1_1(
            data["Plaintext"]
        )
    if "EncryptionAlgorithm" in data:
        import aws_sdk_kms.types.encryption_algorithm_spec

        out["encryption_algorithm"] = (
            aws_sdk_kms.types.encryption_algorithm_spec.deserialize_aws_json_1_1(
                data["EncryptionAlgorithm"]
            )
        )
    if "CiphertextForRecipient" in data:
        import aws_sdk_kms.types.ciphertext_type

        out["ciphertext_for_recipient"] = (
            aws_sdk_kms.types.ciphertext_type.deserialize_aws_json_1_1(
                data["CiphertextForRecipient"]
            )
        )
    if "KeyMaterialId" in data:
        out["key_material_id"] = data["KeyMaterialId"]
    return out
