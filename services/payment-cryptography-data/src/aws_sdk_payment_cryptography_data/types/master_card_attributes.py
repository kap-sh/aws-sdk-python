"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#MasterCardAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.application_cryptogram_type
    import aws_sdk_payment_cryptography_data.types.major_key_derivation_mode
    import aws_sdk_payment_cryptography_data.types.number_length_equals2
    import aws_sdk_payment_cryptography_data.types.primary_account_number_type


class MasterCardAttributes(TypedDict, closed=True):
    major_key_derivation_mode: "aws_sdk_payment_cryptography_data.types.major_key_derivation_mode.MajorKeyDerivationMode"
    """<p>The method to use when deriving the master key for the payment card.</p>"""
    primary_account_number: "aws_sdk_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    """<p>The Primary Account Number (PAN) of the cardholder.</p>"""
    pan_sequence_number: "aws_sdk_payment_cryptography_data.types.number_length_equals2.NumberLengthEquals2"
    """<p>A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). Typically 00 is used, if no value is provided by the terminal.</p>"""
    application_cryptogram: "aws_sdk_payment_cryptography_data.types.application_cryptogram_type.ApplicationCryptogramType"
    """<p>The application cryptogram for the current transaction that is provided by the terminal during transaction processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MasterCardAttributes) -> dict:
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
    return out


def deserialize_json(data: dict) -> MasterCardAttributes:
    out: MasterCardAttributes = {}  # type: ignore[typeddict-item]
    if "MajorKeyDerivationMode" in data:
        import aws_sdk_payment_cryptography_data.types.major_key_derivation_mode

        out["major_key_derivation_mode"] = (
            aws_sdk_payment_cryptography_data.types.major_key_derivation_mode.deserialize_json(
                data["MajorKeyDerivationMode"]
            )
        )
    else:
        raise DeserializationError(
            "MasterCardAttributes.major_key_derivation_mode required"
        )
    if "PrimaryAccountNumber" in data:
        out["primary_account_number"] = data["PrimaryAccountNumber"]
    else:
        raise DeserializationError(
            "MasterCardAttributes.primary_account_number required"
        )
    if "PanSequenceNumber" in data:
        out["pan_sequence_number"] = data["PanSequenceNumber"]
    else:
        raise DeserializationError("MasterCardAttributes.pan_sequence_number required")
    if "ApplicationCryptogram" in data:
        out["application_cryptogram"] = data["ApplicationCryptogram"]
    else:
        raise DeserializationError(
            "MasterCardAttributes.application_cryptogram required"
        )
    return out
