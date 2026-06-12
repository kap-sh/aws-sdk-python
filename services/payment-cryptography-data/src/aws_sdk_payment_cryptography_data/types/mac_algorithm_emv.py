"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#MacAlgorithmEmv``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.major_key_derivation_mode
    import aws_sdk_payment_cryptography_data.types.number_length_equals2
    import aws_sdk_payment_cryptography_data.types.primary_account_number_type
    import aws_sdk_payment_cryptography_data.types.session_key_derivation_mode
    import aws_sdk_payment_cryptography_data.types.session_key_derivation_value


class MacAlgorithmEmv(TypedDict):
    major_key_derivation_mode: "aws_sdk_payment_cryptography_data.types.major_key_derivation_mode.MajorKeyDerivationMode"
    """<p>The method to use when deriving the master key for EMV MAC generation or verification.</p>"""
    primary_account_number: "aws_sdk_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    """<p>The Primary Account Number (PAN), a unique identifier for a payment credit or debit card and associates the card to a specific account holder.</p>"""
    pan_sequence_number: "aws_sdk_payment_cryptography_data.types.number_length_equals2.NumberLengthEquals2"
    """<p>A number that identifies and differentiates payment cards with the same Primary Account Number (PAN).</p>"""
    session_key_derivation_mode: "aws_sdk_payment_cryptography_data.types.session_key_derivation_mode.SessionKeyDerivationMode"
    """<p>The method of deriving a session key for EMV MAC generation or verification.</p>"""
    session_key_derivation_value: "aws_sdk_payment_cryptography_data.types.session_key_derivation_value.SessionKeyDerivationValue"
    """<p>Parameters that are required to generate session key for EMV generation and verification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MacAlgorithmEmv) -> dict:
    out: dict = {}
    import aws_sdk_payment_cryptography_data.types.major_key_derivation_mode

    out["MajorKeyDerivationMode"] = (
        aws_sdk_payment_cryptography_data.types.major_key_derivation_mode.serialize_json(
            value["major_key_derivation_mode"]
        )
    )
    out["PrimaryAccountNumber"] = value["primary_account_number"]
    out["PanSequenceNumber"] = value["pan_sequence_number"]
    import aws_sdk_payment_cryptography_data.types.session_key_derivation_mode

    out["SessionKeyDerivationMode"] = (
        aws_sdk_payment_cryptography_data.types.session_key_derivation_mode.serialize_json(
            value["session_key_derivation_mode"]
        )
    )
    import aws_sdk_payment_cryptography_data.types.session_key_derivation_value

    out["SessionKeyDerivationValue"] = (
        aws_sdk_payment_cryptography_data.types.session_key_derivation_value.serialize_json(
            value["session_key_derivation_value"]
        )
    )
    return out


def deserialize_json(data: dict) -> MacAlgorithmEmv:
    out: MacAlgorithmEmv = {}  # type: ignore[typeddict-item]
    if "MajorKeyDerivationMode" in data:
        import aws_sdk_payment_cryptography_data.types.major_key_derivation_mode

        out["major_key_derivation_mode"] = (
            aws_sdk_payment_cryptography_data.types.major_key_derivation_mode.deserialize_json(
                data["MajorKeyDerivationMode"]
            )
        )
    else:
        raise DeserializationError("MacAlgorithmEmv.major_key_derivation_mode required")
    if "PrimaryAccountNumber" in data:
        out["primary_account_number"] = data["PrimaryAccountNumber"]
    else:
        raise DeserializationError("MacAlgorithmEmv.primary_account_number required")
    if "PanSequenceNumber" in data:
        out["pan_sequence_number"] = data["PanSequenceNumber"]
    else:
        raise DeserializationError("MacAlgorithmEmv.pan_sequence_number required")
    if "SessionKeyDerivationMode" in data:
        import aws_sdk_payment_cryptography_data.types.session_key_derivation_mode

        out["session_key_derivation_mode"] = (
            aws_sdk_payment_cryptography_data.types.session_key_derivation_mode.deserialize_json(
                data["SessionKeyDerivationMode"]
            )
        )
    else:
        raise DeserializationError(
            "MacAlgorithmEmv.session_key_derivation_mode required"
        )
    if "SessionKeyDerivationValue" in data:
        import aws_sdk_payment_cryptography_data.types.session_key_derivation_value

        out["session_key_derivation_value"] = (
            aws_sdk_payment_cryptography_data.types.session_key_derivation_value.deserialize_json(
                data["SessionKeyDerivationValue"]
            )
        )
    else:
        raise DeserializationError(
            "MacAlgorithmEmv.session_key_derivation_value required"
        )
    return out
