"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#EncryptDataInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.encryption_decryption_attributes
    import aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography_data.types.plain_text_type
    import aws_sdk_payment_cryptography_data.types.wrapped_key


class EncryptDataInput(TypedDict):
    key_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the encryption key that Amazon Web Services Payment Cryptography uses for plaintext encryption.</p> <p>When a WrappedKeyBlock is provided, this value will be the identifier to the key wrapping key. Otherwise, it is the key identifier used to perform the operation.</p>"""
    plain_text: "aws_sdk_payment_cryptography_data.types.plain_text_type.PlainTextType"
    """<p>The plaintext to be encrypted.</p> <note> <p>For encryption using asymmetric keys, plaintext data length is constrained by encryption key strength that you define in <code>KeyAlgorithm</code> and padding type that you define in <code>AsymmetricEncryptionAttributes</code>. For more information, see <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/userguide/encrypt-data.html\">Encrypt data</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> </note>"""
    encryption_attributes: "aws_sdk_payment_cryptography_data.types.encryption_decryption_attributes.EncryptionDecryptionAttributes"
    """<p>The encryption key type and attributes for plaintext encryption.</p>"""
    wrapped_key: NotRequired[
        "aws_sdk_payment_cryptography_data.types.wrapped_key.WrappedKey"
    ]
    """<p>The WrappedKeyBlock containing the encryption key for plaintext encryption.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptDataInput) -> dict:
    out: dict = {}
    out["PlainText"] = value["plain_text"]
    import aws_sdk_payment_cryptography_data.types.encryption_decryption_attributes

    out["EncryptionAttributes"] = (
        aws_sdk_payment_cryptography_data.types.encryption_decryption_attributes.serialize_json(
            value["encryption_attributes"]
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


def deserialize_json(data: dict) -> EncryptDataInput:
    out: EncryptDataInput = {}  # type: ignore[typeddict-item]
    if "PlainText" in data:
        out["plain_text"] = data["PlainText"]
    else:
        raise DeserializationError("EncryptDataInput.plain_text required")
    if "EncryptionAttributes" in data:
        import aws_sdk_payment_cryptography_data.types.encryption_decryption_attributes

        out["encryption_attributes"] = (
            aws_sdk_payment_cryptography_data.types.encryption_decryption_attributes.deserialize_json(
                data["EncryptionAttributes"]
            )
        )
    else:
        raise DeserializationError("EncryptDataInput.encryption_attributes required")
    if "WrappedKey" in data:
        import aws_sdk_payment_cryptography_data.types.wrapped_key

        out["wrapped_key"] = (
            aws_sdk_payment_cryptography_data.types.wrapped_key.deserialize_json(
                data["WrappedKey"]
            )
        )
    return out
