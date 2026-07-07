"""Generated from Smithy shape ``com.amazonaws.kms#GenerateRandomRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kms.types.custom_key_store_id_type
    import aws_sdk_kms.types.number_of_bytes_type
    import aws_sdk_kms.types.recipient_info


class GenerateRandomRequest(TypedDict, closed=True):
    number_of_bytes: NotRequired[
        "aws_sdk_kms.types.number_of_bytes_type.NumberOfBytesType"
    ]
    """<p>The length of the random byte string. This parameter is required.</p>"""
    custom_key_store_id: NotRequired[
        "aws_sdk_kms.types.custom_key_store_id_type.CustomKeyStoreIdType"
    ]
    """<p>Generates the random byte string in the CloudHSM cluster that is associated with the specified CloudHSM key store. To find the ID of a custom key store, use the <a>DescribeCustomKeyStores</a> operation.</p> <p>External key store IDs are not valid for this parameter. If you specify the ID of an external key store, <code>GenerateRandom</code> throws an <code>UnsupportedOperationException</code>.</p>"""
    recipient: NotRequired["aws_sdk_kms.types.recipient_info.RecipientInfo"]
    r"""<p>A signed <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitro-enclave-how.html#term-attestdoc\">attestation document</a> from an Amazon Web Services Nitro enclave or NitroTPM, and the encryption algorithm to use with the public key in the attestation document. The only valid encryption algorithm is <code>RSAES_OAEP_SHA_256</code>. </p> <p>This parameter supports the <a href=\"https://docs.aws.amazon.com/enclaves/latest/user/developing-applications.html#sdk\">Amazon Web Services Nitro Enclaves SDK</a> or any Amazon Web Services SDK for Amazon Web Services Nitro Enclaves. It supports any Amazon Web Services SDK for Amazon Web Services NitroTPM. </p> <p>When you use this parameter, instead of returning plaintext bytes, KMS encrypts the plaintext bytes under the public key in the attestation document, and returns the resulting ciphertext in the <code>CiphertextForRecipient</code> field in the response. This ciphertext can be decrypted only with the private key in the attested environment. The <code>Plaintext</code> field in the response is null or empty.</p> <p>For information about the interaction between KMS and Amazon Web Services Nitro Enclaves or Amazon Web Services NitroTPM, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html\">Cryptographic attestation support in KMS</a> in the <i>Key Management Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerateRandomRequest) -> dict:
    out: dict = {}
    if "number_of_bytes" in value:
        out["NumberOfBytes"] = value["number_of_bytes"]
    if "custom_key_store_id" in value:
        out["CustomKeyStoreId"] = value["custom_key_store_id"]
    if "recipient" in value:
        import aws_sdk_kms.types.recipient_info

        out["Recipient"] = aws_sdk_kms.types.recipient_info.serialize_aws_json_1_1(
            value["recipient"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GenerateRandomRequest:
    out: GenerateRandomRequest = {}  # type: ignore[typeddict-item]
    if "NumberOfBytes" in data:
        out["number_of_bytes"] = data["NumberOfBytes"]
    if "CustomKeyStoreId" in data:
        out["custom_key_store_id"] = data["CustomKeyStoreId"]
    if "Recipient" in data:
        import aws_sdk_kms.types.recipient_info

        out["recipient"] = aws_sdk_kms.types.recipient_info.deserialize_aws_json_1_1(
            data["Recipient"]
        )
    return out
