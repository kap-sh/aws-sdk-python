"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#EmvCommonAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.application_cryptogram_type
    import aws_sdk_payment_cryptography_data.types.emv_encryption_mode
    import aws_sdk_payment_cryptography_data.types.major_key_derivation_mode
    import aws_sdk_payment_cryptography_data.types.number_length_equals2
    import aws_sdk_payment_cryptography_data.types.pin_block_length_position
    import aws_sdk_payment_cryptography_data.types.pin_block_padding_type
    import aws_sdk_payment_cryptography_data.types.primary_account_number_type


class EmvCommonAttributes(TypedDict, closed=True):
    major_key_derivation_mode: "aws_sdk_payment_cryptography_data.types.major_key_derivation_mode.MajorKeyDerivationMode"
    """<p>The method to use when deriving the master key for the payment card.</p>"""
    primary_account_number: "aws_sdk_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    """<p>The Primary Account Number (PAN) of the cardholder.</p>"""
    pan_sequence_number: "aws_sdk_payment_cryptography_data.types.number_length_equals2.NumberLengthEquals2"
    """<p>A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). Typically 00 is used, if no value is provided by the terminal.</p>"""
    application_cryptogram: "aws_sdk_payment_cryptography_data.types.application_cryptogram_type.ApplicationCryptogramType"
    """<p>The application cryptogram for the current transaction that is provided by the terminal during transaction processing.</p>"""
    mode: (
        "aws_sdk_payment_cryptography_data.types.emv_encryption_mode.EmvEncryptionMode"
    )
    """<p>The block cipher method to use for encryption.</p>"""
    pin_block_padding_type: "aws_sdk_payment_cryptography_data.types.pin_block_padding_type.PinBlockPaddingType"
    """<p>The padding to be added to the PIN block prior to encryption.</p> <p>Padding type should be <code>ISO_IEC_7816_4</code>, if <code>PinBlockLengthPosition</code> is set to <code>FRONT_OF_PIN_BLOCK</code>. No padding is required, if <code>PinBlockLengthPosition</code> is set to <code>NONE</code>.</p>"""
    pin_block_length_position: "aws_sdk_payment_cryptography_data.types.pin_block_length_position.PinBlockLengthPosition"
    """<p>Specifies if PIN block length should be added to front of the pin block. </p> <p>If value is set to <code>FRONT_OF_PIN_BLOCK</code>, then PIN block padding type should be <code>ISO_IEC_7816_4</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmvCommonAttributes) -> dict:
    out: dict = {}
    import aws_sdk_payment_cryptography_data.types.major_key_derivation_mode

    out["MajorKeyDerivationMode"] = (
        aws_sdk_payment_cryptography_data.types.major_key_derivation_mode.serialize_json(
            value["major_key_derivation_mode"]
        )
    )
    out["PrimaryAccountNumber"] = value["primary_account_number"]
    out["PanSequenceNumber"] = value["pan_sequence_number"]
    out["ApplicationCryptogram"] = value["application_cryptogram"]
    import aws_sdk_payment_cryptography_data.types.emv_encryption_mode

    out["Mode"] = (
        aws_sdk_payment_cryptography_data.types.emv_encryption_mode.serialize_json(
            value["mode"]
        )
    )
    import aws_sdk_payment_cryptography_data.types.pin_block_padding_type

    out["PinBlockPaddingType"] = (
        aws_sdk_payment_cryptography_data.types.pin_block_padding_type.serialize_json(
            value["pin_block_padding_type"]
        )
    )
    import aws_sdk_payment_cryptography_data.types.pin_block_length_position

    out["PinBlockLengthPosition"] = (
        aws_sdk_payment_cryptography_data.types.pin_block_length_position.serialize_json(
            value["pin_block_length_position"]
        )
    )
    return out


def deserialize_json(data: dict) -> EmvCommonAttributes:
    out: EmvCommonAttributes = {}  # type: ignore[typeddict-item]
    if "MajorKeyDerivationMode" in data:
        import aws_sdk_payment_cryptography_data.types.major_key_derivation_mode

        out["major_key_derivation_mode"] = (
            aws_sdk_payment_cryptography_data.types.major_key_derivation_mode.deserialize_json(
                data["MajorKeyDerivationMode"]
            )
        )
    else:
        raise DeserializationError(
            "EmvCommonAttributes.major_key_derivation_mode required"
        )
    if "PrimaryAccountNumber" in data:
        out["primary_account_number"] = data["PrimaryAccountNumber"]
    else:
        raise DeserializationError(
            "EmvCommonAttributes.primary_account_number required"
        )
    if "PanSequenceNumber" in data:
        out["pan_sequence_number"] = data["PanSequenceNumber"]
    else:
        raise DeserializationError("EmvCommonAttributes.pan_sequence_number required")
    if "ApplicationCryptogram" in data:
        out["application_cryptogram"] = data["ApplicationCryptogram"]
    else:
        raise DeserializationError(
            "EmvCommonAttributes.application_cryptogram required"
        )
    if "Mode" in data:
        import aws_sdk_payment_cryptography_data.types.emv_encryption_mode

        out["mode"] = (
            aws_sdk_payment_cryptography_data.types.emv_encryption_mode.deserialize_json(
                data["Mode"]
            )
        )
    else:
        raise DeserializationError("EmvCommonAttributes.mode required")
    if "PinBlockPaddingType" in data:
        import aws_sdk_payment_cryptography_data.types.pin_block_padding_type

        out["pin_block_padding_type"] = (
            aws_sdk_payment_cryptography_data.types.pin_block_padding_type.deserialize_json(
                data["PinBlockPaddingType"]
            )
        )
    else:
        raise DeserializationError(
            "EmvCommonAttributes.pin_block_padding_type required"
        )
    if "PinBlockLengthPosition" in data:
        import aws_sdk_payment_cryptography_data.types.pin_block_length_position

        out["pin_block_length_position"] = (
            aws_sdk_payment_cryptography_data.types.pin_block_length_position.deserialize_json(
                data["PinBlockLengthPosition"]
            )
        )
    else:
        raise DeserializationError(
            "EmvCommonAttributes.pin_block_length_position required"
        )
    return out
