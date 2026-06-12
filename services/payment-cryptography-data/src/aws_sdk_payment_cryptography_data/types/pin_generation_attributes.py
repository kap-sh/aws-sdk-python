"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#PinGenerationAttributes``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.ibm3624_natural_pin
    import aws_sdk_payment_cryptography_data.types.ibm3624_pin_from_offset
    import aws_sdk_payment_cryptography_data.types.ibm3624_pin_offset
    import aws_sdk_payment_cryptography_data.types.ibm3624_random_pin
    import aws_sdk_payment_cryptography_data.types.visa_pin
    import aws_sdk_payment_cryptography_data.types.visa_pin_verification_value


class _PinGenerationAttributes_VisaPin(TypedDict):
    VisaPin: "aws_sdk_payment_cryptography_data.types.visa_pin.VisaPin"


class _PinGenerationAttributes_VisaPinVerificationValue(TypedDict):
    VisaPinVerificationValue: "aws_sdk_payment_cryptography_data.types.visa_pin_verification_value.VisaPinVerificationValue"


class _PinGenerationAttributes_Ibm3624PinOffset(TypedDict):
    Ibm3624PinOffset: (
        "aws_sdk_payment_cryptography_data.types.ibm3624_pin_offset.Ibm3624PinOffset"
    )


class _PinGenerationAttributes_Ibm3624NaturalPin(TypedDict):
    Ibm3624NaturalPin: (
        "aws_sdk_payment_cryptography_data.types.ibm3624_natural_pin.Ibm3624NaturalPin"
    )


class _PinGenerationAttributes_Ibm3624RandomPin(TypedDict):
    Ibm3624RandomPin: (
        "aws_sdk_payment_cryptography_data.types.ibm3624_random_pin.Ibm3624RandomPin"
    )


class _PinGenerationAttributes_Ibm3624PinFromOffset(TypedDict):
    Ibm3624PinFromOffset: "aws_sdk_payment_cryptography_data.types.ibm3624_pin_from_offset.Ibm3624PinFromOffset"


PinGenerationAttributes: TypeAlias = (
    _PinGenerationAttributes_VisaPin
    | _PinGenerationAttributes_VisaPinVerificationValue
    | _PinGenerationAttributes_Ibm3624PinOffset
    | _PinGenerationAttributes_Ibm3624NaturalPin
    | _PinGenerationAttributes_Ibm3624RandomPin
    | _PinGenerationAttributes_Ibm3624PinFromOffset
)


# --- restJson1 ser/de ---
def serialize_json(value: PinGenerationAttributes) -> dict:
    if "VisaPin" in value:
        import aws_sdk_payment_cryptography_data.types.visa_pin

        return {
            "VisaPin": aws_sdk_payment_cryptography_data.types.visa_pin.serialize_json(
                value["VisaPin"]
            )
        }
    elif "VisaPinVerificationValue" in value:
        import aws_sdk_payment_cryptography_data.types.visa_pin_verification_value

        return {
            "VisaPinVerificationValue": aws_sdk_payment_cryptography_data.types.visa_pin_verification_value.serialize_json(
                value["VisaPinVerificationValue"]
            )
        }
    elif "Ibm3624PinOffset" in value:
        import aws_sdk_payment_cryptography_data.types.ibm3624_pin_offset

        return {
            "Ibm3624PinOffset": aws_sdk_payment_cryptography_data.types.ibm3624_pin_offset.serialize_json(
                value["Ibm3624PinOffset"]
            )
        }
    elif "Ibm3624NaturalPin" in value:
        import aws_sdk_payment_cryptography_data.types.ibm3624_natural_pin

        return {
            "Ibm3624NaturalPin": aws_sdk_payment_cryptography_data.types.ibm3624_natural_pin.serialize_json(
                value["Ibm3624NaturalPin"]
            )
        }
    elif "Ibm3624RandomPin" in value:
        import aws_sdk_payment_cryptography_data.types.ibm3624_random_pin

        return {
            "Ibm3624RandomPin": aws_sdk_payment_cryptography_data.types.ibm3624_random_pin.serialize_json(
                value["Ibm3624RandomPin"]
            )
        }
    elif "Ibm3624PinFromOffset" in value:
        import aws_sdk_payment_cryptography_data.types.ibm3624_pin_from_offset

        return {
            "Ibm3624PinFromOffset": aws_sdk_payment_cryptography_data.types.ibm3624_pin_from_offset.serialize_json(
                value["Ibm3624PinFromOffset"]
            )
        }
    else:
        raise SerializationError("PinGenerationAttributes: no variant present")


def deserialize_json(data: dict) -> PinGenerationAttributes:
    if "VisaPin" in data:
        import aws_sdk_payment_cryptography_data.types.visa_pin

        return {
            "VisaPin": aws_sdk_payment_cryptography_data.types.visa_pin.deserialize_json(
                data["VisaPin"]
            )
        }
    elif "VisaPinVerificationValue" in data:
        import aws_sdk_payment_cryptography_data.types.visa_pin_verification_value

        return {
            "VisaPinVerificationValue": aws_sdk_payment_cryptography_data.types.visa_pin_verification_value.deserialize_json(
                data["VisaPinVerificationValue"]
            )
        }
    elif "Ibm3624PinOffset" in data:
        import aws_sdk_payment_cryptography_data.types.ibm3624_pin_offset

        return {
            "Ibm3624PinOffset": aws_sdk_payment_cryptography_data.types.ibm3624_pin_offset.deserialize_json(
                data["Ibm3624PinOffset"]
            )
        }
    elif "Ibm3624NaturalPin" in data:
        import aws_sdk_payment_cryptography_data.types.ibm3624_natural_pin

        return {
            "Ibm3624NaturalPin": aws_sdk_payment_cryptography_data.types.ibm3624_natural_pin.deserialize_json(
                data["Ibm3624NaturalPin"]
            )
        }
    elif "Ibm3624RandomPin" in data:
        import aws_sdk_payment_cryptography_data.types.ibm3624_random_pin

        return {
            "Ibm3624RandomPin": aws_sdk_payment_cryptography_data.types.ibm3624_random_pin.deserialize_json(
                data["Ibm3624RandomPin"]
            )
        }
    elif "Ibm3624PinFromOffset" in data:
        import aws_sdk_payment_cryptography_data.types.ibm3624_pin_from_offset

        return {
            "Ibm3624PinFromOffset": aws_sdk_payment_cryptography_data.types.ibm3624_pin_from_offset.deserialize_json(
                data["Ibm3624PinFromOffset"]
            )
        }
    else:
        raise DeserializationError("PinGenerationAttributes: no recognized variant key")
