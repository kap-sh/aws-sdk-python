"""Generated from Smithy shape ``com.amazonaws.kms#GenerateDataKeyPairResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.backing_key_id_type
    import aws_sdk_kms.types.ciphertext_type
    import aws_sdk_kms.types.data_key_pair_spec
    import aws_sdk_kms.types.key_id_type
    import aws_sdk_kms.types.plaintext_type
    import aws_sdk_kms.types.public_key_type


class GenerateDataKeyPairResponse(TypedDict):
    private_key_ciphertext_blob: NotRequired[
        "aws_sdk_kms.types.ciphertext_type.CiphertextType"
    ]
    """<p>The encrypted copy of the private key. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p>"""
    private_key_plaintext: NotRequired["aws_sdk_kms.types.plaintext_type.PlaintextType"]
    """<p>The plaintext copy of the private key. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p> <p>If the response includes the <code>CiphertextForRecipient</code> field, the <code>PrivateKeyPlaintext</code> field is null or empty.</p>"""
    public_key: NotRequired["aws_sdk_kms.types.public_key_type.PublicKeyType"]
    """<p>The public key (in plaintext). When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p>"""
    key_id: NotRequired["aws_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">key ARN</a>) of the KMS key that encrypted the private key.</p>"""
    key_pair_spec: NotRequired["aws_sdk_kms.types.data_key_pair_spec.DataKeyPairSpec"]
    """<p>The type of data key pair that was generated.</p>"""
    ciphertext_for_recipient: NotRequired[
        "aws_sdk_kms.types.ciphertext_type.CiphertextType"
    ]
    """<p>The plaintext private data key encrypted with the public key from the attestation document. This ciphertext can be decrypted only by using a private key from the attested environment. </p> <p>This field is included in the response only when the <code>Recipient</code> parameter in the request includes a valid attestation document from an Amazon Web Services Nitro enclave or NitroTPM. For information about the interaction between KMS and Amazon Web Services Nitro Enclaves or Amazon Web Services NitroTPM, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html\">Cryptographic attestation support in KMS</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    key_material_id: NotRequired[
        "aws_sdk_kms.types.backing_key_id_type.BackingKeyIdType"
    ]
    """<p>The identifier of the key material used to encrypt the private key.</p>"""
