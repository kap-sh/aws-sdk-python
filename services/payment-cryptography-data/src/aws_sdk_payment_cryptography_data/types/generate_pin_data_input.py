"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#GeneratePinDataInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.integer_range_between4_and12
    import aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography_data.types.pin_block_format_for_pin_data
    import aws_sdk_payment_cryptography_data.types.pin_generation_attributes
    import aws_sdk_payment_cryptography_data.types.primary_account_number_type
    import aws_sdk_payment_cryptography_data.types.wrapped_key


class GeneratePinDataInput(TypedDict):
    generation_key_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the PEK that Amazon Web Services Payment Cryptography uses for pin data generation.</p>"""
    encryption_key_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the PEK that Amazon Web Services Payment Cryptography uses to encrypt the PIN Block. For ECDH, it is the <code>keyARN</code> of the asymmetric ECC key.</p>"""
    generation_attributes: "aws_sdk_payment_cryptography_data.types.pin_generation_attributes.PinGenerationAttributes"
    """<p>The attributes and values to use for PIN, PVV, or PIN Offset generation.</p>"""
    pin_data_length: NotRequired[
        "aws_sdk_payment_cryptography_data.types.integer_range_between4_and12.IntegerRangeBetween4And12"
    ]
    """<p>The length of PIN under generation.</p>"""
    primary_account_number: NotRequired[
        "aws_sdk_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    ]
    """<p>The Primary Account Number (PAN), a unique identifier for a payment credit or debit card that associates the card with a specific account holder.</p>"""
    pin_block_format: "aws_sdk_payment_cryptography_data.types.pin_block_format_for_pin_data.PinBlockFormatForPinData"
    """<p>The PIN encoding format for pin data generation as specified in ISO 9564. Amazon Web Services Payment Cryptography supports <code>ISO_Format_0</code>, <code>ISO_Format_3</code> and <code>ISO_Format_4</code>.</p> <p>The <code>ISO_Format_0</code> PIN block format is equivalent to the ANSI X9.8, VISA-1, and ECI-1 PIN block formats. It is similar to a VISA-4 PIN block format. It supports a PIN from 4 to 12 digits in length.</p> <p>The <code>ISO_Format_3</code> PIN block format is the same as <code>ISO_Format_0</code> except that the fill digits are random values from 10 to 15.</p> <p>The <code>ISO_Format_4</code> PIN block format is the only one supporting AES encryption.</p>"""
    encryption_wrapped_key: NotRequired[
        "aws_sdk_payment_cryptography_data.types.wrapped_key.WrappedKey"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GeneratePinDataInput) -> dict:
    out: dict = {}
    out["GenerationKeyIdentifier"] = value["generation_key_identifier"]
    out["EncryptionKeyIdentifier"] = value["encryption_key_identifier"]
    import aws_sdk_payment_cryptography_data.types.pin_generation_attributes

    out["GenerationAttributes"] = (
        aws_sdk_payment_cryptography_data.types.pin_generation_attributes.serialize_json(
            value["generation_attributes"]
        )
    )
    if "pin_data_length" in value:
        out["PinDataLength"] = value["pin_data_length"]
    if "primary_account_number" in value:
        out["PrimaryAccountNumber"] = value["primary_account_number"]
    import aws_sdk_payment_cryptography_data.types.pin_block_format_for_pin_data

    out["PinBlockFormat"] = (
        aws_sdk_payment_cryptography_data.types.pin_block_format_for_pin_data.serialize_json(
            value["pin_block_format"]
        )
    )
    if "encryption_wrapped_key" in value:
        import aws_sdk_payment_cryptography_data.types.wrapped_key

        out["EncryptionWrappedKey"] = (
            aws_sdk_payment_cryptography_data.types.wrapped_key.serialize_json(
                value["encryption_wrapped_key"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeneratePinDataInput:
    out: GeneratePinDataInput = {}  # type: ignore[typeddict-item]
    if "GenerationKeyIdentifier" in data:
        out["generation_key_identifier"] = data["GenerationKeyIdentifier"]
    else:
        raise DeserializationError(
            "GeneratePinDataInput.generation_key_identifier required"
        )
    if "EncryptionKeyIdentifier" in data:
        out["encryption_key_identifier"] = data["EncryptionKeyIdentifier"]
    else:
        raise DeserializationError(
            "GeneratePinDataInput.encryption_key_identifier required"
        )
    if "GenerationAttributes" in data:
        import aws_sdk_payment_cryptography_data.types.pin_generation_attributes

        out["generation_attributes"] = (
            aws_sdk_payment_cryptography_data.types.pin_generation_attributes.deserialize_json(
                data["GenerationAttributes"]
            )
        )
    else:
        raise DeserializationError(
            "GeneratePinDataInput.generation_attributes required"
        )
    if "PinDataLength" in data:
        out["pin_data_length"] = data["PinDataLength"]
    if "PrimaryAccountNumber" in data:
        out["primary_account_number"] = data["PrimaryAccountNumber"]
    if "PinBlockFormat" in data:
        import aws_sdk_payment_cryptography_data.types.pin_block_format_for_pin_data

        out["pin_block_format"] = (
            aws_sdk_payment_cryptography_data.types.pin_block_format_for_pin_data.deserialize_json(
                data["PinBlockFormat"]
            )
        )
    else:
        raise DeserializationError("GeneratePinDataInput.pin_block_format required")
    if "EncryptionWrappedKey" in data:
        import aws_sdk_payment_cryptography_data.types.wrapped_key

        out["encryption_wrapped_key"] = (
            aws_sdk_payment_cryptography_data.types.wrapped_key.deserialize_json(
                data["EncryptionWrappedKey"]
            )
        )
    return out
