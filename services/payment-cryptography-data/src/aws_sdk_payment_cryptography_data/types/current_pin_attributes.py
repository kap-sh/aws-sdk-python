"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#CurrentPinAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography_data.types.pin_block_length_equals16


class CurrentPinAttributes(TypedDict, closed=True):
    current_pin_pek_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyArn</code> of the current PIN PEK.</p>"""
    current_encrypted_pin_block: "aws_sdk_payment_cryptography_data.types.pin_block_length_equals16.PinBlockLengthEquals16"
    """<p>The encrypted pinblock of the current pin stored on the chip card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CurrentPinAttributes) -> dict:
    out: dict = {}
    out["CurrentPinPekIdentifier"] = value["current_pin_pek_identifier"]
    out["CurrentEncryptedPinBlock"] = value["current_encrypted_pin_block"]
    return out


def deserialize_json(data: dict) -> CurrentPinAttributes:
    out: CurrentPinAttributes = {}  # type: ignore[typeddict-item]
    if "CurrentPinPekIdentifier" in data:
        out["current_pin_pek_identifier"] = data["CurrentPinPekIdentifier"]
    else:
        raise DeserializationError(
            "CurrentPinAttributes.current_pin_pek_identifier required"
        )
    if "CurrentEncryptedPinBlock" in data:
        out["current_encrypted_pin_block"] = data["CurrentEncryptedPinBlock"]
    else:
        raise DeserializationError(
            "CurrentPinAttributes.current_encrypted_pin_block required"
        )
    return out
