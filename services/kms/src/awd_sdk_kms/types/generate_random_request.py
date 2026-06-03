"""Generated from Smithy shape ``com.amazonaws.kms#GenerateRandomRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.custom_key_store_id_type
    import awd_sdk_kms.types.number_of_bytes_type
    import awd_sdk_kms.types.recipient_info


class GenerateRandomRequest(TypedDict):
    number_of_bytes: NotRequired[
        "awd_sdk_kms.types.number_of_bytes_type.NumberOfBytesType"
    ]
    """<p>The length of the random byte string. This parameter is required.</p>"""
    custom_key_store_id: NotRequired[
        "awd_sdk_kms.types.custom_key_store_id_type.CustomKeyStoreIdType"
    ]
    """<p>Generates the random byte string in the CloudHSM cluster that is associated with the specified CloudHSM key store. To find the ID of a custom key store, use the <a>DescribeCustomKeyStores</a> operation.</p> <p>External key store IDs are not valid for this parameter. If you specify the ID of an external key store, <code>GenerateRandom</code> throws an <code>UnsupportedOperationException</code>.</p>"""
    recipient: NotRequired["awd_sdk_kms.types.recipient_info.RecipientInfo"]
    """<p>A signed <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitro-enclave-how.html#term-attestdoc\">attestation document</a> from an Amazon Web Services Nitro enclave or NitroTPM, and the encryption algorithm to use with the public key in the attestation document. The only valid encryption algorithm is <code>RSAES_OAEP_SHA_256</code>. </p> <p>This parameter supports the <a href=\"https://docs.aws.amazon.com/enclaves/latest/user/developing-applications.html#sdk\">Amazon Web Services Nitro Enclaves SDK</a> or any Amazon Web Services SDK for Amazon Web Services Nitro Enclaves. It supports any Amazon Web Services SDK for Amazon Web Services NitroTPM. </p> <p>When you use this parameter, instead of returning plaintext bytes, KMS encrypts the plaintext bytes under the public key in the attestation document, and returns the resulting ciphertext in the <code>CiphertextForRecipient</code> field in the response. This ciphertext can be decrypted only with the private key in the attested environment. The <code>Plaintext</code> field in the response is null or empty.</p> <p>For information about the interaction between KMS and Amazon Web Services Nitro Enclaves or Amazon Web Services NitroTPM, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html\">Cryptographic attestation support in KMS</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
