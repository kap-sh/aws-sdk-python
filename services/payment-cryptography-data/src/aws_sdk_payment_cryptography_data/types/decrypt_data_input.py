"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#DecryptDataInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.cipher_text_type
    import aws_sdk_payment_cryptography_data.types.encryption_decryption_attributes
    import aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography_data.types.wrapped_key


class DecryptDataInput(TypedDict, closed=True):
    key_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the encryption key that Amazon Web Services Payment Cryptography uses for ciphertext decryption.</p> <p>When a WrappedKeyBlock is provided, this value will be the identifier to the key wrapping key. Otherwise, it is the key identifier used to perform the operation.</p>"""
    cipher_text: (
        "aws_sdk_payment_cryptography_data.types.cipher_text_type.CipherTextType"
    )
    """<p>The ciphertext to decrypt.</p>"""
    decryption_attributes: "aws_sdk_payment_cryptography_data.types.encryption_decryption_attributes.EncryptionDecryptionAttributes"
    """<p>The encryption key type and attributes for ciphertext decryption.</p>"""
    wrapped_key: NotRequired[
        "aws_sdk_payment_cryptography_data.types.wrapped_key.WrappedKey"
    ]
    """<p>The WrappedKeyBlock containing the encryption key for ciphertext decryption.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DecryptDataInput) -> dict:
    out: dict = {}
    out["CipherText"] = value["cipher_text"]
    import aws_sdk_payment_cryptography_data.types.encryption_decryption_attributes

    out["DecryptionAttributes"] = (
        aws_sdk_payment_cryptography_data.types.encryption_decryption_attributes.serialize_json(
            value["decryption_attributes"]
        )
    )
    if "wrapped_key" in value:
        import aws_sdk_payment_cryptography_data.types.wrapped_key

        out["WrappedKey"] = (
            aws_sdk_payment_cryptography_data.types.wrapped_key.serialize_json(
                value["wrapped_key"]
            )
        )
    return out


def deserialize_json(data: dict) -> DecryptDataInput:
    out: DecryptDataInput = {}  # type: ignore[typeddict-item]
    if "CipherText" in data:
        out["cipher_text"] = data["CipherText"]
    else:
        raise DeserializationError("DecryptDataInput.cipher_text required")
    if "DecryptionAttributes" in data:
        import aws_sdk_payment_cryptography_data.types.encryption_decryption_attributes

        out["decryption_attributes"] = (
            aws_sdk_payment_cryptography_data.types.encryption_decryption_attributes.deserialize_json(
                data["DecryptionAttributes"]
            )
        )
    else:
        raise DeserializationError("DecryptDataInput.decryption_attributes required")
    if "WrappedKey" in data:
        import aws_sdk_payment_cryptography_data.types.wrapped_key

        out["wrapped_key"] = (
            aws_sdk_payment_cryptography_data.types.wrapped_key.deserialize_json(
                data["WrappedKey"]
            )
        )
    return out
