"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#DerivationMethodAttributes``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.amex_attributes
    import aws_sdk_payment_cryptography_data.types.emv2000_attributes
    import aws_sdk_payment_cryptography_data.types.emv_common_attributes
    import aws_sdk_payment_cryptography_data.types.master_card_attributes
    import aws_sdk_payment_cryptography_data.types.visa_attributes


class _DerivationMethodAttributes_EmvCommon(TypedDict):
    EmvCommon: "aws_sdk_payment_cryptography_data.types.emv_common_attributes.EmvCommonAttributes"


class _DerivationMethodAttributes_Amex(TypedDict):
    Amex: "aws_sdk_payment_cryptography_data.types.amex_attributes.AmexAttributes"


class _DerivationMethodAttributes_Visa(TypedDict):
    Visa: "aws_sdk_payment_cryptography_data.types.visa_attributes.VisaAttributes"


class _DerivationMethodAttributes_Emv2000(TypedDict):
    Emv2000: (
        "aws_sdk_payment_cryptography_data.types.emv2000_attributes.Emv2000Attributes"
    )


class _DerivationMethodAttributes_Mastercard(TypedDict):
    Mastercard: "aws_sdk_payment_cryptography_data.types.master_card_attributes.MasterCardAttributes"


DerivationMethodAttributes: TypeAlias = (
    _DerivationMethodAttributes_EmvCommon
    | _DerivationMethodAttributes_Amex
    | _DerivationMethodAttributes_Visa
    | _DerivationMethodAttributes_Emv2000
    | _DerivationMethodAttributes_Mastercard
)


# --- restJson1 ser/de ---
def serialize_json(value: DerivationMethodAttributes) -> dict:
    if "EmvCommon" in value:
        import aws_sdk_payment_cryptography_data.types.emv_common_attributes

        return {
            "EmvCommon": aws_sdk_payment_cryptography_data.types.emv_common_attributes.serialize_json(
                value["EmvCommon"]
            )
        }
    elif "Amex" in value:
        import aws_sdk_payment_cryptography_data.types.amex_attributes

        return {
            "Amex": aws_sdk_payment_cryptography_data.types.amex_attributes.serialize_json(
                value["Amex"]
            )
        }
    elif "Visa" in value:
        import aws_sdk_payment_cryptography_data.types.visa_attributes

        return {
            "Visa": aws_sdk_payment_cryptography_data.types.visa_attributes.serialize_json(
                value["Visa"]
            )
        }
    elif "Emv2000" in value:
        import aws_sdk_payment_cryptography_data.types.emv2000_attributes

        return {
            "Emv2000": aws_sdk_payment_cryptography_data.types.emv2000_attributes.serialize_json(
                value["Emv2000"]
            )
        }
    elif "Mastercard" in value:
        import aws_sdk_payment_cryptography_data.types.master_card_attributes

        return {
            "Mastercard": aws_sdk_payment_cryptography_data.types.master_card_attributes.serialize_json(
                value["Mastercard"]
            )
        }
    else:
        raise SerializationError("DerivationMethodAttributes: no variant present")


def deserialize_json(data: dict) -> DerivationMethodAttributes:
    if "EmvCommon" in data:
        import aws_sdk_payment_cryptography_data.types.emv_common_attributes

        return {
            "EmvCommon": aws_sdk_payment_cryptography_data.types.emv_common_attributes.deserialize_json(
                data["EmvCommon"]
            )
        }
    elif "Amex" in data:
        import aws_sdk_payment_cryptography_data.types.amex_attributes

        return {
            "Amex": aws_sdk_payment_cryptography_data.types.amex_attributes.deserialize_json(
                data["Amex"]
            )
        }
    elif "Visa" in data:
        import aws_sdk_payment_cryptography_data.types.visa_attributes

        return {
            "Visa": aws_sdk_payment_cryptography_data.types.visa_attributes.deserialize_json(
                data["Visa"]
            )
        }
    elif "Emv2000" in data:
        import aws_sdk_payment_cryptography_data.types.emv2000_attributes

        return {
            "Emv2000": aws_sdk_payment_cryptography_data.types.emv2000_attributes.deserialize_json(
                data["Emv2000"]
            )
        }
    elif "Mastercard" in data:
        import aws_sdk_payment_cryptography_data.types.master_card_attributes

        return {
            "Mastercard": aws_sdk_payment_cryptography_data.types.master_card_attributes.deserialize_json(
                data["Mastercard"]
            )
        }
    else:
        raise DeserializationError(
            "DerivationMethodAttributes: no recognized variant key"
        )
