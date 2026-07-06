"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#Ibm3624PinVerification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.decimalization_table_type
    import aws_sdk_payment_cryptography_data.types.hex_length_equals1
    import aws_sdk_payment_cryptography_data.types.pin_offset_type
    import aws_sdk_payment_cryptography_data.types.pin_validation_data_type


class Ibm3624PinVerification(TypedDict, closed=True):
    decimalization_table: "aws_sdk_payment_cryptography_data.types.decimalization_table_type.DecimalizationTableType"
    """<p>The decimalization table to use for IBM 3624 PIN algorithm. The table is used to convert the algorithm intermediate result from hexadecimal characters to decimal.</p>"""
    pin_validation_data_pad_character: (
        "aws_sdk_payment_cryptography_data.types.hex_length_equals1.HexLengthEquals1"
    )
    """<p>The padding character for validation data.</p>"""
    pin_validation_data: "aws_sdk_payment_cryptography_data.types.pin_validation_data_type.PinValidationDataType"
    """<p>The unique data for cardholder identification.</p>"""
    pin_offset: "aws_sdk_payment_cryptography_data.types.pin_offset_type.PinOffsetType"
    """<p>The PIN offset value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ibm3624PinVerification) -> dict:
    out: dict = {}
    out["DecimalizationTable"] = value["decimalization_table"]
    out["PinValidationDataPadCharacter"] = value["pin_validation_data_pad_character"]
    out["PinValidationData"] = value["pin_validation_data"]
    out["PinOffset"] = value["pin_offset"]
    return out


def deserialize_json(data: dict) -> Ibm3624PinVerification:
    out: Ibm3624PinVerification = {}  # type: ignore[typeddict-item]
    if "DecimalizationTable" in data:
        out["decimalization_table"] = data["DecimalizationTable"]
    else:
        raise DeserializationError(
            "Ibm3624PinVerification.decimalization_table required"
        )
    if "PinValidationDataPadCharacter" in data:
        out["pin_validation_data_pad_character"] = data["PinValidationDataPadCharacter"]
    else:
        raise DeserializationError(
            "Ibm3624PinVerification.pin_validation_data_pad_character required"
        )
    if "PinValidationData" in data:
        out["pin_validation_data"] = data["PinValidationData"]
    else:
        raise DeserializationError(
            "Ibm3624PinVerification.pin_validation_data required"
        )
    if "PinOffset" in data:
        out["pin_offset"] = data["PinOffset"]
    else:
        raise DeserializationError("Ibm3624PinVerification.pin_offset required")
    return out
