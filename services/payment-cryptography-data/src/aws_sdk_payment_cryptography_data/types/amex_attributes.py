"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#AmexAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.current_pin_attributes
    import aws_sdk_payment_cryptography_data.types.hex_length_equals4
    import aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography_data.types.major_key_derivation_mode
    import aws_sdk_payment_cryptography_data.types.number_length_equals2
    import aws_sdk_payment_cryptography_data.types.primary_account_number_type


class AmexAttributes(TypedDict):
    major_key_derivation_mode: "aws_sdk_payment_cryptography_data.types.major_key_derivation_mode.MajorKeyDerivationMode"
    """<p>The method to use when deriving the master key for a payment card using Amex derivation.</p>"""
    primary_account_number: "aws_sdk_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    """<p>The Primary Account Number (PAN) of the cardholder.</p>"""
    pan_sequence_number: "aws_sdk_payment_cryptography_data.types.number_length_equals2.NumberLengthEquals2"
    """<p>A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). Typically 00 is used, if no value is provided by the terminal.</p>"""
    application_transaction_counter: (
        "aws_sdk_payment_cryptography_data.types.hex_length_equals4.HexLengthEquals4"
    )
    """<p>The transaction counter of the current transaction that is provided by the terminal during transaction processing.</p>"""
    authorization_request_key_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyArn</code> of the issuer master key for cryptogram (IMK-AC) for the payment card.</p>"""
    current_pin_attributes: NotRequired[
        "aws_sdk_payment_cryptography_data.types.current_pin_attributes.CurrentPinAttributes"
    ]
    """<p>The encrypted pinblock of the old pin stored on the chip card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmexAttributes) -> dict:
    out: dict = {}
    import aws_sdk_payment_cryptography_data.types.major_key_derivation_mode

    out["MajorKeyDerivationMode"] = (
        aws_sdk_payment_cryptography_data.types.major_key_derivation_mode.serialize_json(
            value["major_key_derivation_mode"]
        )
    )
    out["PrimaryAccountNumber"] = value["primary_account_number"]
    out["PanSequenceNumber"] = value["pan_sequence_number"]
    out["ApplicationTransactionCounter"] = value["application_transaction_counter"]
    out["AuthorizationRequestKeyIdentifier"] = value[
        "authorization_request_key_identifier"
    ]
    if "current_pin_attributes" in value:
        import aws_sdk_payment_cryptography_data.types.current_pin_attributes

        out["CurrentPinAttributes"] = (
            aws_sdk_payment_cryptography_data.types.current_pin_attributes.serialize_json(
                value["current_pin_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> AmexAttributes:
    out: AmexAttributes = {}  # type: ignore[typeddict-item]
    if "MajorKeyDerivationMode" in data:
        import aws_sdk_payment_cryptography_data.types.major_key_derivation_mode

        out["major_key_derivation_mode"] = (
            aws_sdk_payment_cryptography_data.types.major_key_derivation_mode.deserialize_json(
                data["MajorKeyDerivationMode"]
            )
        )
    else:
        raise DeserializationError("AmexAttributes.major_key_derivation_mode required")
    if "PrimaryAccountNumber" in data:
        out["primary_account_number"] = data["PrimaryAccountNumber"]
    else:
        raise DeserializationError("AmexAttributes.primary_account_number required")
    if "PanSequenceNumber" in data:
        out["pan_sequence_number"] = data["PanSequenceNumber"]
    else:
        raise DeserializationError("AmexAttributes.pan_sequence_number required")
    if "ApplicationTransactionCounter" in data:
        out["application_transaction_counter"] = data["ApplicationTransactionCounter"]
    else:
        raise DeserializationError(
            "AmexAttributes.application_transaction_counter required"
        )
    if "AuthorizationRequestKeyIdentifier" in data:
        out["authorization_request_key_identifier"] = data[
            "AuthorizationRequestKeyIdentifier"
        ]
    else:
        raise DeserializationError(
            "AmexAttributes.authorization_request_key_identifier required"
        )
    if "CurrentPinAttributes" in data:
        import aws_sdk_payment_cryptography_data.types.current_pin_attributes

        out["current_pin_attributes"] = (
            aws_sdk_payment_cryptography_data.types.current_pin_attributes.deserialize_json(
                data["CurrentPinAttributes"]
            )
        )
    return out
