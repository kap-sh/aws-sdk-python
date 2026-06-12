"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#ReEncryptDataInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.cipher_text_type
    import aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography_data.types.re_encryption_attributes
    import aws_sdk_payment_cryptography_data.types.wrapped_key


class ReEncryptDataInput(TypedDict):
    incoming_key_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the encryption key of incoming ciphertext data.</p> <p>When a WrappedKeyBlock is provided, this value will be the identifier to the key wrapping key. Otherwise, it is the key identifier used to perform the operation.</p>"""
    outgoing_key_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the encryption key of outgoing ciphertext data after encryption by Amazon Web Services Payment Cryptography.</p>"""
    cipher_text: (
        "aws_sdk_payment_cryptography_data.types.cipher_text_type.CipherTextType"
    )
    """<p>Ciphertext to be encrypted. The minimum allowed length is 16 bytes and maximum allowed length is 4096 bytes.</p>"""
    incoming_encryption_attributes: "aws_sdk_payment_cryptography_data.types.re_encryption_attributes.ReEncryptionAttributes"
    """<p>The attributes and values for incoming ciphertext.</p>"""
    outgoing_encryption_attributes: "aws_sdk_payment_cryptography_data.types.re_encryption_attributes.ReEncryptionAttributes"
    """<p>The attributes and values for outgoing ciphertext data after encryption by Amazon Web Services Payment Cryptography.</p>"""
    incoming_wrapped_key: NotRequired[
        "aws_sdk_payment_cryptography_data.types.wrapped_key.WrappedKey"
    ]
    """<p>The WrappedKeyBlock containing the encryption key of incoming ciphertext data.</p>"""
    outgoing_wrapped_key: NotRequired[
        "aws_sdk_payment_cryptography_data.types.wrapped_key.WrappedKey"
    ]
    """<p>The WrappedKeyBlock containing the encryption key of outgoing ciphertext data after encryption by Amazon Web Services Payment Cryptography.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReEncryptDataInput) -> dict:
    out: dict = {}
    out["OutgoingKeyIdentifier"] = value["outgoing_key_identifier"]
    out["CipherText"] = value["cipher_text"]
    import aws_sdk_payment_cryptography_data.types.re_encryption_attributes

    out["IncomingEncryptionAttributes"] = (
        aws_sdk_payment_cryptography_data.types.re_encryption_attributes.serialize_json(
            value["incoming_encryption_attributes"]
        )
    )
    import aws_sdk_payment_cryptography_data.types.re_encryption_attributes

    out["OutgoingEncryptionAttributes"] = (
        aws_sdk_payment_cryptography_data.types.re_encryption_attributes.serialize_json(
            value["outgoing_encryption_attributes"]
        )
    )
    if "incoming_wrapped_key" in value:
        import aws_sdk_payment_cryptography_data.types.wrapped_key

        out["IncomingWrappedKey"] = (
            aws_sdk_payment_cryptography_data.types.wrapped_key.serialize_json(
                value["incoming_wrapped_key"]
            )
        )
    if "outgoing_wrapped_key" in value:
        import aws_sdk_payment_cryptography_data.types.wrapped_key

        out["OutgoingWrappedKey"] = (
            aws_sdk_payment_cryptography_data.types.wrapped_key.serialize_json(
                value["outgoing_wrapped_key"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReEncryptDataInput:
    out: ReEncryptDataInput = {}  # type: ignore[typeddict-item]
    if "OutgoingKeyIdentifier" in data:
        out["outgoing_key_identifier"] = data["OutgoingKeyIdentifier"]
    else:
        raise DeserializationError(
            "ReEncryptDataInput.outgoing_key_identifier required"
        )
    if "CipherText" in data:
        out["cipher_text"] = data["CipherText"]
    else:
        raise DeserializationError("ReEncryptDataInput.cipher_text required")
    if "IncomingEncryptionAttributes" in data:
        import aws_sdk_payment_cryptography_data.types.re_encryption_attributes

        out["incoming_encryption_attributes"] = (
            aws_sdk_payment_cryptography_data.types.re_encryption_attributes.deserialize_json(
                data["IncomingEncryptionAttributes"]
            )
        )
    else:
        raise DeserializationError(
            "ReEncryptDataInput.incoming_encryption_attributes required"
        )
    if "OutgoingEncryptionAttributes" in data:
        import aws_sdk_payment_cryptography_data.types.re_encryption_attributes

        out["outgoing_encryption_attributes"] = (
            aws_sdk_payment_cryptography_data.types.re_encryption_attributes.deserialize_json(
                data["OutgoingEncryptionAttributes"]
            )
        )
    else:
        raise DeserializationError(
            "ReEncryptDataInput.outgoing_encryption_attributes required"
        )
    if "IncomingWrappedKey" in data:
        import aws_sdk_payment_cryptography_data.types.wrapped_key

        out["incoming_wrapped_key"] = (
            aws_sdk_payment_cryptography_data.types.wrapped_key.deserialize_json(
                data["IncomingWrappedKey"]
            )
        )
    if "OutgoingWrappedKey" in data:
        import aws_sdk_payment_cryptography_data.types.wrapped_key

        out["outgoing_wrapped_key"] = (
            aws_sdk_payment_cryptography_data.types.wrapped_key.deserialize_json(
                data["OutgoingWrappedKey"]
            )
        )
    return out
