"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#PinVerificationAttributes``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.ibm3624_pin_verification
    import aws_sdk_payment_cryptography_data.types.visa_pin_verification


class _PinVerificationAttributes_VisaPin(TypedDict):
    VisaPin: "aws_sdk_payment_cryptography_data.types.visa_pin_verification.VisaPinVerification"


class _PinVerificationAttributes_Ibm3624Pin(TypedDict):
    Ibm3624Pin: "aws_sdk_payment_cryptography_data.types.ibm3624_pin_verification.Ibm3624PinVerification"


PinVerificationAttributes: TypeAlias = (
    _PinVerificationAttributes_VisaPin | _PinVerificationAttributes_Ibm3624Pin
)


# --- restJson1 ser/de ---
def serialize_json(value: PinVerificationAttributes) -> dict:
    if "VisaPin" in value:
        import aws_sdk_payment_cryptography_data.types.visa_pin_verification

        return {
            "VisaPin": aws_sdk_payment_cryptography_data.types.visa_pin_verification.serialize_json(
                value["VisaPin"]
            )
        }
    elif "Ibm3624Pin" in value:
        import aws_sdk_payment_cryptography_data.types.ibm3624_pin_verification

        return {
            "Ibm3624Pin": aws_sdk_payment_cryptography_data.types.ibm3624_pin_verification.serialize_json(
                value["Ibm3624Pin"]
            )
        }
    else:
        raise SerializationError("PinVerificationAttributes: no variant present")


def deserialize_json(data: dict) -> PinVerificationAttributes:
    if "VisaPin" in data:
        import aws_sdk_payment_cryptography_data.types.visa_pin_verification

        return {
            "VisaPin": aws_sdk_payment_cryptography_data.types.visa_pin_verification.deserialize_json(
                data["VisaPin"]
            )
        }
    elif "Ibm3624Pin" in data:
        import aws_sdk_payment_cryptography_data.types.ibm3624_pin_verification

        return {
            "Ibm3624Pin": aws_sdk_payment_cryptography_data.types.ibm3624_pin_verification.deserialize_json(
                data["Ibm3624Pin"]
            )
        }
    else:
        raise DeserializationError(
            "PinVerificationAttributes: no recognized variant key"
        )
