"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#VerifyPinDataOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.key_arn
    import aws_sdk_payment_cryptography_data.types.key_check_value


class VerifyPinDataOutput(TypedDict):
    verification_key_arn: "aws_sdk_payment_cryptography_data.types.key_arn.KeyArn"
    """<p>The <code>keyARN</code> of the PIN encryption key that Amazon Web Services Payment Cryptography uses for PIN or PIN Offset verification.</p>"""
    verification_key_check_value: (
        "aws_sdk_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    )
    """<p>The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.</p> <p>Amazon Web Services Payment Cryptography computes the KCV according to the CMAC specification.</p>"""
    encryption_key_arn: "aws_sdk_payment_cryptography_data.types.key_arn.KeyArn"
    """<p>The <code>keyARN</code> of the PEK that Amazon Web Services Payment Cryptography uses for encrypted pin block generation.</p>"""
    encryption_key_check_value: (
        "aws_sdk_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    )
    """<p>The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.</p> <p>Amazon Web Services Payment Cryptography computes the KCV according to the CMAC specification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerifyPinDataOutput) -> dict:
    out: dict = {}
    out["VerificationKeyArn"] = value["verification_key_arn"]
    out["VerificationKeyCheckValue"] = value["verification_key_check_value"]
    out["EncryptionKeyArn"] = value["encryption_key_arn"]
    out["EncryptionKeyCheckValue"] = value["encryption_key_check_value"]
    return out


def deserialize_json(data: dict) -> VerifyPinDataOutput:
    out: VerifyPinDataOutput = {}  # type: ignore[typeddict-item]
    if "VerificationKeyArn" in data:
        out["verification_key_arn"] = data["VerificationKeyArn"]
    else:
        raise DeserializationError("VerifyPinDataOutput.verification_key_arn required")
    if "VerificationKeyCheckValue" in data:
        out["verification_key_check_value"] = data["VerificationKeyCheckValue"]
    else:
        raise DeserializationError(
            "VerifyPinDataOutput.verification_key_check_value required"
        )
    if "EncryptionKeyArn" in data:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    else:
        raise DeserializationError("VerifyPinDataOutput.encryption_key_arn required")
    if "EncryptionKeyCheckValue" in data:
        out["encryption_key_check_value"] = data["EncryptionKeyCheckValue"]
    else:
        raise DeserializationError(
            "VerifyPinDataOutput.encryption_key_check_value required"
        )
    return out
