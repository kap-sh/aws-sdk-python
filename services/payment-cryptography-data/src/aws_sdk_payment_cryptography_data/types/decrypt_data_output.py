"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#DecryptDataOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.key_arn
    import aws_sdk_payment_cryptography_data.types.key_check_value
    import aws_sdk_payment_cryptography_data.types.plain_text_output_type


class DecryptDataOutput(TypedDict):
    key_arn: "aws_sdk_payment_cryptography_data.types.key_arn.KeyArn"
    """<p>The <code>keyARN</code> of the encryption key that Amazon Web Services Payment Cryptography uses for ciphertext decryption.</p>"""
    key_check_value: (
        "aws_sdk_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    )
    """<p>The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.</p> <p>Amazon Web Services Payment Cryptography computes the KCV according to the CMAC specification.</p>"""
    plain_text: "aws_sdk_payment_cryptography_data.types.plain_text_output_type.PlainTextOutputType"
    """<p>The decrypted plaintext data in hexBinary format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DecryptDataOutput) -> dict:
    out: dict = {}
    out["KeyArn"] = value["key_arn"]
    out["KeyCheckValue"] = value["key_check_value"]
    out["PlainText"] = value["plain_text"]
    return out


def deserialize_json(data: dict) -> DecryptDataOutput:
    out: DecryptDataOutput = {}  # type: ignore[typeddict-item]
    if "KeyArn" in data:
        out["key_arn"] = data["KeyArn"]
    else:
        raise DeserializationError("DecryptDataOutput.key_arn required")
    if "KeyCheckValue" in data:
        out["key_check_value"] = data["KeyCheckValue"]
    else:
        raise DeserializationError("DecryptDataOutput.key_check_value required")
    if "PlainText" in data:
        out["plain_text"] = data["PlainText"]
    else:
        raise DeserializationError("DecryptDataOutput.plain_text required")
    return out
