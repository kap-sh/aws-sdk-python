"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#MacAlgorithmDukpt``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.dukpt_derivation_type
    import aws_sdk_payment_cryptography_data.types.dukpt_key_variant
    import aws_sdk_payment_cryptography_data.types.hex_length16_or20_or24


class MacAlgorithmDukpt(TypedDict):
    key_serial_number: "aws_sdk_payment_cryptography_data.types.hex_length16_or20_or24.HexLength16Or20Or24"
    """<p>The unique identifier known as Key Serial Number (KSN) that comes from an encrypting device using DUKPT encryption method. The KSN is derived from the encrypting device unique identifier and an internal transaction counter.</p>"""
    dukpt_key_variant: (
        "aws_sdk_payment_cryptography_data.types.dukpt_key_variant.DukptKeyVariant"
    )
    """<p>The type of use of DUKPT, which can be MAC generation, MAC verification, or both.</p>"""
    dukpt_derivation_type: NotRequired[
        "aws_sdk_payment_cryptography_data.types.dukpt_derivation_type.DukptDerivationType"
    ]
    """<p>The key type derived using DUKPT from a Base Derivation Key (BDK) and Key Serial Number (KSN). This must be less than or equal to the strength of the BDK. For example, you can't use <code>AES_128</code> as a derivation type for a BDK of <code>AES_128</code> or <code>TDES_2KEY</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MacAlgorithmDukpt) -> dict:
    out: dict = {}
    out["KeySerialNumber"] = value["key_serial_number"]
    import aws_sdk_payment_cryptography_data.types.dukpt_key_variant

    out["DukptKeyVariant"] = (
        aws_sdk_payment_cryptography_data.types.dukpt_key_variant.serialize_json(
            value["dukpt_key_variant"]
        )
    )
    if "dukpt_derivation_type" in value:
        import aws_sdk_payment_cryptography_data.types.dukpt_derivation_type

        out["DukptDerivationType"] = (
            aws_sdk_payment_cryptography_data.types.dukpt_derivation_type.serialize_json(
                value["dukpt_derivation_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> MacAlgorithmDukpt:
    out: MacAlgorithmDukpt = {}  # type: ignore[typeddict-item]
    if "KeySerialNumber" in data:
        out["key_serial_number"] = data["KeySerialNumber"]
    else:
        raise DeserializationError("MacAlgorithmDukpt.key_serial_number required")
    if "DukptKeyVariant" in data:
        import aws_sdk_payment_cryptography_data.types.dukpt_key_variant

        out["dukpt_key_variant"] = (
            aws_sdk_payment_cryptography_data.types.dukpt_key_variant.deserialize_json(
                data["DukptKeyVariant"]
            )
        )
    else:
        raise DeserializationError("MacAlgorithmDukpt.dukpt_key_variant required")
    if "DukptDerivationType" in data:
        import aws_sdk_payment_cryptography_data.types.dukpt_derivation_type

        out["dukpt_derivation_type"] = (
            aws_sdk_payment_cryptography_data.types.dukpt_derivation_type.deserialize_json(
                data["DukptDerivationType"]
            )
        )
    return out
